# split_pdf_with_unique_names
Split a PDF into multiple PDFs, by the given page range and a name assigned for each page range.

Create a text file with Page Range and their respective Names separated by tab space('\t'), similar to the text file in this repo. 
Program asks user for two inputs: PDF source file name/path name (.pdf), and text file name/path name containing page ranges and respective names(.txt).
Each OSs allow only certain characters in their file names. This code is customized to suit Windows OS. Check with your respective OS and edit the RegEx character string to match it. Such special characters are replaced with underscores.
If there are file names which occur more than once, page range is added at the end of such names in order to distinguish between such files and provide chronology.
