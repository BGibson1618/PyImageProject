import pypdf
import sys

inputs = sys.argv[1:]

def pdf_merger(pdf_list):
    merger = pypdf.PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('pdfs/merge_file.pdf')

pdf_merger(inputs)