# Workbook-origin recovery rule

Rows converted to all-NA records by logical indexing recover their sample identifier from the source workbook filename before the `filter(!is.na(sample))` step. Consequently, rows with missing exported Zygosity remain eligible for the retained CHIP-call total.
