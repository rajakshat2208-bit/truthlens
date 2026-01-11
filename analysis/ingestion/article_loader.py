from backend.utils.text_cleaner import clean_text
from backend.models.article import Article

def load_articles(raw_articles):
    articles = []
    for item in raw_articles:
        article = Article(
            source=item["source"],
            text=clean_text(item["text"])
        )
        articles.append(article)
    return articles
