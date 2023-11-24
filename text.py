# Extract text from PDF
import re
from pdfminer.high_level import extract_text

text = extract_text('document.pdf')

pattern = re.compile(r'[a-zA-Z]+')

matches = pattern.findall(text)

print(matches)