# Analyse Juridique - UniDash

**Date:** 2026-01-09
**Objet:** Vérification des risques de marques déposées et droits d'auteur

---

## Résumé

Analyse des risques juridiques potentiels pour le projet UniDash concernant les marques déposées, droits d'auteur et brevets design.

---

## Analyse par Élément

### Nom et Identité

| Élément | Risque | Analyse |
|---------|--------|---------|
| **"UniDash"** | À vérifier | Pas de marque existante trouvée dans les recherches initiales. Vérification formelle recommandée avant lancement commercial |
| **"Universal Dashboard"** | Faible | Terme descriptif, difficile à protéger comme marque |
| **"Store Personnel"** | Aucun | Terme générique français, non protégeable |

### Concepts UI & Design

| Élément | Risque | Analyse |
|---------|--------|---------|
| **Bureau web** | Aucun | Concept UI générique, non protégeable par copyright |
| **Dock latéral** | Aucun | Pattern standard utilisé depuis macOS, Windows, Linux |
| **Tiling Window Manager** | Aucun | Pattern existant depuis les années 80 (i3, Sway, dwm, etc.) |
| **Store d'applications** | Aucun | Pattern standard (App Store, Play Store, etc.) |

### Éléments Visuels

| Élément | Risque | Analyse |
|---------|--------|---------|
| **Boutons "traffic light" (rouge/jaune/vert)** | Faible | Apple n'a pas de brevet design spécifique sur ces boutons. De nombreux projets open source les reproduisent (GitHub, Figma). Éviter une copie pixel-perfect exacte |
| **Palette couleurs Tailwind** | Aucun | Couleurs non protégeables par copyright |
| **Couleurs sémantiques (success/error/warning)** | Aucun | Conventions UX universelles |

### Inspirations Design

| Inspiration | Risque | Analyse |
|-------------|--------|---------|
| **Vercel wizard** | Aucun | S'inspirer d'un style/approche n'est pas une violation |
| **Linear polish** | Aucun | Style minimaliste non protégeable |
| **macOS App Store** | Aucun | Pattern de cards/grille standard |
| **Windows 11 layout** | Aucun | Layout standard non protégeable |

---

## Recommandations

### Avant Lancement Commercial

1. **Recherche de marque formelle** sur "UniDash" auprès de :
   - USPTO (États-Unis)
   - INPI (France)
   - EUIPO (Union Européenne)
   - Bases de données internationales (WIPO)

2. **Enregistrement de marque** si le nom est disponible, dans les classes :
   - Classe 9 : Logiciels téléchargeables
   - Classe 42 : Services SaaS/Cloud

### Design & UI

1. **Boutons fenêtre** : Créer des variations propres à UniDash plutôt que copier exactement le style macOS
2. **Icônes** : Utiliser des icônes open source (Heroicons, Lucide) ou créer des icônes originales
3. **Logo** : Créer un logo original, vérifier qu'il ne ressemble pas à des marques existantes

### Open Source

1. **Licences** : S'assurer que toutes les dépendances utilisées ont des licences compatibles avec le modèle commercial prévu
2. **Attribution** : Respecter les attributions requises par les licences des composants utilisés

---

## Conclusion

**Risque global : FAIBLE**

Le projet UniDash utilise des patterns UI standards et des concepts non protégeables. Les seuls points d'attention sont :
- La vérification formelle du nom "UniDash" comme marque
- Éviter de copier exactement les éléments graphiques d'Apple (boutons, icônes)

Tous les autres éléments (dock, tiling, store, couleurs, inspirations) sont des patterns UI génériques librement utilisables.