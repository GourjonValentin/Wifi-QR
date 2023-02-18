# Valentin Gourjon*
# 18/02/2023

# Objectif : QR code wifi sécurisé

import qrcode

# Variables du wifi

# Type d'authentification : 'WPA', 'WEP', ou '' si aucun mot de passe
auth = 'WPA'
# Nom du réseau (SSID)
network_name = ''
# Mot de passe du réseau
network_pwd = ''
# Réseau caché ? True or False
hidden = False

qr_string = 'WIFI:'
if auth not in ('', None):
    qr_string += f"T:{auth};"
qr_string += f"S:{network_name};"
if auth not in ('', None):
    qr_string += f"P:{network_pwd};"
if hidden:
    qr_string += "H:true;"


code = qrcode.make(qr_string)

code.save(f"wifi_qr_{network_name}.png")