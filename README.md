# split_pdf_with_unique_names
Split a PDF into multiple PDFs, by the given page range and a name assigned for each page range.

Create a text file with Page Range and their respective Names separated by tab space('\t'), similar to the text file in this repo. Feed in the name of PDF and text file in respective fields in the code(if there are spaces in the name, rename the file with _ in place of space )
If there are repeated Names, sequence them with serial numbers.
Some OSs allow only certain characters in their file names. I have customized the code to suit Windows OS. Check with your respective OS and edit the RegEx character string to match it.
