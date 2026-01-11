#!/usr/bin/env python3
"""
Batch extract content from all lecture PDFs using MinerU (magic-pdf).
Saves results to resources/mineru/lec-{num}/
"""
import os
import re
import subprocess
import sys

LECTURES_DIR = "lectures"
OUTPUT_DIR = "resources/mineru"
EXCLUDE_FILES = ["PPCPPMar2025.pdf"]

def extract_lecture_number(filename):
    """Extract lecture number from filename like 'L45 - Graphs.pdf' -> 45"""
    match = re.match(r'L(\d+)', filename)
    if match:
        return int(match.group(1))
    return None

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    # Get all PDF files
    pdf_files = [f for f in os.listdir(LECTURES_DIR) 
                 if f.endswith('.pdf') and f not in EXCLUDE_FILES]
    pdf_files.sort(key=lambda x: extract_lecture_number(x) or 999)
    
    print(f"Found {len(pdf_files)} PDFs to process with MinerU")
    
    for pdf_file in pdf_files:
        lec_num = extract_lecture_number(pdf_file)
        if lec_num is None:
            continue
        
        pdf_path = os.path.join(LECTURES_DIR, pdf_file)
        output_subdir = os.path.join(OUTPUT_DIR, f"lec-{lec_num}")
        
        print(f"Processing L{lec_num}: {pdf_file}")
        
        try:
            # Run magic-pdf CLI
            result = subprocess.run(
                ['magic-pdf', '-p', pdf_path, '-o', output_subdir],
                capture_output=True,
                text=True,
                timeout=300  # 5 min timeout per PDF
            )
            
            if result.returncode == 0:
                print(f"  ✓ Saved to {output_subdir}/")
            else:
                print(f"  ✗ Error: {result.stderr[:200]}")
                
        except subprocess.TimeoutExpired:
            print(f"  ✗ Timeout after 5 minutes")
        except Exception as e:
            print(f"  ✗ Error: {e}")
    
    print(f"\nDone! Extracted to {OUTPUT_DIR}/")

if __name__ == "__main__":
    main()
