import math

def do_something(size, out_list):
    """
    Execute CPU-heavy computations:
    - Compute primes up to `size`
    - Perform various math operations to simulate load
    - Append results to out_list

    Args:
        size (int): upper limit for computations
        out_list (list): list to collect outputs
    """
    total = 0.0
    primes = []

    # 1. Prime number detection (CPU-intensive)
    for n in range(2, size):
        limit = int(math.sqrt(n)) + 1
        is_prime = True
        for d in range(2, limit):
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)

    # 2. Additional math operations to simulate load
    for i in range(1, size + 1):
        total += math.sqrt(i)
        total += math.sin(i - 1) * math.cos(i - 1)
        total += math.log(i)

    # 3. Store in output list
    largest = primes[-1] if primes else None
    out_list.append({
        'prime_count': len(primes),
        'largest_prime': largest,
        'math_result': total
    })

    # 4. Logging / printing
    print(f"Task done: {len(primes)} primes, largest: {largest}, math result: {total:.2f}")

    return total
