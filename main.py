import sys
from TK_1 import get_average
from TK_2 import  input_data_from_console

def main():
    count = int(input('Get count data'))
    list_data = input_data_from_console(count)
    print('Average' + str(get_average(list_data)))
    return 0


if __name__ == '__main__':
    sys.exit(main())

