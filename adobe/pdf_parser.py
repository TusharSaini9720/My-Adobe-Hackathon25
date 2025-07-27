import fitz

def extract_text_with_fonts(pdf_path):
    """Extract text with font information from PDF."""
    doc = fitz.open(pdf_path)
    text_data = []
    
    for page_num, page in enumerate(doc, 1):
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" in block:
                for line in block["lines"]:
                    for span in line["spans"]:
                        text_data.append({
                            "text": span["text"],
                            "font": span["font"],
                            "size": span["size"],
                            "flags": span["flags"],
                            "page": page_num  # Add page number
                        })
    return text_data