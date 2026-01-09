import google.generativeai as genai
import os
import sys
from pdf2image import convert_from_path

# Configure your API key
# Get one from: https://aistudio.google.com/app/apikey
# os.environ["GEMINI_API_KEY"] = "YOUR_API_KEY_HERE"

def analyze_document_with_gemini(pdf_path):
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("Error: GEMINI_API_KEY environment variable not set.")
        print("Please export it: export GEMINI_API_KEY='your_key'")
        return

    genai.configure(api_key=api_key)

    # Use Gemini 2.0 Flash (latest experimental model)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')

    print(f"Converting {pdf_path} to images...")
    images = convert_from_path(pdf_path)

    import time

    # Prepare prompt
    prompt = "Transcribe the handwritten notes on this page. If there are diagrams, describe them in detail or provide Mermaid JS code for them."

    # Prepare markdown file
    output_file = "Gemini_Analysis_Result.md"
    with open(output_file, "w") as f:
        f.write("# Gemini Analysis Results\n\n")

    for i, img in enumerate(images):
        print(f"\n--- Analyzing Page {i+1} with Gemini ---")
        
        retries = 0
        max_retries = 5
        wait_time = 10
        
        while retries < max_retries:
            try:
                response = model.generate_content([prompt, img])
                text_content = response.text
                print(text_content[:200] + "...") # Print preview
                
                # Append to file
                with open(output_file, "a") as f:
                    f.write(f"## Page {i+1}\n")
                    f.write(text_content)
                    f.write("\n\n---\n\n")
                
                # Success! Break the retry loop
                break

            except Exception as e:
                if "429" in str(e):
                    print(f"Rate limit hit (429). Retrying in {wait_time}s... (Attempt {retries+1}/{max_retries})")
                    time.sleep(wait_time)
                    wait_time *= 2 # Exponential backoff
                    retries += 1
                else:
                    print(f"Error calling API: {e}")
                    break # Don't retry other errors
        
        # Standard pause between pages to be nice
        time.sleep(5)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python use_gemini_template.py <pdf_path>")
    else:
        analyze_document_with_gemini(sys.argv[1])
