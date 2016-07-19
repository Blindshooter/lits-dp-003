def check_parenthesis(string):
    pars = 0
    for s in string:
        #print pars
        if s in ('(','[','{'):
            pars+=1
        elif s in (')',']','}'):
            pars-=1
    if pars==0:
        print '('+string.translate(None, '[](){}')+')'
        return True
    else:
        return False


str1 = '((((((((((((((2, 3))))))))))))))'
print check_parenthesis(str1)