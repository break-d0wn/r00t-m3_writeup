import socket
import base64
import re

host = "challenge01.root-me.org"
port = 52023

with socket.create_connection((host, port), timeout=3) as s:
    # Recevoir les données
    data = s.recv(2048).decode()
    print("[QUESTION REÇUE]")
    print(data.strip())

    # Chercher la ligne avec la chaîne encodée
    match = re.search(r"my string is '([^']+)'", data)
    if not match:
        print("[ERREUR] Chaîne non trouvée.")
        exit(1)

    encoded = match.group(1)
    print(f"[ENCODED] {encoded}")

    try:
        decoded = base64.b64decode(encoded).decode()
        print(f"[DECODED] {decoded}")
    except Exception as e:
        print(f"[ERREUR DÉCODAGE] {e}")
        exit(1)

    # Envoyer la réponse décodée
    s.sendall((decoded + "\n").encode())

    # Lire la réponse du serveur
    try:
        response = s.recv(1024).decode().strip()
        print("[RÉPONSE DU SERVEUR]")
        print(response)
    except socket.timeout:
        print("[INFO] Pas de réponse après envoi.")
