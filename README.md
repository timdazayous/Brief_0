# 🛡️ Veille Technologique – Cybersécurité en IA

## 👤 Auteur
*DAZAYOUS Tim*  
Développeur junior – Projet SIDORA IA

## 📌 Objectifs de la veille
- Comprendre les enjeux de cybersécurité appliqués à l’intelligence artificielle.  
- Mettre en place un rituel de veille technologique automatisé et régulier.  
- Identifier les sources fiables et pertinentes.  
- Produire une restitution structurée et compréhensible pour les parties prenantes.

## ⚙️ Outils utilisés
- **Feedly** : agrégateur de flux RSS  
- **Google Alerts** : alertes automatiques par email  
- **Substack** : sauvegarde et annotation d’articles

## 🔗 Sources RSS suivies

### Flux RSS officiels suivis
- Microsoft Security Blog : [https://www.microsoft.com/en-us/security/blog/](https://www.microsoft.com/en-us/security/blog/)  
- Google AI Blog : [https://ai.googleblog.com/](https://ai.googleblog.com/)  
- OpenAI Blog : [https://openai.com/blog](https://openai.com/blog)  
- arXiv Machine Learning (cs.LG) : [https://export.arxiv.org/rss/cs.LG](https://export.arxiv.org/rss/cs.LG)  
- arXiv Artificial Intelligence (cs.AI) : [https://export.arxiv.org/rss/cs.AI](https://export.arxiv.org/rss/cs.AI)  
- The Hacker News : [https://feeds.feedburner.com/TheHackersNews](https://feeds.feedburner.com/TheHackersNews) 
#### Best flux en dur en dehors de logiciels specialisés comme inoreader ou feedly
- [GOOGLE ONLINE SECURITY - ATOM](https://feeds.feedburner.com/GoogleOnlineSecurityBlog")
- [MICROSOFT SECURITY FEED - RSS](https://www.microsoft.com/en-us/security/blog/feed/)
- [CYBER BUILDERS - ATOM](https://cyberbuilders.substack.com/feed)
- [THE CONVESRATION - ATOM](https://theconversation.com/topics/cybersecurity-535/articles.atom)
- [VENTURE IN SECURITY - ATOM](https://ventureinsecurity.net/feed)
- [ALIAS ROBOTICS - ATOM](https://news.aliasrobotics.com/rss/)
- [INTELLIGENCE X](https://incidentdatabase.ai//rss.xml)

#### Good flux en dur en dehors de logiciels specialisés comme inoreader ou feedly
- [FIDELIS SECURITY - RSS](https://fidelissecurity.com/feed/)
- [LYNX TECHNOLOGY - RSS](https://lynxtechnologypartners.com/blog/feed/)
- [ESECURITY PLANET - RSS](https://www.esecurityplanet.com/feed/)
- [INCIDENTDATABASE - ATOM](https://incidentdatabase.ai//rss.xml) 
- [UNDER DEFENSE - RSS](https://underdefense.com/feed/)
- [KREBSON ON SECURITY - RSS](https://krebsonsecurity.com/feed/)
- [CYBLE BLOG - RSS](https://cyble.com/feed/),
- [MIT CYBERSECURITY - ATOM](https://news.mit.edu/topic/mitcyber-security-rss.xml),
- [THE LAST WATCHDOG - RSS](https://www.lastwatchdog.com/feed/)
- [THE CYBER EXPRESS - RSS](https://thecyberexpress.com/feed/)
- [DR ERDAL OZKAYA - RSS](https://erdalozkaya.com/feed/)
- [VMWARE - RSS](https://blogs.vmware.com/security/feed)


### Page suivie via Feedly (pas de RSS officiel)
- OWASP ML Security Top 10 : [https://owasp.org/www-project-machine-learning-security-top-10/](https://owasp.org/www-project-machine-learning-security-top-10/)

## :loudspeaker: Alertes Google paramétrées

### Surveillance en temps réel mise en place sur plusieurs domaines
* Cyber attaque IA
* Cyber attack AI
* Cybersecurité IA
* Cybersecurity AI

## 🕒 Rituel de veille automatisé
- **Lundi** : ouverture de Inoreader → lecture des nouveautés dans le dossier "Cybersécurité IA"  
- **Mercredi** : tri des articles → sauvegarde des plus pertinents dans Substack  
- **Weekend** : mise à jour de la synthèse dans ce fichier README.md

## 🏴‍☠️ Principales menaces
- **Attaques adversariales** : modification subtile des entrées pour tromper le modèle  
- **Poisoning des données** : altération du dataset d’entraînement  
- **Vol ou extraction de modèles** : récupération d’un modèle via ses réponses  
- **Backdoors dans les modèles** : comportements cachés déclenchés par des motifs spécifiques  
- **Prompt injection (LLM)** : manipulation des modèles de langage pour obtenir des données sensibles  
- **Risques de supply chain IA** : dépendances logicielles corrompues ou malveillantes

## 🔐 Bonnes pratiques pour se protéger
- Vérification et nettoyage des données d’entraînement  
- Tests adversariaux réguliers  
- Filtrage des prompts pour les LLM  
- Mise à jour et gestion sécurisée des dépendances  
- Application des cadres de sécurité : NIST AI RMF, normes OWASP

> Exemple d'installation d'outil pour des tests de securité IA
```bash
pip install secml
pip install adversarial-robustness-toolbox
```
> Il existe des bibliothèques pour tester la robustesse d'un modèle IA face à des attaques.
```python
from art.attacks.evasion import FastGradientMethod
from art.estimators.classification import SklearnClassifier

classifier = SklearnClassifier(model=mon_modele)
attack = FastGradientMethod(estimator=classifier)
x_adv = attack.generate(x=test_imgs)
```
## :construction: Intégration de la cybersécurité dès la conception (Security by Design)
* La cybersécurité doit être intégrée dès la phase de conception avec une approche "Security by Design". Cela inclut l'identification des risques, la définition des exigences de sécurité, et la mise en place de contrôles adaptés (contrôle d'accès basé sur le principe du moindre privilège, authentification multi-facteurs, gestion sécurisée des clés et secrets, et détection des vulnérabilités dès le développement). La sécurité continue de la base (tests, supervision, conformité) est également cruciale pour limiter les risques d'intrusion et de fuite de données.

## 📅 Synthèse hebdomadaire

### Semaine 1
- Flux RSS configurés et testés  
- Premiers articles lus et sauvegardés  

### Semaine 2
- Analyse des articles les plus pertinents  
- Mise à jour du README.md avec nouvelles informations
- Alertes Googles definies

### Semaine 3
- Mise à jour du README.md
- Création d'un google slide reprenants les principaux points vu lors de la veille

## 🎯 Conclusion
Cette veille technologique m'a permis :
- de comprendre d'avantage les risques liés à l’IA,  
- de mettre en place un rituel automatisé de suivi des sources "fiables"  
- de commencer à sélectionner des outils et pratiques pour sécuriser les projets IA.

## :books: Glossaire
* **LLM:** :small_red_triangle: Large Language Model est un modèle d'intelligence artificielle entraîné sur de grandes quantités de texte pour comprendre, générer et manipuler le langage naturel. Les LLM sont capables de réaliser diverses tâches linguistiques comme la traduction, la rédaction de texte, la réponse à des questions, et plus encore, en s'appuyant sur des réseaux de neurones profonds et des techniques d'apprentissage supervisé. Exemples célèbres incluent GPT (Generative Pre-trained Transformer) et BERT (Bidirectional Encoder Representations from Transformers).:small_red_triangle:
#####
* **NIST AI RMF:** :small_red_triangle: Le Artificial Intelligence Risk Management Framework est un cadre développé par le National Institute of Standards and Technology pour aider les organisations à gérer les risques liés aux systèmes d'intelligence artificielle tout au long de leur cycle de vie. Il vise à promouvoir des systèmes d'IA sûrs, fiables, transparents et éthiques en fournissant des lignes directrices pour identifier, évaluer, et atténuer les risques d’IA. Le cadre est structuré autour de quatre fonctions clés : Gouverner, Cartographier (Map), Mesurer et Gérer les risques. Il s'agit d'un outil flexible et volontaire pour encourager une adoption responsable de l'IA dans divers contextes organisationnels.:small_red_triangle:
#####
* **Normes OWASP:** :small_red_triangle: Open Web Application Security Project est une organisation internationale à but non lucratif dédiée à l'amélioration de la sécurité des applications web. OWASP fournit des ressources gratuites, des outils, et des normes pour aider les développeurs et les organisations à protéger leurs applications contre les vulnérabilités et attaques courantes. Son projet phare, le Top 10 OWASP, liste les dix risques les plus critiques pour la sécurité des applications web, servant de référence pour guider les efforts de sécurisation. OWASP promeut la sensibilisation, la formation, et les meilleures pratiques en sécurité applicative.:small_red_triangle:
