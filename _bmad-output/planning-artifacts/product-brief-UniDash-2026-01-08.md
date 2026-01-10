---
stepsCompleted: [1, 2, 3, 4, 5]
inputDocuments:
  - "_bmad-output/analysis/brainstorming-session-2026-01-07.md"
  - "_bmad-output/analysis/market-research-2026-01-07.md"
date: 2026-01-08
author: Gabriel
project_name: UniDash
---

# Product Brief: UniDash

## Executive Summary

UniDash est une plateforme B2B de gestion d'infrastructure serveur avec bureau web intégré, conçue pour rendre la gestion de parc aussi simple que l'utilisation d'un smartphone. Née de 4 ans de frustration face à l'absence d'outil unifié sur le marché, UniDash comble un vide critique : aucune solution existante n'offre à la fois la puissance nécessaire aux administrateurs ET l'accessibilité requise pour les employés non-techniques.

**Vision en une phrase :** Si Spotify représente la simplicité pour écouter de la musique, UniDash incarne l'accessibilité quand vous avez besoin d'un serveur.

---

## Core Vision

### Problem Statement

Les entreprises (TPE/PME) et les homelabbers font face à un écosystème fragmenté d'outils de gestion serveur. Un administrateur système typique doit jongler entre 5 à 10 interfaces distinctes (Proxmox, Portainer, Cockpit, etc.) sans aucune unification. Pire encore, les employés non-techniques n'ont aucun accès simplifié aux services hébergés - ils dépendent entièrement de l'admin pour la moindre action.

Il n'existe aucune "feuille de route" claire pour aller d'un point A à un point B dans la gestion d'infrastructure auto-hébergée.

### Problem Impact

| Persona | Impact du problème |
|---------|-------------------|
| **Admin Junior** (capable de debug via forums) | Perd des heures à naviguer entre interfaces, risque d'erreurs de configuration, courbe d'apprentissage excessive |
| **Employé non-tech** ("Giselle la comptable") | Dépendance totale envers l'IT, frustration, perte de productivité, abandon vers solutions cloud |
| **TPE/PME** | Coûts cachés de complexité, migration vers cloud par défaut (perte de souveraineté), sous-utilisation des investissements infrastructure |

### Why Existing Solutions Fall Short

| Solution | Forces | Lacunes critiques |
|----------|--------|-------------------|
| **Portainer** | Docker simple | Pas de bureau web, pas d'orchestration HA |
| **CasaOS** | UX excellente | Trop basique, pas de multi-serveurs, pas enterprise |
| **Proxmox** | Puissant, complet | Complexe, pas accessible aux non-admins |
| **Cockpit** | Léger, Linux natif | Mono-serveur, pas de desktop utilisateur |
| **Rancher** | K8s complet | Courbe d'apprentissage massive, overkill PME |

**Gap critique identifié :** AUCUN concurrent n'offre de bureau web unifié pour les utilisateurs finaux. C'est un "blue ocean" complet.

### Proposed Solution

UniDash est une **surcouche unificatrice** (pas un remplacement) qui chapeaute les outils existants et expose :

1. **Pour les admins :** Interface unifiée de gestion (K3S, Docker, VMs, VPN) avec store d'applications
2. **Pour les employés :** Bureau web Android-like avec accès simplifié aux services autorisés

**Architecture clé :**
- Point d'entrée Docker unique (one-liner installation)
- K3S pour haute disponibilité native
- Système d'extensions modulaire (backend + frontend)
- Store hybride Linux-like (repo officiel + communauté)

### Key Differentiators

| Différenciateur | Unicité | Impact marché |
|-----------------|---------|---------------|
| **Bureau web unifié** | AUCUN concurrent | Ouvre le marché employés non-tech |
| **Surcouche (pas remplacement)** | Approche unique | Adoption sans migration |
| **Accessibilité "niveau Giselle"** | Rare | Démocratise le self-hosting |
| **K3S natif + simplicité CasaOS** | Combinaison unique | Best of both worlds |
| **Né du besoin réel** (4 ans) | Authenticité | Crédibilité communauté |

---

## Target Users

### Primary Users

#### The Technical Spectrum (Administrators)

UniDash cible un spectre d'utilisateurs techniques unis par un besoin commun : l'accessibilité sans sacrifier la puissance.

| Profil | Description | Frustration actuelle | Valeur UniDash |
|--------|-------------|---------------------|----------------|
| **Admin Junior** | Formé IT, début de carrière | Stack technique massive, aucune feuille de route claire pour construire une infra complète | Chemin guidé, apprentissage structuré |
| **Homelabber Autodidacte** | Passionné sans formation formelle, veut du semi-professionnel chez lui | Pas de base saine accessible, courbe d'apprentissage décourageante | Infrastructure pro sans prérequis |
| **Autodidacte Devenu Pro** | A prouvé ses compétences, travaille dans l'IT | Veut efficacité, pas réapprendre | Outil qui valorise son expertise acquise |
| **Dev Senior Fatigué** | Expert technique, saturé au travail | "J'en ai assez, je veux juste que ça marche chez moi" | Simplicité maximale, puissance sous-jacente |

**Point commun :** Tous cherchent l'équilibre entre accessibilité et capacités enterprise-grade.

#### Giselle la Comptable (End Users)

**Rôle :** Utilisateur final obligatoire - pas la cible directe, mais indispensable au succès.

**Contexte :** Si l'entreprise adopte UniDash, TOUS les employés doivent pouvoir l'utiliser, y compris ceux sans aucune compétence technique.

**Profil type :**
- Niveau technique : zéro
- Besoin : "Je veux juste faire mon travail"
- Attente : Interface aussi simple qu'un smartphone

**Services utilisés :**
- Nextcloud (fichiers personnels et partagés)
- Collabora Online / OnlyOffice (édition Word, Excel)
- ERP métier
- Webmail
- Applications métier spécifiques

**Valeur clé :** Accessibilité totale - bureau web depuis la maison, le bureau, un lieu public, chez un ami. Mobilité sans friction.

### Secondary Users

| Profil | Rôle | Motivation principale |
|--------|------|----------------------|
| **Patron / Décideur** | Approbateur d'achat | Réduction des coûts : moins de prestations externes, moins d'employés IT nécessaires, tout préintégré |
| **Homelabber Influenceur** | Prescripteur futur | Accès à un équipement professionnel à domicile sans dette technique massive en apprentissage |

### User Journey

#### Admin (tous profils)

1. **Découverte :** Reddit r/selfhosted, r/homelab, GitHub trending, bouche-à-oreille communauté
2. **Onboarding :** One-liner curl → installation < 30 min → premier service déployé
3. **Moment "Aha!" :** "J'ai mon cluster K3S HA qui tourne et je n'ai pas lu 50 pages de doc"
4. **Usage quotidien :** Interface unifiée pour tous les services, store pour nouveaux besoins
5. **Long terme :** Infra qui grandit avec les besoins, passage homelab → PME sans migration

#### Giselle (End User)

1. **Découverte :** "L'IT m'a dit qu'on change de système"
2. **Onboarding :** URL fournie → connexion → bureau familier (type smartphone)
3. **Moment "Aha!" :** "Je peux accéder à mes fichiers depuis chez moi exactement comme au bureau"
4. **Usage quotidien :** Ouvre son bureau, lance ses apps, travaille - sans penser à l'infrastructure
5. **Long terme :** "C'est devenu normal, je ne pourrais plus revenir en arrière"

---

## Success Metrics

### Philosophy

UniDash est un projet communautaire écrit pour sa communauté. Toute métrique représente un avis qui a de l'importance. Refuser de mesurer quelque chose reviendrait à s'éloigner de sa base utilisateur, de ses clients potentiels et de ses investisseurs.

### North Star Metric

**Ratio Étoiles GitHub / Utilisateurs Totaux**

> "Est-ce que les gens qui utilisent UniDash l'AIMENT vraiment ?"

Cette métrique capture l'essence du projet : un outil communautaire doit plaire à sa communauté. Le volume de téléchargements seul est une vanity metric - le ratio d'appréciation reflète la vraie valeur perçue.

### User Success Metrics

| Métrique | Formule | Signal de succès |
|----------|---------|------------------|
| **Ratio Croissance/Tickets** | (Nouveaux users / mois) ÷ (Tickets ouverts / mois) | Ratio élevé = produit qui fonctionne sans friction |
| **Time-to-Value Admin** | Temps entre installation et premier service HA déployé | < 30 min = onboarding réussi |
| **Adoption Giselle** | % d'end users actifs quotidiens sur users provisionnés | > 80% = adoption réelle (pas juste installé) |
| **Tickets Zero-Touch** | % d'end users n'ayant jamais ouvert de ticket | > 90% = accessibilité atteinte |

### Business Objectives

#### Phase 1 - MVP Open Source (0-12 mois)

| Objectif | Cible | Indicateur de succès |
|----------|-------|---------------------|
| **Téléchargements** | 1 000 | Validation de l'intérêt marché |
| **Étoiles GitHub** | 100 | Appréciation communauté |
| **Contributeurs actifs** | 5 | Communauté engagée |
| **Beta-testeurs PME** | 3-5 | Validation B2B |

#### Phase 2 - Transition (12-18 mois)

| Objectif | Cible | Indicateur de succès |
|----------|-------|---------------------|
| **Téléchargements** | 5 000 | Croissance x5 |
| **Entreprises intéressées** | 15-20 | Pipeline commercial viable |
| **Feedback qualité** | ≥ 4 étoiles | Produit mature |
| **Investissement** | Suffisant pour 1ère embauche | Capacité de scale |

#### Phase 3 - Commercial (18-36 mois)

| Objectif | Cible | Indicateur de succès |
|----------|-------|---------------------|
| **Clients payants** | 30-50 | Revenus récurrents |
| **Churn rate** | < 10% (cible 5%) | Rétention forte |
| **NPS** | 4,5 / 5 étoiles | Satisfaction client |
| **Ratio étoiles/users** | > 10% | Amour de la communauté |

### Key Performance Indicators

#### Technique

| KPI | Cible | Justification |
|-----|-------|---------------|
| **Uptime** | 95% | Maintenance incluse, SLA réaliste |
| **Temps réponse SAV** | < 4-8h moyenne | Majorité < 2h, gros tickets plus longs |
| **Bugs critiques / release** | < 5 (cible 0) | Qualité code et tests |
| **Temps installation / machine** | < 20 min | Équivalent distro Linux automatisée |

#### Engagement

| KPI | Cible | Justification |
|-----|-------|---------------|
| **DAU/MAU Admins** | > 60% | Usage régulier, pas abandonné |
| **Apps installées / instance** | > 5 | Écosystème utilisé |
| **Retention 30 jours** | > 70% | Valeur durable perçue |

---

## MVP Scope

### Technical Stack

| Composant | Technologie | Justification |
|-----------|-------------|---------------|
| **Backend API** | Python (FastAPI) | Librairies AD/LDAP stables et maintenues |
| **Frontend Desktop** | Astro | Performance, compatible API Python |
| **Orchestration** | K3S | HA native, standard enterprise |
| **VPN** | L2TP/IPsec | Éprouvé en production enterprise, recommandé par professionnels |
| **Base de données** | PostgreSQL | Standard enterprise |

### Core Features (V1 MVP)

#### 1. Infrastructure Technique (Priorité 1)
- K3S intégré (orchestration HA)
- Multi-serveurs (minimum 3 pour quorum HA)
- VPN L2TP/IPsec (sécurité admin + multi-site)
- Reverse proxy intégré (sous-domaines auto)

#### 2. API Backend (Priorité 2)
- API REST Python/FastAPI
- Consomme les services K3S/infra existants
- Authentification utilisateurs
- Active Directory comme provider de compte (connexion sur compte AD existant)
- **UniDash comme Provider SSO** - Apps du store auto-intégrées, zéro config
- Optionnel : Client SSO pour MS Auth / Google Auth

#### 3. Desktop Web (Priorité 3)
- Interface splits Android-like (2, 3, 4 zones)
- Système de docks thématiques
- iFrames pour apps web
- Détachement popup navigateur

#### 4. Store Officiel
- Apps gratuites (preuve de concept)
- Format déclaratif YAML/JSON
- 10+ apps au lancement minimum

### Architecture Principle

```
┌─────────────────────────────────────────────────────────┐
│  DESKTOP WEB (consommateur)                             │
│  └─ Consomme l'API, n'est PAS une dépendance           │
└───────────────────────┬─────────────────────────────────┘
                        │ API calls
┌───────────────────────┴─────────────────────────────────┐
│  API BACKEND (Python/FastAPI)                           │
│  └─ Consomme les services K3S/infra                    │
└───────────────────────┬─────────────────────────────────┘
                        │ orchestre
┌───────────────────────┴─────────────────────────────────┐
│  INFRASTRUCTURE (K3S, services)                         │
│  └─ Doit exister EN PREMIER (pré-requis API)           │
└─────────────────────────────────────────────────────────┘
```

**Règle critique :** Si le desktop tombe, les services continuent à tourner.

### Out of Scope for MVP

| Feature | Version cible | Raison du report |
|---------|---------------|------------------|
| Docker standalone | V2 | K3S prioritaire (différenciateur HA) |
| Proxmox / KVM / LXC | V2 | Complexité additionnelle |
| Apps desktop Wayland/Guacamole | V3 | Complexe, pas essentiel pour valider |
| Sandbox isolés | V3 | Dépend de Wayland |
| Certifications & Cours | V3 | Post-validation marché |
| Paiements & Monétisation (Stripe) | V3 | Après construction communauté |
| Repos externes (store) | V1.x si temps | Nice-to-have |

### MVP Success Criteria

**Fonctionnel :**
- [ ] Desktop web stable et utilisable
- [ ] Installation one-liner < 30 min
- [ ] Cluster K3S HA fonctionnel sur 3 serveurs
- [ ] VPN L2TP/IPsec opérationnel
- [ ] Authentification AD fonctionnelle
- [ ] SSO Provider intégré
- [ ] 10+ apps dans le store officiel

**Qualité :**
- [ ] Testé en production sur infra Gabriel
- [ ] Validé par la communauté en release-candidate
- [ ] Zéro bug bloquant confirmé sur environnements variés

### Release Pipeline

```
┌─────────────┐    ┌──────────────┐    ┌───────────────────┐    ┌─────────────┐
│   TEST      │───▶│  PRE-RELEASE │───▶│ RELEASE-CANDIDATE │───▶│   RELEASE   │
│  (1 semaine)│    │  (2 semaines)│    │    (1 mois)       │    │  (stable)   │
│             │    │              │    │                   │    │             │
│ GitHub      │    │ Éprouvé sur  │    │ Validation        │    │ Prêt pour   │
│ Actions     │    │ infra perso  │    │ COMMUNAUTÉ        │    │ production  │
│ Aucune      │    │              │    │ Environnements    │    │             │
│ garantie    │    │              │    │ variés testés     │    │             │
└─────────────┘    └──────────────┘    └───────────────────┘    └─────────────┘
```

**Philosophie :** Projet communautaire = environnements variés = validation communautaire OBLIGATOIRE avant release stable.

### Future Vision

#### V2 (Post-MVP)
- Docker natif (standalone)
- Proxmox / KVM / LXC intégration
- Repos externes communautaires
- **LLDAP (Light LDAP)** - Pour services legacy sans support SSO, auto-intégré zéro-config

#### V3 (Scale)
- Apps desktop Wayland/Guacamole
- Sandbox isolés (éducation + tests)
- Certifications & Cours
- Système de paiement (Stripe)
- Monétisation active

