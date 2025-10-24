# QUIZZ - Python  

## Contexte du projet  
Ce projet a été développé dans le cadre d’un apprentissage du langage **Python** et de la bibliothèque graphique **Arcade**.  
L’objectif était de créer un petit **jeu de quiz interactif** permettant au joueur de tester ses connaissances tout en accumulant des points au fil des parties.  

Le jeu met l’accent sur :  
- la gestion des **vues** et des **interactions utilisateur** (clavier / souris),  
- la **structuration du code** avec des classes et des fichiers de gestion (`views`, `managers`, `core`),  
- et la **sauvegarde des données du joueur** (score, bonus, etc.).  

---

## Description du jeu  
1. Le joueur **entre son nom** puis clique sur **Commencer**.  
2. Le premier quizz démarre : il contient **10 questions**.  
3. Pour chaque **bonne réponse**, le joueur gagne **+1 point**.  
4. À la fin du quizz, un bouton **"Commencer le quizz suivant"** apparaît pour accéder au suivant.  
5. Les **points cumulés** sont conservés d’un quizz à l’autre.  

### Le bonus 50/50  
- Dès que le joueur atteint **au moins 5 points**, il peut utiliser le **bonus “50/50”**.  
- Ce bonus enlève **la moitié des mauvaises réponses** sur la question en cours, facilitant la réflexion.  
- En contrepartie, **5 points** sont retirés du score total.  

---

## Fonctionnalités principales
- Gestion de plusieurs **quizz successifs** (chaque fichier JSON contient un quizz différent)  
- **Boutons interactifs** (réponses, bonus, quizz suivant)  
- **Système de score cumulatif** entre les quizz  
- **Bonus 50/50** dynamique  
- Affichage d’un **message de fin** quand tous les quizz sont terminés  
- **Image de fond personnalisée** pour une meilleure immersion  

---

## Évolutions possibles

- Implémenter plusieurs **niveaux de difficulté** (facile, moyen, difficile) influençant le score obtenu pour chaque bonne réponse.  
- Ajouter un **système de vies** ou de **tentatives limitées** pour renforcer l’aspect stratégique du jeu.  


- Intégrer un **mode chronométré** où la rapidité de réponse rapporte des points bonus.  
- Afficher un **timer visuel** pour chaque question, avec éventuellement une **pénalité de points** ou un passage automatique à la question suivante en cas de dépassement du temps imparti.


- **Sauvegarder les scores localement** (par exemple dans un fichier JSON ou une base SQLite) et afficher un **classement** des meilleurs joueurs.  
- Permettre de **sauvegarder et charger la progression** d’un joueur afin qu’il puisse reprendre sa partie ultérieurement.


- Ajouter des **animations simples** lors de la suppression d’options avec le bonus **50/50**.  
