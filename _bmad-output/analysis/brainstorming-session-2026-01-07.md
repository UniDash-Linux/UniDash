---
stepsCompleted: [1, 2, 3, 4]
inputDocuments: []
session_topic: 'UniDash - Exploration complète de tous les domaines clés'
session_goals: 'Structurer le projet et compléter les zones non explorées'
selected_approach: 'progressive-flow'
techniques_used: ['First Principles Thinking', 'Morphological Analysis', 'Six Thinking Hats', 'Decision Tree Mapping']
ideas_generated: ['Desktop web unifié', 'Flywheel popularité→monétisation', 'SAV scale avec apps internes seulement', 'Programme Ambassadeurs Homelab', 'UniDash Certified Admin', 'UniDash in a Box']
context_file: '_bmad/bmm/data/project-context-template.md'
session_complete: true
---

# Brainstorming Session Results - UniDash

**Facilitator:** Gabriel
**Date:** 2026-01-07

---

## Session Overview

**Sujet :** Exploration complète de UniDash - plateforme B2B de gestion d'infrastructure serveur avec bureau web intégré
Écosystème fragmenté : 5-10 interfaces distinctes à jongler (Proxmox, Portainer, Cockpit, et
**Objectifs :**
- Structurer le projet de manière exhaustive
- Identifier et compléter les zones non explorées
- Créer une base solide pour le Product Brief

**Domaines à explorer :**
1. Architecture globale
2. Bureau web (UX)
3. Marketplace/Store
4. Monétisation
5. Offres (Enterprise/Edu/Homelab)
6. Priorités MVP
7. Risques techniques
8. Métriques de succès

---

## Phase 1 : Exploration (First Principles Thinking)

### Domaine 1 : Architecture Globale

#### Vérités fondamentales identifiées

| Principe | Justification |
|----------|---------------|
| **Docker comme point d'entrée unique** | Universalité, compatibilité toutes distros Linux, stabilité |
| **Accessibilité sans compromis** | Origine du projet : simplifier ce qui est complexe |
| **Fiabilité critique** | Installation conséquente = pas de changements après coup |
| **Séparation Backend/Frontend** | Système d'extensions côté serveur + côté desktop |
| **Surcouche, pas remplacement** | Chapeaute Proxmox, Cockpit, Portainer - ne les remplace pas |

#### Architecture définie

```
┌─────────────────────────────────────────────────────────┐
│                    UNIDASH (Docker)                      │
│  ┌─────────────────┐    ┌─────────────────────────────┐ │
│  │ Frontend/Desktop│    │ Backend/Orchestration       │ │
│  │  - Extensions UI│    │  - Extensions services      │ │
│  │  - Bureau web   │    │  - Reverse proxy (HA Proxy) │ │
│  │  - iFrames apps │    │  - DNS/sous-domaines auto   │ │
│  └────────┬────────┘    └──────────────┬──────────────┘ │
└───────────┼─────────────────────────────┼───────────────┘
            │              APIs           │
     ┌──────┴──────────────────────────────┴──────┐
     │              INFRASTRUCTURE NATIVE          │
     │  ┌─────────┐  ┌─────────┐  ┌─────────────┐ │
     │  │Proxmox  │  │ KVM     │  │ K3S/K8s     │ │
     │  │(API)    │  │(API)    │  │(HA services)│ │
     │  └─────────┘  └─────────┘  └─────────────┘ │
     │  ┌─────────┐  ┌─────────┐                  │
     │  │ Docker  │  │ LXC     │                  │
     │  │(natif)  │  │(legacy) │                  │
     │  └─────────┘  └─────────┘                  │
     └────────────────────────────────────────────┘
```

#### Décisions architecturales clés

**Gestion des dépendances & conflits de versions :**
- NixPKGS pour les installations natives (isolation des dépendances)
- Conteneurs séparés pour les versions conflictuelles

**Niveaux de validation des extensions :**
1. **Non vérifié** (warning) - Proposé par la communauté, non testé
2. **Communauté** - Validé par X utilisateurs, support forum
3. **Certifié UniDash** - Validé par l'équipe, support SAV

**Sécurité & Isolation :**
- Authentification obligatoire (desktop = système privé)
- Permissions granulaires (super-admin → groupes → utilisateur)
- API intermédiaire UniDash entre frontend et backends (Proxmox, Docker, etc.)
- APIs backend non exposées (accès loopback conteneur→système)
- Option "environnement isolé" pour tests admin (conteneur/VM jetable)

**Résilience & Haute disponibilité :**
- UniDash lui-même en HA (instances multiples, failover DNS/IP)
- Services managés indépendants d'UniDash (proxy externe, etc.)
- Si UniDash tombe : services continuent, seul le desktop est indisponible
- Possibilité de séparer UniDash en micro-conteneurs (desktop, API, etc.)
- Détection et intégration des services installés manuellement

**Installation :**
- One-liner curl pour homelabs/monoserveur
- Ansible pour déploiement multi-serveurs (PME)
- Détection automatique de l'existant

#### Technologies cibles

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| Conteneurisation légère | Docker | Standard universel, homelabs |
| Orchestration HA | K3S (→ K8s en upgrade) | TPE/PME ≤100 serveurs |
| Hyperviseur | KVM, Proxmox (API) | Open source, standard |
| Conteneurs legacy | LXC | Compatibilité migrations |
| Reverse proxy | HAProxy (ou équivalent) | HA, performance |
| Gestion dépendances | NixPKGS | Isolation versions |
| Déploiement | curl + Ansible | Simple → Enterprise |

---

### Domaine 2 : Bureau Web (UX)

#### Philosophie UX

| Principe | Application |
|----------|-------------|
| **Simplicité forcée** | Pas de liberté totale = moins de bordel |
| **Organisation guidée** | Docks thématiques, groupes d'icônes, layouts |
| **Fullscreen natif** | Bureau en plein écran comme une vidéo |
| **Mobile-first ready** | Wayland pour support tactile |

#### Gestion des fenêtres

**Système de split Android-like :**
- Split 2, 3, ou 4 zones (vertical/horizontal)
- Pas de fenêtres flottantes libres (trop chaotique)
- Layouts sauvegardables (ex: "Dev" = IDE + terminal + browser)
- Raccourcis layouts dans le dock

**Actions sur fenêtres :**
- Redimensionnable (dans les splits)
- Minimisable (changement de layout sans fermer)
- Détachable → popup navigateur sans chrome (style Electron mais natif browser)

#### Système de Docks

**Docks thématiques (innovation clé) :**
- Bouton pour switcher entre docks
- Ex: Dock "Bureautique", Dock "Dev", Dock "Admin"
- Taille limitée par dock (force l'organisation)
- Icônes apps + icônes layouts sauvegardés

#### Affichage des applications

| Type | Technologie | Notes |
|------|-------------|-------|
| Apps web | iFrame | Standard, simple |
| Apps desktop | Guacamole (RDP/VNC) | Mono-app, pas UI complète |
| Protocole cible | Wayland | Support tactile mobile |
| Fallback X11 | XWayland | Rétrocompatibilité |

**Détachement :** Popup navigateur sans barre d'URL (Firefox/Chrome le permettent)

**Multi-écran :**
- Idéal : fullscreen sur plusieurs écrans (à valider techniquement)
- Fallback : détacher apps en popups séparées

#### Notifications

- Système type Android/Gnome/Windows
- Connexion possible : téléphone pro, mail, SMS
- Communication inter-employés
- Protocoles à investiguer

#### Personnalisation (limitée volontairement)

**Autorisé :**
- Fond d'écran
- Thème couleur (+ adaptation auto au fond d'écran)
- Groupes d'icônes sur bureau (pas placement libre)
- Choix des apps affichées (faux store personnel)

**Interdit :**
- Placement libre d'icônes (= bordel)
- Widgets (superflu, déjà dans dashboards admin)
- Customisation excessive

#### Faux Store Personnel

Concept clé : l'utilisateur choisit ses apps parmi celles autorisées par l'admin
- Admin donne accès à 20 apps
- User en affiche 5 sur son bureau
- Sensation de contrôle pour l'user

#### Performance & Réseau

**Prérequis :**
- Connexion internet minimum (à définir post-dev)
- Critique côté serveur > côté client
- Pas de mode offline (incompatible avec le concept)

**Sécurité réseau :**
- Intégration VPN (WireGuard prioritaire, OpenVPN option)
- VPN pour multi-sites serveurs
- VPN pour accès clients (optionnel)
- APIs admin derrière VPN obligatoire (non exposées sur internet)

---

### Domaine 3 : Marketplace / Store

#### Types de contenu

| Type | Description | Exemple |
|------|-------------|---------|
| **Apps Backend** | Services natifs, BDD, outils sysadmin | PostgreSQL, Nginx, Prometheus |
| **Apps Frontend** | UI, dashboards, extensions desktop | Dashboard monitoring, UI backup |
| **Apps hybrides** | Backend + Frontend intégrés | Nextcloud (service + iframe) |
| **Bundles** | Packs d'apps complémentaires | "Pack comptabilité PME" |
| **Configurations** | Templates de config par app | "Nextcloud - mode entreprise" |

**Note :** Une app peut être à la fois backend ET frontend (ex: Nextcloud = service + iframe dans le desktop)

#### Architecture des repositories

**Modèle inspiré de Linux :**

```
┌─────────────────────────────────────────────────────────┐
│                 REPO OFFICIEL UNIDASH                    │
│  - Apps développées par l'équipe                        │
│  - Apps validées/certifiées (PR GitHub approuvées)      │
│  - Vente d'apps payantes (contrôle légal)               │
└─────────────────────────────────────────────────────────┘
                          │
┌─────────────────────────┴─────────────────────────────┐
│                  REPOS EXTERNES                        │
│  - Ajoutés par les admins (comme apt sources)          │
│  - Auto-enregistrés sur serveurs UniDash (URL + IDs)   │
│  - Notés par la communauté (confiance + qualité)       │
│  - Apps gratuites uniquement                           │
└────────────────────────────────────────────────────────┘
```

**Niveaux de confiance :**
1. **Non vérifié** (warning) - Nouveau repo/app, pas de feedback
2. **Communauté** - X votes positifs, bon score qualité
3. **Certifié UniDash** - Validé par l'équipe, support SAV

#### Format de packaging

**Package = ZIP contenant :**
- Fichier déclaratif YAML/JSON (pas de bash pour sécurité)
- Métadonnées (voir ci-dessous)
- Instructions de déploiement

**Format déclaratif :**
```yaml
type: docker | lxc | vm | kubernetes | hybrid
source: docker-hub | incus | custom-url
image: nextcloud:latest
config_templates:
  - name: "Mode entreprise"
    description: "..."
  - name: "Mode homelab"
    description: "..."
dependencies:
  backend: [postgres, redis]
  frontend: [nextcloud-ui-extension]
```

**Avantage :** Se base sur les stores existants (Docker Hub, Incus, etc.) sans réinventer la roue

#### Métadonnées requises

**Minimum obligatoire :**
- Titre + Icône
- Description (200-300 caractères min)
- 3-4 screenshots minimum
- Version + Changelog
- Licence
- Dépendances

**Maximum :** Limite haute pour éviter overflow (ex: 50 images max)

**Transparence :** Plus de métadonnées = plus de confiance utilisateur

#### Gestion des versions

- Versioning standard type gestionnaire de paquets Linux
- Interface admin : mise à jour individuelle ou globale
- "apt update && apt upgrade" like
- Notifications de mises à jour disponibles

#### Soumission & Publication

**Repo officiel :**
- Pull Request GitHub
- Review par équipe ou contributeur de confiance
- Apps payantes = contrôle légal obligatoire (licences, TOS)

**Repos externes :**
- Hébergement libre par la communauté
- Auto-référencement anonymisé (URL + IDs uniquement)
- Système de notation communautaire

#### Modèle économique du Store

**Commission UniDash :**
- Cible : 15-20% (à affiner)
- Aligné sur Epic Games Store / grilles basses GAFAM
- Objectif : attractivité > marge unitaire

**Modèles de pricing (choix du dev) :**
- One-time purchase
- Subscription
- Freemium
- Gratuit

**Paiement :** Stripe (standard, fiable)

**Règle :** Apps payantes UNIQUEMENT sur repo officiel (contrôle légal)

#### Découvrabilité

**Recherche multi-critères :**
- Par nom
- Par catégorie
- Par date
- Par popularité/notes

**Recommandations personnalisées :**
- Basées sur historique d'installation admin
- Apps similaires
- "Les admins comme vous ont aussi installé..."

**UX cible :** Play Store-like (confortable, attrayant, simple)

#### Question ouverte à investiguer

- Comment gérer les apps payantes sur repos privés ? (inspiration Play Store à étudier)

---

### Domaine 4 : Monétisation

#### Philosophie de pricing

| Principe | Application |
|----------|-------------|
| **Core gratuit & open source** | Fidélité à l'origine homelab/apprentissage |
| **Pricing par cœurs CPU** | Proxy du niveau de besoin, pas punition |
| **Transparence totale** | Simulateur de prix accessible à tous |
| **Accessibilité PME** | Offre micro-entreprise très légère |

#### Sources de revenus

```
┌─────────────────────────────────────────────────────────┐
│                   REVENUS UNIDASH                        │
├─────────────────────────────────────────────────────────┤
│  📦 STORE                                                │
│  └─ Commission 15-20% sur apps payantes                 │
├─────────────────────────────────────────────────────────┤
│  💼 ABONNEMENTS (par cœurs CPU)                          │
│  ├─ Micro-entreprise (très petit prix)                  │
│  ├─ PME                                                  │
│  ├─ Enterprise                                           │
│  └─ Éducation (tarif spécial + cours intégrés)          │
├─────────────────────────────────────────────────────────┤
│  🛠️ SERVICES                                             │
│  ├─ Prestations sur-mesure (hors abonnement)            │
│  ├─ Implémentations spécifiques                         │
│  └─ SAV premium                                          │
├─────────────────────────────────────────────────────────┤
│  🎓 CERTIFICATIONS                                       │
│  ├─ X certifications gratuites (5-10-20 à définir)      │
│  ├─ Crédits certifications supplémentaires              │
│  └─ Bundles certifications thématiques (monitoring...)  │
├─────────────────────────────────────────────────────────┤
│  📚 E-LEARNING (optionnel entreprises)                   │
│  └─ Accès aux cours éducation pour formation interne    │
└─────────────────────────────────────────────────────────┘
```

#### Modèle d'abonnement par cœurs

**Logique :**
- Plus de cœurs = machine plus puissante = besoins plus complexes
- Le pricing reflète le niveau de support/features attendu
- Pas une punition pour avoir du bon matériel

**Gestion des dépassements :**
- Seuil de demandes d'implémentation par tranche
- Si dépassement → 2 options :
  1. Monter de tranche (plus de marge incluse)
  2. Payer à la prestation (comme ESN classique)

#### Tiers d'abonnement

| Tier | Cible | Caractéristiques |
|------|-------|------------------|
| **Open Source** | Homelabs | Gratuit, communauté, pas de SAV |
| **Micro** | TPE (2-3 PC) | Très petit prix, SAV basique |
| **PME** | PME standard | Prix modéré, SAV inclus, features enterprise |
| **Enterprise** | Grandes structures | Prix premium, SLA, implémentations incluses |
| **Éducation** | Écoles/Universités | Tarif spécial, cours intégrés, pas de store apps |

#### Offre Éducation - Stratégie "Biberonnage"

**Inspiration :** Microsoft Office pour étudiants

**Concept :**
- Remplacer le store par des cours
- Chaque service officiel = un cours associé
- Former les futurs admins sur UniDash
- Ils l'utiliseront en entreprise plus tard

**Cours par app :**
- Demandé aux contributeurs (PR) OU rédigé par l'équipe
- Explique : installation, configuration, troubleshooting
- Prépare à la certification

#### Certifications

**Gratuites (limite à définir : 5/10/20) :**
- Certification par service unique
- Ex: "Certifié Nextcloud", "Certifié Grafana"

**Payantes :**
- Bundles thématiques (ex: "Pack Monitoring" = Prometheus + Grafana + Alertmanager)
- Crédits supplémentaires après limite gratuite atteinte

**Usage entreprise :**
- Formation alternants
- Montée en compétences équipes
- Validation compétences recrutement

#### Simulateur de prix (innovation clé)

**Outil interne + client :**
- Inputs : nb cœurs, nb users, features souhaitées, niveau support
- Calcul transparent du prix
- Visible par UniDash ET par le client
- Objectif : prix honnêtes, pas de négociation opaque

**À développer :**
- Interface web simple
- Formule de calcul à définir (coûts + marge)
- Export devis PDF

#### Version gratuite vs payante

| Feature | Open Source | Micro | PME+ |
|---------|-------------|-------|------|
| Core UniDash | ✅ | ✅ | ✅ |
| Desktop web | ✅ | ✅ | ✅ |
| Store communautaire | ✅ | ✅ | ✅ |
| Store officiel | ✅ | ✅ | ✅ |
| Active Directory | ❌ | ❌ | ✅ |
| SAV | ❌ (forum) | Basique | Complet |
| Implémentations custom | ❌ | Payant | Inclus (quota) |
| Certifications | X gratuites | X gratuites | Bundles inclus |

---

### Domaine 5 : Offres (Enterprise/Edu/Homelab)

#### Vue comparative des offres

| Aspect | Homelab (OS) | Éducation | Enterprise |
|--------|--------------|-----------|------------|
| **Interface** | Identique | Identique | Identique |
| **Store admin** | Complet | Complet | Complet |
| **Store users** | Complet | Cours uniquement | Complet + Cours (option) |
| **Sandbox isolé** | ❌ | ✅ (par étudiant) | ✅ (pour tests/formation) |
| **Features enterprise** | Payantes | Incluses | Incluses |
| **Limite serveurs** | 3 max | Selon contrat | Illimité |
| **Limite users** | 15 max | Selon contrat | Illimité |
| **SAV** | Forum communauté | Support école | Support complet + SLA |
| **Prix** | Gratuit | Préférentiel | Standard/Premium |

#### Homelab Open Source

**Philosophie :** Gratuit et complet, mais limité en scale

**Limitations :**
- **3 serveurs max** (minimum pour HA/quorum)
- **15 utilisateurs max** (généreux pour usage perso)
- **Pas de SAV** (forum communauté uniquement)
- **Features enterprise payantes** (AD, etc. disponibles en achat séparé)

**Protection contre abus entreprises :**
- Conditions d'utilisation (recours légal si besoin)
- Limites techniques (serveurs/users)
- Pas de chasse aux sorcières, mais action si flagrant

**Zone grise TPE :**
- Petite entreprise 2-3 PC qui n'a pas plus de besoins
- Offre "Micro" très légère pour les inciter à payer un minimum
- À affiner selon retours marché

#### Offre Éducation

**Vérification statut :** GitHub Education (fiable, établi, pas à réinventer)

**Architecture :**
```
┌─────────────────────────────────────────────────────────┐
│                 UNIDASH ÉDUCATION                        │
├─────────────────────────────────────────────────────────┤
│  👨‍🏫 ADMIN ÉCOLE                                         │
│  └─ Accès complet : Store + Infra + Gestion étudiants   │
├─────────────────────────────────────────────────────────┤
│  👨‍🎓 ÉTUDIANTS (users de l'admin)                        │
│  ├─ Desktop : Identique                                 │
│  ├─ Store : Remplacé par zone COURS                     │
│  └─ Sandbox isolé personnel pour pratique               │
└─────────────────────────────────────────────────────────┘
```

**Sandbox étudiant :**
- Environnement admin restreint
- Permet de pratiquer les cours
- Pas d'accès au vrai store (apprentissage, pas clic-bouton)
- Ressources limitées (beaucoup d'étudiants = optimisation)

**Stratégie "Biberonnage" :**
- Étudiants formés sur UniDash
- Futurs employés qui demanderont UniDash en entreprise
- ROI long terme

#### Offre Enterprise

**Quasi-identique à Éducation sauf :**

| Différence | Éducation | Enterprise |
|------------|-----------|------------|
| **Tarif** | Préférentiel | Standard |
| **Nb Sandbox** | Beaucoup (tous les étudiants) | Peu (admins en formation) |
| **Focus** | Apprentissage | Production + Formation optionnelle |
| **Cours** | Obligatoire (remplace store) | Optionnel (en plus du store) |

**Features enterprise (incluses) :**
- Active Directory / LDAP
- Autres features "typées entreprise" (à lister)
- Ces features = apps store payantes pour Homelab

**Sandbox enterprise :**
- Environnement de test pré-production
- Formation interne (e-learning)
- Même techno que sandbox éducation

#### Features Enterprise - À définir

Liste des features réservées aux abonnements payants :
- ✅ Active Directory / LDAP
- ❓ Multi-tenant (plusieurs orgas sur même infra)
- ❓ Audit logs avancés
- ❓ Compliance (RGPD, SOC2...)
- ❓ SSO entreprise
- ❓ Backup enterprise (rétention longue, chiffrement)
- ❓ API avancée
- ❓ Intégrations tierces (Slack, Teams, SIEM...)

→ À affiner lors du PRD

---

### Domaine 6 : Priorités MVP

#### Stratégie de lancement

```
┌─────────────────────────────────────────────────────────┐
│  PHASE 1 : MVP OPEN SOURCE                              │
│  Objectif : Valider le concept, construire communauté   │
│  Cible : Homelabs + quelques PME beta-testeurs          │
├─────────────────────────────────────────────────────────┤
│  PHASE 2 : TRANSITION                                   │
│  - Téléchargements suffisants                           │
│  - Retours beta-testeurs entreprises                    │
│  - Recherche investisseurs (Stripe, infra, etc.)        │
├─────────────────────────────────────────────────────────┤
│  PHASE 3 : SPLIT DES OFFRES                             │
│  - Open Source → Homelab (features retirées)            │
│  - Nouvelle version Enterprise (features payantes)      │
│  - Monétisation active (store, abonnements)             │
└─────────────────────────────────────────────────────────┘
```

#### Roadmap par version

| Feature | V1 (MVP) | V2 | V3+ |
|---------|:--------:|:--:|:---:|
| **Desktop web basique** | ✅ | | |
| **K3S (HA + conteneurs)** | ✅ | | |
| **VPN intégré (L2TP/IPsec)** | ✅ | | |
| **Multi-serveurs** | ✅ | | |
| **Active Directory** | ✅ | | |
| **Store apps officielles** | ✅ | | |
| **Store repos externes** | ⚡ si temps | ✅ | |
| **Docker natif** | | ✅ | |
| **Proxmox / KVM** | | ✅ | |
| **LXC** | | ✅ | |
| **Apps Wayland/Guacamole** | | | ✅ |
| **Sandbox isolés** | | | ✅ |
| **Certifications/Cours** | | | ✅ |
| **Système paiement (Stripe)** | | | ✅ |

#### MVP V1 - Scope détaillé

**MUST HAVE (bloquant) :**
- Desktop web fonctionnel (splits, dock, iframes)
- Authentification utilisateurs
- K3S intégré (orchestration HA)
- VPN L2TP/IPsec (sécurité admin + multi-site)
- Multi-serveurs (minimum 3 pour HA)
- Active Directory (projection entreprises beta)
- Store officiel (apps gratuites, preuve de concept pour investisseurs)

**NICE TO HAVE V1 :**
- Repos externes (si temps disponible)
- Thèmes/personnalisation basique

**EXPLICITEMENT HORS SCOPE V1 :**
- Docker standalone (V2)
- Proxmox/KVM/LXC (V2)
- Apps desktop Wayland/Guacamole (V3)
- Sandbox isolés (V3)
- Certifications & Cours (V3)
- Paiements & Monétisation (V3)

#### Justifications clés

| Choix | Pourquoi |
|-------|----------|
| **K3S avant Docker** | HA est le différenciateur, Docker seul = Portainer existe déjà |
| **VPN (L2TP/IPsec) en V1** | Sécurité non-négociable pour multi-site et admin, éprouvé en production enterprise |
| **AD en V1** | Permet aux entreprises beta de se projeter |
| **Store officiel V1** | Preuve aux investisseurs du potentiel de revenus |
| **Wayland/Guacamole V3** | Complexe, pas essentiel pour valider le concept |

#### Utilisateur cible MVP

**Persona principal :**
- Admin système homelab avancé
- Veut simplifier sa gestion multi-services
- Prêt à tester une solution nouvelle
- Actif sur forums/Discord pour feedback

**Persona secondaire (beta) :**
- Admin IT de petite PME (5-20 employés)
- Cherche à moderniser son infra
- Budget limité, intéressé par l'open source
- Prêt à essuyer les plâtres contre gratuité

#### Critères de succès MVP

**Validation technique :**
- [ ] Desktop web stable et utilisable
- [ ] Installation en < 30 min (one-liner)
- [ ] HA fonctionnelle sur 3 serveurs
- [ ] VPN opérationnel
- [ ] 10+ apps dans le store officiel

**Validation marché :**
- [ ] X téléchargements (à définir)
- [ ] X étoiles GitHub (à définir)
- [ ] 3-5 PME beta-testeurs actifs
- [ ] Feedback positif communauté
- [ ] Intérêt investisseurs

---

### Domaine 7 : Risques Techniques

#### Matrice des risques (par ordre de priorité)

| Risque | Niveau | Impact | Mitigation |
|--------|--------|--------|------------|
| **Complexité K3S** | 🔴 Élevé | Bloquant MVP | Formation, POC isolé avant intégration |
| **Multi-site (VPN)** | 🔴 Élevé | HA compromise | Tester L2TP/IPsec comme alternative à WireGuard |
| **Dépendances externes** | 🟠 Moyen | Projet bloqué | Plan fallback, royalties si nécessaire |
| **SAV 24/7 en phase 3** | 🟠 Moyen | Impossible seul | Recrutement obligatoire, ratio clients/employés |
| **Sécurité APIs** | 🟢 Faible | Faille sécurité | VPN + auth systématique |
| **Perf desktop (iframes)** | 🟢 Faible | UX dégradée | Astro/WebAssembly pour compenser |

#### Risques d'architecture

**1. Complexité K3S (🔴 CRITIQUE)**
- Technologie non maîtrisée actuellement
- **Mitigation :** POC isolé, formation approfondie avant intégration MVP
- **Fallback :** Docker Swarm si K3S trop complexe (moins de features mais plus simple)

**2. Multi-site / VPN (🔴 CRITIQUE)**
- Expériences passées : clés SSH corrompues via WireGuard
- **Investigation :** Déterminer si c'était WireGuard ou mauvaise manip
- **Alternative à évaluer :** L2TP/IPsec (ancienne, éprouvée, stable)
- **Mitigation :** Tests intensifs avant production

**3. Sécurité APIs (🟢 MAÎTRISÉ)**
- APIs admin derrière VPN
- Authentification sur chaque appel
- La plupart des entreprises utiliseront VPN pour tous les users
- **Confiance :** Si sécurité bien faite = OK

**4. Performance desktop web (🟢 ACCEPTABLE)**
- Limitation technique inhérente au projet (iframes)
- **Mitigation :** Framework Astro → compilation WebAssembly
- Desktop léger compense la lourdeur des iframes
- **Acceptation :** On ne peut pas tout optimiser, c'est un trade-off

#### Risques dépendances externes

**Projets critiques :**
- K3S, Docker, Proxmox, Guacamole, WireGuard, etc.

**Scénarios à risque :**
- Projet abandonné
- Changement de licence
- Blocage d'accès (ex: Docker Hub)
- Changement breaking de l'API

**Plan de mitigation :**
| Dépendance | Fallback potentiel |
|------------|-------------------|
| K3S | Docker Swarm, K0s |
| Docker | Podman |
| Proxmox API | API KVM directe |
| WireGuard | L2TP/IPsec, OpenVPN |
| Guacamole | Autre solution RDP/VNC web |
| Docker Hub | Harbor (self-hosted), GitHub Container Registry |

**Actions préventives :**
- Vérifier TOS de chaque dépendance
- Prévoir royalties/licences si nécessaire
- Documenter les fallbacks dans l'architecture
- Ne pas dépendre d'une seule source (multi-registry pour images)

#### Risques de marché

**Concurrents identifiés :**
- Portainer, Cockpit, Cosmos, Proxmox VE

**Différenciation UniDash :**
- PAS un concurrent direct → c'est une SURCOUCHE
- Desktop unifié sysadmin + employés (pas juste admin)
- Environnement de travail complet, pas juste gestion infra
- **Conclusion :** Différenciation suffisante, pas le même marché

**Stratégie d'adoption :**
- NE PAS cibler entreprises avec infra existante (résistance au changement)
- CIBLER TPE/PME naissantes qui s'informatisent
- Grandir AVEC les clients (évolution progressive)
- Éviter la "marche d'escalier" technique trop brutale

#### Risques d'exécution

**Équipe actuelle :**
- Gabriel : Seul sur la technique (dev + sysadmin)
- Associé : Partie commerciale et administrative

**Contraintes :**
- Travail salarié en parallèle (temps limité : soirs + week-ends)
- Motivation forte (préfère bosser sur projets que jouer)

**Compétences à acquérir/renforcer :**
- K3S / Kubernetes
- Multi-site networking avancé
- Sécurité enterprise-grade

#### Risques légaux/business

**Licences open source :**
- Pas de modification du code des dépendances = pas de problème de licence
- **À vérifier :** TOS de chaque outil pour usage commercial/redistribution

**RGPD :**

| Composant | Données perso | Solution |
|-----------|---------------|----------|
| Store (soumission apps) | Évité via PR GitHub | GitHub gère la RGPD |
| Comptes utilisateurs store | À éviter si possible | Pas de compte = pas de RGPD |
| Infra cliente (users internes) | Oui, inévitable | Documentation légale, DPA |

**Responsabilité apps store :**
- Phase Open Source : Support communautaire, pas d'obligation commerciale
- Phase 3 (vente) :
  - Contrats avec limites de responsabilité
  - CGV/CGU solides
  - Assurance professionnelle
  - Distinction apps certifiées vs communauté

#### Risque critique ajouté : SAV 24/7

**Constat :**
> "Il sera IMPOSSIBLE de mettre le projet en vente sans une équipe d'employés"

**Raison :**
- Projet B2B enterprise = SAV 24/7 attendu
- Une personne seule ne peut pas assurer ça

**Implications :**
- Recrutement OBLIGATOIRE avant phase 3
- Ratio clients/employés SAV à calculer
- Basé sur : téléchargements OS + tests beta entreprises

**Formule à définir :**
```
Nb employés SAV = f(nb clients payants, SLA contractuel, complexité tickets)
```

**Garde-fou :**
- Limiter le nombre de clients acceptés en phase 3
- Croissance maîtrisée = qualité SAV maintenue
- Ne pas vendre plus que ce qu'on peut supporter

---

### Domaine 8 : Métriques de Succès

#### Phase 1 : MVP Open Source (1 mois post-release)

| Métrique | Objectif | Commentaire |
|----------|----------|-------------|
| **Téléchargements** | 1 000 | Seuil de validation intérêt |
| **Étoiles GitHub** | 100 | Visibilité communauté |
| **Contributeurs actifs** | 5 | Communauté engagée |
| **Beta-testeurs PME** | 3-5 (sous 6 mois) | Validation B2B |

#### Phase 2 : Transition (même délais)

| Métrique | Objectif | Commentaire |
|----------|----------|-------------|
| **Téléchargements** | 5 000 | x5 croissance |
| **Entreprises intéressées** | 15-20 | Pipeline commercial |
| **Feedback qualité** | ≥ 4 étoiles | Validation qualité |
| **Investissement concret** | Suffisant pour embauche | Permet phase 3 |

**Priorité investissement :**
- Salaires employés SAV en premier
- Fondateurs acceptent rémunération réduite au début
- Objectif : avoir les moyens de déployer phase 3

#### Phase 3 : Commercialisation (6 mois - 1 an)

**Métriques financières :**

| Métrique | Objectif | Commentaire |
|----------|----------|-------------|
| **Amortissement investisseurs** | Stable | Plus de stress financier |
| **Rémunération équipe** | Convenable | Employés + fondateurs |
| **Capacité réinvestissement** | Oui | Croissance continue |

**Métriques clients :**

| Métrique | Objectif | Commentaire |
|----------|----------|-------------|
| **Clients payants** | 30-50 (6 mois - 1 an) | Réaliste, pas sur-optimiste |
| **Churn rate** | < 10% (cible 5%) | Rétention importante |
| **NPS / Satisfaction** | 4,5 / 5 étoiles | Standard bons produits |

#### Métriques techniques (qualité produit)

| Métrique | Objectif | Justification |
|----------|----------|---------------|
| **Uptime** | 95% | Maintenance = redémarrages, pas de SLA irréaliste |
| **Temps réponse SAV** | < 4-8h moyenne | Majorité < 2h, quelques gros tickets longs |
| **Bugs critiques / release** | < 3-5 (cible 0) | Qualité code, tests |
| **Temps installation / machine** | < 15-20 min | Équivalent distro Linux auto |

#### Tableau de bord récapitulatif

```
┌─────────────────────────────────────────────────────────────────┐
│                    MÉTRIQUES UNIDASH                             │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 1 (MVP)           │  PHASE 2 (Transition)                │
│  ─────────────────────   │  ─────────────────────               │
│  📥 1 000 téléchargements │  📥 5 000 téléchargements            │
│  ⭐ 100 étoiles GitHub    │  🏢 15-20 entreprises intéressées    │
│  👥 5 contributeurs       │  ⭐ Feedback ≥ 4 étoiles             │
│  🏢 3-5 PME beta (6 mois) │  💰 Investissement = embauche        │
├─────────────────────────────────────────────────────────────────┤
│  PHASE 3 (Commercial - 6 mois à 1 an)                           │
│  ─────────────────────────────────────                          │
│  💰 Amortissement stable    │  📊 Churn < 10%                    │
│  👥 30-50 clients payants   │  ⭐ NPS 4,5/5                       │
│  💵 Équipe bien rémunérée   │  🔄 Capacité réinvestissement      │
├─────────────────────────────────────────────────────────────────┤
│  TECHNIQUE (toutes phases)                                       │
│  ─────────────────────────                                       │
│  ⏱️ Uptime 95%              │  🐛 < 5 bugs critiques / release   │
│  📞 SAV < 4-8h moyenne      │  🚀 Install < 20 min / machine     │
└─────────────────────────────────────────────────────────────────┘
```

---

## Synthèse Phase 1 : First Principles Thinking

### Vue d'ensemble

L'exploration exhaustive des 8 domaines a permis de définir une vision claire et structurée de UniDash :

**Architecture :** Docker comme point d'entrée unique, K3S pour la HA, séparation backend/frontend avec système d'extensions modulaire. UniDash est une surcouche qui chapeaute les outils existants (Proxmox, Cockpit, Portainer) sans les remplacer.

**Bureau Web :** Système de splits Android-like (pas de fenêtres flottantes), docks thématiques interchangeables, iframes pour les apps web, Wayland/Guacamole pour les apps desktop (V3). Personnalisation limitée volontairement pour maintenir l'ordre.

**Marketplace :** Modèle Linux avec repo officiel (PR GitHub) + repos externes auto-enregistrés et notés par la communauté. Format ZIP déclaratif YAML/JSON, commission 15-20% sur apps payantes.

**Monétisation :** Core gratuit et open source, pricing par cœurs CPU, simulateur de prix transparent. Revenus via store, abonnements, services, certifications, et e-learning optionnel.

**Offres :** Homelab (3 serveurs/15 users gratuit), Éducation (stratégie "biberonnage" avec cours), Enterprise (features premium + SAV). Vérification via GitHub Education.

**MVP :** V1 = Desktop + K3S + VPN + AD + Store officiel. V2 = Docker/Proxmox/KVM/LXC. V3 = Wayland/Guacamole + Certifications + Paiements.

**Risques :** Complexité K3S (🔴), Multi-site VPN (🔴), Dépendances externes (🟠), SAV 24/7 (🟠). Plan de mitigation et fallbacks documentés.

**Métriques :** Phase 1 = 1000 téléchargements, Phase 2 = 5000 + investisseurs, Phase 3 = 30-50 clients payants avec churn <10%.

### Questions ouvertes à investiguer

- Apps payantes sur repos privés (inspiration Play Store)
- Liste complète des features enterprise
- Formule exacte ratio clients/employés SAV
- Protocoles notifications (téléphone pro, mail, SMS)
- Validation technique fullscreen multi-écrans

### Prêt pour Phase 2

L'exploration First Principles a créé une base solide. La Phase 2 (Morphological Analysis) permettra d'identifier les patterns et connexions entre domaines.

---

## Phase 2 : Morphological Analysis

### Matrice des variables critiques

| Variable | Option A | Option B | Option C | **Choix** |
|----------|----------|----------|----------|-----------|
| **Point d'entrée** | Docker seul | Docker + Ansible | Packages natifs | **Docker + Ansible** |
| **Orchestration** | K3S | Docker Swarm | Kubernetes full | **K3S** (non-négociable) |
| **Desktop** | iFrames only | iFrames + Wayland | Wayland only | **iFrames → Wayland (V3)** |
| **Store model** | Centralisé | Hybride (officiel+externe) | Décentralisé | **Hybride** |
| **Pricing** | Per-seat | Per-core CPU | Flat tiers | **Per-core CPU** |
| **Target market** | Homelab first | PME first | Enterprise first | **Homelab first** |

### Analyse des connexions inter-domaines

#### Connexion 1 : K3S = Investissement stratégique (🟢 Résolu)

**Décision :** K3S est non-négociable, malgré le risque technique élevé.

**Justifications :**
- Standard entreprise actuel → crédibilité B2B
- Compétence à acquérir de toute façon (projet + carrière)
- Docker Swarm = dévalorisation du projet
- Différenciateur clé vs Portainer/Cosmos

**Mitigation du risque :** Formation + POC isolé avant intégration MVP

#### Connexion 2 : Store = Écosystème organique (🟢 Clarifié)

**Insight clé :** Le volume du store est fonction de la popularité, pas de l'effort interne.

**Modèle SAV découvert :**
```
┌─────────────────────────────────────────────────────────┐
│  APPS UNIDASH (5-10)        │  APPS TIERS (potentiel: │
│  → SAV UniDash              │  des centaines)          │
│  → Coût employés            │  → SAV par le tiers      │
│  → Contrôle qualité total   │  → Commission 15-20%     │
│                             │  → Pas de coût SAV       │
└─────────────────────────────────────────────────────────┘
```

**Implication :** Le SAV scale avec les apps internes, pas le store total. Énorme soulagement opérationnel !

**Stratégie :** Popularité du projet = attractivité pour développeurs tiers = revenus passifs (commission sans SAV)

#### Connexion 3 : Transition Homelab → Enterprise (🟢 Simple)

**Architecture de transition :**
```
V1 (Homelab OS)           V3 (Enterprise)
─────────────────         ─────────────────
Feature A [incluse]  →    Feature A [paywall]
Feature B [incluse]  →    Feature B [paywall]
Feature C [incluse]  →    Feature C [paywall]
```

**Mécanisme :** Extensions = même code, source différente (gratuit → store payant)

**Risque identifié :** Apps V1 restent accessibles jusqu'à incompatibilité → forks possibles par la communauté

**Acceptation :** Risque acceptable, inhérent à l'open source

#### Connexion 4 : Priorité = Projet qui vit > Commercialisation (🔴 CRITIQUE)

**Philosophie fondatrice révélée :**

> "Si la commercialisation devait empêcher le projet de vivre, je préférerais qu'il reste libre et open source plutôt que de le vendre."

**Hiérarchie des priorités :**
1. **Technique** : Projet techniquement excellent → montée en compétences
2. **Personnel** : Répondre à un besoin non satisfait sur le marché
3. **Communauté** : Partager quelque chose qui marche
4. **Business** : Rentabilité (objectif secondaire)

**Implication stratégique :** UniDash = projet passion-first, business-second

### Pattern central identifié

**"Popularité d'abord, monétisation ensuite"**

```
┌─────────────────────────────────────────────────────────┐
│                    FLYWHEEL UNIDASH                      │
│                                                          │
│    Projet excellent    →    Adoption massive             │
│          ↑                        ↓                      │
│    Communauté active   ←    Devs tiers intéressés       │
│          ↑                        ↓                      │
│    Crédibilité B2B     ←    Store riche (apps tiers)    │
│          ↓                        ↓                      │
│    Clients payants     ←    Commission passive           │
└─────────────────────────────────────────────────────────┘
```

**Insight :** La monétisation est un effet secondaire de l'excellence technique, pas l'objectif premier.

### Tensions résolues

| Tension initiale | Résolution |
|------------------|------------|
| K3S complexe vs MVP simple | K3S = investissement obligatoire |
| Volume store vs revenus | Popularité → devs tiers → revenus passifs |
| Homelab → Enterprise | Extensions = même code, paywall différent |
| Business vs Passion | Passion first, business suivra |

### Questions émergentes

1. **Comment maximiser la popularité initiale ?** (marketing open source, communautés cibles)
2. **Quelles apps internes développer vs laisser aux tiers ?** (core = interne, reste = écosystème)
3. **Comment attirer les premiers développeurs tiers ?** (documentation, SDK, incentives)

---

## Phase 3 : Six Thinking Hats

### ⚪ Chapeau Blanc (Faits)

**Données disponibles :**
- ✅ Infrastructure serveur existante (4-5 machines + onduleurs + double connexion)
- ✅ K3S léger, pas d'inquiétude performance
- ✅ Retours positifs cercle fermé (amis sur Nidash)
- 🔄 Étude de marché (recherche en cours)

**Données manquantes :**
- Retours utilisateurs hors cercle fermé → post-MVP via communauté
- Validation technique multi-écrans fullscreen → POC à faire

### 🔴 Chapeau Rouge (Émotions/Intuitions)

**Ce qui excite :**
> "UniDash, c'est le projet de ma vie. La possibilité de créer une entreprise d'avenir, peut-être une multinationale, des revenus pour d'autres projets, et apprendre énormément."

**Ce qui inquiète :**
> "Le projet est très conséquent, je suis seul. J'ai peur de me décourager, de ne jamais respecter la deadline. Peur aussi que le marché soit pris si je mets trop longtemps."

**Ressenti timeline :**
> "Réaliste SI je m'y tiens de A à Z. C'est ça qui risque d'être compliqué."

**Analyse émotionnelle :**

```
┌─────────────────────────────────────────────────────────┐
│           PROFIL ÉMOTIONNEL DU PROJET                    │
├─────────────────────────────────────────────────────────┤
│  MOTIVATION        ████████████████████ 100%            │
│  (projet de vie, vision long terme)                     │
├─────────────────────────────────────────────────────────┤
│  CONFIANCE TECH    ████████████████░░░░  80%            │
│  (compétences + infra OK, K3S à apprendre)              │
├─────────────────────────────────────────────────────────┤
│  RISQUE BURNOUT    ████████████░░░░░░░░  60%            │
│  (projet solo, ampleur massive)                         │
├─────────────────────────────────────────────────────────┤
│  PRESSION MARCHÉ   ████████░░░░░░░░░░░░  40%            │
│  (fenêtre d'opportunité perçue)                         │
└─────────────────────────────────────────────────────────┘
```

**Insight critique :** Le projet réussira ou échouera sur la **discipline**, pas sur la technique. L'IA (Claude) comme co-pilote permanent = facteur de mitigation majeur du risque burnout.

**Stratégie anti-découragement identifiée :**
- Découper en micro-victoires (MVPs successifs)
- Célébrer chaque milestone
- Communauté = motivation externe
- Claude = pair programming permanent

### ⚫ Chapeau Noir (Risques/Critiques)

**Risques marché (étude complète : [market-research-2026-01-07.md](market-research-2026-01-07.md)) :**

| Risque | Probabilité | Impact | Mitigation |
|--------|-------------|--------|------------|
| Portainer ajoute bureau web | Faible | Élevé | First-mover advantage |
| Cloud devient trop pas cher | Faible | Élevé | Focus souveraineté/privacy |
| K8s remplacé par autre tech | Faible | Moyen | Architecture modulaire |
| Consolidation marché (rachats) | Moyen | Moyen | Rester agile, niche |

**Risques exécution :**

| Risque | Niveau | Mitigation |
|--------|--------|------------|
| Burnout solo | 🔴 Élevé | Claude co-pilote, micro-MVPs, communauté |
| K3S trop complexe | 🔴 Élevé | POC isolé, formation préalable |
| VPN multi-site instable | 🟠 Moyen | Tester L2TP/IPsec comme fallback |
| Fenêtre marché fermée | 🟢 Faible | Marché en croissance 30%/an |

### 🟡 Chapeau Jaune (Bénéfices/Opportunités)

**Différenciateurs UNIQUES confirmés par l'étude de marché :**

| Différenciateur | Concurrents | Impact |
|-----------------|-------------|--------|
| **Bureau web unifié** | AUCUN | 🔥 Majeur |
| **Surcouche (pas remplacement)** | AUCUN | 🔥 Majeur |
| **K3S + Docker + VM unifié** | Rancher (partiel) | Fort |
| **Programme Éducation** | Microsoft/VMware (cloud only) | Fort |
| **Pricing par cœurs CPU** | VMware (différent) | Moyen |

**Marché adressable :**
- **TAM :** $15B (2028)
- **SAM :** $2B (PME + Éducation Europe/NA)
- **SOM 3 ans :** $2M ARR (0.1% SAM)

**Tendances favorables :**
- r/selfhosted : +40%/an (100K → 400K+ membres)
- r/homelab : +25%/an (500K → 1.2M+ membres)
- K3s : +60%/an (1M+ installations)
- Self-hosted PaaS : +35%/an ($5B → $15B)

**Positionnement validé :**
```
Simplicité CasaOS + Puissance Proxmox + Bureau web UNIQUE
```

### 🟢 Chapeau Vert (Créativité/Alternatives)

**Idées émergentes pour accélérer l'adoption :**

1. **"UniDash in a Box"** - Partenariat hardware (comme Umbrel Home)
   - Appliance pré-configurée
   - Revenus hardware + software

2. **Programme "Ambassadeurs Homelab"**
   - Homelabbers influents = futurs décideurs PME
   - Accès beta anticipé, swag, reconnaissance

3. **"UniDash Certified Admin"**
   - Certification gratuite (X premières)
   - Valeur sur le marché de l'emploi (+20-30% salaire comme CKA)

4. **Intégration GitHub Education**
   - Déjà prévu, mais exploiter le réseau existant
   - 10M+ étudiants potentiels

### 🔵 Chapeau Bleu (Processus/Prochaines étapes)

**Go-To-Market validé :**

| Phase | Durée | Focus | Objectif |
|-------|-------|-------|----------|
| **Phase 1** | 0-12 mois | Community building | 1000 installs, 100 GitHub stars |
| **Phase 2** | 12-18 mois | Early adopters PME | Beta-testeurs, case studies |
| **Phase 3** | 18-36 mois | Scale | Équipe commerciale, partenariats |

**Prochaines étapes immédiates :**
1. Finaliser cette session brainstorming
2. Créer Product Brief structuré
3. PRD détaillé
4. Commencer développement MVP

---

## Phase 4 : Decision Tree Mapping

### Arbre de décision principal

```
                        ┌─────────────────────────────┐
                        │     DÉMARRER UNIDASH        │
                        └─────────────┬───────────────┘
                                      │
                    ┌─────────────────┴─────────────────┐
                    ▼                                   ▼
        ┌───────────────────┐               ┌───────────────────┐
        │  PHASE PRÉPARATION │               │  FORMATION K3S    │
        │  (parallélisable)  │               │  (bloquant)       │
        └─────────┬─────────┘               └─────────┬─────────┘
                  │                                   │
    ┌─────────────┼─────────────┐                     │
    ▼             ▼             ▼                     ▼
┌───────┐   ┌───────────┐   ┌───────┐         ┌─────────────┐
│Product│   │Architecture│   │ UX    │         │ POC K3S     │
│Brief  │   │Doc        │   │Design │         │ isolé       │
└───┬───┘   └─────┬─────┘   └───┬───┘         └──────┬──────┘
    │             │             │                    │
    └─────────────┴─────────────┴────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   MVP V1 READY?     │
                    │   (Gate décision)   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        ┌──────────┐    ┌──────────────┐   ┌──────────┐
        │ Desktop  │    │ K3S + VPN    │   │ Store    │
        │ Web Core │    │ Integration  │   │ Officiel │
        └────┬─────┘    └──────┬───────┘   └────┬─────┘
             │                 │                │
             └─────────────────┴────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   RELEASE V1 MVP    │
                    │   (Open Source)     │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │   VALIDATION        │
                    │   1000 downloads?   │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │ OUI           │                │ NON
              ▼               │                ▼
        ┌──────────┐          │          ┌──────────┐
        │ Phase 2  │          │          │ Itérer   │
        │ (V2)     │          │          │ feedback │
        └──────────┘          │          └──────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │   SUITE: V2 → V3    │
                    └─────────────────────┘
```

### Points de décision critiques

#### Décision 1 : Ordre de développement MVP

| Composant | Priorité | Dépendances | Durée estimée |
|-----------|----------|-------------|---------------|
| **Desktop Web Core** | 🔴 P0 | Aucune | Premier |
| **K3S Integration** | 🔴 P0 | POC K3S validé | Après Desktop |
| **VPN (WireGuard)** | 🔴 P0 | K3S fonctionnel | Après K3S |
| **Active Directory** | 🟠 P1 | Desktop + K3S | Parallèle VPN |
| **Store Officiel** | 🟠 P1 | Desktop fonctionnel | Parallèle AD |

**Chemin critique :** Desktop → K3S → VPN → Release

#### Décision 2 : Stack technique

| Choix | Décision | Justification |
|-------|----------|---------------|
| **Frontend** | Astro + WebAssembly | Performance desktop web |
| **Backend** | Go ou Rust | Performance + K3S natif |
| **Base de données** | PostgreSQL | Standard enterprise |
| **Reverse Proxy** | HAProxy ou Traefik | HA native |
| **VPN** | WireGuard (fallback L2TP) | Performance + simplicité |

#### Décision 3 : Critères de "Go/No-Go" par phase

**V1 MVP → Release :**
- [ ] Desktop web fonctionnel (splits, dock, iframes)
- [ ] K3S cluster 3 nodes stable
- [ ] VPN WireGuard opérationnel
- [ ] Auth utilisateurs fonctionnelle
- [ ] 10+ apps dans le store

**V1 → V2 (transition) :**
- [ ] 1000+ téléchargements
- [ ] 100+ GitHub stars
- [ ] Feedback positif communauté
- [ ] 3-5 beta-testeurs PME

**V2 → V3 (commercialisation) :**
- [ ] 5000+ téléchargements
- [ ] 15-20 entreprises intéressées
- [ ] Investissement sécurisé (embauche SAV)
- [ ] Infrastructure paiement prête

### Plan d'action immédiat

#### Semaine 1-2 : Fondations

| Action | Priorité | Livrable |
|--------|----------|----------|
| Finaliser Product Brief | 🔴 | Document structuré |
| Setup repo GitHub | 🔴 | Repo + README + License |
| Architecture document | 🔴 | Diagrammes + décisions |
| POC K3S personnel | 🔴 | Cluster 3 nodes fonctionnel |

#### Semaine 3-4 : Prototypage

| Action | Priorité | Livrable |
|--------|----------|----------|
| Prototype Desktop Web | 🔴 | UI basique splits/dock |
| Tests K3S intégration | 🔴 | API K3S fonctionnelle |
| Design système extensions | 🟠 | Spec technique |

#### Mois 2-3 : MVP Core

| Action | Priorité | Livrable |
|--------|----------|----------|
| Desktop Web complet | 🔴 | V1 fonctionnelle |
| K3S + VPN intégrés | 🔴 | HA opérationnelle |
| Store officiel basique | 🟠 | 10 apps disponibles |
| Documentation utilisateur | 🟠 | Getting started |

### Risques avec triggers

| Risque | Trigger | Action si déclenché |
|--------|---------|---------------------|
| K3S trop complexe | POC échoue après 2 semaines | Évaluer Docker Swarm comme fallback temporaire |
| VPN instable multi-site | Tests échouent | Tester L2TP/IPsec, documenter limitations |
| Desktop perf insuffisante | >500ms latence UI | Optimiser avec WebAssembly, réduire features |
| Burnout | 2 semaines sans progrès | Pause 1 semaine, revoir scope MVP |

### Métriques de suivi

**Hebdomadaire :**
- Commits / semaine
- Features complétées vs planifiées
- Bugs ouverts / fermés

**Mensuel :**
- % avancement MVP
- Temps passé vs estimé
- Moral / motivation (1-10)

**Release :**
- Téléchargements
- GitHub stars
- Issues ouvertes
- Feedback qualitatif

---

## Synthèse finale du brainstorming

### Ce qui a été exploré

| Phase | Technique | Résultat clé |
|-------|-----------|--------------|
| **1** | First Principles | 8 domaines structurés, vision claire |
| **2** | Morphological Analysis | Flywheel identifié, tensions résolues |
| **3** | Six Thinking Hats | Risques/opportunités, étude marché |
| **4** | Decision Tree Mapping | Plan d'action concret |

### Décisions prises

1. **K3S** = non-négociable (standard entreprise + apprentissage)
2. **Homelab first** = validation avant commercialisation
3. **Passion > Business** = projet qui vit avant tout
4. **Claude co-pilote** = mitigation risque burnout
5. **Desktop web** = différenciateur UNIQUE sur le marché

### Prochaines étapes

1. **Immédiat :** Product Brief avec workflow BMM
2. **Court terme :** PRD détaillé + Architecture
3. **Moyen terme :** Développement MVP V1
4. **Long terme :** Release open source + community building

---

## Technique Selection

**Approche :** Progressive Technique Flow
**Design :** Développement systématique de l'exploration à l'action

**Techniques utilisées :**
- **Phase 1 - Exploration :** First Principles Thinking ✅
- **Phase 2 - Patterns :** Morphological Analysis ✅
- **Phase 3 - Développement :** Six Thinking Hats ✅
- **Phase 4 - Action :** Decision Tree Mapping ✅

**Session complétée avec succès.**

---
