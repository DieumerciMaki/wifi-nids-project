from scapy.all import rdpcap
from scapy.layers.dot11 import Dot11Deauth, Dot11ProbeReq, Dot11

def analyze_pcap(pcap_file):
    
    packets = rdpcap(pcap_file)

    deauth_count = 0
    probe_count = 0
    clients = {}

    for pkt in packets:

        # 🔹 Détection deauth
        if pkt.haslayer(Dot11Deauth):
            deauth_count += 1

        # 🔹 Détection probe requests
        if pkt.haslayer(Dot11ProbeReq):
            probe_count += 1

        # 🔹 Analyse activité client
        if pkt.haslayer(Dot11):
            src = pkt.addr2  # MAC source

            if src:
                if src not in clients:
                    clients[src] = 0
                clients[src] += 1

    # ===== RESULTATS =====

    print("\n=== ANALYSE DU TRAFIC ===")

    print(f"Deauth frames : {deauth_count}")
    print(f"Probe requests : {probe_count}")

    # 🔹 Alertes
    if deauth_count > 20:
        print("ALERTE : Attaque de désauthentification possible")

    if probe_count > 50:
        print("ALERTE : Probe flood détecté")

    # 🔹 Analyse clients
    print("\n=== ACTIVITÉ CLIENTS ===")

    for client, count in clients.items():
        if count > 100:
            print(f"Client suspect : {client} ({count} paquets)")


if __name__ == "__main__":
    analyze_pcap("captures/capture-01.cap")