#Programa para encontrar requests modulo.
# Sortida --> version, licencia,informacion copyright, autor, autor correo, documento url, titulo y descripcion

import requests

print("Python Requestsversion:",requests.__version__)
print("Licencia:",requests. __license__)
print("Informacion Copyright:",requests.__copyright__)
print("Autor:",requests.__author__)
print("Correo del autor",requests.__author_email__)
print("Document url:", requests.__url__)
print("Document titulo, ", requests.__title__)
print("Document  description:", requests.__description__)
