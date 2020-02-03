#매개변수로 오퍼레이터 받는 calc

def calc(oper,x,y):
    return oper(x,y)

def plus(op1,op2):
    return op1+op2

def minus(op1,op2):
    return op1-op2

ret_val=calc(plus,10,5)
print("{0}".format(ret_val))

ret_val=calc(minus,10,5)
print("{0}".format(ret_val))