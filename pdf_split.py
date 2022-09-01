from PyPDF2 import PdfFileReader, PdfFileWriter

pdf_file_path = 'Back_packs_BCP_1372.pdf'   # enter name of the PDF file to be extracted from
file_base_name = pdf_file_path.replace('Back_packs_BCP_1372.pdf', '')

pdf = PdfFileReader(pdf_file_path)

totalpages = pdf.numPages
print("Total number of pages in the pdf: ", totalpages)
pgs = []
with open("page_range.txt", "r") as f:  # enter the name of text file which contains list of Page Range and their respective Names separated by tab space("\t")
    lines = f.readlines()
for line in lines:
    pg = line.split("\t")
    pgs.append(pg)
for x in pgs:
    for l in x:
        e = x[0]
        pg_range = e.split("-")
        for y in pg_range:
            m = int(pg_range[0])
            n = int(pg_range[1])
            string = x[1]
            new_name = string.strip('\n')
            pages = []
            for p in range(m,n+1):
                pages.append(p-1)

            pdfWriter = PdfFileWriter()
            for page_num in pages:
                pdfWriter.addPage(pdf.getPage(page_num))

            with open(f'{new_name}.pdf', 'wb') as f:
                pdfWriter.write(f)
                f.close()
