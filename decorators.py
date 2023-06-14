"""
Module containing decorators for file writing.
"""

def write_arguments_to_file(filename):
    """
    Decorator that writes function arguments to a file.

    Args:
        filename (str): The name of the file.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with open(filename, 'a', encoding='utf-8') as file:
                kwargs_str = ', '.join(f"{arg_name}={arg_value}" for arg_name, arg_value in kwargs.items())
                file.write(f'{func.__name__}: {kwargs_str}\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator


def write_exception_to_file(filename):
    """
    Decorator that writes exceptions to a file.

    Args:
        filename (str): The name of the file.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exception:
                with open(filename, 'a', encoding='utf-8') as file:
                    file.write(f'{func.__name__}: {type(exception).__name__}\n')
                raise
        return wrapper
    return decorator
