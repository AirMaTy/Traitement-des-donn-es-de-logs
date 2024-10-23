Voici une nouvelle version détaillée du fichier `README.md` pour ton projet. Elle inclut toutes les sections importantes, basées sur la structure des fichiers et les attentes générales d'un projet Python.

---

# SAE_1.05 - Traitement des données de logs

## Introduction
Ce projet a pour objectif de traiter et d'analyser des fichiers de logs à l'aide de différents scripts Python. Il fait partie de la SAE 1.05, centrée sur la gestion et le traitement des données. Les scripts permettent d'extraire des informations importantes telles que les adresses IP, les navigateurs utilisés, ainsi que les systèmes d'exploitation, et de les formater pour analyse.

## Installation

### Prérequis
- **Python 3.x** doit être installé sur votre machine.
- Les bibliothèques Python requises sont listées ci-dessous et peuvent être installées via `pip` :
  ```bash
  pip install requests
  ```

### Étapes d'installation
1. Clonez ce dépôt sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/SAE_15.git
   cd SAE_15
   ```
2. Installez les dépendances avec `pip` (si nécessaire) :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. **Extraction des adresses IP depuis le fichier de logs** :  
   Utilisez le script `ip_fichier_log.py` pour extraire les adresses IP à partir du fichier de logs.
   ```bash
   python ip_fichier_log.py controltower_access.log
   ```

2. **Utilisation de l'API IP pour des informations sur les IP** :  
   Le script `IP_API.py` permet de récupérer des informations supplémentaires sur les adresses IP extraites, telles que la localisation géographique.
   ```bash
   python IP_API.py
   ```

3. **Analyse du type de navigateur** :  
   Le script `navigateur.py` permet d'analyser le type de navigateur utilisé dans les logs.
   ```bash
   python navigateur.py controltower_access.log
   ```

4. **Analyse des systèmes d'exploitation** :  
   Utilisez `OS_fichier_log.py` pour identifier le système d'exploitation utilisé à partir des données de log.
   ```bash
   python OS_fichier_log.py controltower_access.log
   ```

5. **Analyse des dates** :  
   Le script `date_fichier_log.py` extrait et analyse les dates contenues dans le fichier de logs.
   ```bash
   python date_fichier_log.py controltower_access.log
   ```

## Structure du projet

- **controltower_access.log** : Fichier de logs à analyser.
- **date_fichier_log.py** : Script pour extraire et traiter les dates dans les logs.
- **IP_API.py** : Script interagissant avec une API pour obtenir des informations sur les adresses IP.
- **ip_fichier_log.py** : Script pour extraire les adresses IP des logs.
- **navigateur.py** : Analyse des informations de navigateur dans les logs.
- **OS_fichier_log.py** : Analyse des systèmes d'exploitation détectés dans les logs.
- **SAE_1.05_DOC.docx** : Document de spécifications et de documentation du projet.
- **Sujet_SAE-15_Traiter_les_données.pdf** : Sujet officiel de la SAE 15.

## Dépendances

- `requests` : Utilisé pour interagir avec des APIs dans le script `IP_API.py`.
  
Installez-le via :
```bash
pip install requests
```

## Auteurs

- Lacoste Maxime
  
Ce projet a été réalisé dans le cadre de la SAE 1.05 pour BUTR&T de Mont-De-Marsan. 

