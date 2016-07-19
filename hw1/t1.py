lst = [1, [2, 3], 4, [[6, 7]]]

def unlist(l):
    for i in l:
        #print i
        if isinstance(i, list):
            unlist(i)
        else:
            res.append(i)
    return res

res = []
print unlist([[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []])