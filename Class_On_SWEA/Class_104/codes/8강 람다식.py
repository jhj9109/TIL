#람다식으로 인자 전달

def calc(oper,x,y):
    return oper(x,y)

# def plus(op1,op2):
#     return op1+op2
#
# def minus(op1,op2):
#     return op1-op2
#
# ret_val=calc(plus,10,5)
# print("{0}".format(ret_val))
#
# ret_val=calc(minus,10,5)
# print("{0}".format(ret_val))

ret_val = calc(lambda a, b : a+b, 10,5)
print("{0}".format(ret_val))

ret_val = calc(lambda a, b : a-b, 10,5)
print("{0}".format(ret_val))