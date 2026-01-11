#!/usr/bin/env python3
"""
Convert a single PDF to images for direct analysis.
Usage: python pdf_to_images.py <pdf_path> <output_dir>
"""
import sys
import os
from pdf2image import convert_from_path

def main():
    if len(sys.argv) < 3:
        print("Usage: python pdf_to_images.py <pdf_path> <output_dir>")
        sys.exit(1)
    
    pdf_path = sys.argv[1]
    output_dir = sys.argv[2]
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Converting {pdf_path} to images...")
    images = convert_from_path(pdf_path, dpi=150)
    
    for i, img in enumerate(images):
        output_path = os.path.join(output_dir, f"page_{i+1:02d}.png")
        img.save(output_path, 'PNG')
        print(f"  Saved {output_path}")
    
    print(f"Done! {len(images)} pages saved to {output_dir}/")

if __name__ == "__main__":
    main()
