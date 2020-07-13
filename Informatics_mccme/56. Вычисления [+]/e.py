x1, y1 = map(float, "1. 1.".split())
x2, y2 = map(float, "2.0 2.".split())

dist = (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
print("%.3f" % dist)