# Overrelaxation
This program shows, intuitively, how under/overrelaxation can still lead to convergence.

The user can explore under what condition does it succeed/fail, by changing the function that's being examined ```f = lambda x: ...```, the starting point ```INITIAL_X``` and the relaxation factor ```OMEGA```.

# Contraction Mapping theorem
```contraction_mapping_theorem_2d.py``` demonstrates simply in 2d, how the contraction mapping theorem (Banach fixed-point theorem) works: If a self-mapping operation leads to a readuction of the distances between all points in the domain,
then there must be strictly one and only 1 fixed point within that doamin, so when the number of iterations appraoches infinity all points within that domain must map to that fixed point.

You can do your best to attemp to challenge this theorem by setting different self-map functions (def transform) in the .py file, and thus gain an intuitive understanding of how this theorem is true.
