import os, sys, PyPDF2
from PyPDF2 import PdfReader, PdfWriter, PdfMerger


def main():
    inp_path = './input/'
    # inp_dir_list = sys.argv()
    inp_dir_list = os.listdir(inp_path)
    pdfMerger = PdfMerger()
    filename = ''
    for i,v in enumerate(inp_dir_list):
        if v.endswith('.pdf'):
            print(i)
            print(inp_dir_list)
            filename += v.split('.')[0] + ("_" if i < len(inp_dir_list)-1 else "")
            pdfMerger.append(inp_path+v)
    print(filename)
    pdfMerger.write(open('./result/{}.pdf'.format(filename),'wb'))
    return

if __name__ == '__main__':
    main()