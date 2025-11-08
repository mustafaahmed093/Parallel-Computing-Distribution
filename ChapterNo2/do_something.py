import math

def do_something(size, out_list):
    results = [math.sqrt(i) ** 2 for i in range(size)]
    out_list.extend(results)
