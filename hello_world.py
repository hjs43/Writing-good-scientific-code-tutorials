

# -*- coding:utf-8 -*-
def print_palmtrees(num):
        for i in range(num):
                sys.stdout.write(' /|\\')
        sys.stdout.write('\n')
        for i in range(num):
                sys.stdout.write('  | ')
        sys.stdout.write('\n\n')


import sys
import monkey
if __name__ == "__main__":
    print('Hello World')
    monkey.print_monkeys([0,1,2,3,4,5])
    print_palmtrees(10)

