from fpdf import FPDF
import os

def convert_txt_to_pdf(txt_file, pdf_file):
    pdf = FPDF()
    pdf.add_page()
    
    with open(txt_file, 'r', encoding='utf-8') as file:
        text = file.read()

    text = text.encode("latin1", errors="replace").decode("latin1")

    pdf.set_font('Arial', size=12)
    pdf.multi_cell(0, 10, text)

    pdf.output(pdf_file)
def Convert(path):
    txt_files = []
    pdf_files = []
    
    # Get the path of all .txt files in the output folder
    for file in os.listdir(path):
        if file.endswith(".txt"):
            txt_files.append(os.path.join(path, file))
    
    # Generate the .pdf path for each .txt file
    for txt_file in txt_files:
        pdf_file = txt_file.replace(".txt", ".pdf")
        pdf_files.append(pdf_file)
    
    # Convert each .txt file to .pdf
    for i in range(len(txt_files)):
        convert_txt_to_pdf(txt_files[i], pdf_files[i])