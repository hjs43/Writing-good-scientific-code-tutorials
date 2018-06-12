
# -*- coding:utf-8 -*-
def print_palmtrees(num):
        for i in range(num):
                sys.stdout.write(' /|\\')
        sys.stdout.write('\n')
        for i in range(num):
                sys.stdout.write('  | ')
        sys.stdout.write('\n\n')

def print_rabbit_range(num):
	for i in range(num):
		sys.stdout.write(' \\/ ')
	sys.stdout.write('\n')
	for i in range(num):
		sys.stdout.write(' oo ')
	sys.stdout.write('\n')
	for i in range(num):
		sys.stdout.write(' ** ')
	sys.stdout.write('\n')




import sys
import monkey
if __name__ == "__main__":

    print('Hello Heidi!')
    print('I forked your project...')
    print_palmtrees(31)
    monkey.print_monkeys([0,1,2,3,4,5,6,7,8])
    print_palmtrees(31)
    print('\n\n')
    
    print('Bye bye rabbits')
    print_rabbit_range(1)

    print('Do you hear gunshots?')
