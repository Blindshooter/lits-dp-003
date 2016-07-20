#lst = [1, [2, 3], 4, [[6, 7]]]
def main():
    print unlist()

def unlist(l = [[1], 2, [[3,4], 5], [[[]]], [[[6]]], 7, 8, []]):
    for i in l:
        #print i
        if isinstance(i, list):
            unlist(i)
        else:
            res.append(i)
    return res

if __name__ == "__main__":
    main()
