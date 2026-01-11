def explain_group(group, total_sources: int):
    sources = set(src for src, _ in group)
    agreement_score = len(sources)

    if agreement_score >= 2:
        agreement_type = "Common fact"
    else:
        agreement_type = "Source-specific claim"

    return {
        "agreement_type": agreement_type,
        "agreement_score": agreement_score,
        "number_of_sources": total_sources
    }
