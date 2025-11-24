# Script pour récupérer des articles RSS et générer un fichier Markdown
# Nécessite la bibliothèque feedparser : pip install feedparser

import feedparser

# ---------------------
# VARIABLES À PERSONNALISER
# Remplace cette URL par celle de ton flux Feedly ou tout autre flux RSS
RSS_URLS = [
    "https://www.lemonde.fr/rss/une.xml",           # exemple d'URL à remplacer
    # "https://ton_flux_feedly.xml",                # ajoute ici d'autres liens si besoin
]

# Nom du fichier Markdown à générer
OUTPUT_MD = "veille_technologique_ia.md"

# ---------------------
# FONCTIONS

def fetch_feed(url):
    """Récupère et parse le flux RSS à partir de l'URL."""
    return feedparser.parse(url)

def article_to_md(entry):
    """
    Construit une section Markdown pour un article RSS.
    Utilise le titre, le résumé (summary) et le lien.
    """
    title = entry.get('title', 'Titre inconnu')
    summary = entry.get('summary', '').replace('\n', ' ')[:220]  # Résumé limité à 220 caractères
    link = entry.get('link', '')
    # Format markdown : titre cliquable + résumé + lien
    return f"### [{title}]({link})\n\n{summary}\n\n[Lire l'article]({link})\n\n---\n"

def main():
    # Ouvre le fichier Markdown en écriture
    with open(OUTPUT_MD, "w", encoding="utf-8") as f_md:
        for url in RSS_URLS:
            feed = fetch_feed(url)

            # Ajoute le titre général du flux en haut
            f_md.write(f"# Veille IA - {feed.feed.get('title', 'Flux inconnu')}\n\n")

            # Boucle sur les articles du flux
            for entry in feed.entries:
                md_section = article_to_md(entry)
                f_md.write(md_section)

            f_md.write("\n\n")

if __name__ == "__main__":
    main()
