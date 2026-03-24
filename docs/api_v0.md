# API v0

## Authentification

POST /auth/register
Créer un utilisateur

POST /auth/login
Connecter un utilisateur

GET /auth/me
Récupérer l'utilisateur connecté

---

## Ressource principale (exemple)

GET /items
Récupérer tous les items

POST /items
Créer un item

GET /items/:id
Récupérer un item

PUT /items/:id
Modifier un item

DELETE /items/:id
Supprimer un item