import pyperclip
import qrcode

print('Before use, copy what you want to turn into qr-code')
print('To start click x\n')

inp = input()

if inp == 'x':
    filename = input('Enter filename for this qr\n')
    clipboard = pyperclip.paste()
    img = qrcode.make(clipboard)
    imgpath = r'folder path to save file'
    img.save(f'{imgpath}/{filename}.jpg')
else:
    print('That\'s not x')


