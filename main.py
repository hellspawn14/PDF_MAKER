from os import listdir
from fpdf import FPDF
from PIL import Image
from PyPDF2 import PdfMerger
from os import remove as del_file 

def merge_pdf_files(n_pdf_list, n_output_file):
    merger = PdfMerger()
    for pdf in n_pdf_list: 
        merger.append(pdf)
        del_file(pdf)

    merger.write(n_output_file)
    merger.close()

def convert_img_to_pdf(n_img_file, n_output_file):
    img_obj = Image.open(n_img_file)
    img_h, img_w = img_obj.size
    n_margin = 10
    n_padding = n_margin / 2 
    pdf = FPDF('P', 'mm', (img_h + n_margin, img_w + n_margin))
    pdf.add_page()
    pdf.image(n_img_file, x = n_padding, y = n_padding, w = img_h, h = img_w)
    pdf.output(n_output_file, 'F')

def convert(n_input_folder, n_output_file):
    base_path = './FILES'
    input_path, output_path = base_path + '/INPUT/' + n_input_folder, base_path + '/OUTPUT/' 
    output_file = output_path + n_output_file
    img_list = sorted(x for x in listdir(input_path) if not x.endswith('.DS_Store'))
    pdf_list = []
    for i in range(0, len(img_list)): 
        img_file = input_path + img_list[i]
        output_img_to_pdf_file = output_path + str(i) + '.pdf'
        pdf_list.append(output_img_to_pdf_file)
        convert_img_to_pdf(img_file, output_img_to_pdf_file)

    merge_pdf_files(pdf_list, output_file)

def bulk_convert(n_tasks): 
    for input_folder, output_file in n_tasks.items():
        convert(input_folder, output_file)

convert_tasks = {
    # 'Chainsaw Man v01 (2020) (Digital) (F) (LuCaZ)/': 'Chainsaw Man Vol - 01.pdf',
    # 'Chainsaw Man v02 (2020) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 02.pdf',
    # 'Chainsaw Man v03 (2021) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 03.pdf',
    # 'Chainsaw Man v04 (2021) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 04.pdf', 
    # 'Chainsaw Man v05 (2021) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 05.pdf', 
    # 'Chainsaw Man v06 (2021) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 06.pdf', 
    # 'Chainsaw Man v07 (2021) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 07.pdf', 
    # 'Chainsaw Man v08 (2021) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 08.pdf', 
    # 'Chainsaw Man v09 (2022) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 09.pdf', 
    # 'Chainsaw Man v10 (2022) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 10.pdf', 
    # 'Chainsaw Man v11 (2022) (Digital) (LuCaZ)/': 'Chainsaw Man Vol - 11.pdf'
    'Volume 01/': 'Persona 5 Vol - 01.pdf', 
    'Volume 02/': 'Persona 5 Vol - 02.pdf', 
    'Volume 03/': 'Persona 5 Vol - 03.pdf', 
    'Volume 04/': 'Persona 5 Vol - 04.pdf', 
    'Volume 05/': 'Persona 5 Vol - 05.pdf', 
    'Volume 06/': 'Persona 5 Vol - 06.pdf', 
    'Volume 07/': 'Persona 5 Vol - 07.pdf', 
    'Volume 08/': 'Persona 5 Vol - 08.pdf',
    'Volume 09/': 'Persona 5 Vol - 09.pdf'
}

bulk_convert(convert_tasks)
