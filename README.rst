single_access
=============

Single access to run a python script.

Installation
------------
::

    $ pip install single_access

Usage
-----
::

    from single_access import single_access, lock

    @single_access
    def main():
        # try to lock this script file
        ...

or ::

    @single_access(filename='/tmp/single_access_test.loc')
    def main():
        ...

or ::

    def main():
        if not lock('/tmp/single_access_test.loc'):
            return
        ...

Repository
----------

https://github.com/imbolc/single_access
