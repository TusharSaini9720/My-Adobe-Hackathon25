
# Adobe Hackathon - Round 1A: PDF Outline Extractor

## 📄 Overview
This project extracts a structured outline from PDF files, including:
- Title
- Headings (H1, H2, H3)
- Page numbers

It is designed to run offline in a Docker container as required by the Adobe Hackathon guidelines.

---

## 🧰 Tech Stack
- Python
- PyMuPDF (fitz)
- Docker

---

## 📁 Folder Structure
```
Round1A/
├── Dockerfile
├── main.py
├── extractor.py
├── pdf_parser.py
├── requirements.txt
├── input/          # Place your .pdf files here
└── output/         # Generated .json output will appear here
```

---

## 🚀 How to Run

### 1. Build Docker Image
```bash
docker build --platform linux/amd64 -t pdf-outline-extractor .
```

### 2. Run the Docker Container
```bash
docker run --rm -v $(pwd)/input:/app/input -v $(pwd)/output:/app/output --network none pdf-outline-extractor
```

> Input PDFs must be placed inside the `input/` folder. Output JSON files will be generated in the `output/` folder.

---

## 📦 Requirements
- Offline execution
- Model size ≤ 200MB (no external model used)
- Must complete within 10 seconds for 50-page PDF

---

## 📝 Notes
- No internet access is required.
- Works purely on layout and font size using PyMuPDF.
