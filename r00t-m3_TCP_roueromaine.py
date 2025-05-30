import socket
import re
import codecs

# Connexion au serveur
host = "challenge01.root-me.org"
port = 52021

with socket.create_connection((host, port), timeout=3) as s:
    # Lecture de la question envoyée
    data = s.recv(2048).decode()
    print("[QUESTION REÇUE]")
    print(data.strip())

    # Extraction de la chaîne ROT13
    match = re.search(r"my string is '([^']+)'", data)
    if not match:
        print("[ERREUR] Chaîne non trouvée dans la question.")
        exit(1)

    encoded = match.group(1)
    print(f"[ENCODED] {encoded}")

    # Décodage ROT13
    decoded = codecs.decode(encoded, 'rot_13')
    print(f"[DECODED] {decoded}")

    # Envoi de la réponse
    s.sendall((decoded + "\n").encode())

    # Réception de la réponse du serveur
    try:
        response = s.recv(1024).decode().strip()
        print("[RÉPONSE DU SERVEUR]")
        print(response)
    except socket.timeout:
        print("[INFO] Pas de réponse du serveur.")
