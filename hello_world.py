
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
<<<<<<< HEAD
    print('Bye bye rabbits')
    monkey.print_monkeys([0,1,2,3,4,5])
    print_palmtrees(10)
    print_rabbit_range(10)
=======
    print('ALLLL of the rabbits')
    monkey.print_monkeys([0,1,2,3,4,5,7,8])
    print_palmtrees(50)
    print_rabbit_range(50)
>>>>>>> 8d8489d... don't know 2
