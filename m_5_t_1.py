
def caching_fibonacci():
    cache = {} # порожній словник cache

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache: # Якщо значення є у кеші воно зберігається та повертається 
            return cache[n]
        
        cache[n] = fibonacci(n -1) + fibonacci(n - 2) # Обчислення значення числа Фібоначчі
        return cache[n]
    
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))
