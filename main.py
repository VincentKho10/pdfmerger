import os, sys, PyPDF2
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


def main():
    inp_path = './input/'
    os.makedirs(inp_path, exist_ok=True)
    # inp_dir_list = sys.argv()
    inp_dir_list = os.listdir(inp_path)
    if len(inp_dir_list) == 0:
        return
    pdfMerger = PdfMerger()
    for i,v in enumerate(inp_dir_list):
        if v.endswith('.pdf'):
            pdfMerger.append(inp_path+v)
    pdfMerger.write(open('result.pdf','wb'))
    return

if __name__ == '__main__':
    main()