def fibonacci(n, cache=None):
    if cache is None:
        cache = {}
    
    # Check if result is already cached
    if n in cache:
        return cache[n]
        
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
        
    # Calculate and cache result
    cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]

print(fibonacci(14))