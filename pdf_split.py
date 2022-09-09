from PyPDF2 import PdfFileReader, PdfFileWriter
import re

def pdf_split_mult(pdf_file_path, text_file):
    pdf_file_path.replace(pdf_file_path, '')
    pdf = PdfFileReader(pdf_file_path)
    totalpages = pdf.numPages
    print("Total number of pages in the pdf: ", totalpages)  # prints total number of pages in the source PDF
    
    pgs = []
    with open(text_file, "r") as f:   # enter text file containing page range and names
        lines = f.readlines()
    for line in lines:
        pg = line.split("\t")  # splits page range and respective names into list
        pgs.append(pg)
    df = []
    for c in pgs:
        tr = c[1].strip('\n')
        df.append(tr)
        
    for x in pgs:
        for l in x:
            e = x[0]
            pg_range = e.split("-")  # splits page range into individual pages into a list
            for y in pg_range:
                if len(pg_range)==2:
                    m = int(pg_range[0])
                    n = int(pg_range[1])  # if page range is multiple page
                else:
                    m = int(pg_range[0])
                    n = m                 # if single page 
                string = x[1]
                name = string.strip('\n')
                new_name = re.sub("[/\?*:|<>]", "_", name)  # to recognize and replace characters not supported in files by windows
                pages = []                                  # supported characters depends on the respective OS
                for p in range(m,n+1):
                    pages.append(p-1)

                pdfWriter = PdfFileWriter()
                for page_num in pages:
                    pdfWriter.addPage(pdf.getPage(page_num))

                if df.count(name)==1:                   # checks if similar file names are present
                    with open(f'{new_name}.pdf', 'wb') as f:
                        pdfWriter.write(f)
                        f.close()
                else:
                    with open(f'{new_name}({m}-{n}).pdf', 'wb') as f:  # adds starting and ending page numbers if names are repeated
                        pdfWriter.write(f)
                        f.close()

if __name__ == '__main__':
    a = input("Enter source PDF file name/path: ")
    b = input("Enter text file name/path: ")
    try:
        pdf_split_mult(a,b)
    except:
        print("->Enter valid File Name/Path Address")
        print("->Make sure the Page Range and respective File Names in\n  text file are separated by single tab space")
