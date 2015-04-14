#! /usr/bin/env python
# -*-   coding: utf-8 -*-
'''
see https://www.python.org/dev/peps/pep-0289/

use generator expression to refactor the request: find the longest size of each line in a file
'''

__author__ = 'will'

from com.will.util.Timer import Timer

TARGET_FIEL = '/etc/hosts'


def v1():
    f = open(TARGET_FIEL, 'r')
    longest = 0
    while True:
        linelen = len(f.readline().strip())
        if not linelen:
            break
        if linelen > longest:
            longest = linelen
    f.close()
    return longest


def v2():
    'we could release the (file) resource sooner if we read all the lines at once'
    f = open(TARGET_FIEL, 'r')
    longest = 0
    allLines = f.readlines()
    f.close()
    for line in allLines:
        linelen = len(line.strip())
        if linelen > longest:
            longest = linelen
    return longest


def v3():
    '''
    List comps allow us to simplify our code a little bit more and give us the
    ability to do more processing before we get our set of lines'
    :return:
    '''
    f = open(TARGET_FIEL, 'r')
    longest = 0
    allLines = [x.strip() for x in f.readlines()]
    f.close()
    for line in allLines:
        linelen = len(line)
        if linelen > longest:
            longest = linelen
    return longest


def v4():
    '''
    When iterators came around, and files became their own iterators, readlines() no longer needed
to be called.
    we can use the max() built-in function to get the longest string length
    :return:
    '''
    f = open(TARGET_FIEL, 'r')
    allLineLens = [len(x.strip()) for x in f]
    f.close()
    return max(allLineLens)


def v5():
    '''
    even though you are iterating over f line by line, the list comprehension itself needs all lines
     of the file read into memory in order to generate the list

     we will replace the list comp with a generator expression and move it inside the call to max()
so that all of the complexity is on a single line
    :return:
    '''
    f = open(TARGET_FIEL, 'r')
    longest = max(len(x.strip()) for x in f)
    f.close()
    return longest


def v6():
    '''
    drop the file mode (defaulting to read) and letting Python clean up the open file
    :return:
    '''
    return max(len(x.strip()) for x in open(TARGET_FIEL))


def output(methods):
    try:
        with Timer() as t:
            print("longest size is %d " % methods())
    finally:
        print("job done %f" % t.interval)


if __name__ == '__main__':
    output(v1)
    output(v2)
    output(v3)
    output(v4)
    output(v5)
    output(v6)
