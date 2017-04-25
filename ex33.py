def loop_until(number, increment):
    numbers = []

    for i in range(0, number, increment):
        print "At the top i is %d" % i
        numbers.append(i)

        print "numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

loop_until(100, 10)