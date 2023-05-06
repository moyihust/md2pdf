import os
import sys
import markdown2
from weasyprint import HTML, CSS
from io import BytesIO


def markdown_to_pdf(input_file, output_file, css_file=None):
    with open(input_file, "r", encoding="utf-8") as md_file:
        md_content = md_file.read()

    # Convert markdown to HTML
    html_content = markdown2.markdown(md_content)

    # Add HTML tags
    html_content = f"<html><body>{html_content}</body></html>"

    # Convert HTML to PDF using WeasyPrint
    html_doc = HTML(string=html_content)

    if css_file:
        with open(css_file, "r", encoding="utf-8") as css:
            css_content = css.read()
        css_doc = CSS(string=css_content)
        html_doc.write_pdf(output_file, stylesheets=[css_doc])
    else:
        html_doc.write_pdf(output_file)

    print(f"Successfully converted {input_file} to {output_file}.")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python markdown_to_pdf.py <input_file.md> <output_file.pdf> [<css_file.css>]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    if len(sys.argv) == 4:
        css_file = sys.argv[3]
        if not os.path.exists(css_file):
            print(f"Error: {css_file} does not exist.")
            sys.exit(1)
    else:
        css_file = None

    if not os.path.exists(input_file):
        print(f"Error: {input_file} does not exist.")
        sys.exit(1)

    markdown_to_pdf(input_file, output_file, css_file)