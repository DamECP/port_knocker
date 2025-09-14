# Port Knocking Automation Script

![Python](https://img.shields.io/badge/Python-3.x-blue) ![nmap](https://img.shields.io/badge/nmap-required-orange) ![License](https://img.shields.io/badge/License-MIT-green)

This repository contains a Python script to automate **port knocking** to discover open ports after a specific sequence.

> ⚠️ Note: The code was written manually, but this README was generated automatically.

Originally developed for the **[Cat Pictures](https://tryhackme.com/room/catpictures)** room on TryHackMe, but it can be adapted to other **legitimate environments** (personal labs, CTFs, authorized test environments).

## Table of Contents

- [Features](#features)  
- [Requirements](#requirements)  
- [Usage](#usage)  
- [⚠️ Legal Notice](#-legal-notice)  
- [Technical Notice](#technical-notice)  
- [Contributing](#contributing)  
- [Script d'automatisation du Port Knocking (FR)](#script-dautomatisation-du-port-knocking-fr)

## Features

- Scan specific ports using `nmap`.
- Generate all possible permutations of a **port knocking sequence**.
- Automatically test each sequence and detect newly opened ports.
- Display the sequence that changed the port state with the corresponding `nmap` output.

## Requirements

- Python 3.x
- `nmap` installed and accessible from the command line
- Network access to the target machine (authorized environment)

## Usage

1. Modify the variables in the script:

   ```python
   host = "TARGET_IP"
   knocked_ports = [1111, 2222, 3333, 4444]  # sequence of ports to test
   tested_ports = [21, 22, 2375, 4420, 8080]  # ports to scan before/after

2. Run the script

   ```python
   python3 knocking.py
   ```

3. The script will display the port knocking sequence that opened a new port and the corresponding nmap output.

   ## ⚠️ Legal Notice

   This script **should only be used in authorized environments**:

   - CTFs / labs / machines you own or have explicit permission to test.
   - **Do NOT** use it against production systems or public machines without authorization.
   - Unauthorized use is **illegal and may result in criminal charges**.

## Technical Notice

- Performs SYN scans (`-sS`) and sends TCP connections to the knocking ports.
- Can generate detectable network traffic.
- Use only in controlled environments.

## Contributing

Contributions are welcome for bug fixes or improvements, but please ensure the script remains for **educational or authorized testing purposes only**.

1. Fork the repository  
2. Create a new branch (`git checkout -b feature-name`)  
3. Make your changes  
4. Submit a pull request



## Script d'automatisation du Port Knocking (FR)

![Python](https://img.shields.io/badge/Python-3.x-blue) ![nmap](https://img.shields.io/badge/nmap-required-orange) ![License](https://img.shields.io/badge/License-MIT-green)

Ce dépôt contient un script Python permettant d’automatiser le **port knocking** pour découvrir des ports ouverts suite à une séquence spécifique.

> ⚠️ Note : Le code a été écrit à la main, mais ce README a été généré automatiquement.

Initialement développé pour la room **[Cat Pictures](https://tryhackme.com/room/catpictures)** sur TryHackMe, mais peut être adapté à d’autres environnements **légitimes** (laboratoires personnels, CTF, environnements de test autorisés).

## Table des Matières

- [Fonctionnalités](#fonctionnalités)  
- [Prérequis](#prérequis)  
- [Utilisation](#utilisation)  
- [⚠️ Avertissement légal](#-avertissement-légal)  
- [Avertissement technique](#avertissement-technique)  
- [Contribuer](#contribuer)

## Fonctionnalités

- Scanner des ports spécifiques avec `nmap`.
- Générer toutes les permutations possibles d’une séquence de **port knocking**.
- Tester automatiquement chaque séquence et détecter l’ouverture de nouveaux ports.
- Afficher la séquence ayant modifié l’état des ports et la sortie `nmap` correspondante.

## Utilisation

1. Modifier les variables dans le script :

   ```python
   host = "IP_CIBLE"
   knocked_ports = [1111, 2222, 3333, 4444]  # séquence de ports à tester
   tested_ports = [21, 22, 2375, 4420, 8080]  # ports à scanner avant/après

2. Lancer le script :

   ```python
   python3 knocking.py
   ```

3. Le script affichera la séquence de ports ayant ouvert un nouveau port et la sortie nmap correspondante.

## ⚠️ Avertissement légal

Ce script **ne doit être utilisé que dans des environnements autorisés** :

- CTF / labs / machines que vous possédez ou pour lesquelles vous avez une autorisation explicite.
- **Interdit** de l’utiliser sur des systèmes en production ou des machines publiques sans autorisation.
- Toute utilisation non autorisée est **illégale et peut entraîner des poursuites pénales**.

## Avertissement technique

- Effectue des scans SYN (`-sS`) et envoie des connexions TCP sur les ports de knocking.
- Peut générer du trafic réseau détectable par des systèmes de sécurité.
- Testez uniquement dans un environnement contrôlé.

## Contribuer

Les contributions sont les bienvenues (corrections de bugs, améliorations), mais le script doit rester **à usage éducatif ou pour tests autorisés uniquement**.

1. Fork du dépôt  
2. Créer une nouvelle branche (`git checkout -b feature-name`)  
3. Effectuer vos modifications  
4. Soumettre un pull request