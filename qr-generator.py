import qrcode

# myPage = "https://github.com/muhreyhan"

myPage = input("Your Page URL : ")

myQr = qrcode.QRCode(version=1,
                     box_size=10,
                     border=5)

myQr.add_data(myPage)
myQr.make(fit=True)

img = myQr.make_image()
img.save('myPageQr.png')

