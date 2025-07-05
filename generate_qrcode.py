import qrcode

data=input("enter text or url: ").strip()
filename=input("enter filename to save qr code: ").strip()
qr=qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
image=qr.make_image(fill_color="black", back_color="white")
image.save(filename)
print(f"QR code saved as {filename}")

