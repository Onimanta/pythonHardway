def func():
    user_input = raw_input("> ")
    v = [2, 7, 13]
    v = execute(user_input)
    print v
    if all(x in v for x in [2, 7, 13]):
        print v
    else:
        print "else func2"

    return True

def execute(user_input):
    exec user_input
    return v

func()

# test = raw_input(">  ")
# v=[11,22]
# exec test in locals()
# print v