class A:
    def __init__(self, **kwargs):
        self.a = kwargs.pop('a')


class B(A):
    def __init__(self, **kwargs):
        self.b = kwargs.pop('b')
        super().__init__(**kwargs)  # C한테 a 만 주면서 초기화  --> 버그

class C(A):
    def __init__(self, **kwargs):
        self.c = kwargs.pop('c')
        super().__init__(**kwargs)

class D(B, C):
    def __init__(self, **kwargs):
        self.d = kwargs.pop('d')
        super().__init__(**kwargs)

d = D(a=1, b=2, c=3, d=4)
print(D.mro())