#!/usr/bin/env python3
"""
Batch extract content from all lecture PDFs using vision model via Ollama.
Saves results to resources/qwen/lec-{num}.md
"""
import os
import re
import base64
import io
import traceback
from pdf2image import convert_from_path

try:
    import ollama
except ImportError:
    print("Please install ollama: pip install ollama")
    exit(1)

LECTURES_DIR = "lectures"
OUTPUT_DIR = "resources/qwen"
EXCLUDE_FILES = ["PPCPPMar2025.pdf"]
MODEL_NAME = "moondream"  # Smaller, more stable model

def extract_lecture_number(filename):
    """Extract lecture number from filename like 'L45 - Graphs.pdf' -> 45"""
    match = re.match(r'L(\d+)', filename)
    if match:
        return int(match.group(1))
    return None

def image_to_base64(pil_image):
    """Convert PIL Image to base64 string"""
    # Convert to RGB if needed (JPEG doesn't support RGBA)
    if pil_image.mode in ('RGBA', 'P'):
        pil_image = pil_image.convert('RGB')
    # Resize to reduce memory usage
    max_size = 1024
    if max(pil_image.size) > max_size:
        ratio = max_size / max(pil_image.size)
        new_size = (int(pil_image.width * ratio), int(pil_image.height * ratio))
        pil_image = pil_image.resize(new_size)
    buffer = io.BytesIO()
    pil_image.save(buffer, format='JPEG', quality=75)
    img_bytes = buffer.getvalue()
    print(f"    [DEBUG] Image size: {pil_image.size}, bytes: {len(img_bytes)}")
    return base64.b64encode(img_bytes).decode()

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Check if model is available
    print(f"[INFO] Checking model {MODEL_NAME}...")
    try:
        ollama.show(MODEL_NAME)
        print(f"✓ Model {MODEL_NAME} is available")
    except Exception as e:
        print(f"[ERROR] Model {MODEL_NAME} not found: {e}")
        print(f"[INFO] Pulling model...")
        ollama.pull(MODEL_NAME)
    
    # Get all PDF files
    pdf_files = [f for f in os.listdir(LECTURES_DIR) 
                 if f.endswith('.pdf') and f not in EXCLUDE_FILES]
    pdf_files.sort(key=lambda x: extract_lecture_number(x) or 999)
    
    print(f"[INFO] Found {len(pdf_files)} PDFs to process")
    
    prompt = "Describe this image from a DSA lecture. Include any text, diagrams, flowcharts, or algorithms you see."

    for pdf_file in pdf_files:  # Process all PDFs
        lec_num = extract_lecture_number(pdf_file)
        if lec_num is None:
            continue
        
        pdf_path = os.path.join(LECTURES_DIR, pdf_file)
        output_path = os.path.join(OUTPUT_DIR, f"lec-{lec_num}.md")
        
        print(f"\n[INFO] Processing L{lec_num}: {pdf_file}")
        
        try:
            print(f"  [DEBUG] Converting PDF to images...")
            images = convert_from_path(pdf_path, dpi=100)  # Lower DPI
            print(f"  [DEBUG] Got {len(images)} pages")
            
            content = f"# Lecture {lec_num} (Vision Model Analysis)\n\n"
            content += f"**Source:** `{pdf_file}`\n\n"
            content += "---\n\n"
            
            for i, img in enumerate(images):  # All pages
                print(f"  [INFO] Page {i+1}/{len(images)}...")
                
                try:
                    # Convert image to base64
                    print(f"    [DEBUG] Converting to base64...")
                    img_b64 = image_to_base64(img)
                    print(f"    [DEBUG] Base64 length: {len(img_b64)}")
                    
                    # Call vision model
                    print(f"    [DEBUG] Calling ollama.chat with {MODEL_NAME}...")
                    response = ollama.chat(
                        model=MODEL_NAME,
                        messages=[{
                            'role': 'user',
                            'content': prompt,
                            'images': [img_b64]
                        }]
                    )
                    
                    page_content = response['message']['content']
                    print(f"    [DEBUG] Response length: {len(page_content)} chars")
                    content += f"## Page {i+1}\n\n{page_content}\n\n---\n\n"
                    print(f"  ✓ Page {i+1} done")
                    
                except Exception as e:
                    print(f"  ✗ Page {i+1} error: {e}")
                    print(f"    [DEBUG] Traceback:")
                    traceback.print_exc()
                    content += f"## Page {i+1}\n\n*Error: {e}*\n\n---\n\n"
            
            with open(output_path, 'w') as f:
                f.write(content)
            print(f"  ✓ Saved to {output_path}")
            
        except Exception as e:
            print(f"  ✗ Error processing {pdf_file}: {e}")
            traceback.print_exc()
    
    print(f"\n[INFO] Test extraction complete. Check {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
