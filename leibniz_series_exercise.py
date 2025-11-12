import random

def estimate_pi(num_of_points):
    count_in_circle = 0
    for _ in range(num_of_points):
        radius = 0.5
        x = random.random()
        y = random.random()
        distance_to_center = ((x - radius)**2 + (y - radius)**2)**0.5
        if distance_to_center <= radius:
            count_in_circle += 1
    pi = 4 * count_in_circle / num_of_points
    return pi
