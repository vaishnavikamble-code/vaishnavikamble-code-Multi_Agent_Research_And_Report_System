from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def generate_pdf(report_text, filename="report.pdf"):

    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    for line in report_text.split("\n"):
        line = line.strip()

        if not line:
            continue

        content.append(Paragraph(line, styles["Normal"]))
        content.append(Spacer(1, 10))

    doc.build(content)

    return filename