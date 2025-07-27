import os
import json
from job_parser import parse_job_file
from text_splitter import extract_sections
from embedding import embed_text
from ranker import rank_sections
from json_formatter import format_output

INPUT_DIR = "input"
OUTPUT_DIR = "output"
JOB_FILE = os.path.join(INPUT_DIR, "job.txt")

def main():
    persona, job = parse_job_file(JOB_FILE)
    query = persona + " - " + job

    input_files = [f for f in os.listdir(INPUT_DIR) if f.endswith('.pdf')]
    all_sections = []

    for f in input_files:
        path = os.path.join(INPUT_DIR, f)
        sections = extract_sections(path)
        all_sections.extend(sections)

    # Embed query and sections
    query_embedding = embed_text([query])[0]
    section_texts = [s["section_text"] for s in all_sections]
    section_embeddings = embed_text(section_texts)

    # Rank and format output
    ranked = rank_sections(query_embedding, section_embeddings, all_sections)
    final_output = format_output(input_files, persona, job, ranked)

    # Write JSON
    with open(os.path.join(OUTPUT_DIR, "job_output.json"), "w", encoding="utf-8") as f:
        json.dump(final_output, f, indent=2)

if __name__ == "__main__":
    main()
