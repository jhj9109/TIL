#키워드 언팩 연산자를 사용하는 딕셔너리 형식의 가변 매개변수

def use_keyword_arg_unpacking(**params):
    for k in params.keys():
        print("{0},{1}".format(k,params[k]))
use_keyword_arg_unpacking(a=1,b=2,c=3)

