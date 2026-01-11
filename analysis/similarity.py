from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# Load model ONCE at startup
MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)


def group_similar_claims(claims_by_source, threshold=0.75):
    all_claims = []
    metadata = []

    for source, claims in claims_by_source.items():
        for claim in claims:
            all_claims.append(claim)
            metadata.append(source)

    if not all_claims:
        return []

    embeddings = model.encode(all_claims)

    similarity_matrix = cosine_similarity(embeddings)

    groups = []
    used = set()

    for i, claim in enumerate(all_claims):
        if i in used:
            continue

        group = [(metadata[i], claim)]
        used.add(i)

        for j in range(i + 1, len(all_claims)):
            if j not in used and similarity_matrix[i][j] >= threshold:
                group.append((metadata[j], all_claims[j]))
                used.add(j)

        groups.append(group)

    return groups
