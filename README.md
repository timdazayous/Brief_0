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
- **Pocket** : sauvegarde et annotation d’articles

## 🔗 Sources RSS suivies

### Flux RSS officiels suivis via Feedly
- Microsoft Security Blog : [https://www.microsoft.com/en-us/security/blog/](https://www.microsoft.com/en-us/security/blog/)  
- Google AI Blog : [https://ai.googleblog.com/](https://ai.googleblog.com/)  
- OpenAI Blog : [https://openai.com/blog](https://openai.com/blog)  
- arXiv Machine Learning (cs.LG) : [https://export.arxiv.org/rss/cs.LG](https://export.arxiv.org/rss/cs.LG)  
- arXiv Artificial Intelligence (cs.AI) : [https://export.arxiv.org/rss/cs.AI](https://export.arxiv.org/rss/cs.AI)  
- The Hacker News : [https://feeds.feedburner.com/TheHackersNews](https://feeds.feedburner.com/TheHackersNews)  

### Page suivie via Feedly (pas de RSS officiel)
- OWASP ML Security Top 10 : [https://owasp.org/www-project-machine-learning-security-top-10/](https://owasp.org/www-project-machine-learning-security-top-10/)

## :loudspeaker: Alertes Google paramétrées

### Surveillance en temps réel mise en place sur plusieurs domaines
* Cyber attaque IA
* Cyber attack AI
* Cybersecurité IA
* Cybersecurity AI

## 🕒 Rituel de veille automatisé
- **Lundi** : ouverture de Feedly → lecture des nouveautés dans le dossier "Cybersécurité IA"  
- **Mercredi** : tri des articles → sauvegarde des plus pertinents dans Pocket  
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
## Intégration de la cybersécurité dès la conception (Security by Design)**
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

