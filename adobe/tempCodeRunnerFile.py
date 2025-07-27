import os
import json
from pdf_parser import extract_text_with_fonts  
from extractor import identify_heading_levels, extract_title


INPUT_PDF = r"C:\Users\krish\Downloads\6874faecd848a_Adobe_India_Hackathon_-_Challenge_Doc.pdf"
OUTPUT_JSON = r"C:\Users\krish\Downloads\abc.json"

def process_file(pdf_path, output_path):
    text_data = extract_text_with_fonts(pdf_path)
    title = extract_title(text_data)
    outline = identify_heading_levels(text_data)

    output = {
        "title": title,
        "outline": outline
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

def main():
    process_file(INPUT_PDF, OUTPUT_JSON)

if __name__ == "__main__":
    main()