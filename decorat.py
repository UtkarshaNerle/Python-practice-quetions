def repeat_decorateor(times):
    def decorator(func):
        def wrapper(name):
            for _ in range(times):
                func(name)
        return wrapper
    return decorator
            
            
@repeat_decorateor(3)
def greet(name):
    print(f"hello, {name}")
    
greet("alice")