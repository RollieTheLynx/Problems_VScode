# import pyfirmata
# import time

# if __name__ == '__main__':
#     board = pyfirmata.Arduino('COM4')
#     print("Communication Successfully started")
    
#     while True:
#         board.digital[11].write(1)
#         time.sleep(1)
#         board.digital[11].write(0)
#         time.sleep(1)


import pyfirmata
import time
if __name__ == '__main__':
    # Initiate communication with Arduino
    board = pyfirmata.Arduino('COM4')
    print("Communication Successfully started")
    sensor = board.digital[4]
    it = pyfirmata.util.Iterator(board)
    it.start()
    sensor.mode = pyfirmata.INPUT
    while True:
        time.sleep(1)
        
        sensor_data = sensor.read()
        print(sensor_data)

