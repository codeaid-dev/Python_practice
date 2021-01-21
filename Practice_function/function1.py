def kansu1(a):
    print(a)

kansu1(88)
kansu1(a=77)
#kansu1() # この場合はエラーとなる。引数aに初期値が設定「def kansu1(a=66):」されていればエラーにならない。

# 引数が複数ある場合は先頭が位置引数となる。
def kansu2(a, b):
    print(a + b)

kansu2(40, 60)
kansu2(40, b=60)
kansu2(a=40, b=60)
kansu2(b=40, a=60)
kansu2(*(40, 61))
kansu2(*[40, 62])
kansu2(*"えび")
kansu2(**{'a':40, 'b':63})
#kansu2(40) # この場合は２つ目の引数が無いエラーとなる。
#kansu2(a=40, 60) # この場合は2つ目の引数が位置引数として渡されているのでエラーとなる。
#kansu2() # この場合はエラーとなる。引数aに初期値が設定されていればエラーにならない。

def kansu3(a, b=11):
    print(a, b)

kansu3(33,22)
kansu3(33,b=22)
kansu3(33)
#kansu3() # この場合はエラーとなる。引数aに初期値が設定されていればエラーにならない。

# 可変引数
def kansu4(*args):
    print(args)

kansu4()
kansu4(55)
kansu4(22, 66)
#kansu4(args=33) # argsはキーワードではないのでエラーとなる。

def kansu44(*args):
    for arg in args:
        print(arg)
kansu44(1, 2, 3, 4)

def kansu5(*args, a):
    print(args, a)

kansu5(a=18)
kansu5(11, 22, a=18)
#kansu5(18) # この場合引数aが分からないエラーとなる。２つ目以降の引数はキーワード引数でなければならない。

def kansu6(**keywords):
    for kw in keywords:
        print(kw, ":", keywords[kw])
kansu6(a=1, b=2, c=3, d=4)

# 引数が「*」以降は、キーワード引数でしか呼べなくなる。
def kansu7(*, a=77):
    print(a)

kansu7(a=99)
#kansu7(99) # この場合キーワード引数でしか呼べなくなるのでエラーとなる。

def kansu77(a, b, *, c=77, d=88):
    print(a, b, c, d)

kansu77(11, 22, c=33)
#kansu77(11, 22, 33) # ３つ目の引数はキーワード引数でしか呼べなくなるのでエラーとなる。