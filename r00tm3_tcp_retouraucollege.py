import socket
import re
import math


def extract_numbers(calculation_line):
    """Extrait les deux nombres de la ligne de calcul."""
    pattern = r"square root of (\d+(?:\.\d+)?) and multiply by (\d+(?:\.\d+)?)"
    match = re.search(pattern, calculation_line)
    if match:
        return float(match.group(1)), float(match.group(2))
    return None, None


def calculate_answer(n1, n2):
    """Calcule la réponse selon la formule du challenge."""
    return round(math.sqrt(n1) * n2, 2)


def main():
    host = "challenge01.root-me.org"
    port = 52002

    try:
        with socket.create_connection((host, port), timeout=3) as s:
            # Réception du message initial
            data = s.recv(1024).decode()
            print("[QUESTION REÇUE]\n", data)

            # Recherche de la ligne contenant le calcul
            calc_line = next((line for line in data.splitlines() if "Calculate the square root" in line), None)
            if not calc_line:
                print("[ERREUR] Ligne de calcul introuvable.")
                return

            # Extraction des deux nombres
            n1, n2 = extract_numbers(calc_line)
            if n1 is None or n2 is None:
                print("[ERREUR] Impossible d'extraire les nombres.")
                return

            # Calcul du résultat
            result = calculate_answer(n1, n2)
            formatted_result = f"{result:.2f}"
            print(f"[CALCUL] √{n1} * {n2} = {formatted_result}")

            # Envoi de la réponse
            s.sendall((formatted_result + "\n").encode())

            # Réception de la réponse du serveur
            response = s.recv(1024).decode().strip()
            print("[RÉPONSE]", response)

    except socket.timeout:
        print("[TIMEOUT] Le serveur n'a pas répondu à temps.")
    except Exception as e:
        print(f"[ERREUR] {e}")


if __name__ == "__main__":
    main()
