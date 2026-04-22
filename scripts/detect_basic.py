from scapy.all import rdpcap   # Permet de lire un fichier de capture (.cap / .pcap)
from scapy.layers.dot11 import Dot11Deauth  # Type de trame WiFi : désauthentification


# Fonction principale de détection
def detect_deauth(pcap_file):
    
    # Charger tous les paquets du fichier capture
    packets = rdpcap(pcap_file)

    # Compteur de trames de désauthentification
    count = 0

    # Parcourir tous les paquets capturés
    for pkt in packets:
        
        # Vérifier si le paquet contient une couche "deauth"
        if pkt.haslayer(Dot11Deauth):
            count += 1   # Si oui → incrémenter

    # Afficher le nombre total détecté
    print(f"Nombre de trames de deauth détectées : {count}")

    # Règle simple de détection (seuil)
    if count > 20:
        print("ALERTE : Attaque possible de désauthentification !")
    else:
        print("Pas d'activité suspecte détectée.")


# Point d'entrée du script
if __name__ == "__main__":
    
    # Ici tu mets le chemin vers ton fichier capture
    detect_deauth("captures/capture-01.cap")