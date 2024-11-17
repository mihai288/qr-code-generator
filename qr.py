import qrcode
url = input()
qr_img = qrcode.make(url)
qr_img.save("qr_code.png")
