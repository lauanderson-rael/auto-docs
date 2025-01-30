from fillpdf import fillpdfs

campos = list(fillpdfs.get_form_fields('edit2.pdf').keys())

print(campos)