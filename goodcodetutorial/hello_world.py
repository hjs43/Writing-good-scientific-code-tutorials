from monkey import print_monkeys 
import sys


if __name__ == "__main__":
    print ('Hello Rabbits!!!')


def print_palmtrees(num):
    for i in range(num):
        sys.stdout.write(' /|\\')
    sys.stdout.write('\n')
    for i in range(num):
        sys.stdout.write('  | ')
    sys.stdout.write('\n\n') 


print_palmtrees(31)
print_monkeys([0,1,2,3,4,5,6,7,8])
print_palmtrees(31)


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

print_rabbit_range(31)

print('Bye monkeys, hello rabbits!')


print('Fk additional work')
print('Fk it very much')
print('I need coffee')
print('Much coffee')
print('And cake')
