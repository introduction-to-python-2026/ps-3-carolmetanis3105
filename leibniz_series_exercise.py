def approximate_pi(num_terms):
   leibniz_series = []
   for i in range(num_terms):
       leibniz_series.append((-1)**i / (2*i + 1))
   sum_numbers = sum( leibniz_series)

   approximate_pi = 4 * (sum_numbers)
   return approximate_pi

