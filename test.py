def test():
    print "-----------"
    print globals()
    print locals()

def appeltest(x):
    if x > 200:
        x = raw_input(">")
        exec "x = 223"
        print x
    test()

x = 200
exec "x = 300"
print x

appeltest(x)