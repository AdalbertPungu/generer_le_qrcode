## Générer du code QR avec le Python

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