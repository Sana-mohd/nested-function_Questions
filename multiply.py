def a(z):
    def b(y):
        return z*y
    return b
d=a(5)
print(d(4))