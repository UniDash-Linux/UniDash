---
stepsCompleted: [1, 2, 3, 4, 6, 7, 8, 9, 10, 11]
inputDocuments:
  - "_bmad-output/planning-artifacts/product-brief-UniDash-2026-01-08.md"
  - "_bmad-output/analysis/market-research-2026-01-07.md"
  - "_bmad-output/analysis/brainstorming-session-2026-01-07.md"
workflowType: 'prd'
lastStep: 2
documentCounts:
  brief: 1
  research: 1
  brainstorming: 1
  projectDocs: 0
  projectContext: 0
projectType: greenfield
---

# Product Requirements Document - UniDash

**Author:** Gabriel
**Date:** 2026-01-08

## Executive Summary

UniDash (Universal Dashboard) est une plateforme B2B de gestion d'infrastructure serveur avec bureau web intégré. Sa mission : rendre la gestion de parc serveur aussi simple que l'utilisation d'un smartphone, accessible à tous - des administrateurs système aux employés non-techniques.

**Vision :** Si Spotify représente la simplicité pour écouter de la musique, UniDash incarne l'accessibilité quand vous avez besoin d'un serveur.

**Problème résolu :**
- Écosystème fragmenté : 5-10 interfaces distinctes à jongler (Proxmox, Portainer, Cockpit, etc.)
- Aucune accessibilité pour les employés non-techniques
- Absence de "feuille de route" claire pour construire une infrastructure

**Le moment "Wow" :**
L'utilisateur installe le système et réalise qu'il n'a plus rien à penser, rien à gérer. "Je veux ça, je l'installe, ça marche" - zéro friction, même pour quelqu'un qui veut un homelab sans comprendre les détails techniques.

### What Makes This Special

**Le bureau web unifié** est LE différenciateur d'UniDash - le nom même (Universal Dashboard) en témoigne. Ce qui a commencé comme un panneau d'administration universel a évolué en un véritable bureau web.

| Différenciateur | Unicité | Impact |
|-----------------|---------|--------|
| **Bureau web unifié** | AUCUN concurrent | Blue ocean - ouvre le marché des non-techniciens |
| **Surcouche (pas remplacement)** | Approche unique | Adoption sans migration brutale |
| **Accessibilité "niveau Giselle"** | Rare | Démocratise le self-hosting |
| **Zéro friction** | Philosophie core | "Je veux, j'installe, ça marche" |
| **Né du besoin réel (4 ans)** | Authenticité | Crédibilité communauté |

## Project Classification

**Technical Type:** SaaS B2B + Web Application (plateforme avec desktop web)
**Domain:** Infrastructure Management (général)
**Complexity:** Medium-High (K3S, multi-serveurs, SSO, AD, VPN)
**Project Context:** Greenfield - nouveau projet

**Stack technique définie :**
- Backend : Python (FastAPI)
- Frontend : Astro
- Orchestration : K3S
- VPN : L2TP/IPsec
- Database : PostgreSQL

**Ordre de build :**
1. Infrastructure technique (K3S, services)
2. API Backend (consomme l'infra)
3. Desktop Web (consomme l'API)

---

## Success Criteria

### User Success

**Admin (Spectre Technique) :**
- Installation + premier service HA fonctionnel en < 30 minutes
- "Je veux ça, je l'installe, ça marche" - zéro friction
- Aucune documentation de 50 pages à lire pour démarrer

**Giselle (End User) :**
- Accède à ses fichiers/apps sans appeler l'IT
- Interface aussi intuitive qu'un smartphone
- Mobilité totale : maison, bureau, lieu public - même expérience

### Business Success

#### Métriques par Segment

| Segment | Métrique principale | Cible | Justification |
|---------|---------------------|-------|---------------|
| **Homelabs / Gratuits** | Ratio étoiles GitHub / users | 20-30% (idéal 40%) | Communauté active, indicateur d'amour produit |
| **Entreprises / Payants** | Rétention | > 90-95% | Choix réfléchi, investissement durable |

#### Objectifs par Phase

**Phase 1 - MVP Open Source (0-12 mois)**

| Objectif | Cible |
|----------|-------|
| Téléchargements | 1 000 |
| Étoiles GitHub | 200-400 (20-40% ratio) |
| Contributeurs actifs | 5 |
| Beta-testeurs PME | 3-5 |

**Phase 2 - Transition (12-18 mois)**

| Objectif | Cible |
|----------|-------|
| Téléchargements | 5 000 |
| Étoiles GitHub | 1 000-2 000 (20-40% ratio) |
| Entreprises intéressées | 15-20 |
| Feedback qualité | ≥ 4 étoiles |

**Phase 3 - Commercial (18-36 mois)**

| Objectif | Cible |
|----------|-------|
| Clients payants | 30-50 |
| Rétention entreprises | > 90-95% (churn < 5-10%) |
| Ratio étoiles/users gratuits | 20-40% maintenu |

### Technical Success

| KPI | Cible | Justification |
|-----|-------|---------------|
| **Uptime** | 95% | Maintenance incluse, SLA réaliste |
| **Temps réponse SAV** | < 4-8h moyenne | Majorité < 2h, gros tickets plus longs |
| **Bugs critiques / release** | < 5 (cible 0) | Qualité code et tests |
| **Installation / machine** | < 20 min | Équivalent distro Linux automatisée |
| **Chargement desktop (vide)** | < 1-2 sec | Astro + WebAssembly = quasi-instantané |
| **Apps simultanées sans lag** | 4-5 / user | Power user frontend, scalabilité serveur = client |

### Measurable Outcomes

**North Star Metric :** Ratio Étoiles GitHub / Utilisateurs Gratuits
> "Est-ce que les gens qui utilisent UniDash l'AIMENT vraiment ?"

**Indicateur secondaire :** Ratio Croissance/Tickets
> (Nouveaux users / mois) ÷ (Tickets ouverts / mois) = produit sans friction

---

## Product Scope

### MVP - Minimum Viable Product

**Infrastructure Technique (Priorité 1)**
- K3S intégré (orchestration HA)
- Multi-serveurs (minimum 3 pour quorum)
- VPN L2TP/IPsec
- Reverse proxy intégré

**API Backend (Priorité 2)**
- Python/FastAPI
- Authentification AD comme provider
- UniDash comme Provider SSO (apps auto-intégrées)

**Desktop Web (Priorité 3)**
- Interface splits Android-like
- Système de docks thématiques
- iFrames pour apps web

**Store Officiel**
- 10+ apps gratuites au lancement
- Format déclaratif YAML/JSON

### Growth Features (Post-MVP)

**V2 :**
- Docker natif (standalone)
- Proxmox / KVM / LXC intégration
- Repos externes communautaires
- LLDAP pour services legacy

### Vision (Future)

**V3 :**
- Apps desktop Wayland/Guacamole
- Sandbox isolés (éducation + tests)
- Certifications & Cours
- Système de paiement (Stripe)
- Monétisation active

---

## User Journeys

### Journey 1: Thomas - L'Admin Junior qui Découvre sa Voie

Thomas a 24 ans, administrateur système junior dans une PME de 30 personnes. Il a fait un BTS SIO, il sait installer Windows Server et configurer un Active Directory basique. Mais quand son patron lui demande de "mettre en place un cloud privé pour l'équipe", il panique.

Il passe des nuits sur YouTube à regarder des tutoriels Kubernetes. Il essaie Proxmox - trop complexe. Docker Compose - ça marche jusqu'à ce que ça casse. Il a 15 onglets ouverts en permanence : Portainer, Traefik, Authelia, Nextcloud admin, chaque service avec son interface.

Un jour, sur Reddit, quelqu'un mentionne UniDash. Thomas est sceptique mais il essaie quand même un samedi matin.

**20 minutes plus tard**, son cluster K3S tourne sur 3 VMs. Il n'a pas écrit une ligne de YAML. Le bureau web s'affiche, il voit un Store, il clique sur "Nextcloud", puis "Installer". 2 minutes après, Nextcloud est accessible, déjà connecté au SSO.

Thomas réalise qu'il vient de faire en 30 minutes ce qui lui aurait pris un week-end entier. Il montre le bureau web à son patron le lundi. "C'est... propre", dit le patron. Thomas sourit - c'est la première fois qu'on ne lui demande pas "c'est quoi cette interface moche ?".

**Six mois plus tard**, Thomas gère l'infrastructure de 3 PME clientes de son entreprise, toutes sur UniDash. Il contribue même au projet sur GitHub - son premier vrai projet open source. Il a trouvé sa voie.

**Cette journey révèle des besoins pour :**
- **Installation guidée** - wizard pas-à-pas, pas de YAML manuel
- **Store intégré** - apps one-click avec SSO automatique
- **Interface professionnelle** - le bureau web impressionne les décideurs
- **Documentation accessible** - pas besoin d'être expert K8s
- **Chemin vers la contribution** - communauté accueillante

### Journey 2: Marc - Le Dev Senior Fatigué

Marc a 38 ans, 15 ans d'expérience en développement. La journée, il architece des systèmes distribués pour une scale-up. Le soir, il rêve d'un homelab simple - Plex pour les films, Nextcloud pour les photos de famille, peut-être un petit serveur Minecraft pour ses enfants.

Mais chaque tentative se transforme en cauchemar. Il a essayé Proxmox - trop de clics, trop de maintenance. Docker Compose - ça marche jusqu'au jour où ça casse et il passe son dimanche à debugger. Kubernetes à la maison ? "Je fais ça toute la journée au boulot, je veux pas le refaire le soir."

Un collègue lui parle d'UniDash. Marc est sceptique - "encore un truc à apprendre". Mais il tente quand même, un samedi matin.

**20 minutes plus tard**, son cluster tourne. Pas de YAML à écrire. Pas de certificats à générer. Il ouvre le Store, clique sur Plex, clique sur Nextcloud. Les deux apps apparaissent sur son bureau web, déjà connectées à son compte UniDash.

Le dimanche, sa femme lui demande : "Tu travailles pas sur tes serveurs aujourd'hui ?" Marc réalise qu'il n'a rien eu à faire. Tout fonctionne. Il passe la journée avec ses enfants au lieu de debugger des containers.

**Six mois plus tard**, Marc a ajouté 8 apps à son homelab sans jamais ouvrir un terminal. Quand un ami développeur lui demande comment il gère tout ça, Marc sourit : "Je gère pas. C'est ça le truc."

**Cette journey révèle des besoins pour :**
- **Zéro maintenance** - le système doit se gérer seul
- **Installation one-click** depuis le Store
- **SSO transparent** - pas de comptes à créer par app
- **Stabilité** - "ça marche" sans intervention
- **Expérience "set and forget"** - opposé de l'expérience pro quotidienne

### Journey 3: Giselle - La Comptable qui Veut Juste Travailler

Giselle a 52 ans, comptable dans une PME de 25 personnes. Elle utilise un ordinateur depuis Windows 95, mais pour elle, c'est un outil - pas une passion. Quand ça marche, elle n'y pense pas. Quand ça casse, elle appelle Julien de l'IT.

Depuis le COVID, son patron a décidé de "moderniser l'infrastructure". Julien a installé des serveurs, parlé de "cloud privé", de "sécurité des données". Giselle a hoché la tête poliment sans comprendre.

**Le problème :** maintenant elle doit accéder à ses fichiers Excel depuis chez elle, mais c'est un parcours du combattant. VPN qui ne se connecte pas, mot de passe différent pour chaque application, Julien pas toujours disponible. Elle finit souvent par s'envoyer des fichiers par email - pas sécurisé, mais au moins ça marche.

**L'installation (une seule fois) :** Julien passe à son bureau. "Je t'installe un truc, ça prend 2 minutes." Il configure le client VPN sur son PC, coche "connexion automatique", et lui donne un raccourci bureau "Mon Espace UniDash". "Tu cliques là, tu mets ton mot de passe Windows habituel, c'est tout."

Un lundi matin, Giselle clique sur le raccourci. Son mot de passe Active Directory. Un bureau apparaît - familier, comme Windows mais dans son navigateur.

Elle voit une icône "Fichiers" (NextCloud intégré). Elle clique, l'application s'ouvre dans le bureau web. Ses dossiers sont là - les mêmes qu'au bureau. Elle navigue jusqu'à son Excel, double-clique, ça s'ouvre dans OnlyOffice (ou l'éditeur intégré). Elle modifie, elle ferme. C'est sauvegardé.

**Le soir, depuis chez elle :** elle ouvre son laptop personnel. Le VPN est configuré là aussi (Julien l'a fait la semaine dernière). Elle clique sur le même raccourci, même mot de passe. Même bureau. Son fichier Excel est là, avec ses modifications du matin.

Giselle ne sait pas ce qu'est K3S, ni ce qu'est un container. Elle sait que Julien a "installé un truc" une fois. Elle sait juste que maintenant, "ça marche comme au bureau, mais partout."

**Six mois plus tard**, Giselle ne demande plus à Julien comment accéder à ses fichiers. Elle montre même à ses collègues comment naviguer dans l'app Fichiers. Elle dit souvent : "Tu ouvres Fichiers, tu cherches ton dossier, c'est tout."

**Cette journey révèle des besoins pour :**
- **SSO transparent** - un seul mot de passe (AD), zéro compte supplémentaire
- **Gestionnaire de fichiers intégré** - NextCloud ou équivalent comme app première classe
- **Installation VPN one-time** - IT configure une fois, ça marche ensuite
- **Expérience cohérente** - même bureau web sur tous les appareils configurés
- **Apps dans le bureau** - navigation intuitive dans les applications

**Point technique à explorer (V2+) :**
- VPN L2TP over HTTPS pour éviter l'installation client ? À valider faisabilité

### Journey 4: Philippe - Le Patron qui Veut des Résultats

Philippe a 48 ans, co-fondateur d'une PME industrielle de 45 employés. Il n'est pas technique - il a fait une école de commerce et son expertise c'est le business développement. Mais il comprend une chose : l'IT coûte cher et pose problème.

**Le contexte :** son admin sys, Julien, lui parle depuis des mois de "moderniser l'infrastructure". Philippe entend : "dépenser de l'argent". Il a déjà eu des mauvaises expériences - un projet SharePoint à 50K€ que personne n'utilise, des licences Microsoft qui augmentent chaque année, un prestataire IT qui facture 800€ pour chaque intervention.

Julien lui propose UniDash. Philippe est sceptique. "C'est quoi encore ce truc ?"

**La démonstration :** Julien lui montre le bureau web. Philippe voit quelque chose qu'il comprend - ça ressemble à Windows, mais dans un navigateur. Julien lui montre que Giselle de la compta peut accéder à ses fichiers depuis chez elle. Que le commercial terrain peut consulter le CRM depuis son téléphone. Même interface partout.

**L'argument qui fait mouche :** "C'est open source. Le core est gratuit. On paie juste le support si on veut, et on peut changer de prestataire quand on veut - pas de lock-in."

Philippe pose LA question : "Et si Julien part, je fais comment ?"

Julien lui montre le réseau de partenaires SAV certifiés. "N'importe quel prestataire certifié peut reprendre. Tout est standard."

**La décision :** Philippe accepte un pilote de 3 mois. Coût : le temps de Julien + 3 serveurs reconditionnés. Risque minimal.

**Trois mois plus tard :** les tickets IT ont baissé. Giselle n'appelle plus pour ses fichiers. Le commercial accède au CRM sans VPN compliqué. Philippe voit le ROI.

**Un an plus tard :** Philippe a souscrit au support entreprise. Pas parce qu'il en a besoin, mais parce que "ça vaut le coup de soutenir le projet". Il recommande UniDash à d'autres patrons de PME de son réseau.

**Cette journey révèle des besoins pour :**
- **Argument économique clair** - open source, pas de lock-in, coût prévisible
- **Réduction des risques** - pilote possible, prestataires interchangeables
- **ROI visible** - moins de tickets IT, productivité employés
- **Réseau partenaires certifiés** - rassure sur la pérennité
- **Démo "compréhensible"** - le bureau web parle aux non-techniques

### Journey 5: Sophie - La Développeuse qui Devient Partenaire

Sophie a 32 ans, développeuse freelance spécialisée dans les outils de gestion pour PME. Elle a créé un petit logiciel de suivi de temps et facturation - TimFlow - qu'elle vend en SaaS à 15€/mois. Ça marche, elle a 200 clients, mais la croissance stagne.

**Le problème :** chaque nouveau client, c'est du support. "Comment je me connecte ?", "J'ai perdu mon mot de passe", "Ça marche pas sur le PC de ma collègue". Sophie passe plus de temps en support qu'en développement.

Elle découvre UniDash sur Reddit. Un commentaire attire son attention : "Les apps du Store héritent automatiquement du SSO et du système de permissions."

**L'exploration :** Sophie lit la documentation développeur. Le format de packaging est simple - un fichier YAML déclaratif, son image Docker, et c'est tout. Pas besoin de refaire son système d'authentification. Pas besoin de gérer les utilisateurs. UniDash fait tout ça.

**Le calcul :** si elle publie TimFlow sur le Store UniDash, elle perd le contrôle du hosting (le client héberge). Mais elle gagne :
- Zéro support authentification (SSO UniDash)
- Zéro gestion utilisateurs (AD/LDAP du client)
- Accès à une base d'utilisateurs existante
- Possibilité de vendre une licence "premium" via le Store

**Le pivot :** Sophie adapte TimFlow en 2 semaines. Elle retire tout son code d'authentification (500 lignes en moins). Elle publie sur le Store avec un modèle freemium : gratuit pour 3 utilisateurs, 10€/mois au-delà.

**Trois mois plus tard :** TimFlow a 50 nouvelles installations via le Store. Les tickets support ont chuté de 80% - plus de "mot de passe perdu". Sophie peut enfin développer les fonctionnalités que ses clients demandent.

**Un an plus tard :** Sophie a 3 apps sur le Store. Elle participe aux discussions GitHub d'UniDash, suggère des améliorations à l'API développeur. Elle est devenue ambassadrice du projet - pas parce qu'on lui a demandé, mais parce que son business en dépend.

**Cette journey révèle des besoins pour :**
- **SDK/API développeur simple** - packaging YAML déclaratif
- **SSO hérité automatiquement** - zéro code auth pour les apps
- **Modèle économique clair** - freemium, licences, paiement via Store (V3)
- **Documentation développeur** - onboarding rapide pour publier
- **Écosystème gagnant-gagnant** - les devs externes enrichissent le Store

### Journey 6: Karim - Le Prestataire IT qui Se Certifie

Karim a 35 ans, gérant d'une petite société de services IT avec 2 techniciens. Il fait du support pour une douzaine de TPE/PME locales - dépannage, installation de postes, maintenance réseau. Le problème : chaque client a une infrastructure différente. Synology ici, QNAP là, un NAS bricolé ailleurs, trois qui sont "full cloud Microsoft".

**La frustration :** chaque intervention demande de réapprendre. Les marges sont faibles, le temps passé à comprendre l'existant mange le profit. Et quand un client veut "moderniser", Karim propose du Microsoft 365 par défaut - pas parce que c'est le mieux, mais parce que c'est ce qu'il connaît.

Karim découvre UniDash via un article sur le self-hosting. Il voit le programme partenaire certifié.

**La formation :** Karim suit la certification en ligne (gratuite pour le niveau 1). En 2 jours, il comprend l'architecture, le déploiement, les bases du troubleshooting. Il passe l'examen, obtient son badge "Partenaire Certifié".

**Le premier client UniDash :** une PME de 15 personnes qui hésite entre Microsoft 365 et "quelque chose de moins cher". Karim propose UniDash. Installation en une demi-journée. Le client est impressionné par le bureau web.

**L'avantage concurrentiel :** maintenant, tous ses clients UniDash ont la même base. Un ticket chez Client A ? Karim connaît déjà l'interface, les logs, les commandes. Le temps de diagnostic chute de 60%. Ses techniciens peuvent intervenir chez n'importe quel client sans formation spécifique.

**Le modèle économique :** Karim facture l'installation, le support mensuel, et les interventions. Mais surtout, il peut répondre à la question de Philippe (Journey 4) : "Et si notre admin part ?" - "Je reprends, c'est standard."

**Un an plus tard :** 6 de ses 12 clients sont sur UniDash. Karim est listé sur le site comme partenaire certifié de sa région. Il reçoit des leads entrants de PME qui cherchent un installateur local. Son chiffre d'affaires support récurrent a doublé.

**Cette journey révèle des besoins pour :**
- **Programme de certification** - niveaux, formation, examen, badge
- **Documentation partenaire** - troubleshooting, best practices, architecture
- **Annuaire partenaires** - visibilité géographique, leads entrants
- **Standardisation** - même interface partout = expertise transférable
- **Outillage support** - logs centralisés, diagnostics, accès distant

### Journey Requirements Summary

| Capability | Journeys concernées |
|------------|---------------------|
| Installation < 30 min | Thomas, Marc, Philippe |
| SSO/AD intégré | Tous |
| Bureau web unifié | Giselle, Philippe, Thomas |
| Store apps one-click | Marc, Thomas, Sophie |
| SDK développeur | Sophie |
| Programme partenaires | Karim, Philippe |
| Documentation | Thomas, Sophie, Karim |
| VPN configuration simple | Giselle, Marc |
| Zéro maintenance | Marc |
| Interface professionnelle | Thomas, Philippe |

---

## Innovation & Novel Patterns

### Detected Innovation Areas

**Le Bureau Web comme Paradigme d'Interface**

UniDash ne propose pas simplement un dashboard d'administration - il réinvente l'accès à l'infrastructure serveur à travers la métaphore du bureau. Cette approche est unique :

| Aspect | Approche Traditionnelle | Approche UniDash |
|--------|------------------------|------------------|
| Interface | Dashboards techniques (Portainer, Cockpit) | Bureau familier type Windows/macOS |
| Audience | Admins système uniquement | Tous les employés |
| Apps | Interfaces séparées par service | Apps intégrées dans un espace unifié |
| Navigation | URLs, onglets multiples | Fenêtres, docks, raccourcis |

### Market Context & Competitive Landscape

**Analyse du marché :**
- Les solutions existantes (Proxmox, Portainer, Cockpit, CasaOS, Umbrel) ciblent les utilisateurs techniques
- Aucune ne propose une métaphore de bureau web
- Le marché des "non-techniciens qui veulent accéder à l'infrastructure" n'est pas servi

**Positionnement Blue Ocean :**
- Ne pas concurrencer les outils techniques existants
- Créer une nouvelle catégorie : "Desktop-as-a-Service pour infrastructure self-hosted"

### Validation Approach

**Comment valider cette innovation :**

1. **Test Giselle** - Une personne non-technique peut-elle accéder à ses fichiers sans formation ?
2. **Test Philippe** - Un décideur comprend-il l'interface en 30 secondes de démo ?
3. **Métrique** - Temps avant premier usage productif par un non-technicien

### Risk Mitigation

**Risques identifiés :**

| Risque | Impact | Mitigation |
|--------|--------|------------|
| La métaphore bureau paraît "datée" | Medium | Design moderne, pas de skeuomorphisme excessif |
| Performance iFrames | High | Lazy loading, virtualisation, tests charge |
| Complexité SSO multi-apps | High | Architecture solide dès le MVP |
| Adoption par les techniciens | Medium | Garder l'accès aux outils sous-jacents |

**Fallback :** Si le bureau web ne convainc pas, les fonctionnalités techniques (K3S, Store, SSO) restent valides comme dashboard classique.

---

## SaaS B2B Specific Requirements

### Deployment Model

**Dual-track approach :**
- **Self-hosted** (primary) - Client installe sur sa propre infra
- **SaaS hébergé** (secondary) - Partenariat hébergeur avec serveurs préinstallés

### Tenant Architecture

**Modèle single-tenant self-hosted :**
- Une installation = une infrastructure isolée
- Bureau personnel par utilisateur (espace privé)
- Apps installées une fois sur l'infra, chaque utilisateur a son compte via SSO

### Permission Model

**Système de permissions fines (pas de rôles rigides) :**

| Niveau | Portée | Exemples |
|--------|--------|----------|
| Global infra | Tout le système | Installer apps, gérer cluster, backup |
| Par application - Admin | Une app spécifique | Configurer Nextcloud, gérer quotas |
| Par application - Usage | Une app spécifique | Utiliser Nextcloud, accéder aux fichiers |

**Principe :** Un utilisateur = ensemble de permissions assignées.

**Permission maître :** Super-admin avec toutes les permissions (owner de l'installation).

### Authentication Strategy

| Provider | Statut | Notes |
|----------|--------|-------|
| UniDash natif | ✅ MVP | Gestion de comptes intégrée |
| Active Directory | ✅ MVP | Intégration entreprises existantes |
| OpenID Connect | ✅ MVP | SSO standard |
| OAuth (Google/Microsoft) | V2 | Client SSO optionnel |

### Subscription Model

**Pas de tiers fixes.** Calculateur basé sur :
- Nombre de cœurs machines
- Besoins estimés du client
- Offre adaptée automatiquement

**Deux offres distinctes :**
- **Free / Open Source** - Communauté, self-support
- **Éducation** - Calcul similaire au pro, tarif adapté

### Store & App Distribution (interface unique avec switch)

**Un seul Store, deux vues :**
- Interface unique avec switch button "Admin / User"
- Le switch n'apparait que si l'utilisateur a les permissions admin

**Vue Admin (switch sur Admin) :**
- Catalogue complet des apps disponibles
- Bouton "Installer" pour deployer sur l'infrastructure
- Configuration des permissions d'acces par utilisateur/groupe
- Actions : installer, desinstaller, mettre a jour

**Vue User (switch sur User, ou vue par defaut pour non-admins) :**
- Memes apps, filtrees par permissions de l'utilisateur
- Affiche uniquement les apps auxquelles l'utilisateur a droit
- Bouton "Ajouter au bureau" (pas d'installation)
- Actions : ajouter/retirer du bureau personnel

---

## Project Scoping & Phased Development

### MVP Philosophy

**Approche Platform MVP** - Construire les fondations pour l'expansion future tout en délivrant une valeur immédiate.

UniDash MVP doit permettre :
- Installation complète en < 30 min
- Bureau web fonctionnel avec apps
- Store avec 10+ apps validées
- SSO transparent pour l'utilisateur final

### User Journeys par Phase

| Journey | MVP | V2 | V3 |
|---------|-----|----|----|
| Thomas (Admin Junior) | ✅ Complet | - | - |
| Marc (Dev Fatigué) | ✅ Complet | - | - |
| Giselle (Comptable) | ✅ Complet | VPN browser? | - |
| Philippe (Patron) | ✅ Démo/Argument | - | - |
| Sophie (Dev Store) | ⚠️ SDK basique | SDK avancé | Paiements Store |
| Karim (Prestataire) | ❌ | Docs partenaire | Certifications, Annuaire |

### Permission Model Evolution

**Architecture :** Base de code unique, granularité progressive.

**MVP - 3 niveaux simples :**

| Rôle | Permissions |
|------|-------------|
| Super-admin | Tout (owner installation) |
| Admin | Installer apps, gérer users, configurer |
| Utilisateur | Utiliser les apps autorisées |

**V2/V3 - Permissions fines (même base) :**
- Permissions par application (admin/usage)
- Permissions custom définissables par l'admin
- Groupes de permissions

### MVP Feature Boundaries

**Inclus dans MVP :**
- Infrastructure K3S HA (3 nœuds minimum)
- VPN L2TP/IPsec
- API Backend FastAPI
- Auth : UniDash natif + AD + OpenID
- SSO Provider (apps auto-intégrées)
- Auth proxy pour apps legacy
- Bureau web (splits, docks, fenêtres)
- Store unique avec switch Admin/User
- 10+ apps validées
- Permissions simples (3 niveaux)

**Exclu du MVP (V2+) :**
- Docker standalone
- Proxmox/KVM/LXC
- Repos communautaires externes
- LLDAP
- OAuth client (Google/Microsoft)
- VPN browser (L2TP over HTTPS)
- Permissions fines par app

**Exclu du MVP (V3+) :**
- Apps desktop Wayland/Guacamole
- Sandboxes isolés
- Programme certification formalisé
- Paiements Store (Stripe)
- Permissions custom

### Risk Mitigation Strategy

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Performance bureau multi-fenêtres | High | Lazy loading iFrames, limite 4-5 apps simultanées, tests charge |
| Intégration AD formats variés | High | Tests sur AD réels, documentation edge cases |
| Auth proxy apps legacy | Medium | Liste apps compatibles validées, fallback manuel |
| Adoption par techniciens | Medium | Accès CLI/kubectl préservé |

---

## Functional Requirements

### Installation & Infrastructure

- FR1: Le système installe automatiquement un cluster K3S HA via un wizard guidé
- FR2: L'administrateur peut ajouter un nœud au cluster (installation serveur + lien d'ajout)
- FR3: Le système configure automatiquement le VPN L2TP/IPsec côté serveur
- FR4: Le système configure automatiquement le reverse proxy pour les services
- FR5: Le système gère automatiquement les certificats SSL

### Authentification & Utilisateurs

- FR6: L'administrateur peut créer et gérer des comptes utilisateurs natifs UniDash
- FR7: L'administrateur peut connecter UniDash à un Active Directory existant
- FR8: Le système active automatiquement l'authentification OpenID Connect pour les apps compatibles
- FR9: Les utilisateurs peuvent s'authentifier avec un seul compte (SSO) pour toutes les apps
- FR10: L'administrateur peut assigner un rôle (super-admin, admin, utilisateur) à chaque compte
- FR11: Le système configure automatiquement l'authentification LDAP/AD pour les apps compatibles LDAP mais non OIDC
- FR12: Le système peut authentifier les apps legacy via proxy auth

### Store & Applications

- FR13: L'administrateur peut parcourir le Store officiel des applications
- FR14: L'administrateur peut installer une application depuis le Store en one-click
- FR15: L'administrateur peut définir quels utilisateurs ont accès à chaque application
- FR16: L'utilisateur peut parcourir son Store personnel (apps autorisées uniquement)
- FR17: L'utilisateur peut ajouter une application autorisée à son bureau
- FR18: L'administrateur peut désinstaller une application
- FR19: L'administrateur peut mettre à jour une application
- FR20: Le développeur peut packager une application au format YAML déclaratif

### Bureau Web

- FR21: L'utilisateur peut accéder à son bureau personnel via navigateur
- FR22: L'utilisateur peut organiser ses applications en fenêtres redimensionnables
- FR23: L'utilisateur peut utiliser des splits (division écran type Android)
- FR24: L'utilisateur peut organiser ses apps dans des docks thématiques
- FR25: L'utilisateur peut créer des raccourcis vers ses applications favorites
- FR26: L'utilisateur peut ouvrir plusieurs applications simultanément (4-5)
- FR27: L'utilisateur peut personnaliser l'apparence de son bureau

### Gestion des Permissions (MVP Simple)

- FR28: Le super-admin peut accéder à toutes les fonctionnalités du système
- FR29: L'admin peut installer des applications et gérer les utilisateurs
- FR30: L'utilisateur peut uniquement utiliser les applications qui lui sont autorisées

### Administration Système

- FR31: L'administrateur peut visualiser l'état du cluster (nœuds, services)
- FR32: L'administrateur peut consulter les logs centralisés
- FR33: Le système intègre une solution de sauvegarde (Velero/Longhorn)
- FR34: L'administrateur peut accéder directement aux outils sous-jacents (kubectl, Proxmox, etc.)

---

## Non-Functional Requirements

### Performance

- NFR1: Le bureau web vide se charge en < 2 secondes sur connexion standard
- NFR2: L'ouverture d'une app dans le bureau prend < 1 seconde (hors chargement app elle-même)
- NFR3: Le système supporte 4-5 applications ouvertes simultanément sans dégradation perceptible
- NFR4: L'installation d'une application depuis le Store prend < 5 minutes
- NFR5: L'installation initiale du cluster complet prend < 30 minutes

### Sécurité

- NFR6: Toutes les communications sont chiffrées (HTTPS, VPN)
- NFR7: Les mots de passe sont stockés avec hachage sécurisé (bcrypt/argon2)
- NFR8: Les sessions expirent après 24h d'inactivité
- NFR9: L'accès au cluster est restreint au VPN ou réseau local
- NFR10: Chaque app tourne dans son namespace isolé

### Fiabilité & Disponibilité

- NFR11: Le cluster K3S supporte la perte d'un nœud sans interruption de service (HA)
- NFR12: Les sauvegardes automatiques sont effectuées quotidiennement (Velero/Longhorn)
- NFR13: La restauration d'une sauvegarde est possible en < 30 minutes
- NFR14: Le système maintient une disponibilité de 95% (hors maintenance planifiée)

### Intégration

- NFR15: L'intégration AD supporte les formats LDAP standards
- NFR16: Les apps OpenID compatibles s'intègrent automatiquement au SSO
- NFR17: Les apps legacy peuvent être intégrées via proxy auth
- NFR18: Le format de packaging d'apps utilise YAML déclaratif standard

### Maintenabilité

- NFR19: Les mises à jour du système ne nécessitent pas de downtime complet
- NFR20: Les logs sont centralisés et consultables via interface
- NFR21: L'accès aux outils sous-jacents (kubectl, etc.) reste toujours disponible

### Accessibilité (Basique)

- NFR22: L'interface est navigable au clavier
- NFR23: Les contrastes respectent les standards WCAG AA
- NFR24: Le bureau web passe le "test Giselle" - utilisable sans formation technique
