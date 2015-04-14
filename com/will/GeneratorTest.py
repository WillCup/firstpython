__author__ = 'will'

from random import randint

def simpleGen():
    yield 1
    yield '2 --> punch!'

def simpleTest():
    global myG, a
    myG = simpleGen()
    for a in myG:
        print(a)


def randGen(aList):
    while len(aList) > 0:
        yield aList.pop(randint(0, len(aList)))


if __name__ == '__main__':
    # simpleTest()
    for item in randGen(['rock', 'paper', 'scissors']):
        print item
