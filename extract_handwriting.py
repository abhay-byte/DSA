import easyocr
import numpy as np
from pdf2image import convert_from_path
import sys

def extract_handwriting(pdf_path):
    print(f"Processing {pdf_path}...")
    
    try:
        # Initialize Reader (loads model into memory)
        # Using 'en' (English). gpu=True enabled for user's GTX 1650
        reader = easyocr.Reader(['en'], gpu=True) 

        # Convert PDF pages to Images
        images = convert_from_path(pdf_path)

        # Extract Text from each page
        for i, img in enumerate(images):
            print(f"\n--- Page {i+1} ---")
            img_np = np.array(img)
            result = reader.readtext(img_np, detail=0)
            full_text = " ".join(result)
            print(full_text)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python extract_handwriting.py <pdf_path>")
    else:
        extract_handwriting(sys.argv[1])
