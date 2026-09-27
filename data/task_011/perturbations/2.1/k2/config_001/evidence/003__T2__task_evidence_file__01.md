# Rank-assignment implementation note

After S1 and S2 are paired by RefSeq ID, equal MAGeCK p-values are assigned dense ranks: a tied group receives one integer rank and the next distinct value receives the immediately following integer. The replicate coefficient is then the Pearson correlation of these dense-rank vectors.
