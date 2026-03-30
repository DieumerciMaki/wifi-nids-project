# Projet WiFi NIDS

## Présentation
Ce projet vise la conception et la réalisation d’un système simple de détection d’intrusion réseau sans fil (WiFi NIDS) dans un environnement universitaire.

## Contexte
Les réseaux WiFi universitaires sont largement utilisés et exposés à diverses activités suspectes telles que :
- les tentatives d’accès non autorisées
- les attaques de désauthentification
- le flood de requêtes probe
- les comportements réseau anormaux
- d’autres anomalies du trafic

## Objectif principal
L’objectif principal de ce projet est de construire un système simple de détection d’intrusion réseau basé sur des règles, capable de :
- capturer le trafic WiFi
- observer le comportement réseau
- détecter des événements suspects
- générer des alertes pour l’administrateur

## Phase actuelle
Cette première phase concerne la mise en place d’un NIDS simple sans intelligence artificielle.

## Phase future
Dans une seconde phase, des techniques d’intelligence artificielle et de machine learning seront intégrées pour la détection d’anomalies à partir des données réelles collectées.

## Structure du projet
- `captures/` : captures du trafic WiFi (`.cap`, `.pcap`, `.csv`)
- `data/raw/` : données brutes
- `data/processed/` : données nettoyées ou transformées
- `scripts/` : scripts d’analyse et de détection
- `docs/` : notes, architecture, méthodologie
- `reports/` : résultats, journaux et rapports de test

## Fonctionnalités initiales
- surveiller le trafic WiFi
- identifier des trames ou comportements suspects
- détecter des anomalies simples à l’aide de règles
- enregistrer ou afficher des alertes

## Outils envisagés
- Python
- Scapy
- Tshark / Wireshark
- Airodump-ng
- GitHub

## Auteur
Dieumerci Maki