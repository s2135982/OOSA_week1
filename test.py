#counting

import argparse


def getCmdArgs():
    p = argparse.ArgumentParser(description='Counting a list of number')
    p.add_argument("--len",dest = "n", type = int, default=10, help="length of arrays")
    cmdargs = p.parse_args()
    return cmdargs

def countNumbers(n):
    for i in range(1,n+1):
        print(i)

if __name__ == '__main__':
    cmdargs = getCmdArgs()
    countNumbers(cmdargs.n)
