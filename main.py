# Valentin Gourjon*
# 18/02/2023

# Objectif : QR code wifi sécurisé

import os
import qrcode

# Variables du wifi

# Type d'authentification : 'WPA', 'WEP', ou '' si aucun mot de passe
auth = ''
# Nom du réseau (SSID)
network_name = ''
# Mot de passe du réseau
network_pwd = ''
# Réseau caché ? True or False
hidden = False


inp = ' '
while inp.upper() not in ['WPA', 'WEP', '']:
    inp = input("Entrez le type d'authentification : (WPA, WEP ou laisser vide si pas de code) ")
auth = inp.upper()

network_name = input("Entrez le nom du réseau(SSID) : ")

if auth != '':
    network_pwd = input("Saississez le mot de passe du réseau wifi: ")

while inp not in ("Oui", "Non"):
    inp = input("Le réseau est-il caché ? (Oui/Non) ")
hidden = True if inp == "Oui" else False


qr_string = 'WIFI:'
if auth != '':
    qr_string += f"T:{auth};"
qr_string += f"S:{network_name};"
if auth != '':
    qr_string += f"P:{network_pwd};"
if hidden:
    qr_string += "H:true;"

code = qrcode.make(qr_string)
code_path = f'Wifi_QR_{network_name}.png'

code.save(code_path)

print(f"Le QR code à été créer. Il est disponible à l'adresse {os.path.abspath(code_path)}")