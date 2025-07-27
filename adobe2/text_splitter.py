import PyPDF2
import re

def extract_sections(pdf_path):
    """
    Extract sections from a PDF file.
    
    Args:
        pdf_path (str): Path to the PDF file
        
    Returns:
        list: List of dictionaries containing section information
    """
    sections = []
    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            
            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                
                # Split text into sections (you can modify this logic based on your PDF structure)
                section_texts = text.split('\n\n')  # Split on double newlines
                
                for section_text in section_texts:
                    if section_text.strip():  # Skip empty sections
                        # Create section dictionary
                        section = {
                            "document": pdf_path,
                            "page": page_num + 1,
                            "section_title": get_section_title(section_text),
                            "section_text": clean_text(section_text)
                        }
                        sections.append(section)
                        
        return sections
    
    except FileNotFoundError:
        raise FileNotFoundError(f"PDF file not found at: {pdf_path}")
    except Exception as e:
        raise Exception(f"Error processing PDF file: {str(e)}")

def get_section_title(text):
    """Extract a title from the section text."""
    lines = text.split('\n')
    return lines[0] if lines else "Untitled Section"

def clean_text(text):
    """Clean and normalize text."""
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove special characters
    text = re.sub(r'[^\w\s.,!?-]', '', text)
    return text.strip()

# Make functions available for import
__all__ = ['extract_sections']