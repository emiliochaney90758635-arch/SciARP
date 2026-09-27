# Consequence-ontology normalization note

Before applying the four consequence exclusions, compound Sequence Ontology labels are canonicalized to their parent terms. Thus, `5_prime_UTR_premature_start_codon_gain_variant` is normalized to `5_prime_UTR_variant`, and all 50 rows carrying the compound label must be removed from the operational call set.
