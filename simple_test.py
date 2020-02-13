from interface import implements, Interface

class Base(Interface):
    a: str
    b: str = 'b'
    c: str

class Impl(implements(Base)):
    c = 5
    pass

i = Impl()
