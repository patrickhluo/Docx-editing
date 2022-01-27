from docx import Document

# acquire text location
location = str(input('Please enter file location:'))
# location = '/Users/patrickluo/Documents/Coding/abc.docx'
# location = 'abc.docx'
doc = Document(location)

# acquire target text and replacing text
search_text =str(input('Please enter target text:'))
replace_text =str(input('Please enter replace text:'))

# loop
for paragraph in doc.paragraphs:
    print(paragraph)
    for run in paragraph.runs:
        print(run.text)
        if run.text.find(search_text) != -1:
            
            text = run.text
            text = text.replace(search_text,replace_text)
            print(text)
            run.text = text


doc.save(location)
