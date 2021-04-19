# Application de tournois d'échecs

Cette application de tournois d'échecs est une application en console pour gérer les joueurs et les tournois basée sur le système Suisse.

## Prérequis

1. Installer [Python 3](https://www.python.org/downloads/).

2. Télécharger le programme via GitHub avec la commande ci-dessous ou en téléchargeant [l'archive](https://github.com/MaeRiz/OC_P4_Chess/archive/refs/heads/master.zip).
```bash
git clone https://github.com/MaeRiz/OC_P4_Chess.git
```

3. installer les modules via la commande:
```cmd
pip install -r requirements.txt
```

## Utilisation

Utiliser la commande ci-dessous pour lancer l'application.

```cmd
py start.py
```
## Génération de rapport Flake8
Utiliser la commande ci-dessous pour générer un rapport Flake8.
```cmd
flake8 app --format=html --htmldir=flake-report
```

## Informations

- Les informations sur les tournois et les joueurs sont enregistrées dans des bases de données JSON dans le répertoire: ../app/data/
- Les données sont automatiquement sauvegardées dans les bases de données durant l'utilisation normale de l'application.
- Étant une application console, l’interaction se fait avec les choix de l'utilisateur selon la demande de l'application. 
