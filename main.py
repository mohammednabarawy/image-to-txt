import img2pdf
import os
import subprocess
import markdown2

# Step 1: Convert the image to PDF


def image_to_pdf(image_path, pdf_path):
    with open(image_path, 'rb') as img_file:
        pdf_bytes = img2pdf.convert(img_file)
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_bytes)
    print(f"Converted {image_path} to PDF: {pdf_path}")

# Step 2: Use Marker to convert the PDF to markdown with OCR for English and Arabic


def pdf_to_markdown(pdf_path, output_dir, batch_multiplier=2, max_pages=10, languages='English,Arabic'):
    try:
        subprocess.run([
            'marker_single',
            pdf_path,
            output_dir,
            '--batch_multiplier', str(batch_multiplier),
            '--max_pages', str(max_pages),
            '--langs', languages,
        ], check=True)
        print(f"Converted {pdf_path} to Markdown")
    except subprocess.CalledProcessError as e:
        print(f"Error during Marker conversion: {e}")

# Step 3: Convert markdown to text


def markdown_to_text(markdown_path, text_path):
    try:
        with open(markdown_path, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()
        text_content = markdown2.markdown(markdown_content)
        with open(text_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)
        print(f"Converted {markdown_path} to Text: {text_path}")
    except Exception as e:
        print(f"Error converting markdown to text: {e}")


# Paths to input and output files
image_path = r'D:\original\coding\marker-pdf\02.jpg'  # Path to your image file
pdf_path = 'output.pdf'         # Path to the generated PDF file
# Use the current working directory as the output folder
output_dir = os.getcwd()
# Path to the generated markdown file
markdown_path = os.path.join(os.path.join(output_dir, 'output'), 'output.md')
# Path to the generated text file
text_path = os.path.join(output_dir, 'output.txt')

# Perform the conversions
image_to_pdf(image_path, pdf_path)
pdf_to_markdown(pdf_path, output_dir)
markdown_to_text(markdown_path, text_path)

print("Process completed.")
