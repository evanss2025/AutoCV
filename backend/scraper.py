import fitz
from experiences import parse_experiences_with_ai

def scraper_text(pdf):
    pages = fitz.open(stream=pdf.read(), filetype="pdf")

    sections = [
        "Summary", "Experience", "Education", "Contact", "Top Skills",
        "Languages", "Certifications", "Honors-Awards"
    ]
    parsed_resume = {section: [] for section in sections}

    width = pages[0].rect.width
    height = pages[0].rect.height
    name_rect = fitz.Rect(width / 3, 0, width, height / 12)
    name = pages[0].get_text("text", clip=name_rect).strip()

    all_left_lines, all_right_lines = [], []
    for i, page in enumerate(pages):
        left_rect = fitz.Rect(0, 0, width / 3, height)
        if i == 0:
            right_rect = fitz.Rect(width / 3, height / 7, width, height)
        else:
            right_rect = fitz.Rect(width / 3, 0, width, height)
        all_left_lines += [line.strip() for line in page.get_text("text", clip=left_rect).splitlines() if line.strip()]
        all_right_lines += [line.strip() for line in page.get_text("text", clip=right_rect).splitlines() if line.strip()]
    lines = all_left_lines + all_right_lines

    current_section = ""
    for line in lines:
        if "page" in line.lower():
            continue
        if line in sections:
            current_section = line
        else:
            parsed_resume[current_section].append(line)

    if "" in parsed_resume:
        parsed_resume.pop("")

    experience_lines = parsed_resume.get("Experience", [])
    experience_text = "\n".join(experience_lines)
    structured_experiences = parse_experiences_with_ai(experience_text)

    parsed_resume["Experience"] = structured_experiences

    return {
        "name": name,
        "contact": parsed_resume.get("Contact", []),
        "summary": parsed_resume.get("Summary", []),
        "experiences": parsed_resume.get("Experience", []),
        "education": parsed_resume.get("Education", []),
        "skills": parsed_resume.get("Top Skills", []),
        "languages": parsed_resume.get("Languages", []),
        "certifications": parsed_resume.get("Certifications", []),
        "awards": parsed_resume.get("Honors-Awards", []),
        "file-content": lines
    }