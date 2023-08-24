import argparse
from pyPDFTool import read_pdf, add_password, remove_password, rotate_pages, split_pdf, merge_pdfs, split_pdf_at_page, read_metadata

def main():
    # Create an ArgumentParser object with a custom description and epilog
    parser = argparse.ArgumentParser(
        description='PDF Modification Tool',
        epilog='Example usage: python pdf_tool.py read example.pdf'
    )
    # Create a subparsers object to handle subcommands
    subparsers = parser.add_subparsers(dest='command')

    # define commands and arguments
    read_parser = subparsers.add_parser('read', help='Read a PDF file')
    read_parser.add_argument('input_file', help='Path to the input PDF file')

    add_password_parser = subparsers.add_parser('add_password', help='Password protect a PDF file')
    add_password_parser.add_argument('input_file', help='Path to the input PDF file')
    add_password_parser.add_argument('password', help='Password to protect the PDF file with')
    add_password_parser.add_argument('--output_file', help='Path to the output PDF file')

    remove_password_parser = subparsers.add_parser('remove_password', help='Remove password from a PDF file')
    remove_password_parser.add_argument('input_file', help='Path to the input PDF file')
    remove_password_parser.add_argument('password', help='Password of the input PDF file')
    remove_password_parser.add_argument('--output_file', help='Path to the output PDF file')

    rotate_pages_parser = subparsers.add_parser('rotate_pages', help='Rotate pages of a PDF file')
    rotate_pages_parser.add_argument('input_file', help='Path to the input PDF file')
    rotate_pages_parser.add_argument('rotation', type=int, help='Angle to rotate the pages by (in degrees)')
    rotate_pages_parser.add_argument('--output_file', help='Path to the output PDF file')

    split_pdf_parser = subparsers.add_parser('split_pdf', help='Split a PDF into multiple files')
    split_pdf_parser.add_argument('input_file', help='Path to the input PDF file')
    split_pdf_parser.add_argument('output_path', help='Path to the directory where the output files will be saved')

    merge_pdfs_parser = subparsers.add_parser('merge_pdfs', help='Merge multiple PDF files into one')
    merge_pdfs_parser.add_argument('input_files', nargs='+', help='Paths to the input PDF files')
    merge_pdfs_parser.add_argument('--output_file', help='Path to the output PDF file')

    split_pdf_at_page_parser = subparsers.add_parser('split_pdf_at_page', help='Split a PDF at a specific page')
    split_pdf_at_page_parser.add_argument('input_file', help='Path to the input PDF file')
    split_pdf_at_page_parser.add_argument('split_page', type=int, help='Page number at which to split the PDF (starting from 0)')
    split_pdf_at_page_parser.add_argument('--output_file_1', help='Path to the first output PDF file')
    split_pdf_at_page_parser.add_argument('--output_file_2', help='Path to the second output PDF file')

    read_metadata_pearser = subparsers.add_parser('read_metadata', help='Read metadata of a PDF file')
    read_metadata_pearser.add_argument('input_file', help='Path to the input PDF file')
    
    # Parse the command line arguments
    args = parser.parse_args()

    # call function corresponding to the argument
    if args.command == 'read':
        text = read_pdf(args.input_file)
        print(text)
    elif args.command == 'add_password':
        output_file = args.output_file
        add_password(args.input_file, args.password, output_file)
    elif args.command == 'remove_password':
        output_file = args.output_file
        remove_password(args.input_file, args.password, output_file)
    elif args.command == 'rotate_pages':
        output_file = args.output_file
        rotate_pages(args.input_file, args.rotation, output_file)
    elif args.command == 'split_pdf':
        split_pdf(args.input_file, args.output_path)
    elif args.command == 'merge_pdfs':
        output_file = args.output_file if args.output_file else args.input_files[0].replace('.pdf', 'Test.pdf')
        merge_pdfs(args.input_files, output_file)
    elif args.command == 'split_pdf_at_page':
        output_file_1 = args.output_file_1 if args.output_file_1 else f'{args.input_file.replace(".pdf", "")}_part1.pdf'
        output_file_2 = args.output_file_2 if args.output_file_2 else f'{args.input_file.replace(".pdf", "")}_part2.pdf'
        split_pdf_at_page(args.input_file, output_file_1, output_file_2, args.split_page)
    elif args.command == 'read_metadata':
        metadata = read_metadata(args.input_file)
        for key, value in metadata.items():
            print(f'{key}: {value}')

if __name__ == '__main__':
    main()
