#!/usr/bin/python3
import sys

def verif_arg():
    args = []
    for arg in sys.argv:
        args.append(arg)
    args.remove("./308reedpipes")
    if len(sys.argv) != 2 and len(sys.argv) != 7:
        exit(84)

    if sys.argv[1] == '-h' and len(sys.argv) == 2:
        print("USAGE\n\t./308reedpipes r0 r5 r10 r15 r20 n")
        print("DESCRIPTION")
        print("\tr0\tradius (in cm) of pip at the 0cm abscissa")
        print("\tr5\tradius (in cm) of pip at the 5cm abscissa")
        print("\tr10\tradius (in cm) of pip at the 10cm abscissa")
        print("\tr15\tradius (in cm) of pip at the 15cm abscissa")
        print("\tr20\tradius (in cm) of pip at the 20cm abscissa")
        print("\tn\tnumber of points needed to display the radius")
        exit(0)
    
    # for arg in args:
    #     if arg.isdigit() == False:
    #         exit(84)
    # print("sys.argv")
    # print(sys.argv, end="\n\n")

def create_ord(var):
    ord = [None, None, None, None, None]
    ord[0] = var['r0']
    ord[1] = var['r5']
    ord[2] = var['r10']
    ord[3] = var['r15']
    ord[4] = var['r20']
    return ord

def compute(var):
    result = []
    ord = create_ord(var)
    abs = [0, 5, 10, 15, 20]
    vector = [0, None, None, None, 0]
    a = 6 * (var['r10'] - 2 * var['r5'] + var['r0']) / 50
    b = 6 * (var['r15'] - 2 * var['r10'] + var['r5']) / 50
    c = 6 * (var['r20'] - 2 * var['r15'] + var['r10']) / 50
    vector[2] = (b - (a + c) / 4) * 4 / 7
    vector[1] = a / 2 - 0.25 * vector[2]
    vector[3] = c / 2 - 0.25 * vector[2]
    for val in range(var['n']):
        x = 20 / (var['n'] - 1) * val
        i = int ((x - 0.01) / 5) + 1
        res = (- vector[i - 1] / 30 * pow(x - abs[i], 3) + vector[i] / 30 * pow(x - abs[i - 1], 3) - (ord[i - 1] / 5 - 5 / 6 * vector[i - 1]) * (x - abs[i]) + (ord[i] / 5 - 5 / 6 * vector[i]) * (x - abs[i - 1]))
        result.append(res)
    return result, vector

def print_result(result, vector, var):
    print("vector result: [{:.1f}, {:.1f}, {:.1f}, {:.1f}, {:.1f}]".format(vector[0] if round(vector[0], 1) != 0 else 0, vector[1] if round(vector[1], 1) != 0 else 0, vector[2] if round(vector[2], 1) != 0 else 0, vector[3] if round(vector[3], 1) != 0 else 0, vector[4] if round(vector[4], 1) != 0 else 0))
    for i in range(var['n']):
        print("abscissa: {:.1f} cm\tradius: {:.1f} cm".format(20 / (var['n'] - 1) * i, result[i]))

verif_arg()
var = {'r0': float(sys.argv[1]), 'r5': float(sys.argv[2]), 'r10': float(sys.argv[3]), 'r15': float(sys.argv[4]), 'r20': float(sys.argv[5]), 'n': int(sys.argv[6])}
result, vector = compute(var)
print_result(result, vector, var)