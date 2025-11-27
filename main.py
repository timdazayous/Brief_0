"""
Script de veille RSS -> Markdown
--------------------------------
1. Lit une liste de flux RSS depuis un fichier texte (rss_feeds.txt).
2. Récupère les articles de chaque flux (via feedparser).
3. Génère un fichier Markdown prêt à être collé dans Substack.
4. Enregistre le résultat dans le dossier feed_cybersecu.

Pré-requis :
- Python 3
- pip install feedparser
"""

import feedparser
from datetime import datetime
import os

# Nom du fichier contenant la liste des flux RSS
# (doit se trouver au même niveau que main.py)
FEEDS_FILE = "rss_feeds.txt"

# Dossier de sortie pour les fichiers Markdown
OUTPUT_FOLDER = "feed_cybersecu"


def load_feed_urls_from_file(filepath):
    """
    Lit un fichier texte et renvoie la liste des URLs de flux RSS.

    Format attendu du fichier :
    - 1 URL par ligne
    - lignes vides ou espaces en plus autorisés (elles sont ignorées)

    :param filepath: chemin du fichier (ex: "rss_feeds.txt")
    :return: liste de chaînes (URLs)
    """
    urls = []

    # with gère automatiquement l'ouverture/fermeture du fichier
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            # strip() enlève les espaces, tabulations, retours à la ligne
            url = line.strip()
            # On ignore les lignes vides
            if not url:
                continue
            urls.append(url)

    return urls


def fetch_articles_from_feed(feed_url, max_items=10):
    """
    Récupère les articles d'un flux RSS donné.

    :param feed_url: URL du flux RSS.
    :param max_items: nombre max d'articles à récupérer par flux.
    :return: liste de dicts {title, link, published, summary, source}
    """
    parsed = feedparser.parse(feed_url)
    articles = []

    for entry in parsed.entries[:max_items]:
        title = entry.get("title", "Sans titre")
        link = entry.get("link", "")
        summary = entry.get("summary", "")
        published = entry.get("published", "")
        source = ""

        # Certains flux incluent la source
        if "source" in entry and hasattr(entry.source, "title"):
            source = entry.source.title

        articles.append(
            {
                "title": title,
                "link": link,
                "summary": summary,
                "published": published,
                "source": source,
                "feed_url": feed_url,
            }
        )

    return articles


def collect_all_articles(feed_urls, max_items_per_feed=10):
    """
    Récupère les articles pour tous les flux de la liste.

    :param feed_urls: liste d'URLs de flux RSS.
    :param max_items_per_feed: limite d'articles par flux.
    :return: liste globale d'articles.
    """
    all_articles = []

    for url in feed_urls:
        print(f"Lecture du flux : {url}")
        feed_articles = fetch_articles_from_feed(url, max_items=max_items_per_feed)
        all_articles.extend(feed_articles)

    return all_articles


def generate_markdown_newsletter(articles, title="Veille RSS Cybersecurity / IA"):
    """
    Génère le contenu Markdown de la newsletter.

    :param articles: liste de dicts {title, link, published, summary, source}
    :param title: titre principal du document.
    :return: texte Markdown (str)
    """
    today = datetime.now().strftime("%d/%m/%Y")
    md = f"# {title} - {today}\n\n"
    md += "Sélection d’articles issus de différents flux RSS (Google Alerts, Feedly, Inoreader, etc.).\n\n"

    for idx, art in enumerate(articles, start=1):
        md += f"## {idx}. [{art['title']}]({art['link']})\n"

        if art["source"]:
            md += f"*Source : {art['source']}*\n\n"
        if art["published"]:
            md += f"*Publié : {art['published']}*\n\n"

        if art["summary"]:
            md += f"{art['summary']}\n\n"

        md += "---\n\n"

    return md


def save_markdown_to_folder(markdown_content, folder_name, filename):
    """
    Enregistre le Markdown dans un fichier, dans le dossier indiqué.
    Crée le dossier s'il n'existe pas.

    :param markdown_content: texte Markdown à sauvegarder.
    :param folder_name: nom du dossier (ex: "feed_cybersecu").
    :param filename: nom du fichier (ex: "veille_2025_11_27.md").
    """
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"✅ Dossier créé : {folder_name}")

    filepath = os.path.join(folder_name, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(markdown_content)

    print(f"✅ Fichier Markdown enregistré : {filepath}")


def main():
    """
    1) Charge les URLs de flux RSS depuis rss_feeds.txt.
    2) Récupère les articles.
    3) Génère du Markdown.
    4) Sauvegarde dans feed_cybersecu.
    """
    # 1) Charger les URLs depuis le fichier
    if not os.path.exists(FEEDS_FILE):
        raise FileNotFoundError(
            f"Le fichier {FEEDS_FILE} est introuvable. "
            f"Crée un fichier texte à la racine du projet avec une URL de flux par ligne."
        )

    feed_urls = load_feed_urls_from_file(FEEDS_FILE)
    print(f"Nombre de flux trouvés dans {FEEDS_FILE} : {len(feed_urls)}")

    # 2) Récupérer les articles
    all_articles = collect_all_articles(feed_urls, max_items_per_feed=5)

    # 3) Générer le Markdown
    newsletter_md = generate_markdown_newsletter(
        all_articles, title="Veille RSS Cybersecurity / IA"
    )

    # 4) Sauvegarder dans le dossier feed_cybersecu
    filename = f"veille_{datetime.now().strftime('%Y_%m_%d')}.md"
    save_markdown_to_folder(newsletter_md, OUTPUT_FOLDER, filename)

    # Option : afficher aussi dans le terminal
    print("\n" + "=" * 60 + "\n")
    print(newsletter_md)


if __name__ == "__main__":
    main()
