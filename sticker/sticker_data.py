from abc import ABC


class StickerData(ABC):
    def __init__(self, name, template_name):
        self.name = name
        self.template_name = template_name


class StickerDataNumber(StickerData):
    def __init__(self, name, template_name, value):
        super().__init__(name, template_name)
        self.value = value


class StickerDataText(StickerData):
    def __init__(self, name, template_name, value):
        super().__init__(name, template_name)
        self.value = value


class StickerDataDate(StickerData):
    def __init__(self, name, template_name, value):
        super().__init__(name, template_name)
        self.value = value


class StickerDataList(StickerData):
    def __init__(self, name, template_name, values):
        super().__init__(name, template_name)
        self.values = values
        self.selected_value = None
