import PyPDF2
import argparse

def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page)
            text += page_obj.extractText()
    return text

def add_password(input_file, password, output_file=None):
    if not output_file:
        output_file = output_file.replace('.pdf', '-withpassword.pdf')
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page))
        pdf_writer.encrypt(password)
        with open(output_file, 'wb') as output:
            pdf_writer.write(output)

def remove_password(input_file, password, output_file=None):
    if not output_file:
        output_file = output_file.replace('.pdf', '-nopassword.pdf')
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()

        if pdf_reader.isEncrypted:
            pdf_reader.decrypt(password)

        for page in range(pdf_reader.numPages):
            pdf_writer.addPage(pdf_reader.getPage(page))
        with open(output_file, 'wb') as output:
            pdf_writer.write(output)

def rotate_pages(input_file, rotation, output_file=None):
    if not output_file:
        output_file = output_file.replace('.pdf', '-rotated.pdf')
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer = PyPDF2.PdfFileWriter()
        for page in range(pdf_reader.numPages):
            page_obj = pdf_reader.getPage(page)
            page_obj.rotateClockwise(rotation)
            pdf_writer.addPage(page_obj)
        with open(output_file, 'wb') as output:
            pdf_writer.write(output)

def split_pdf(input_file, output_path):
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        for page in range(pdf_reader.numPages):
            pdf_writer = PyPDF2.PdfFileWriter()
            pdf_writer.addPage(pdf_reader.getPage(page))
            output_file = f'{output_path}/page_{page+1}.pdf'
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)

def split_pdf_at_page(input_file, split_page, output_file_1=None, output_file_2=None):
    if not output_file_1:
        output_file = output_file_1.replace('.pdf', '-1.pdf')
    if not output_file_2:
        output_file = output_file_1.replace('.pdf', '-2.pdf')
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        pdf_writer_1 = PyPDF2.PdfFileWriter()
        pdf_writer_2 = PyPDF2.PdfFileWriter()
        for page in range(split_page):
            pdf_writer_1.addPage(pdf_reader.getPage(page))
        for page in range(split_page, pdf_reader.numPages):
            pdf_writer_2.addPage(pdf_reader.getPage(page))
        with open(output_file_1, 'wb') as output:
            pdf_writer_1.write(output)
        with open(output_file_2, 'wb') as output:
            pdf_writer_2.write(output)

def merge_pdfs(input_files, output_file=None):
    if not output_file:
        output_file = input_files[0].replace('.pdf', '-merged.pdf')
    merger = PyPDF2.PdfFileMerger()
    for input_file in input_files:
        merger.append(input_file)
    merger.write(output_file)
    merger.close()

def read_metadata(input_file):
    with open(input_file, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)
        metadata = pdf_reader.getDocumentInfo()
    return metadata