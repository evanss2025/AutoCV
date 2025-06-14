import fitz

def scraper_text(pdf):
    print("scraper text running")
    pages = fitz.open(stream=pdf.read(), filetype="pdf")

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

    contact = lines[1]

    return {
        "name": name,
        "contact": contact,
        "experiences": [],
        "file-content": lines
    }
