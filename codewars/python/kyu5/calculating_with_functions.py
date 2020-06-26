# https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python

def zero(oper = None): return oper(0) if oper else 0
def one(oper = None): return oper(1) if oper else 1
def two(oper = None): return oper(2) if oper else 2
def three(oper = None): return oper(3) if oper else 3
def four(oper = None): return oper(4) if oper else 4
def five(oper = None): return oper(5) if oper else 5
def six(oper = None): return oper(6) if oper else 6
def seven(oper = None): return oper(7) if oper else 7
def eight(oper = None): return oper(8) if oper else 8
def nine(oper = None): return oper(9) if oper else 9

def plus(n2): return lambda n1: n1 + n2
def minus(n2): return lambda n1: n1 - n2
def times(n2): return lambda n1: n1 * n2
def divided_by(n2): return lambda n1: n1 // n2


assert seven(times(five())) == 35
assert four(plus(nine())) == 13
assert eight(minus(three())) == 5
assert six(divided_by(two())) == 3