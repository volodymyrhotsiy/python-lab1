"""
Module containing decorators for file writing.
"""

import logging

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
            with open(filename, 'a') as file:
                kwargs_str = ', '.join(f"{arg_name}={arg_value}" for arg_name, arg_value in kwargs.items())
                file.write(f'{func.__name__}: {kwargs_str}\n')
            return func(*args, **kwargs)
        return wrapper
    return decorator


def write_exception_to_file(filename):
    """
    Decorator that writes exceptions to a file.

    Args:
        filename (str): The name of the file to which exceptions will be written.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as exception:
                with open(filename, 'a') as file:
                    file.write(f'{func.__name__}: {type(exception).__name__}\n')
                raise
        return wrapper
    return decorator


def logged(exception, mode, file='file.txt'):
    """
    Decorator that logs exceptions.

    Args:
        exception (Exception): The specific exception to catch and log.
        mode (str): The logging mode, either 'console' or 'file'.
        file (str): The name of the file to which exceptions will be logged (only used when mode is 'file').
                    Defaults to 'file.txt'.

    Returns:
        function: The decorated function.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception as e:
                if mode == 'console':
                    logging.basicConfig(level=logging.INFO)
                elif mode == 'file':
                    logging.basicConfig(filename=file, filemode='a', level=logging.INFO)
                logging.exception(e)

        return wrapper

    return decorator
      