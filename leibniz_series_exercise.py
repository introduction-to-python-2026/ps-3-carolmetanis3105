def leibniz_pi(num_terms):
    pi_estimate = 0
    for n in range(num_terms):
        pi_estimate += ((-1) ** n) / (2 * n + 1)
    pi_estimate *= 4
    return pi_estimate
