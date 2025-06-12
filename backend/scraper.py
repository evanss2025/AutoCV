import fitz

def scraper_text(pdf):
    print("scraper text running")
    pages = fitz.open(stream=pdf.read(), filetype="pdf")

    left_column = ""
    right_column = ""

    for page in pages:
        width = page.rect.width

        left_rect = fitz.Rect(0, 0, width / 3, page.rect.height)
        right_rect = fitz.Rect(width / 3, 0, width, page.rect.height)

        left_column += page.get_text("text", clip=left_rect)
        right_column += page.get_text("text", clip=right_rect)

        left_column.strip()
        right_column.strip()

    lines = left_column.splitlines() + right_column.splitlines()
    lines = [line.strip() for line in lines if line.strip()]

    contact = lines[1]

    return {
        "name": "scraper name",
        "contact": contact,
        "experiences": [],
    }
