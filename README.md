Voici une nouvelle version d�taill�e du fichier `README.md` pour ton projet. Elle inclut toutes les sections importantes, bas�es sur la structure des fichiers et les attentes g�n�rales d'un projet Python.

---

# SAE_1.05 - Traitement des donn�es de logs

## Introduction
Ce projet a pour objectif de traiter et d'analyser des fichiers de logs � l'aide de diff�rents scripts Python. Il fait partie de la SAE 1.05, centr�e sur la gestion et le traitement des donn�es. Les scripts permettent d'extraire des informations importantes telles que les adresses IP, les navigateurs utilis�s, ainsi que les syst�mes d'exploitation, et de les formater pour analyse.

## Installation

### Pr�requis
- **Python 3.x** doit �tre install� sur votre machine.
- Les biblioth�ques Python requises sont list�es ci-dessous et peuvent �tre install�es via `pip` :
  ```bash
  pip install requests
  ```

### �tapes d'installation
1. Clonez ce d�p�t sur votre machine locale :
   ```bash
   git clone https://github.com/votre-utilisateur/SAE_15.git
   cd SAE_15
   ```
2. Installez les d�pendances avec `pip` (si n�cessaire) :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. **Extraction des adresses IP depuis le fichier de logs** :  
   Utilisez le script `ip_fichier_log.py` pour extraire les adresses IP � partir du fichier de logs.
   ```bash
   python ip_fichier_log.py controltower_access.log
   ```

2. **Utilisation de l'API IP pour des informations sur les IP** :  
   Le script `IP_API.py` permet de r�cup�rer des informations suppl�mentaires sur les adresses IP extraites, telles que la localisation g�ographique.
   ```bash
   python IP_API.py
   ```

3. **Analyse du type de navigateur** :  
   Le script `navigateur.py` permet d'analyser le type de navigateur utilis� dans les logs.
   ```bash
   python navigateur.py controltower_access.log
   ```

4. **Analyse des syst�mes d'exploitation** :  
   Utilisez `OS_fichier_log.py` pour identifier le syst�me d'exploitation utilis� � partir des donn�es de log.
   ```bash
   python OS_fichier_log.py controltower_access.log
   ```

5. **Analyse des dates** :  
   Le script `date_fichier_log.py` extrait et analyse les dates contenues dans le fichier de logs.
   ```bash
   python date_fichier_log.py controltower_access.log
   ```

## Structure du projet

- **controltower_access.log** : Fichier de logs � analyser.
- **date_fichier_log.py** : Script pour extraire et traiter les dates dans les logs.
- **IP_API.py** : Script interagissant avec une API pour obtenir des informations sur les adresses IP.
- **ip_fichier_log.py** : Script pour extraire les adresses IP des logs.
- **navigateur.py** : Analyse des informations de navigateur dans les logs.
- **OS_fichier_log.py** : Analyse des syst�mes d'exploitation d�tect�s dans les logs.
- **SAE_1.05_DOC.docx** : Document de sp�cifications et de documentation du projet.
- **Sujet_SAE-15_Traiter_les_donn�es.pdf** : Sujet officiel de la SAE 15.

## D�pendances

- `requests` : Utilis� pour interagir avec des APIs dans le script `IP_API.py`.
  
Installez-le via :
```bash
pip install requests
```

## Auteurs

- Lacoste Maxime
  
Ce projet a �t� r�alis� dans le cadre de la SAE 1.05 pour BUTR&T de Mont-De-Marsan. 

