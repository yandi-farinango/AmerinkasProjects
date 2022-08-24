import docx

doc = docx.Document('Stones.docx')

for table in doc.tables:
    for row in table.rows:
        for cell in row.cells:
            if cell.paragraphs[1]:
                print(cell.paragraphs[1].text)
            else:
                continue

