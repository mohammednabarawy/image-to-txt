import img2pdf
import os
import subprocess
import markdown2


def convert_image_to_text(image_path, output_dir, batch_multiplier=2, max_pages=10, languages='English,Arabic'):
    # Step 1: Convert the image to PDF
    pdf_path = os.path.join(output_dir, 'output.pdf')
    with open(image_path, 'rb') as img_file:
        pdf_bytes = img2pdf.convert(img_file)
        with open(pdf_path, 'wb') as pdf_file:
            pdf_file.write(pdf_bytes)
    print(f"{image_path} Converted  to PDF: {pdf_path}")

    # Step 2: Use Marker to convert the PDF to markdown with OCR for English and Arabic
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
    markdown_path = os.path.join(output_dir, 'output', 'output.md')
    text_path = os.path.join(output_dir, 'output.txt')
    try:
        with open(markdown_path, 'r', encoding='utf-8') as md_file:
            markdown_content = md_file.read()
        text_content = markdown2.markdown(markdown_content)
        with open(text_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content)
        print(f"Converted {markdown_path} to Text: {text_path}")
    except Exception as e:
        print(f"Error converting markdown to text: {e}")
