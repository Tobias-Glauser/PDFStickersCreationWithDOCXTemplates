import json

from UI.gui import App
from sticker.stickers import Stickers
from sticker.sticker_data import StickerDataNumber, StickerDataText, StickerDataDate, StickerDataList
from sticker.sticker_type import StickerType

data = json.load(open('model/data.json', encoding='utf-8-sig'))
print(data)

stickers = Stickers()
for sticker in data:
    print(sticker)
    datas = []
    for data in sticker['data']:
        print(data)
        if data['type'] == 'number':
            datas.append(StickerDataNumber(data['name'], data['template_name'], None))
        elif data['type'] == 'text':
            datas.append(StickerDataText(data['name'], data['template_name'], None))
        elif data['type'] == 'date':
            datas.append(StickerDataDate(data['name'], data['template_name'], None))
        elif data['type'] == 'list':
            datas.append(StickerDataList(data['name'], data['template_name'], data['values']))

    stickers.add_sticker(StickerType(sticker['name'], sticker['template'], datas))

app = App(stickers)
app.mainloop()
