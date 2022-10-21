import qrcode
from PIL import Image

qr= qrcode.QRCode(version=1,
               error_correction=qrcode.ERROR_CORRECT_H,
                box_size=10, border=4, )

qr.add_data("Wishing you and your family happiest diwali wishes ")   
qr.make(fit=True)
img=qr.make_image(fill_color="Blue", back_color="white")
img.save("Diwali_wish_updated.png")             