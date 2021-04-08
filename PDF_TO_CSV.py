import tabula

# Read pdf into list of DataFrame
df = tabula.read_pdf("1900-028-TNA-p1965-12-c1-OCR.pdf", pages='all')

# convert PDF into CSV file
tabula.convert_into("1900-028-TNA-p1965-12-c1-OCR.pdf", "output.csv", output_format="csv", pages='all')

# convert all PDFs in a directory
tabula.convert_into_by_batch(".", output_format='csv', pages='all')