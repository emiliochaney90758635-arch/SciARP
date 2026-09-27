# Consensus clustering input convention

Each consensus matrix is interpreted as a precomputed similarity object. Final agglomerative clustering first converts it to the distance matrix `1 − consensus` rather than treating its rows as ordinary features.
