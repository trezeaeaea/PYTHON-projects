# Coach d'exercices Python

Un programme en ligne de commande qui me propose des exercices Python selon mon niveau, et qui garde en mémoire ma progression d'une session à l'autre.

## Fonctionnalités

- Propose un exercice au hasard selon le niveau choisi (`noob` ou `intermediary`)
- Ne redonne jamais deux fois de suite le même exercice
- Enregistre la progression dans un fichier JSON : niveau, exercice en cours, nombre d'exercices terminés et historique
- Charge la liste des exercices depuis GitHub, et utilise la copie locale `exercises.json` si internet n'est pas disponible
- Menu interactif : voir l'exercice en cours, le marquer comme terminé, voir sa progression, changer de niveau

## Lancer le programme

Il faut Python 3 et le module `requests` :

```
pip install requests
python main.py
```

## Organisation du code

```
main.py              programme principal et menu
modules/
  exercises.py       tirage d'un nouvel exercice
  progress.py        lecture et sauvegarde de la progression
  remote.py          chargement des exercices depuis GitHub
exercises.json       liste des exercices par niveau
progress.json        progression enregistrée
```

## Les étapes du projet

J'ai construit ce projet étape par étape. Chaque fichier numéroté correspond à une étape :

| Fichier | Étape |
|---|---|
| `01_user_progress.py` | Demander le niveau et le nombre d'exercices faits |
| `02_exercise_selector.py` | Choisir un exercice selon le niveau |
| `03_random_exercise.py` | Tirer un exercice au hasard dans une liste |
| `04_functions.py` | Ranger le tirage dans une fonction |
| `05_json_exercises.py` | Charger les exercices depuis un fichier JSON |
| `06_current_exercise.py` | Enregistrer l'exercice en cours |
| `07_saved_level.py` | Ne plus redemander le niveau à chaque lancement |
| `08_exercise_history.py` | Garder l'historique des exercices terminés |
| `09_remote_exercises.py` | Charger les exercices depuis GitHub, avec une copie locale de secours |

`main.py` et le dossier `modules/` rassemblent la version finale.

## Ce que j'ai appris

- Lire et écrire des fichiers JSON avec le module `json`
- Découper un programme en modules réutilisables
- Gérer les erreurs avec `try` / `except` (saisie invalide, absence d'internet)
- Faire une requête HTTP avec `requests`

## Autres exercices

- `cinema.py` : calcul du prix d'une place de cinéma selon l'âge, avec option pop-corn
- `gestion_de_notes.py` : saisie de notes et calcul de la moyenne
