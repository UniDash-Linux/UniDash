---
stepsCompleted: [1, 2, 3, 4]
status: complete
totalEpics: 6
totalStories: 49
frCoverage: 34/34
inputDocuments:
  - "_bmad-output/planning-artifacts/prd.md"
  - "_bmad-output/planning-artifacts/architecture.md"
  - "_bmad-output/planning-artifacts/ux-design-specification.md"
  - "_bmad-output/planning-artifacts/product-brief-UniDash-2026-01-08.md"
  - "_bmad-output/project-context.md"
---

# UniDash - Epic Breakdown

## Overview

This document provides the complete epic and story breakdown for UniDash, decomposing the requirements from the PRD, UX Design, and Architecture into implementable stories.

## Requirements Inventory

### Functional Requirements

**Installation & Infrastructure (FR1-FR5)**

- FR1: Le systeme installe automatiquement un cluster K3S HA via un wizard guide
- FR2: L'administrateur peut ajouter un noeud au cluster (installation serveur + lien d'ajout)
- FR3: Le systeme configure automatiquement le VPN L2TP/IPsec cote serveur
- FR4: Le systeme configure automatiquement le reverse proxy pour les services
- FR5: Le systeme gere automatiquement les certificats SSL

**Authentification & Utilisateurs (FR6-FR12)**

- FR6: L'administrateur peut creer et gerer des comptes utilisateurs natifs UniDash
- FR7: L'administrateur peut connecter UniDash a un Active Directory existant
- FR8: Le systeme active automatiquement l'authentification OpenID Connect pour les apps compatibles
- FR9: Les utilisateurs peuvent s'authentifier avec un seul compte (SSO) pour toutes les apps
- FR10: L'administrateur peut assigner un role (super-admin, admin, utilisateur) a chaque compte
- FR11: Le systeme configure automatiquement l'authentification LDAP/AD pour les apps compatibles LDAP mais non OIDC
- FR12: Le systeme peut authentifier les apps legacy (non OIDC, non LDAP) via proxy auth

**Store & Applications (FR13-FR20)**

- FR13: L'administrateur peut parcourir le Store officiel des applications
- FR14: L'administrateur peut installer une application depuis le Store en one-click
- FR15: L'administrateur peut definir quels utilisateurs ont acces a chaque application
- FR16: L'utilisateur peut parcourir son Store personnel (apps autorisees uniquement)
- FR17: L'utilisateur peut ajouter une application autorisee a son bureau
- FR18: L'administrateur peut desinstaller une application
- FR19: L'administrateur peut mettre a jour une application
- FR20: Le developpeur peut packager une application au format YAML declaratif

**Bureau Web (FR21-FR27)**

- FR21: L'utilisateur peut acceder a son bureau personnel via navigateur
- FR22: L'utilisateur peut organiser ses applications en fenetres redimensionnables
- FR23: L'utilisateur peut utiliser des splits (division ecran type Android)
- FR24: L'utilisateur peut organiser ses apps dans des docks thematiques
- FR25: L'utilisateur peut creer des raccourcis vers ses applications favorites
- FR26: L'utilisateur peut ouvrir plusieurs applications simultanement (4-5)
- FR27: L'utilisateur peut personnaliser l'apparence de son bureau

**Gestion des Permissions MVP (FR28-FR30)**

- FR28: Le super-admin peut acceder a toutes les fonctionnalites du systeme
- FR29: L'admin peut installer des applications et gerer les utilisateurs
- FR30: L'utilisateur peut uniquement utiliser les applications qui lui sont autorisees

**Administration Systeme (FR31-FR34)**

- FR31: L'administrateur peut visualiser l'etat du cluster (noeuds, services)
- FR32: L'administrateur peut consulter les logs centralises
- FR33: Le systeme integre une solution de sauvegarde (Velero/Longhorn)
- FR34: L'administrateur peut acceder directement aux outils sous-jacents (kubectl, Proxmox, etc.)

### NonFunctional Requirements

**Performance (NFR1-NFR5)**

- NFR1: Le bureau web vide se charge en < 2 secondes sur connexion standard
- NFR2: L'ouverture d'une app dans le bureau prend < 1 seconde (hors chargement app elle-meme)
- NFR3: Le systeme supporte 4-5 applications ouvertes simultanement sans degradation perceptible
- NFR4: L'installation d'une application depuis le Store prend < 5 minutes
- NFR5: L'installation initiale du cluster complet prend < 30 minutes

**Securite (NFR6-NFR10)**

- NFR6: Toutes les communications sont chiffrees (HTTPS, VPN)
- NFR7: Les mots de passe sont stockes avec hachage securise (bcrypt/argon2)
- NFR8: Les sessions expirent apres 24h d'inactivite
- NFR9: L'acces au cluster est restreint au VPN ou reseau local
- NFR10: Chaque app tourne dans son namespace isole

**Fiabilite & Disponibilite (NFR11-NFR14)**

- NFR11: Le cluster K3S supporte la perte d'un noeud sans interruption de service (HA)
- NFR12: Les sauvegardes automatiques sont effectuees quotidiennement (Velero/Longhorn)
- NFR13: La restauration d'une sauvegarde est possible en < 30 minutes
- NFR14: Le systeme maintient une disponibilite de 95% (hors maintenance planifiee)

**Integration (NFR15-NFR18)**

- NFR15: L'integration AD supporte les formats LDAP standards
- NFR16: Les apps OpenID compatibles s'integrent automatiquement au SSO
- NFR17: Les apps legacy peuvent etre integrees via proxy auth
- NFR18: Le format de packaging d'apps utilise YAML declaratif standard

**Maintenabilite (NFR19-NFR21)**

- NFR19: Les mises a jour du systeme ne necessitent pas de downtime complet
- NFR20: Les logs sont centralises et consultables via interface
- NFR21: L'acces aux outils sous-jacents (kubectl, etc.) reste toujours disponible

**Accessibilite (NFR22-NFR24)**

- NFR22: L'interface est navigable au clavier
- NFR23: Les contrastes respectent les standards WCAG AA
- NFR24: Le bureau web passe le "test Giselle" - utilisable sans formation technique

### Additional Requirements

**From Architecture Document:**

- AR1: Starter template Astro minimal + TypeScript strict + Tailwind v4 + Headless UI
- AR2: Backend FastAPI avec src layout PyPA (unidash_* packages)
- AR3: 5 APIs separees pour resilience maximale :
  - api/db (ClusterIP) - Acces base de donnees
  - api/sso (Internet/VPN User - meme exposition qu'api/unidash) - Authentification SSO, sessions, provider OIDC, consomme API-DB
  - api/unidash (Internet/VPN User) - API metier utilisateurs
  - api/admin (VPN Admin) - API administration
  - api/backup (ClusterIP) - Gestion sauvegardes
- AR16: Dependencies API SSO : Authlib (OIDC), python-ldap (AD), redis-py + hiredis (sessions), argon2-cffi (hashing), PyJWT (tokens OIDC), python-cryptography (secrets)
- AR4: PostgreSQL HA via Patroni + etcd (3 noeuds)
- AR5: Sessions Redis server-side gerees par api/sso (pas de JWT)
- AR6: JSON:API format pour toutes les reponses
- AR7: GitFlow branching (main/develop + feature/release/hotfix)
- AR8: Conventional Commits (feat/fix/docs/style/refactor/test/chore)
- AR9: Coverage 100% blocking in CI (pytest + Vitest + Playwright)
- AR10: Monitoring Prometheus + Grafana + Loki
- AR11: Architecture SPA-like Islands - toutes les pages avec React islands client:load
- AR12: View Transitions API (Astro 5) pour navigation fluide
- AR13: HAProxy (HTTP/TCP) + Nginx (UDP) pour reverse proxy
- AR14: cert-manager (K3S) + Certbot (autres) pour TLS
- AR15: Cascade d'authentification apps : OIDC natif > LDAP/AD natif > Proxy Auth

**From UX Design Document:**

- UX1: Dock lateral gauche (compact 48px desktop, standard 56px tablette, bottom bar mobile)
- UX2: Tiling system avec layouts predéfinis (1/2/3/4 zones)
- UX3: WindowFrame avec titlebar (nav-controls back/forward + window-controls)
- UX4: Store cards style macOS App Store
- UX5: Wizard installation style Vercel (etapes visuelles)
- UX6: Onboarding 3-4 slides au premier login (skip visible, ne revient jamais)
- UX7: Sons macOS-like discrets (optionnel)
- UX8: Animations subtiles (transitions 150-200ms)
- UX9: Dark/Light mode avec detection systeme auto
- UX10: Responsive breakpoints : mobile <768px, tablette 768-1023px, desktop >=1024px
- UX11: WCAG 2.1 AA compliance

### FR Coverage Map

| FR | Epic | Description |
|----|------|-------------|
| FR1 | Epic 1 | Installation cluster K3S HA via wizard |
| FR2 | Epic 1 | Ajout de noeuds au cluster |
| FR3 | Epic 1 | Configuration VPN L2TP/IPsec |
| FR4 | Epic 1 | Configuration reverse proxy |
| FR5 | Epic 1 | Gestion certificats SSL |
| FR6 | Epic 2 | Comptes utilisateurs natifs |
| FR7 | Epic 2 | Connexion Active Directory |
| FR8 | Epic 2 | Auth OIDC automatique |
| FR9 | Epic 2 | SSO pour toutes les apps |
| FR10 | Epic 2 | Assignation des roles |
| FR11 | Epic 2 | Auth LDAP/AD pour apps compatibles |
| FR12 | Epic 2 | Proxy auth pour apps legacy |
| FR13 | Epic 3 | Parcourir store officiel |
| FR14 | Epic 3 | Installation one-click |
| FR15 | Epic 3 | Definition acces utilisateurs |
| FR16 | Epic 3 | Store personnel utilisateur |
| FR17 | Epic 3 | Ajout app au bureau |
| FR18 | Epic 3 | Desinstallation apps |
| FR19 | Epic 3 | Mise a jour apps |
| FR20 | Epic 3 | Packaging YAML |
| FR21 | Epic 4 | Acces bureau web |
| FR22 | Epic 4 | Fenetres redimensionnables |
| FR23 | Epic 4 | Splits ecran |
| FR24 | Epic 4 | Docks thematiques |
| FR25 | Epic 4 | Raccourcis favoris |
| FR26 | Epic 4 | Multi-apps simultanees |
| FR27 | Epic 4 | Personnalisation apparence |
| FR28 | Epic 5 | Acces super-admin |
| FR29 | Epic 5 | Acces admin |
| FR30 | Epic 5 | Acces utilisateur |
| FR31 | Epic 6 | Visualisation cluster |
| FR32 | Epic 6 | Logs centralises |
| FR33 | Epic 6 | Sauvegardes Velero |
| FR34 | Epic 6 | Acces outils sous-jacents |

**Couverture : 34/34 FRs (100%)**

## Epic List

### Epic 1: L'Admin Deploie un Cluster Pret a l'Emploi
L'administrateur peut installer et securiser un cluster UniDash pret a heberger des services.

**Ce que l'utilisateur peut accomplir :**
- Installer UniDash sur 3+ serveurs via wizard guide
- Avoir un cluster K3S HA fonctionnel
- Securiser l'acces via VPN L2TP/IPsec
- Avoir des certificats SSL auto-geres
- Avoir un reverse proxy fonctionnel

**FRs couverts :** FR1, FR2, FR3, FR4, FR5
**NFRs adresses :** NFR5, NFR6, NFR9, NFR11

---

### Epic 2: Authentification & Gestion des Identites
Les utilisateurs peuvent s'authentifier de maniere unifiee, qu'ils soient natifs UniDash ou depuis Active Directory.

**Ce que l'utilisateur peut accomplir :**
- Creer/gerer des comptes natifs UniDash
- Connecter un AD existant
- Se connecter avec SSO sur toutes les apps
- Avoir les apps auto-configurees (OIDC > LDAP > Proxy Auth)
- Assigner des roles (super-admin, admin, user)

**FRs couverts :** FR6, FR7, FR8, FR9, FR10, FR11, FR12
**NFRs adresses :** NFR7, NFR8, NFR15, NFR16, NFR17

**Implementation technique :**
- API SSO separee (`api/sso` - `unidash_sso`) pour resilience maximale
- Meme exposition qu'api/unidash (Internet/VPN User)
- Consomme API-DB pour users/apps/permissions
- Sessions Redis server-side (pas JWT)
- Dependencies : Authlib, python-ldap, redis-py, argon2-cffi, PyJWT, python-cryptography

---

### Epic 3: Store & Installation d'Applications
Les administrateurs peuvent installer des applications depuis le store, et les utilisateurs autorises peuvent y acceder via la meme interface avec un switch de vue.

**Ce que l'utilisateur peut accomplir :**
- Parcourir le store (vue admin ou user selon permissions)
- Basculer entre vue Admin et vue User via switch button
- Installer une app en one-click (vue admin)
- Definir qui a acces a chaque app (vue admin)
- Voir ses apps autorisees (vue user)
- Ajouter une app autorisee a son bureau (vue user)
- Mettre a jour/desinstaller des apps (vue admin)
- Packager des apps (developpeur)

**FRs couverts :** FR13, FR14, FR15, FR16, FR17, FR18, FR19, FR20
**NFRs adresses :** NFR4, NFR10, NFR18

---

### Epic 4: Bureau Web & Experience Utilisateur
Les utilisateurs peuvent acceder a leurs applications via un bureau web intuitif, style smartphone/Android.

**Ce que l'utilisateur peut accomplir :**
- Acceder a son bureau personnel via navigateur
- Organiser ses apps en fenetres redimensionnables
- Utiliser des splits (2/3/4 zones)
- Organiser ses apps dans des docks thematiques
- Creer des raccourcis favoris
- Ouvrir 4-5 apps simultanement
- Personnaliser l'apparence (theme, wallpaper)

**FRs couverts :** FR21, FR22, FR23, FR24, FR25, FR26, FR27
**NFRs adresses :** NFR1, NFR2, NFR3, NFR22, NFR23, NFR24

---

### Epic 5: Permissions & Controle d'Acces
Le systeme de permissions garantit que chaque utilisateur n'accede qu'a ce qui lui est autorise.

**Ce que l'utilisateur peut accomplir :**
- Super-admin : acces total
- Admin : installer apps, gerer users
- User : utiliser apps autorisees uniquement

**FRs couverts :** FR28, FR29, FR30
**NFRs adresses :** NFR10

---

### Epic 6: Administration & Observabilite
Les administrateurs peuvent surveiller, maintenir et sauvegarder l'infrastructure.

**Ce que l'utilisateur peut accomplir :**
- Visualiser l'etat du cluster (noeuds, services)
- Consulter les logs centralises
- Configurer et restaurer des sauvegardes
- Acceder aux outils sous-jacents (kubectl, etc.)

**FRs couverts :** FR31, FR32, FR33, FR34
**NFRs adresses :** NFR12, NFR13, NFR14, NFR19, NFR20, NFR21

**Implementation technique :**
- API Admin (`api/admin` - `unidash_admin`) - VPN Admin only
- API Backup separee (`api/backup` - `unidash_backup`) - ClusterIP interne
- Backup service : abstraction layer avec backends (Velero V1, PBS/Docker V2+)
- Monitoring : Prometheus + Grafana + Loki

---

## Continuous Documentation Policy

**Principe :** La documentation fait partie intégrante de chaque story, pas un epic séparé.

**Language :** English only (code comments, docstrings, JSDoc, Starlight docs, commits, PRs)

**Règles :**
1. **Story 1.1** inclut le setup initial complet :
   - GitHub Community Standards (README, CONTRIBUTING, LICENSE, SECURITY, templates)
   - Starlight documentation structure
   - CI/CD with documentation enforcement
2. **Chaque story** met à jour la documentation Starlight correspondante
3. **CI bloque** les PRs sans documentation (docstrings, JSDoc, Starlight)

**Documentation par story :**

| Type de story | Documentation requise |
|---------------|----------------------|
| Infrastructure | `docs/deployment/` |
| API | `docs/api/` + OpenAPI auto |
| Frontend | `docs/getting-started/` |
| Architecture majeure | `docs/architecture/` |

**Enforcement automatique (CI) :**
- `Ruff D rules` (Python) - 100% docstring coverage (Google style)
- `eslint-plugin-jsdoc` (TypeScript) - JSDoc on exports
- Custom action - Starlight update required based on changed files
- `CodeRabbit AI` - AI code review (advisory)

## Flux de Dependances

```
Epic 1 (Infrastructure)
    │
    └──► Epic 2 (Auth) ──► Epic 5 (Permissions)
              │
              └──► Epic 3 (Store) ──► Epic 4 (Bureau)
                        │
                        └──► Epic 6 (Admin)
```

**Chaque epic est autonome et fonctionnel apres completion.**

---

## Epic 1: L'Admin Deploie un Cluster Pret a l'Emploi - Stories

### Story 1.1: Initialisation du Projet UniDash

As a **developpeur**,
I want **une structure de projet initialisee avec les outils de developpement et la documentation**,
So that **je puisse commencer le developpement avec les bonnes pratiques et une documentation automatisee**.

**Acceptance Criteria:**

**Given** un repository git vide
**When** le script d'initialisation est execute
**Then** la structure de repertoires est creee selon project-context.md
**And** les fichiers pyproject.toml sont configures pour chaque API (avec Ruff docstring rules)
**And** les linters (Ruff, Black, ESLint, Prettier) sont configures avec documentation enforcement
**And** les hooks pre-commit sont installes
**And** le workflow CI GitHub Actions est cree avec:
  - Tests + coverage 100%
  - Docstring/JSDoc enforcement (blocking)
  - Starlight docs check (blocking)
  - CodeRabbit AI review (advisory)
  - Auto-generation API docs (mkdocstrings + starlight-typedoc)

**GitHub Community Standards (100%):**
**And** README.md est cree (English, liens vers Starlight)
**And** CONTRIBUTING.md est cree (English, GitFlow, Conventional Commits)
**And** CODE_OF_CONDUCT.md est cree (Contributor Covenant v2.1)
**And** LICENSE est cree (MIT)
**And** SECURITY.md est cree (English)
**And** .github/ISSUE_TEMPLATE/ est configure (bug, feature, question)
**And** .github/PULL_REQUEST_TEMPLATE.md est cree
**And** .github/dependabot.yml est configure

**Starlight Documentation:**
**And** docs/ est initialise avec Astro Starlight
**And** la structure de base est creee (getting-started/, architecture/, api/, deployment/, development/)
**And** starlight-typedoc est configure pour auto-generation
**And** la sidebar est configuree avec liens Community vers GitHub .md

**Couvre:** AR2, AR7, AR8, AR9, Documentation Policy (enablement story)

---

### Story 1.2: Installation du Premier Noeud K3S

As a **administrateur systeme**,
I want **installer le premier noeud K3S via un wizard guide**,
So that **je dispose d'un cluster Kubernetes fonctionnel de base**.

**Acceptance Criteria:**

**Given** un serveur Linux avec les prerequis systeme
**When** l'administrateur execute le wizard d'installation
**Then** K3S server est installe et demarre
**And** kubectl est configure et accessible
**And** le noeud est marque comme control-plane
**And** etcd est initialise pour le cluster HA
**And** l'etat du cluster est verifiable via kubectl get nodes

**Couvre:** FR1 (partiellement)

---

### Story 1.3: Ajout de Noeuds au Cluster K3S HA

As a **administrateur systeme**,
I want **ajouter des noeuds supplementaires au cluster**,
So that **le cluster soit hautement disponible avec 3+ noeuds**.

**Acceptance Criteria:**

**Given** un cluster K3S avec au moins un noeud control-plane
**When** l'administrateur execute la commande d'ajout de noeud
**Then** un token de join est genere automatiquement
**And** le nouveau serveur rejoint le cluster
**And** etcd est replique sur le nouveau noeud
**And** le cluster supporte la perte d'un noeud sans interruption
**And** kubectl get nodes affiche tous les noeuds en Ready

**Couvre:** FR1, FR2, NFR11

---

### Story 1.4: Configuration VPN L2TP/IPsec

As a **administrateur systeme**,
I want **configurer automatiquement le VPN L2TP/IPsec**,
So that **l'acces au cluster soit securise depuis l'exterieur**.

**Acceptance Criteria:**

**Given** un cluster K3S fonctionnel
**When** le wizard de configuration VPN est execute
**Then** strongSwan est installe et configure
**And** les certificats IPsec sont generes
**And** le service L2TP est demarre et accessible
**And** les utilisateurs peuvent se connecter via client VPN natif
**And** le traffic VPN est route vers le cluster
**And** les logs de connexion sont disponibles

**Couvre:** FR3, NFR6, NFR9

---

### Story 1.5: Gestion Automatique des Certificats SSL

As a **administrateur systeme**,
I want **que les certificats SSL soient geres automatiquement**,
So that **toutes les communications soient chiffrees sans maintenance manuelle**.

**Acceptance Criteria:**

**Given** un cluster K3S avec acces Internet
**When** cert-manager est deploye
**Then** cert-manager est installe dans le cluster
**And** un ClusterIssuer Let's Encrypt est configure
**And** les certificats sont automatiquement renouveles avant expiration
**And** les certificats wildcard sont supportes
**And** Certbot est disponible pour les services hors K3S (Proxmox, Docker)
**And** les certificats sont stockes en secrets Kubernetes

**Couvre:** FR5, NFR6

---

### Story 1.6: Configuration Reverse Proxy HAProxy (HTTP/TCP)

As a **administrateur systeme**,
I want **un reverse proxy configure automatiquement pour les services HTTP/TCP**,
So that **les applications soient accessibles via des URLs propres avec TLS**.

**Acceptance Criteria:**

**Given** un cluster K3S avec cert-manager fonctionnel
**When** HAProxy est deploye
**Then** HAProxy est installe et configure
**And** les certificats SSL sont automatiquement utilises
**And** le traffic HTTP est redirige vers HTTPS
**And** les health checks sont actifs pour chaque backend
**And** les headers de securite sont ajoutes (HSTS, X-Frame-Options)
**And** la configuration est rechargeable sans downtime

**Couvre:** FR4 (HTTP/TCP), NFR6

---

### Story 1.7: Configuration Nginx Stream pour Traffic UDP

As a **administrateur systeme**,
I want **Nginx stream configure pour le traffic UDP**,
So that **les services necessitant UDP (comme le VPN) soient correctement routes**.

**Acceptance Criteria:**

**Given** un cluster K3S avec HAProxy fonctionnel
**When** Nginx stream est deploye
**Then** le module stream de Nginx est installe et configure
**And** le traffic UDP est route vers les services appropries
**And** les ports UDP du VPN (500, 4500) sont exposes
**And** la configuration coexiste avec HAProxy sans conflit
**And** les logs UDP sont disponibles pour debug

**Couvre:** FR4 (UDP)

---

**Resume Epic 1:** 7 stories | FRs couverts: FR1, FR2, FR3, FR4, FR5 | NFRs: NFR5, NFR6, NFR9, NFR11

---

## Epic 2: Authentification & Gestion des Identites - Stories

### Story 2.1: Structure API SSO et API-DB

As a **developpeur**,
I want **les APIs SSO et DB initialisees avec leur structure FastAPI**,
So that **je puisse implementer les fonctionnalites d'authentification**.

**Acceptance Criteria:**

**Given** le projet UniDash initialise
**When** les packages unidash_sso et unidash_db sont crees
**Then** la structure src layout PyPA est respectee
**And** les dependances SSO sont installees (Authlib, python-ldap, redis-py, argon2-cffi, PyJWT, python-cryptography)
**And** les endpoints de health check repondent
**And** la connexion Redis est etablie
**And** les tests unitaires de base passent

**Couvre:** AR2, AR3, AR5, AR6, AR16 (enablement story)

---

### Story 2.2: Modele Utilisateur et Creation de Comptes Natifs

As a **administrateur UniDash**,
I want **creer des comptes utilisateurs natifs**,
So that **les utilisateurs puissent acceder a UniDash sans Active Directory**.

**Acceptance Criteria:**

**Given** l'API-DB fonctionnelle
**When** l'administrateur cree un utilisateur via API
**Then** l'utilisateur est stocke en base avec mot de passe hashe (argon2)
**And** les champs requis sont valides (email, username)
**And** les doublons sont rejetes
**And** l'administrateur peut lister, modifier et supprimer les utilisateurs
**And** les mots de passe ne sont jamais retournes dans les reponses

**Couvre:** FR6, NFR7

---

### Story 2.3: Sessions Redis et Login Natif

As a **utilisateur UniDash**,
I want **me connecter avec mes identifiants natifs**,
So that **j'accede a mon espace personnel de maniere securisee**.

**Acceptance Criteria:**

**Given** un compte utilisateur natif existant
**When** l'utilisateur soumet email/mot de passe valides
**Then** une session est creee dans Redis
**And** un cookie de session securise est retourne
**And** la session expire apres 24h d'inactivite
**And** l'utilisateur peut se deconnecter (revocation session)
**And** les tentatives echouees sont loggees

**Couvre:** FR9 (partiellement), NFR8

---

### Story 2.4: Connexion Active Directory

As a **administrateur UniDash**,
I want **connecter UniDash a un Active Directory existant**,
So that **les utilisateurs AD puissent se connecter avec leurs identifiants entreprise**.

**Acceptance Criteria:**

**Given** les parametres de connexion AD (host, base DN, bind DN)
**When** l'administrateur configure la connexion AD
**Then** la connexion LDAP est testee et validee
**And** les utilisateurs AD peuvent s'authentifier
**And** les attributs utilisateur sont mappes (email, displayName, groups)
**And** les erreurs de connexion AD sont clairement reportees
**And** le fallback vers auth native fonctionne si AD indisponible

**Couvre:** FR7, NFR15

---

### Story 2.5: Assignation des Roles Utilisateurs

As a **administrateur UniDash**,
I want **assigner un role a chaque utilisateur**,
So that **les permissions soient correctement appliquees**.

**Acceptance Criteria:**

**Given** un utilisateur existant (natif ou AD)
**When** l'administrateur assigne un role
**Then** le role est enregistre (super-admin, admin, user)
**And** le role est inclus dans les informations de session
**And** seul un super-admin peut creer d'autres super-admins
**And** le premier utilisateur cree est automatiquement super-admin
**And** les changements de role sont audites

**Couvre:** FR10

---

### Story 2.6: Provider OIDC UniDash

As a **application compatible OIDC**,
I want **UniDash comme provider OIDC**,
So that **les utilisateurs beneficient du SSO automatique**.

**Acceptance Criteria:**

**Given** l'API SSO fonctionnelle avec sessions
**When** une app demande l'authentification OIDC
**Then** l'endpoint /.well-known/openid-configuration est accessible
**And** le flow Authorization Code fonctionne
**And** les tokens JWT sont signes correctement
**And** l'endpoint /oauth/userinfo retourne les claims utilisateur
**And** les apps enregistrees peuvent utiliser le SSO

**Couvre:** FR8, FR9, NFR16

---

### Story 2.7: Configuration LDAP/AD pour Applications

As a **administrateur UniDash**,
I want **configurer automatiquement LDAP pour les apps non-OIDC**,
So that **les apps compatibles LDAP utilisent l'AD sans config manuelle**.

**Acceptance Criteria:**

**Given** une app installee supportant LDAP mais pas OIDC
**When** l'app est configuree
**Then** le systeme detecte la compatibilite LDAP
**And** les parametres LDAP sont auto-generes vers l'AD connecte
**And** les utilisateurs AD peuvent s'authentifier sur l'app
**And** la synchronisation des groupes fonctionne
**And** un fallback vers proxy auth est propose si echec

**Couvre:** FR11, NFR15

---

### Story 2.8: Proxy Auth pour Applications Legacy

As a **administrateur UniDash**,
I want **authentifier les apps legacy via headers proxy**,
So that **meme les apps sans OIDC/LDAP soient securisees**.

**Acceptance Criteria:**

**Given** une app installee sans support OIDC ni LDAP
**When** l'app est configuree en mode Proxy Auth
**Then** HAProxy injecte les headers d'authentification (X-Forwarded-User, X-Forwarded-Email)
**And** l'acces a l'app necessite une session UniDash valide
**And** les headers sont securises (non-forgeable depuis l'exterieur)
**And** le logout UniDash deconnecte aussi de l'app
**And** la configuration HAProxy est generee automatiquement

**Couvre:** FR12, NFR17

---

**Resume Epic 2:** 8 stories | FRs couverts: FR6, FR7, FR8, FR9, FR10, FR11, FR12 | NFRs: NFR7, NFR8, NFR15, NFR16, NFR17

---

## Epic 3: Store & Installation d'Applications - Stories

### Story 3.1: Modele Application et Catalogue Store

As a **administrateur UniDash**,
I want **un catalogue d'applications disponibles**,
So that **je puisse decouvrir les applications installables**.

**Acceptance Criteria:**

**Given** l'API UniDash fonctionnelle
**When** l'administrateur accede au Store
**Then** les applications du catalogue sont listees
**And** chaque app affiche nom, description, icone, version
**And** les apps sont categorisees (productivite, media, dev, etc.)
**And** la recherche par nom fonctionne
**And** les metadonnees incluent les compatibilites auth (OIDC/LDAP/Proxy)

**Couvre:** FR13

---

### Story 3.2: Repository Store GitHub et Infrastructure de Contribution

As a **developpeur communautaire**,
I want **un repository GitHub template pour contribuer des applications au Store**,
So that **je puisse soumettre mes apps facilement avec un processus clair et securise**.

**Acceptance Criteria:**

**Given** le besoin d'un ecosysteme d'applications ouvert
**When** le repository unidash-store est cree
**Then** la structure de fichiers est documentee et coherente :
```
unidash-store/
├── apps/
│   ├── <app-name>/
│   │   ├── unidash-app.yaml      # Manifest app
│   │   ├── README.md             # Documentation app
│   │   ├── CHANGELOG.md          # Historique versions
│   │   ├── icon.png              # Icone 512x512
│   │   └── screenshots/          # Captures ecran
│   └── ...
├── categories.yaml               # Definition categories
├── schema/
│   └── unidash-app.schema.json   # JSON Schema validation
├── .github/
│   ├── workflows/
│   │   ├── validate-pr.yml       # Validation automatique PR
│   │   ├── release.yml           # Publication branche prod
│   │   └── security-scan.yml     # Scan securite images
│   ├── ISSUE_TEMPLATE/
│   │   ├── new-app.md
│   │   └── bug-report.md
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── CODEOWNERS
├── CONTRIBUTING.md               # Guide contribution
├── CODE_OF_CONDUCT.md            # Code de conduite (Contributor Covenant)
├── LICENSE                       # MIT ou Apache 2.0
└── README.md                     # Documentation principale
```
**And** le repo est ajoute en git submodule dans le repo principal UniDash
**And** les branches sont protegees :
- `main` : production, deploiement auto vers Store officiel
- `develop` : integration, review obligatoire
- PR obligatoire avec 2 reviewers minimum pour `main`
- Signed commits requis
**And** les GitHub Actions valident :
- Schema YAML valide
- Image Docker existe et est pullable
- Pas de secrets hardcodes (gitleaks)
- Scan vulnerabilites (trivy)
- Tests de deploiement en sandbox
**And** le repository est template GitHub pour fork/clone
**And** le CONTRIBUTING.md explique le processus pas a pas

**Couvre:** FR20 (partiellement), NFR18

---

### Story 3.3: Format de Packaging YAML Declaratif

As a **developpeur d'application**,
I want **packager mon app au format YAML UniDash**,
So that **elle soit installable depuis le Store**.

**Acceptance Criteria:**

**Given** une application a packager
**When** le developpeur cree le fichier unidash-app.yaml
**Then** le format YAML est valide par un schema JSON
**And** les champs requis sont presents (name, version, image, ports)
**And** les options auth sont declarees (oidc_support, ldap_support)
**And** les ressources K8S sont generees automatiquement
**And** la documentation du format est disponible dans le repo Store

**Couvre:** FR20, NFR18

---

### Story 3.4: Installation One-Click depuis le Store

As a **administrateur UniDash**,
I want **installer une application en un clic**,
So that **le deploiement soit simple et rapide**.

**Acceptance Criteria:**

**Given** une application dans le catalogue Store
**When** l'administrateur clique sur "Installer"
**Then** les ressources K8S sont creees dans un namespace dedie
**And** l'app est configuree avec la cascade auth appropriee (OIDC > LDAP > Proxy)
**And** l'URL d'acces est generee automatiquement
**And** l'installation prend < 5 minutes
**And** le statut d'installation est affiche en temps reel

**Couvre:** FR14, NFR4, NFR10

---

### Story 3.5: Gestion des Permissions par Application

As a **administrateur UniDash**,
I want **definir quels utilisateurs ont acces a chaque application**,
So that **l'acces soit controle selon les besoins**.

**Acceptance Criteria:**

**Given** une application installee
**When** l'administrateur configure les permissions
**Then** il peut autoriser des utilisateurs individuels
**And** il peut autoriser des groupes AD
**And** les permissions sont verifiees a chaque acces
**And** les changements de permission sont immediats
**And** un utilisateur non autorise voit un message clair

**Couvre:** FR15

---

### Story 3.6: Store Personnel Utilisateur

As a **utilisateur UniDash**,
I want **voir uniquement les applications auxquelles j'ai acces**,
So that **je ne sois pas confus par des apps interdites**.

**Acceptance Criteria:**

**Given** un utilisateur connecte avec des permissions specifiques
**When** l'utilisateur accede a son Store personnel
**Then** seules les apps autorisees sont affichees
**And** les apps deja sur son bureau sont marquees
**And** l'utilisateur peut filtrer par categorie
**And** l'utilisateur peut rechercher dans ses apps autorisees

**Couvre:** FR16

---

### Story 3.7: Ajout d'Application au Bureau

As a **utilisateur UniDash**,
I want **ajouter une application autorisee a mon bureau**,
So that **j'y accede rapidement**.

**Acceptance Criteria:**

**Given** une application autorisee dans le Store personnel
**When** l'utilisateur clique sur "Ajouter au bureau"
**Then** l'app apparait dans son dock
**And** l'icone et le nom sont affiches
**And** l'app est accessible en un clic depuis le bureau
**And** l'ajout est persiste pour les sessions suivantes

**Couvre:** FR17

---

### Story 3.8: Mise a Jour d'Application

As a **administrateur UniDash**,
I want **mettre a jour une application installee**,
So that **les utilisateurs beneficient des dernieres versions**.

**Acceptance Criteria:**

**Given** une application installee avec une nouvelle version disponible
**When** l'administrateur lance la mise a jour
**Then** la nouvelle version est deployee
**And** les donnees utilisateur sont preservees
**And** le rollback est possible en cas d'echec
**And** les utilisateurs sont notifies de la mise a jour
**And** le downtime est minimise

**Couvre:** FR19

---

### Story 3.9: Desinstallation d'Application

As a **administrateur UniDash**,
I want **desinstaller une application**,
So that **je libere les ressources inutilisees**.

**Acceptance Criteria:**

**Given** une application installee
**When** l'administrateur lance la desinstallation
**Then** une confirmation est demandee
**And** les ressources K8S sont supprimees
**And** le namespace est nettoye
**And** l'app est retiree des bureaux utilisateurs
**And** les donnees peuvent etre sauvegardees avant suppression (optionnel)

**Couvre:** FR18

---

**Resume Epic 3:** 9 stories (3.1-3.9) | FRs couverts: FR13, FR14, FR15, FR16, FR17, FR18, FR19, FR20 | NFRs: NFR4, NFR10, NFR18

---

## Epic 4: Bureau Web & Experience Utilisateur - Stories

### Story 4.1: Structure Frontend Astro et Configuration

As a **developpeur**,
I want **le frontend Astro initialise avec la stack complete**,
So that **je puisse developper l'interface du bureau**.

**Acceptance Criteria:**

**Given** le projet UniDash initialise
**When** le package web/ est configure
**Then** Astro 5+ est installe avec TypeScript strict
**And** Tailwind v4 est configure avec la nouvelle architecture
**And** React est configure pour les islands
**And** Nanostores est installe pour la gestion d'etat
**And** TanStack Query est configure pour les appels API
**And** ESLint + Prettier sont configures
**And** les View Transitions API sont actives

**Couvre:** AR1, AR11, AR12 (enablement story)

---

### Story 4.2: Acces au Bureau Personnel

As a **utilisateur connecte**,
I want **acceder a mon bureau personnel via navigateur**,
So that **je retrouve mon espace de travail personnalise**.

**Acceptance Criteria:**

**Given** un utilisateur authentifie
**When** l'utilisateur accede a l'URL du bureau
**Then** le bureau se charge en < 2 secondes
**And** l'etat du bureau est restaure (apps ouvertes, positions)
**And** le dock lateral gauche est affiche
**And** le wallpaper personnalise est affiche
**And** la session est validee cote serveur

**Couvre:** FR21, NFR1

---

### Story 4.3: Systeme de Fenetres WindowFrame

As a **utilisateur UniDash**,
I want **ouvrir des applications dans des fenetres**,
So that **je puisse travailler avec plusieurs apps visibles**.

**Acceptance Criteria:**

**Given** une application ajoutee au bureau
**When** l'utilisateur clique sur l'icone de l'app
**Then** l'app s'ouvre dans un WindowFrame
**And** le WindowFrame a une titlebar avec nav-controls (back/forward)
**And** le WindowFrame a window-controls (minimize, maximize, close)
**And** l'iframe de l'app charge correctement
**And** le focus est gere entre les fenetres
**And** l'ouverture prend < 1 seconde (hors chargement app)

**Couvre:** NFR2

---

### Story 4.4: Fenetres Redimensionnables et Deplacables

As a **utilisateur UniDash**,
I want **redimensionner et deplacer mes fenetres**,
So that **j'organise mon espace de travail comme je veux**.

**Acceptance Criteria:**

**Given** un WindowFrame ouvert
**When** l'utilisateur drag les bords ou la titlebar
**Then** la fenetre se redimensionne fluidement
**And** la fenetre se deplace sur le bureau
**And** les dimensions minimales sont respectees
**And** la position est sauvegardee pour la session suivante
**And** le drag-and-drop fonctionne au clavier (accessibilite)

**Couvre:** FR22, NFR22

---

### Story 4.5: Tiling System et Splits

As a **utilisateur UniDash**,
I want **diviser mon ecran en zones predefinies**,
So that **j'organise rapidement mes apps comme sur Android**.

**Acceptance Criteria:**

**Given** le bureau avec une ou plusieurs fenetres
**When** l'utilisateur active le mode tiling
**Then** des layouts predefinies sont proposes (1/2/3/4 zones)
**And** l'utilisateur peut drag une fenetre vers une zone
**And** les zones se redimensionnent proportionnellement
**And** le snap aux bords fonctionne
**And** le double-tap sur titlebar toggle fullscreen
**And** les raccourcis clavier fonctionnent (Alt+fleches)

**Couvre:** FR23, UX2

---

### Story 4.6: Docks Thematiques

As a **utilisateur UniDash**,
I want **organiser mes applications dans des docks thematiques**,
So that **je retrouve facilement mes apps par categorie**.

**Acceptance Criteria:**

**Given** des applications sur le bureau
**When** l'utilisateur cree ou modifie un dock
**Then** il peut nommer le dock (Travail, Media, Dev, etc.)
**And** il peut drag-and-drop des apps vers le dock
**And** il peut reordonner les apps dans le dock
**And** le dock est collapsible (icone + chevron)
**And** le dock lateral gauche suit les specs UX (48px desktop, 56px tablette)
**And** les docks sont persistes entre sessions

**Couvre:** FR24, UX1

---

### Story 4.7: Raccourcis Favoris dans le Dock

As a **utilisateur UniDash**,
I want **creer des raccourcis vers mes applications favorites**,
So that **j'accede rapidement a mes apps les plus utilisees**.

**Acceptance Criteria:**

**Given** des applications sur le bureau
**When** l'utilisateur ajoute une app aux favoris
**Then** un raccourci apparait dans la section favoris du dock
**And** le raccourci affiche l'icone de l'app
**And** le clic droit propose "Retirer des favoris"
**And** les favoris sont limites a un nombre raisonnable (configurable)
**And** les favoris sont persistes entre sessions

**Couvre:** FR25 (partiellement)

---

### Story 4.8: Grille de Raccourcis Bureau

As a **utilisateur UniDash**,
I want **personnaliser une grille de raccourcis au centre du bureau**,
So that **j'accede a mes apps style smartphone avec des dossiers et groupes**.

**Acceptance Criteria:**

**Given** le bureau UniDash affiche
**When** l'utilisateur personnalise la grille centrale
**Then** une grille d'icones style smartphone est affichee
**And** l'utilisateur peut creer des dossiers/groupes d'apps
**And** l'utilisateur peut nommer les dossiers
**And** le drag-and-drop permet de reorganiser
**And** les dossiers s'ouvrent avec animation style iOS/Android
**And** la grille est responsive selon la taille d'ecran
**And** la personnalisation est persistee entre sessions

**Couvre:** FR25

---

### Story 4.9: Barre de Recherche Configurable

As a **utilisateur UniDash**,
I want **une barre de recherche configurable en haut du bureau**,
So that **je puisse utiliser UniDash comme page d'accueil navigateur**.

**Acceptance Criteria:**

**Given** le bureau UniDash affiche
**When** l'utilisateur configure la barre de recherche
**Then** la barre est affichee en haut du bureau (style new tab page)
**And** le moteur de recherche est configurable (Google, DuckDuckGo, Qwant, Bing, etc.)
**And** l'utilisateur peut ajouter des moteurs personnalises
**And** le raccourci clavier focus la barre (Ctrl+K ou /)
**And** l'autocompletion propose les apps du bureau
**And** Enter ouvre la recherche dans un nouvel onglet ou dans une fenetre bureau
**And** la barre peut etre masquee si non souhaitee

---

### Story 4.10: Multi-Applications Simultanees

As a **utilisateur UniDash**,
I want **ouvrir plusieurs applications en meme temps**,
So that **je travaille efficacement avec plusieurs outils**.

**Acceptance Criteria:**

**Given** le bureau avec des applications disponibles
**When** l'utilisateur ouvre plusieurs apps
**Then** jusqu'a 4-5 apps peuvent etre ouvertes simultanement
**And** les performances restent fluides (pas de lag perceptible)
**And** la memoire est geree efficacement (lazy loading iframes)
**And** le z-index des fenetres est gere correctement
**And** les apps en arriere-plan continuent de fonctionner

**Couvre:** FR26, NFR3

---

### Story 4.11: Personnalisation de l'Apparence

As a **utilisateur UniDash**,
I want **personnaliser l'apparence de mon bureau**,
So that **il reflete mes preferences visuelles**.

**Acceptance Criteria:**

**Given** un utilisateur connecte
**When** l'utilisateur accede aux parametres d'apparence
**Then** il peut choisir entre Dark/Light mode
**And** la detection du theme systeme est proposee (auto)
**And** il peut choisir un wallpaper parmi une selection ou upload
**And** il peut ajuster les couleurs d'accent
**And** les animations peuvent etre reduites (accessibilite)
**And** les preferences sont sauvegardees cote serveur

**Couvre:** FR27, UX9

---

### Story 4.12: Onboarding Premier Login

As a **nouvel utilisateur UniDash**,
I want **un onboarding guide lors de mon premier login**,
So that **je comprenne rapidement comment utiliser le bureau**.

**Acceptance Criteria:**

**Given** un utilisateur qui se connecte pour la premiere fois
**When** le bureau se charge
**Then** un onboarding de 3-4 slides est affiche
**And** chaque slide explique une fonctionnalite cle
**And** un bouton "Skip" est visible a tout moment
**And** l'onboarding ne reapparait jamais apres completion ou skip
**And** l'utilisateur peut revoir l'onboarding depuis les parametres

**Couvre:** UX6

---

### Story 4.13: Responsive et Accessibilite Bureau

As a **utilisateur mobile ou en situation de handicap**,
I want **un bureau responsive et accessible**,
So that **j'utilise UniDash sur tous mes appareils**.

**Acceptance Criteria:**

**Given** le bureau UniDash
**When** l'utilisateur accede depuis differents devices
**Then** le layout s'adapte (mobile <768px, tablette 768-1023px, desktop >=1024px)
**And** le dock passe en bottom bar sur mobile
**And** le bureau est navigable au clavier
**And** les contrastes respectent WCAG AA
**And** les focus states sont visibles
**And** les animations respectent prefers-reduced-motion

**Couvre:** NFR22, NFR23, NFR24, UX10, UX11

---

**Resume Epic 4:** 13 stories | FRs couverts: FR21, FR22, FR23, FR24, FR25, FR26, FR27 | NFRs: NFR1, NFR2, NFR3, NFR22, NFR23, NFR24

---

## Epic 5: Permissions & Controle d'Acces - Stories

### Story 5.1: Middleware de Verification des Permissions

As a **systeme UniDash**,
I want **verifier les permissions a chaque requete**,
So that **l'acces soit securise de maniere coherente**.

**Acceptance Criteria:**

**Given** une requete API authentifiee
**When** la requete est traitee
**Then** le role de l'utilisateur est verifie depuis la session
**And** les permissions specifiques sont validees
**And** un acces refuse retourne 403 avec message clair
**And** les tentatives d'acces non autorise sont loggees
**And** le middleware est applique sur toutes les routes protegees

**Couvre:** NFR10, AR6 (enablement story - securite cross-cutting)

---

### Story 5.2: Acces Super-Admin Total

As a **super-administrateur UniDash**,
I want **acceder a toutes les fonctionnalites du systeme**,
So that **je puisse gerer l'infrastructure complete**.

**Acceptance Criteria:**

**Given** un utilisateur avec role super-admin
**When** l'utilisateur accede aux fonctionnalites
**Then** toutes les APIs sont accessibles sans restriction
**And** l'acces admin est autorise (api/admin via VPN)
**And** la gestion des autres super-admins est possible
**And** l'acces aux outils sous-jacents est autorise
**And** les actions sensibles sont auditees

**Couvre:** FR28

---

### Story 5.3: Acces Admin Applications et Utilisateurs

As a **administrateur UniDash**,
I want **installer des applications et gerer les utilisateurs**,
So that **je puisse administrer le quotidien sans acces systeme complet**.

**Acceptance Criteria:**

**Given** un utilisateur avec role admin
**When** l'utilisateur accede aux fonctionnalites admin
**Then** l'installation/desinstallation d'apps est autorisee
**And** la gestion des permissions par app est autorisee
**And** la creation/modification d'utilisateurs (non super-admin) est autorisee
**And** l'acces aux outils sous-jacents est refuse
**And** l'acces au panel admin K8S est limite (read-only)

**Couvre:** FR29

---

### Story 5.4: Acces Utilisateur Restreint

As a **utilisateur standard UniDash**,
I want **acceder uniquement a mes applications autorisees**,
So that **je ne voie que ce qui m'est pertinent**.

**Acceptance Criteria:**

**Given** un utilisateur avec role user
**When** l'utilisateur utilise UniDash
**Then** seules les apps autorisees sont visibles dans son Store
**And** seules les apps autorisees peuvent etre ouvertes
**And** l'acces aux APIs admin est refuse (403)
**And** les parametres systeme ne sont pas accessibles
**And** la personnalisation du bureau reste possible

**Couvre:** FR30

---

### Story 5.5: Audit Trail des Actions Sensibles

As a **administrateur securite**,
I want **un log des actions sensibles**,
So that **je puisse auditer les acces et modifications**.

**Acceptance Criteria:**

**Given** des actions sensibles dans le systeme
**When** une action est effectuee (login, permission change, install, etc.)
**Then** l'action est loggee avec timestamp, user, action, target
**And** les logs sont stockes de maniere securisee
**And** les logs sont consultables via l'interface admin
**And** les logs sont exportables pour analyse
**And** la retention des logs est configurable

---

**Resume Epic 5:** 5 stories | FRs couverts: FR28, FR29, FR30 | NFRs: NFR10

---

## Epic 6: Administration & Observabilite - Stories

### Story 6.1: Dashboard Etat du Cluster

As a **administrateur systeme**,
I want **visualiser l'etat du cluster en temps reel**,
So that **je detecte rapidement les problemes**.

**Acceptance Criteria:**

**Given** un cluster UniDash en fonctionnement
**When** l'administrateur accede au dashboard
**Then** l'etat de chaque noeud est affiche (Ready/NotReady)
**And** les ressources sont visualisees (CPU, RAM, stockage)
**And** les services critiques sont listes avec leur status
**And** les alertes sont mises en evidence
**And** le rafraichissement est automatique

**Couvre:** FR31

---

### Story 6.2: Interface Logs Centralises

As a **administrateur systeme**,
I want **consulter les logs centralises via interface web**,
So that **je diagnostique les problemes sans ligne de commande**.

**Acceptance Criteria:**

**Given** le stack Prometheus + Grafana + Loki deploye
**When** l'administrateur accede aux logs
**Then** les logs de tous les services sont accessibles
**And** la recherche par texte fonctionne
**And** le filtrage par service/niveau/date est disponible
**And** l'export des logs est possible
**And** les logs sont structures en JSON (parseable)

**Couvre:** FR32, NFR20

---

### Story 6.3: Configuration Sauvegardes Velero

As a **administrateur systeme**,
I want **configurer et gerer les sauvegardes**,
So that **les donnees soient protegees contre la perte**.

**Acceptance Criteria:**

**Given** un cluster UniDash fonctionnel
**When** l'administrateur configure les sauvegardes
**Then** Velero est deploye et configure
**And** les sauvegardes automatiques quotidiennes sont actives
**And** le stockage de destination est configurable (S3, NFS, etc.)
**And** la retention des sauvegardes est parametrable
**And** le statut des sauvegardes est visible dans le dashboard

**Couvre:** FR33, NFR12

---

### Story 6.4: Restauration depuis Sauvegarde

As a **administrateur systeme**,
I want **restaurer une sauvegarde en cas de besoin**,
So that **je puisse recuperer apres un incident**.

**Acceptance Criteria:**

**Given** des sauvegardes Velero disponibles
**When** l'administrateur lance une restauration
**Then** la liste des sauvegardes est affichee
**And** une restauration complete ou partielle est possible
**And** la restauration prend < 30 minutes
**And** les donnees sont coherentes apres restauration
**And** un rapport de restauration est genere

**Couvre:** FR33, NFR13

---

### Story 6.5: Acces Outils Sous-Jacents

As a **super-administrateur**,
I want **acceder directement aux outils sous-jacents**,
So that **je puisse effectuer des operations avancees**.

**Acceptance Criteria:**

**Given** un super-admin connecte via VPN
**When** l'administrateur accede aux outils
**Then** kubectl est accessible via terminal web ou SSH
**And** l'interface Proxmox est accessible
**And** l'interface Grafana est accessible
**And** l'interface Longhorn est accessible
**And** les acces sont authentifies et audites

**Couvre:** FR34, NFR21

---

### Story 6.6: Monitoring Prometheus et Alerting

As a **administrateur systeme**,
I want **recevoir des alertes en cas de probleme**,
So that **je sois informe proactivement**.

**Acceptance Criteria:**

**Given** le stack monitoring deploye
**When** une condition d'alerte est detectee
**Then** les metriques Prometheus sont collectees automatiquement
**And** les dashboards Grafana sont preconfigures
**And** les alertes sont declenchees selon des seuils configurables
**And** les notifications sont envoyees (email, webhook)
**And** l'historique des alertes est consultable

**Couvre:** AR10

---

### Story 6.7: Mises a Jour Systeme sans Downtime

As a **administrateur systeme**,
I want **mettre a jour UniDash sans interruption complete**,
So that **les utilisateurs ne soient pas impactes**.

**Acceptance Criteria:**

**Given** une nouvelle version d'UniDash disponible
**When** l'administrateur lance la mise a jour
**Then** la mise a jour se fait en rolling update
**And** les services restent accessibles pendant la mise a jour
**And** le rollback automatique se declenche en cas d'echec
**And** les utilisateurs sont notifies de la maintenance
**And** la version actuelle est affichee dans le dashboard

**Couvre:** NFR19

---

**Resume Epic 6:** 7 stories | FRs couverts: FR31, FR32, FR33, FR34 | NFRs: NFR12, NFR13, NFR14, NFR19, NFR20, NFR21
