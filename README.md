## Générer du code QR avec Python

Python a une bibliothèque « qrcode » pour générer des images de code QR. Il peut être installé à l’aide de pip

### Etape 1: Installation de la bibliothèque qrcode

```python
pip installer qrcode
```
### Etape 2: Générer un qrcode 

* importé la bibliothèque qrcode
* Créez un Qrcode en utilisant la fonction make()
* qrcode.make() pour créer un qrcode et il renvoie un objet PilImage. Enregistrer dans l’image
```python
qrcode.make('Données à encoder')
```
### Exemple 1

```python

#importation de la bibliothèque qrcode
import qrcode
#dans la varible on stocke les données à encoder  
data = 'https://www.linkedin.com/in/AdalbertPungu/'
#generation de l'image
img = qrcode.make(data) 
#enreqistrement de l'image  
img.save('qrCode1.png')

```
### Exemple 2

```python

#importation de la bibliothèque qrcode
import qrcode 
#dans la varible on stocke les données à encoder
data = "Follow me on Linkedin: https://www.linkedin.com/in/AdalbertPungu/"
  
qr = qrcode.QRCode(version = 1, 
                   box_size = 5, 
                   border = 5) 
# La méthode add_data() est utilisée pour ajouter des données à l’objet QRCode. 
# Il prend les données à encoder en tant que paramètre.
qr.add_data(data) 

# La méthode make(fit = True) garantit que toute la dimension du QR Code est utilisée, 
# même si nos données d’entrée peuvent tenir dans moins de cases.
qr.make(fit = True)

# Ont convertie convertir l’objet QRCode en un fichier image à l'aide de la méthode
# make_image() et en définissent la couleur de premier plan et d’arrière-plan
img = qr.make_image(fill_color = 'black', 
                    back_color = 'white') 
#enreqistrement de l'image
img.save('qrCode2.png')

```
