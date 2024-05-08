from PyPDF2 import PdfFileMerger

def merge_pdfs(pdf1_path, pdf2_path, output_path):
    merger = PdfFileMerger()
    merger.append(pdf1_path)
    merger.append(pdf2_path)
    merger.write(output_path)
    merger.close()

if __name__ == "__main__":
    pdf1_path = "input_pdf1.pdf"
    pdf2_path = "input_pdf2.pdf"
    output_path = "merged_output.pdf"
    merge_pdfs(pdf1_path, pdf2_path, output_path)
