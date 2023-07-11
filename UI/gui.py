import customtkinter
from sticker.sticker_data import StickerDataNumber, StickerDataText, StickerDataDate, StickerDataList

customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    sticker_frame = None

    def __init__(self, stickers):
        super().__init__()
        self.stickers = stickers
        self.geometry("370x480")
        self.title("Etiquettes")
        # self.resizable(False, False)

        self.label = customtkinter.CTkLabel(self, text="Type d'autocollant", font=("Calibri", 30))
        self.label.pack(pady=10, padx=10, expand=False)

        self.combobox_stickers = customtkinter.CTkComboBox(self, values=(self.stickers.get_stickers_values()),
                                                           command=self.display_sticker, font=("Calibri", 24),
                                                           dropdown_font=("Calibri", 24), width=280)
        self.combobox_stickers.pack(pady=10, padx=10, expand=False)

    def display_sticker(self, choice):
        if self.stickers.selected_sticker is not None and choice == self.stickers.selected_sticker.name:
            return
        if self.sticker_frame is not None:
            self.sticker_frame.destroy()
            self.sticker_frame.pack_forget()
        self.stickers.selected_sticker = next(
            sticker for sticker in self.stickers.stickers_list if sticker.name == choice)
        print(choice, self.stickers.selected_sticker)
        self.sticker_frame = StickerFrame(self, self.stickers.selected_sticker)


class StickerFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, parent, sticker, **kwargs):
        super().__init__(parent, **kwargs, height=340, width=280)
        self.pack(pady=10, padx=10)
        self.sticker = sticker
        self.entries = []

        for data in self.sticker.data:
            if isinstance(data, StickerDataText):
                customtkinter.CTkLabel(self, text=data.name, font=("Calibri", 14)).pack(pady=0, padx=10, expand=False,
                                                                                        anchor="w")
                entry = customtkinter.CTkEntry(self, placeholder_text=data.name, width=280, font=("Calibri", 14))
                entry.pack(pady=(0, 10), padx=10)
                self.entries.append({
                    'entry': entry,
                    'data': data})
            elif isinstance(data, StickerDataNumber):
                customtkinter.CTkLabel(self, text=data.name, font=("Calibri", 14)).pack(pady=0, padx=10, expand=False,
                                                                                        anchor="w")
                entry = customtkinter.CTkEntry(self, placeholder_text=data.name,  width=280, font=("Calibri", 14))
                entry.pack(pady=(0, 10), padx=10)
                self.entries.append({
                    'entry': entry,
                    'data': data})
            elif isinstance(data, StickerDataDate):
                customtkinter.CTkLabel(self, text=data.name, font=("Calibri", 14)).pack(pady=0, padx=10, expand=False,
                                                                                        anchor="w")
                entry = customtkinter.CTkEntry(self, placeholder_text=data.name, width=280, font=("Calibri", 14))
                entry.pack(pady=(0, 10), padx=10)
                self.entries.append({
                    'entry': entry,
                    'data': data})
            elif isinstance(data, StickerDataList):
                customtkinter.CTkLabel(self, text=data.name, font=("Calibri", 14)).pack(pady=0, padx=10, expand=False,
                                                                                        anchor="w")
                entry = customtkinter.CTkComboBox(self, values=data.values, width=280, font=("Calibri", 14),
                                                  dropdown_font=("Calibri", 14))
                entry.pack(pady=(0, 10), padx=10)
                entry.set(data.values[0])
                self.entries.append({
                    'entry': entry,
                    'data': data})

        self.button = customtkinter.CTkButton(self, text="Générer", command=self.generate_sticker, width=280)
        self.button.pack(pady=10, padx=10)

    def generate_sticker(self):
        self.get_data()

        if not self.sticker.is_valid():
            return

        self.sticker.generate()

    def get_data(self):
        for thing in self.entries:
            if isinstance(thing['data'], StickerDataText):
                thing['data'].value = thing['entry'].get()
            elif isinstance(thing['data'], StickerDataNumber):
                thing['data'].value = thing['entry'].get()
            elif isinstance(thing['data'], StickerDataDate):
                thing['data'].value = thing['entry'].get()
            elif isinstance(thing['data'], StickerDataList):
                thing['data'].selected_value = thing['entry'].get()
