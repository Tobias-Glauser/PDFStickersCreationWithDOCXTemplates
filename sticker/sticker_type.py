from sticker.sticker_data import StickerDataNumber, StickerDataText, StickerDataDate, StickerDataList
from sticker.sticker_generation import StickerGenerator
import os


class StickerType:
    """This object represents a sticker."""

    def __init__(self, name, template, data):
        self.name = name
        self.template = template
        self.data = data

    def __str__(self):
        return self.name

    def is_valid(self):
        for data in self.data:
            if isinstance(data, StickerDataText):
                if data.value is None or data.value == "":
                    return False
            elif isinstance(data, StickerDataNumber):
                if data.value is None or data.value == "":
                    return False
            elif isinstance(data, StickerDataDate):
                if data.value is None or data.value == "":
                    return False
            elif isinstance(data, StickerDataList):
                if data.selected_value is None or data.selected_value == "" or data.selected_value not in data.values:
                    return False
        return True

    def generate(self, save_file_path):
        print(save_file_path)
        try:
            sticker_generator = StickerGenerator()
            sticker_generator.generate_sticker(self, save_file_path)
        except Exception as e:
            print(e)
            return
