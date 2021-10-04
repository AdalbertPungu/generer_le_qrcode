#importation de la bibliothèque qrcode
import qrcode
#dans la varible on stocke les données à encoder  
data = 'https://www.linkedin.com/in/AdalbertPungu/'
#generation de l'image
img = qrcode.make(data) 
#enreqistrement de l'image  
img.save('qrCode1.png')
