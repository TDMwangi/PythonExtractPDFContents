# Extract table from PDF
import tabula

table = tabula.read_pdf('document.pdf', pages='all')

print(table[0])