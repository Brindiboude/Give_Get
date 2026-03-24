461;7600;1c# 🟦 PROJET INTÉGRATEUR — JOUR 3

## Guide pas à pas : démarrage du projet + bases Git + documentation en Markdown

### Objectif : mettre en place un workflow propre et travailler comme une équipe

---

# 🎯 Objectifs de la journée

À la fin de cette journée, chaque groupe doit avoir :

* Un dépôt Git initialisé et poussé sur GitHub (ou équivalent)
* Une structure de projet claire (frontend / backend / docs)
* Un `README.md` complet et utile
* Une convention de commits et un workflow d’équipe minimal
* Des branches de travail + des merges propres
* Une documentation `.md` qui peut évoluer avec le projet
* Un premier lot de fichiers “fondations” versionnés (pas seulement du vide)

👉 Aujourd’hui, l’objectif n’est pas “coder beaucoup”.
👉 L’objectif est de créer un **cadre de travail propre** qui évite 80% des problèmes plus tard.

---

# 🧠 1) Comprendre ce que vous construisez (5 min)

Avant Git, on clarifie :

Un projet web complet =

* **Frontend** : interface + interactions + appels API
* **Backend** : règles + validation + accès DB + sécurité
* **Base de données** : stockage + cohérence + relations
* **Documentation** : ce qui rend le projet lisible et maintenable

Sans documentation et sans Git :

* vous ne savez plus ce que vous avez décidé,
* vous vous perdez dans la structure,
* vous ne pouvez pas collaborer proprement.

---

# ✅ 2) Pré-requis (checklist technique)

Avant de commencer, vérifiez :

* [ ] Git est installé (`git --version`)
* [ ] Vous avez un compte GitHub (ou GitLab)
* [ ] Vous êtes connectés au bon compte
* [ ] Vous savez où se trouve votre dossier de travail
* [ ] Vous avez un terminal opérationnel

### Vérifier Git

```bash
git --version
```

Si la commande ne fonctionne pas : Git n’est pas installé ou pas dans le PATH.

---

# 🧱 3) Étape 1 — Créer la structure de projet (pas à pas)

## 3.1 Choisir un nom de projet

Règles :

* pas d’espaces
* pas d’accents
* pas de caractères spéciaux
* tout en minuscules

Exemple :

* `trackmyapps`
* `alt-dashboard`
* `campus-market`

## 3.2 Créer le dossier racine

```bash
mkdir nom-du-projet
cd nom-du-projet
```

## 3.3 Créer une structure claire

Structure recommandée (simple et solide) :

```bash
mkdir frontend backend docs
touch README.md
touch .gitignore
```

Vous obtenez :

```
nom-du-projet/
├── frontend/
├── backend/
├── docs/
├── README.md
└── .gitignore
```

### Pourquoi cette structure ?

* `frontend/` : tout ce qui concerne l’interface
* `backend/` : API, logique métier, DB
* `docs/` : documents, schémas, décisions, notes
* `README.md` : page d’entrée du projet
* `.gitignore` : évite de versionner les fichiers inutiles

---

# 🧹 4) Étape 2 — Créer un `.gitignore` propre (explication + exemple)

## 4.1 Pourquoi `.gitignore` est indispensable ?

Sans `.gitignore`, vous risquez de versionner :

* des dépendances (très lourdes)
* des fichiers temporaires
* des secrets (clés API)
* des builds
* des logs

👉 Un repo propre ne doit pas contenir ce qui est re-générable.

## 4.2 Exemple de `.gitignore` (générique)

Copiez-collez dans `.gitignore` :

```gitignore
# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Env files (secrets)
.env
.env.local
.env.*.local

# Node
node_modules/

# Builds
dist/
build/

# Python
__pycache__/
*.pyc

# IDE
.vscode/
.idea/
```

👉 Point important : `.env` ne doit jamais être commité.

---

# 🧠 5) Étape 3 — Écrire un README.md utile (guide + template)

## 5.1 Pourquoi un README est un outil de dev (pas du marketing)

Un README sert à :

* comprendre le projet en 2 minutes
* savoir comment l’installer
* connaître l’architecture
* connaître les routes API
* savoir quoi faire ensuite

Le README est le “mode d’emploi” du repo.

## 5.2 Template de README (à remplir aujourd’hui)

Copiez-collez ce plan dans `README.md` puis remplissez :

```markdown
# Nom du projet

## 1) Problème
- Segment cible :
- Problème :
- Exemple concret :
- Solutions actuelles + limites :

## 2) Proposition de valeur
- En une phrase :
- Différenciation (vs alternatives) :

## 3) MVP (périmètre 3 mois)
### Inclus
- ...
### Exclu
- ...

## 4) Architecture (vue d’ensemble)
Frontend → Backend (API) → Base de données

## 5) Modèle de données (v0)
- Entité 1 : ...
- Entité 2 : ...
- Entité 3 : ...
Relations :
- 1:N ...
- N:N ...

## 6) Routes API (v0)
Auth :
- POST /auth/register
- POST /auth/login
- GET /auth/me

Entité principale :
- GET /...
- POST /...
- GET /.../:id
- PUT /.../:id
- DELETE /.../:id

## 7) Logique métier (v0)
- Règle 1 :
- Règle 2 :
- Transitions / contraintes :

## 8) Installation (à compléter quand le code existe)
### Frontend
- ...
### Backend
- ...

## 9) Roadmap 3 mois
- S1-S3 :
- S4-S6 :
- S7-S9 :
- S10-S12 :

## 10) Conventions d’équipe
- Convention de branches :
- Convention de commits :
- Règles de merge :
```

👉 Aujourd’hui, vous devez remplir au minimum les sections 1 à 7 + 9 + 10.

---

# 🧩 6) Étape 4 — Initialiser Git (pas à pas, expliqué)

## 6.1 Initialiser le dépôt

Dans le dossier du projet :

```bash
git init
```

👉 Ça crée un dossier caché `.git/` qui contient tout l’historique.

## 6.2 Vérifier l’état

```bash
git status
```

Vous devriez voir :

* des fichiers “Untracked” (pas encore suivis)

## 6.3 Ajouter les fichiers

```bash
git add .
```

👉 `git add` prépare les fichiers pour le commit.
Ça ne “sauvegarde” pas encore, ça prépare.

## 6.4 Faire le premier commit

```bash
git commit -m "chore: init repo structure and README"
```

👉 Message clair, action logique, compréhensible.

---

# 🌍 7) Étape 5 — Créer le repo distant (GitHub) et pousser (pas à pas)

## 7.1 Créer un repo sur GitHub

Sur GitHub :

* New repository
* Nom = `nom-du-projet`
* Public ou private (selon consigne)
* Ne pas générer README (vous l’avez déjà)

## 7.2 Lier votre repo local à GitHub

Copiez l’URL du repo GitHub puis :

```bash
git remote add origin <URL_DU_REPO>
```

Vérifier :

```bash
git remote -v
```

## 7.3 Pousser sur GitHub

Selon votre branche (souvent `main`) :

```bash
git branch -M main
git push -u origin main
```

👉 `-u` associe votre branche locale à la branche distante.

---

# 🧠 8) Comprendre les commits (et comment bien commiter)

## 8.1 Un commit doit être petit et cohérent

Règle :

> 1 commit = 1 intention

Mauvais :

* “j’ai fait plein de trucs”
* 50 fichiers modifiés
* message “update”

Bon :

* “docs: add initial data model"
* “docs: define API routes v0"
* “chore: add gitignore"

## 8.2 Convention simple de message (recommandée)

* `chore:` : config, structure, outils
* `docs:` : documentation
* `feat:` : nouvelle fonctionnalité
* `fix:` : correction de bug
* `refactor:` : refactor sans changer le comportement

Exemples :

* `docs: add v0 API routes`
* `docs: describe business rules for status transitions`
* `chore: setup frontend and backend folders`

---