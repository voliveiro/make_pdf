import os
from PIL import Image
from PyPDF2 import PdfMerger
import re

def natural_sort_key(s):
    # This function generates a sort key for natural sorting of filenames
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]

def convert_jpg_to_pdf(jpg_files):
    pdf_files = []
    for jpg_file in jpg_files:
        try:
            with Image.open(jpg_file) as image:
                # Ensure the image is in RGB mode
                if image.mode != 'RGB':
                    image = image.convert('RGB')
                pdf_file = jpg_file.replace('.jpg', '.pdf')
                image.save(pdf_file, 'PDF', resolution=100.0)
                pdf_files.append(pdf_file)
                print(f"Converted {jpg_file} to {pdf_file}")
        except Exception as e:
            print(f"Failed to convert {jpg_file}: {e}")
    return pdf_files

def merge_pdfs(pdf_files, output_path):
    merger = PdfMerger()
    for pdf_file in pdf_files:
        try:
            merger.append(pdf_file)
            print(f"Added {pdf_file} to the merger")
        except Exception as e:
            print(f"Failed to add {pdf_file} to the merger: {e}")
    merger.write(output_path)
    merger.close()
    print(f"Created merged PDF: {output_path}")

def main():
    # Get a list of all jpg files in the current directory
    jpg_files = [file for file in os.listdir() if file.lower().endswith('.jpg')]
    # Sort files naturally
    jpg_files.sort(key=natural_sort_key)
    print(f"Found {len(jpg_files)} jpg files: {jpg_files}")
    
    # Convert each jpg to pdf
    pdf_files = convert_jpg_to_pdf(jpg_files)
    
    if pdf_files:
        # Merge all pdfs into a single pdf
        output_pdf = 'combined.pdf'
        merge_pdfs(pdf_files, output_pdf)
    else:
        print("No PDF files were created. Exiting.")

if __name__ == '__main__':
    main()

