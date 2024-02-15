Projet par Romain TAMIC et Marion DEFFEE

Pour utiliser ce projet, il faut :

Pour préparer le projet :
- Créer une database locale : dans un CMD ou un utilitaire WAMP/MAMP, et copier le fichier 'script.sql' situé dans le dossier 'SQLFiles'
- Installer des dépendances et librairies :
  -   Dans le dossier racine, utiliser 'pip install -r requirements.txt'
- Utiliser le fichier 'insert_data.py' en suivant ces étapes :
  - Remplacer les champs host_name, user_name, user_password, db_name avec les champs correspondants
  - Remplacer le PATH de votre fichier 'prix_immobilier_fictif.csv' pour permettre l'ingestion des données
  - Lancer le programme 'insert_data.py'

Pour lancer le projet :
- Lancer le serveur app.py :
  - Dans le dossier 'server', lancer le programme 'app.py'
  - N.B : les parties en commentaires sont utiles pour utiliser le fichier CSV à la place de de la BDD
- Dans un terminal, aller jusqu'au dossier 'client':
  - Lancer la commande 'streamlit run client.py'
  - Un lien local va apparaitre, cliquer sur ce lien pour accéder au site
- Sur ce site, vous pouvez changer de ville, quartier, voir le prix et le mettre à jour