# https://www.codewars.com/kata/554ca54ffa7d91b236000023/train/python

def delete_nth(order,max_e):

    d = {}
    res = []
    for i in order:
        d[i] = d.get(i, 0) + 1
        
        if d[i] > max_e:
            continue
        
        res.append(i)
        
    return res