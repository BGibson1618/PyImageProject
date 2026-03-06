import pypdf
import sys

orig_pdf = sys.argv[1]

def pdf_water_mark(pdf):
    mark = pypdf.PdfReader('pdfs/wtr.pdf').pages[0]
    writer = pypdf.PdfWriter(pdf)
    for page in writer.pages:
        page.merge_page(mark, over=False)
    writer.write('pdfs/out_watermark.pdf')

pdf_water_mark(orig_pdf)