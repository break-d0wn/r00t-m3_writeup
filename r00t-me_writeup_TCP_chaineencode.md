# Challenge : TCP - Chaîne encodée

## Description
Un serveur TCP nous envoie une chaîne encodée en Base64. Il faut la décoder et renvoyer le contenu clair dans un délai de 2 secondes.

## Connexion
- Host : challenge01.root-me.org
- Port : 52023

## Solution
Connexion via socket, extraction de la chaîne encodée, décodage avec base64, réponse envoyée.

## Script
Voir : `tcp_string_decode.py`

