#pip install qrcode[pil]
import qrcode

#qr = qrcode.make('sister magret')
#qr.save('Myqrcode.png')

#generating qrcode image
qr = qrcode.QRCode(version=1,box_size=15,border=5)

#encoding link or information
data = 'https://youtube.com' #this could be a link or a string of information as required
qr.add_data(data)
qr.make(fit=True)

#styling qrcode
img = qr.make_image(fill = 'blue', back_color='white')

#saving image
img.save('videos.jpg')
