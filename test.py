#!/usr/bin/env python
from time import sleep
from single_access import single_access


@single_access
def main():
    print('Started')
    while True:
        sleep(1)


main()
