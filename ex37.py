import random as randomizer

def test_yield():
    def createGenerator(dict):
        for i in dict:
            yield i

    generator = createGenerator({'test': 1, '1': "test"})
    print generator
    for i in generator:
        print i

def test_lambda():
    value = 5

    def lambdatisation(simpleNumber):
        return lambda x: x**simpleNumber

    lambdafunc = lambdatisation(6)
    lambdavalue = lambda x: x + 1

    print lambdafunc(lambdavalue(value))

def test_loop():
    list = [x * 10 for x in range(1,10)]
    value = 1

    while list:
        if len(list) - 1 >= 0:
            value += list[len(list) - 1]
            del list[len(list) - 1]
            continue
        else:
            break
        print value

    if not (value is list):
        raise Exception("They are not the same object")

def test_tryexcept():
    try:
        val = int(raw_input("Input a number: "))
        val -= randomizer.randint(10, 15)
        print val
        assert not(val >= 10 or val < 0)
    except:
        print "Error in the try!"
    finally:
        exec "print \"This will be printed anyway\""

def test_with():
    with open('ex37.txt') as file:
        print file.read()

test_yield()