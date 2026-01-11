#!/usr/bin/env python3
"""
Batch extract text from all lecture PDFs using pdftotext.
Saves results to /resources/lec-{num}.md
"""
import os
import subprocess
import re
import sys

LECTURES_DIR = "lectures"
OUTPUT_DIR = "resources"
EXCLUDE_FILES = ["PPCPPMar2025.pdf"]

def extract_lecture_number(filename):
    """Extract lecture number from filename like 'L45 - Graphs.pdf' -> 45"""
    match = re.match(r'L(\d+)', filename)
    if match:
        return int(match.group(1))
    return None

def extract_pdf_text(pdf_path):
    """Extract text from PDF using pdftotext"""
    try:
        result = subprocess.run(
            ['pdftotext', pdf_path, '-'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error extracting {pdf_path}: {e}")
        return None

def main():
    # Ensure output directory exists
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Get all PDF files
    pdf_files = [f for f in os.listdir(LECTURES_DIR) 
                 if f.endswith('.pdf') and f not in EXCLUDE_FILES]
    
    # Sort by lecture number
    pdf_files.sort(key=lambda x: extract_lecture_number(x) or 999)
    
    print(f"Found {len(pdf_files)} PDFs to process (excluding {EXCLUDE_FILES})")
    
    for pdf_file in pdf_files:
        lec_num = extract_lecture_number(pdf_file)
        if lec_num is None:
            print(f"Skipping {pdf_file} - could not extract lecture number")
            continue
        
        pdf_path = os.path.join(LECTURES_DIR, pdf_file)
        output_path = os.path.join(OUTPUT_DIR, f"lec-{lec_num}.md")
        
        print(f"Processing L{lec_num}: {pdf_file} -> {output_path}")
        
        text = extract_pdf_text(pdf_path)
        if text:
            # Add header with source info
            content = f"# Lecture {lec_num}\n\n"
            content += f"**Source:** `{pdf_file}`\n\n"
            content += "---\n\n"
            content += text
            
            with open(output_path, 'w') as f:
                f.write(content)
            print(f"  ✓ Saved to {output_path}")
        else:
            print(f"  ✗ Failed to extract text")
    
    print(f"\nDone! Extracted {len(pdf_files)} lectures to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
