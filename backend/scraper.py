import fitz

def scraper_text(pdf):
    pages = fitz.open(stream=pdf.read(), filetype="pdf")

    sections = [
        "Summary", "Experience", "Education", "Contact", "Top Skills", "Languages", "Certifications", "Honors-Awards"
    ]

    parsed_resume = {section: [] for section in sections} #dictionary, creates list for each section

    left_column = ""
    right_column = ""
    name = ""

    width = pages[0].rect.width
    height = pages[0].rect.height

    name_rect = fitz.Rect(width / 3, 0, width, height / 12)

    name += pages[0].get_text("text", clip=name_rect)

    for page in pages:

        left_rect = fitz.Rect(0, 0, width / 3, height)
        right_rect = fitz.Rect(width / 3, 0, width, height)

        left_column += page.get_text("text", clip=left_rect)
        right_column += page.get_text("text", clip=right_rect)

    lines = left_column.splitlines() + right_column.splitlines()
    lines = [line.strip() for line in lines if line.strip()]

    current_section = ""

    for line in lines:
        if line in sections:
            current_section = line
        else:
            parsed_resume[current_section].append(line)

    # for section in parsed_resume:
    #     if section == "":
    #         parsed_resume.pop(section)

    return {
        "name": name,
        "contact": parsed_resume['Contact'],
        "summary": parsed_resume['Summary'],
        "experiences": parsed_resume['Experience'],
        "education": parsed_resume['Education'],
        "top-skills": parsed_resume['Top Skills'],
        "languages": parsed_resume['Languages'],
        "certifications": parsed_resume['Certifications'],
        "awards": parsed_resume['Honors-Awards'],
        "file-content": lines
    }
