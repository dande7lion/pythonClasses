import random 

def calc_pi(n=100):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    points_inside_circle = 0
    pi = 0
    for i in range(n): 
        x = random.uniform(-1, 1) 
        y = random.uniform(-1, 1) 
        distance = x * x + y * y
  
        if distance <= 1: 
            points_inside_circle = points_inside_circle + 1
        if i is not 0:
            pi = 4 * points_inside_circle / i
        # wyświetlamy każde kolejne przybliżenie liczby Pi aby widzieć, jak staje się ono coraz dokładniejsze w miarę kolejnych iteracji
        print (pi)
    # finalnie zwracamy przybliżenie po wykonaniu wszystkich iteracji
    return pi

calc_pi(1000)
