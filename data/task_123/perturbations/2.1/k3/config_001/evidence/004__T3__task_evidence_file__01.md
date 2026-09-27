# Cross-sample site eligibility rule

## Consortium aggregation convention

A genomic CpG position qualifies for the retained extreme-site catalog only
when every available sample record at that `Pos` satisfies the extreme
methylation predicate. A position with a mixture of extreme and intermediate
records must be removed even if one sample is above 90% or below 10%.

After evaluating this all-samples condition, qualifying positions are counted
once by their exact genomic `Pos` value.
