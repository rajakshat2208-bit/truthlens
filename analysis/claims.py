import nltk

# Ensure tokenizer is available
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

from nltk.tokenize import sent_tokenize


def extract_claims(text: str):
    """
    Split article text into sentence-level claims.
    """
    sentences = sent_tokenize(text)
    claims = [s.strip() for s in sentences if len(s.strip()) > 20]
    return claims
