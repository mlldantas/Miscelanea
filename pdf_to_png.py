import os
from pdf2image import convert_from_path

path = './'

pdf_page = convert_from_path(os.path.join(path, 'mypdf.pdf'), 500)

for page in pdf_page:
    page.save(os.path.join(path, 'mypng.png'), 'PNG')

# check if loop is really necessary
