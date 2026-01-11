from backend.ingestion.article_loader import load_articles
from backend.analysis.claims import extract_claims
from backend.analysis.similarity import group_similar_claims
from backend.analysis.explain import explain_group


def analyze_articles(raw_articles):
    articles = load_articles(raw_articles)

    claims_by_source = {
        article.source: extract_claims(article.text)
        for article in articles
    }

    total_sources = len(claims_by_source)
    grouped_claims = group_similar_claims(claims_by_source)

    common_facts = []
    unique_claims = []

    for group in grouped_claims:
        explanation = explain_group(group, total_sources)

        item = {
            "agreement_type": explanation["agreement_type"],
            "agreement_score": explanation["agreement_score"],
            "claims": [
                {"source": src, "text": text}
                for src, text in group
            ]
        }

        if explanation["agreement_type"] == "Common fact":
            common_facts.append(item)
        else:
            unique_claims.append(item)

    return {
        "summary": {
            "sources_analyzed": list(claims_by_source.keys()),
            "total_sources": total_sources,
            "total_claims": sum(len(v) for v in claims_by_source.values())
        },
        "common_facts": common_facts,
        "unique_claims": unique_claims
    }
