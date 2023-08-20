# PyPDFTool

This is a Python tool for modifying PDF files. It includes the following functionalities:
- Reading a PDF file
- Extracting text from a PDF
- Password protecting a PDF
- Removing password from a PDF
- Rotating pages of a PDF
- Splitting a PDF into multiple files
- Splitting a PDF at a specific page
- Merging multiple PDF files into one
- Reading metadata of a PDF

## Installation

To use this tool, you need to have Python 3 installed on your computer. You also need to install the required libraries by running the following command in your command prompt or terminal:

```
pip install PyPDF2 Pillow
```

## Usage

To use this tool, you need to import the functions from the script and call them with the appropriate arguments. Here's an example of how to use the `read_pdf` function to read the text from a PDF file:

```python
from pyPDFTool import read_pdf

text = read_pdf('example.pdf')
print(text)
```

You can find more detailed information on how to use each function in the docstrings of the functions in the script.