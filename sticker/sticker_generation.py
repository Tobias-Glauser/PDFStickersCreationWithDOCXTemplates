import os
import time
from threading import Thread
from datetime import datetime

from docxtpl import DocxTemplate
from sticker.sticker_data import StickerDataNumber, StickerDataText, StickerDataDate, StickerDataList
from pdf_generation.pdf_generation import PDFGenerator


class StickerGenerator:
    thread = None

    @staticmethod
    def generate_sticker(sticker, save_file_path):
        if StickerGenerator.thread is not None and StickerGenerator.thread.is_alive():
            raise Exception('Already generating a sticker')

        time.sleep(1.5)
        main_path = os.path.join(os.getcwd(), "templates")
        template_path = os.path.join(main_path, sticker.template)
        print(main_path)
        template = DocxTemplate(template_path)

        to_fill_in = {}
        for data in sticker.data:
            if isinstance(data, StickerDataNumber) or isinstance(data, StickerDataText) or isinstance(data,
                                                                                                      StickerDataDate):
                to_fill_in[data.template_name] = data.value
            elif isinstance(data, StickerDataList):
                to_fill_in[data.template_name] = data.selected_value

        template.render(to_fill_in)
        template.save(save_file_path.replace(".pdf", ".docx"))

        StickerGenerator.thread = Thread(target=generate_pdf, args=[save_file_path])
        StickerGenerator.thread.start()


def generate_pdf(save_file_path):
    file_existed = os.path.exists(save_file_path)
    now = datetime.now()

    pdf_generator = PDFGenerator()
    pdf_generator.generate_pdf(save_file_path.replace(".pdf", ".docx"))
    timeout = 0
    while not ((os.path.exists(save_file_path) or file_existed) and now.timestamp() < os.path.getmtime(save_file_path)):
        time.sleep(0.1)
        print("Waiting for pdf generation...")
        timeout += 1
        if timeout > 100:
            raise Exception("Timeout while waiting for pdf generation")
        # if os.path.exists(save_file_path):
        #     print(os.path.exists(save_file_path), now.timestamp(), os.path.getctime(save_file_path))

    os.startfile(save_file_path)
    print("Sticker generated.")
