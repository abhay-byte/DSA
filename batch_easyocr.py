#!/usr/bin/env python3
"""
Batch extract handwritten text from all lecture PDFs using EasyOCR.
Saves results to resources/easyocr/lec-{num}.md
"""
import os
import re
import sys
import numpy as np
import easyocr
from pdf2image import convert_from_path

LECTURES_DIR = "lectures"
OUTPUT_DIR = "resources/easyocr"
EXCLUDE_FILES = ["PPCPPMar2025.pdf"]

def extract_lecture_number(filename):
    """Extract lecture number from filename like 'L45 - Graphs.pdf' -> 45"""
    match = re.match(r'L(\d+)', filename)
    if match:
        return int(match.group(1))
    return None

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Initialize EasyOCR reader (GPU enabled for GTX 1650)
    print("Initializing EasyOCR with GPU...")
    reader = easyocr.Reader(['en'], gpu=True)
    
    # Get all PDF files
    pdf_files = [f for f in os.listdir(LECTURES_DIR) 
                 if f.endswith('.pdf') and f not in EXCLUDE_FILES]
    pdf_files.sort(key=lambda x: extract_lecture_number(x) or 999)
    
    print(f"Found {len(pdf_files)} PDFs to process")
    
    for pdf_file in pdf_files:
        lec_num = extract_lecture_number(pdf_file)
        if lec_num is None:
            continue
        
        pdf_path = os.path.join(LECTURES_DIR, pdf_file)
        output_path = os.path.join(OUTPUT_DIR, f"lec-{lec_num}.md")
        
        print(f"Processing L{lec_num}: {pdf_file}")
        
        try:
            # Convert PDF to images
            images = convert_from_path(pdf_path)
            
            content = f"# Lecture {lec_num} (EasyOCR)\n\n"
            content += f"**Source:** `{pdf_file}`\n\n"
            content += "---\n\n"
            
            for i, img in enumerate(images):
                print(f"  Page {i+1}/{len(images)}...", end=" ", flush=True)
                img_np = np.array(img)
                result = reader.readtext(img_np, detail=0)
                page_text = " ".join(result)
                content += f"## Page {i+1}\n\n{page_text}\n\n"
                print("✓")
            
            with open(output_path, 'w') as f:
                f.write(content)
            print(f"  ✓ Saved to {output_path}")
            
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print(f"\nDone! Extracted to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
