class Stickers:
    def __init__(self, stickers=None):
        if stickers is None:
            self.stickers_list = []
        else:
            self.stickers_list = stickers
        self.selected_sticker = None

    def get_stickers_values(self):
        return [str(sticker.name) for sticker in self.stickers_list]

    def add_sticker(self, sticker):
        self.stickers_list.append(sticker)

    def remove_sticker(self, sticker):
        self.stickers_list.remove(sticker)
