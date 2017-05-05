from random import sample # used to choose the 3 working escape pods (out of 5)

working_pods = sample(range(1, 6), 3)
print working_pods