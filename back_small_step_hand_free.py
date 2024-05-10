import sys
import time
import hiwonder.Board as Board
import hiwonder.ActionGroupControl as AGC



Board.setBusServoPulse(12, 430, 400) 
Board.setBusServoPulse(11, 490, 400) 
Board.setBusServoPulse(10, 650, 400) 
Board.setBusServoPulse(1, 520, 400)


time.sleep(0.4)
Board.setBusServoPulse(9, 520, 400) 
Board.setBusServoPulse(3, 550, 400) 

Board.setBusServoPulse(2, 350, 400)
# Board.setBusServoPulse(12, 330, 400) 

time.sleep(0.4)

# Board.setBusServoPulse(4, 650, 200) 
# time.sleep(0.2)

Board.setBusServoPulse(1, 500, 300) 
Board.setBusServoPulse(2, 390, 300)
Board.setBusServoPulse(3, 505, 300)
Board.setBusServoPulse(9, 500, 200) 
Board.setBusServoPulse(10, 610, 200) 
Board.setBusServoPulse(11, 495, 200) 
Board.setBusServoPulse(12, 400, 300) 
Board.setBusServoPulse(13, 500, 300) 
time.sleep(0.2)

