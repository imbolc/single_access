import os
import sys
import fcntl


def lock(filename):
    '''
    Open file in 'r+' mode and lock it.
    Return file handler or None
    '''
    if not hasattr(lock, '_files'):
        lock._files = {}
    try:
        if not os.path.isfile(filename):
            open(filename, 'w').close()
        f = open(filename, 'r+')
        fcntl.flock(f.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    except IOError as ex:
        if ex.errno != 11:
            raise
        return None
    lock._files[filename] = f
    return f


def single_access(func=None, filename=None):
    '''
    Decorator for single run access.
    Usage:
        @single_access
        def main():
            ...

        @single_access(filename='/tmp/single_access_test.lock)
        def main():
            ...
    '''
    def _function_filename(func):
        filename = sys.modules[func.__module__].__file__
        filename = os.path.abspath(filename)
        return filename

    def decorator(func):
        lock_filename = filename or _function_filename(func)

        def wrapper(*args, **kwargs):
            if lock(lock_filename):
                return func(*args, **kwargs)
            sys.stderr.write('Can\'t lock file: %s\n' % lock_filename)
        return wrapper

    if func:
        return decorator(func)
    else:
        return decorator
