from collections import Counter

def identify_heading_levels(text_data):
    """Identify heading levels based on font sizes."""
    # Count font sizes for text entries longer than 2 chars
    size_counter = Counter(entry["size"] for entry in text_data if len(entry["text"].strip()) > 2)
    
    # Get sorted font sizes
    size_ranking = [size for size, _ in size_counter.most_common()]
    size_to_level = {}
    
    # Map top 3 sizes to heading levels
    if len(size_ranking) >= 3:
        size_to_level[size_ranking[0]] = "H1"
        size_to_level[size_ranking[1]] = "H2"
        size_to_level[size_ranking[2]] = "H3"
    
    outline = []
    for entry in text_data:
        level = size_to_level.get(entry["size"])
        if level and entry["text"].strip():
            outline.append({
                "level": level,
                "text": entry["text"].strip(),
                "page": entry["page"]
            })
    
    return outline

def extract_title(text_data):
    """Extract document title from first page."""
    # Get first page entries
    first_page_data = [entry for entry in text_data 
                      if entry["page"] == 1 and entry["text"].strip()]
    
    if not first_page_data:
        return "Untitled"
    
    # Find largest font size on first page
    largest_font = max(first_page_data, key=lambda x: x["size"])["size"]
    
    # Get text with largest font size
    candidates = [entry["text"] for entry in first_page_data 
                 if entry["size"] == largest_font]
    
    return candidates[0] if candidates else "Untitled"