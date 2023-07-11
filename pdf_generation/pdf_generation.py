import os.path
import subprocess


class PDFGenerator:
    def __init__(self):
        self.libreoffice_path = "C:\\Users\\glautob\\Downloads\\LibreOfficePortable\\LibreOfficeWriterPortable.exe"

    def generate_pdf(self, save_directory_path, docx_file_path):

        command = "\"" + self.libreoffice_path + "\" --headless --convert-to pdf --outdir \"" + \
                  save_directory_path + "\" \"" + docx_file_path + "\""

        ret_code = subprocess.call(command)

        if ret_code == 0:
            print("PDF generated successfully")
        else:
            print("PDF generation failed")
