import os
import json
from pdf_parser import extract_text_with_fonts  
from extractor import identify_heading_levels, extract_title

INPUT_PDF = r"C:\Users\krish\Downloads\15782_3_7925538_1746163246_AWS Course Completion Certificate.pdf"
OUTPUT_JSON = r"C:\Users\krish\Downloads\output1.json"

def process_file(pdf_path, output_path):
    print(f"Processing PDF: {pdf_path}")
    text_data = extract_text_with_fonts(pdf_path)
    print(f"Extracted {len(text_data)} text elements")
    
    title = extract_title(text_data)
    print(f"Found title: {title}")
    
    outline = identify_heading_levels(text_data)
    print(f"Found {len(outline)} heading elements")

    output = {
        "title": title,
        "outline": outline
    }

    print(f"Writing output to: {output_path}")
    with open(output_path, "w", encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print("Done writing JSON file")

def main():
    if not os.path.exists(INPUT_PDF):
        print(f"Error: Input PDF not found at {INPUT_PDF}")
        return
    process_file(INPUT_PDF, OUTPUT_JSON)

if __name__ == "__main__":
    main()