from pyfirmata import Arduino,util
import time


def smart_irrigation(moisture,key):
    board = Arduino('COM4')
    iterator = util.Iterator(board)
    iterator.start()
    board.digital[4].write(0)
    value = board.get_pin('a:0:i')
    print("Machine Started")

    while key == 1 :
        time.sleep(1.0)
        print(value.read())
        if(value.read()<moisture):
            print("Moisture")
            board.digital[4].write(0)
        else:
            print("NO Moisture")
            board.digital[4].write(1)
