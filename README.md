Give_Get

La plateforme d'échange d'objets sans argent entre étudiants.


1) Problème

Segment cible : Étudiants et jeunes adultes (18-25 ans)
Problème : Les jeunes ont des placards et des chambres pleins d'objets qu'ils n'utilisent plus, mais peu de budget pour en acquérir de nouveaux. Les plateformes existantes comme Vinted ou Leboncoin impliquent de gérer de l'argent, des frais et de la logistique — une friction inutile quand on veut juste échanger.
Exemple concret : Tu as une console que tu n'utilises plus, tu voudrais un vélo. Sur Leboncoin tu dois vendre, attendre, encaisser, puis racheter. Sur Give_Get tu proposes un échange directement.
Solutions actuelles + limites :

Vinted / Leboncoin → implique de l'argent, des frais, de la logistique
Groupes Facebook → pas structuré, aucun système d'échange propre
Donner à des amis → limité à son cercle social




2) Proposition de valeur

En une phrase : La plateforme d'échange d'objets sans argent entre étudiants.
Différenciation vs alternatives : Zéro transaction financière, zéro frais, zéro prise de tête — juste du troc direct entre pairs, toutes catégories d'objets confondues.


3) MVP (périmètre 3 mois)
Inclus

Création de compte et connexion
Publier un objet (photo, état, catégorie, description)
Parcourir et filtrer les annonces (par catégorie, état)
Proposer un échange à quelqu'un
Messagerie entre utilisateurs
Système de notation / avis après échange

Exclu

Paiement en argent
Application mobile
Système de points ou crédits
Gestion de la livraison / logistique


4) Architecture (vue d'ensemble)
React (Frontend) → Flask API (Backend) → SQLite (Base de données, dev)

Frontend (React) : interface utilisateur, navigation, appels API
Backend (Flask) : logique métier, validation, authentification, accès DB
Base de données (MySQL) : stockage persistant des utilisateurs, items, échanges, messages et avis


5) Modèle de données (v0)

User — id, username, email, password, avatar, created_at
Item — id, user_id, title, description, category, condition, size, photo_url, status, created_at
Exchange — id, item_offered_id, item_requested_id, sender_id, receiver_id, status, created_at
Message — id, exchange_id, sender_id, content, sent_at
Review — id, reviewer_id, reviewed_id, exchange_id, rating, comment, created_at

Catégories d'objets :

Vêtements
Livres
Électronique (consoles, téléphones...)
Sport & loisirs (vélos, équipements...)
Maison & déco
Autres

Notes :

Le champ size est optionnel — pertinent uniquement pour les vêtements
Le champ condition est obligatoire : neuf, très bon état, bon état, état correct

Relations :

1:N — Un User peut avoir plusieurs Items
1:N — Un User peut envoyer plusieurs Exchanges
1:N — Un Exchange peut avoir plusieurs Messages
1:N — Un Exchange peut générer plusieurs Reviews (une par participant)
N:N — Deux Items sont liés via un Exchange


6) Routes API (v0)
Auth
MéthodeRouteDescriptionPOST/auth/registerCréer un comptePOST/auth/loginSe connecterGET/auth/meRécupérer l'utilisateur connectéPOST/auth/logoutSe déconnecter
Items (objets)
MéthodeRouteDescriptionGET/itemsLister tous les items disponiblesPOST/itemsPublier un nouvel objetGET/items/:idVoir le détail d'un itemPUT/items/:idModifier un itemDELETE/items/:idSupprimer un item
Exchanges (échanges)
MéthodeRouteDescriptionPOST/exchangesProposer un échangeGET/exchanges/:idVoir le détail d'un échangePUT/exchanges/:id/acceptAccepter un échangePUT/exchanges/:id/declineRefuser un échangePUT/exchanges/:id/completeFinaliser un échange
Messages
MéthodeRouteDescriptionGET/exchanges/:id/messagesLister les messages d'un échangePOST/exchanges/:id/messagesEnvoyer un message
Reviews
MéthodeRouteDescriptionPOST/exchanges/:id/reviewsLaisser un avis après échange

7) Logique métier (v0)
Cycle de vie d'un échange
pending → accepted → completed
pending → declined
accepted → cancelled
Règles

Règle 1 : Un échange ne peut être proposé que si les deux items ont le statut available
Règle 2 : Quand un échange passe à accepted, les deux items concernés passent automatiquement en unavailable
Règle 3 : Si un échange est declined ou cancelled, les items repassent en available
Règle 4 : Une review ne peut être laissée que si l'échange est completed
Règle 5 : Chaque participant ne peut laisser qu'une seule review par échange

Statuts d'un item
available → unavailable (quand échange accepted)
unavailable → available (quand échange declined ou cancelled)

8) Installation (à compléter quand le code existe)
Frontend
bashcd frontend
npm install
npm run dev
Backend
bashcd backend
pip install -r requirements.txt
flask run

9) Roadmap 3 mois
PériodeObjectifS1-S3Setup projet, auth, modèle de données, structure Flask + ReactS4-S6CRUD items, upload photo, parcourir et filtrer par catégorieS7-S9Système d'échange (propose, accept, decline, complete), messagerieS10-S12Reviews, polish UI, tests, déploiement

10) Conventions d'équipe
Convention de branches
main          → version stable et déployable
develop       → intégration des features en cours
feature/xxx   → une branche par fonctionnalité (ex: feature/auth, feature/item-upload)
Convention de commits
feat:      nouvelle fonctionnalité
fix:       correction de bug
docs:      documentation
chore:     configuration, structure, outils
refactor:  amélioration du code sans changer le comportement
Exemples :

feat: add item creation form
fix: correct exchange status transition
docs: update API routes in README
chore: setup flask project structure

Règles de merge

On ne merge jamais directement sur main
Toute feature passe par une Pull Request vers develop
develop → main uniquement quand la feature est testée et validée