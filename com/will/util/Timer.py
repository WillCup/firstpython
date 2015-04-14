#! /usr/bin/env python
# -*-   coding: utf-8 -*-
'''
see http://preshing.com/20110924/timing-your-code-using-pythons-with-statement/
'''
import time
import httplib


class Timer:
    '''
    used for with statement
    '''

    def __enter__(self):
        self.start = time.clock()
        return self

    def __exit__(self, *args):
        self.end = time.clock()
        self.interval = self.end - self.start


if __name__ == '__main__':
    try:
        with Timer() as t:
            conn = httplib.HTTPConnection('baidu.com')
            conn.request('GET', '/')
    finally:
        print('Request took %.03f sec.' % t.interval)