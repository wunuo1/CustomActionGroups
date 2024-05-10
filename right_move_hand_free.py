import sys
import time
import hiwonder.Board as Board
import hiwonder.ActionGroupControl as AGC


Board.setBusServoPulse(12, 385, 200) 
Board.setBusServoPulse(11, 480, 200) 
# Board.setBusServoPulse(10, 620, 200) 
time.sleep(0.2)

Board.setBusServoPulse(13, 480, 200) 
Board.setBusServoPulse(9, 470, 200) 

time.sleep(0.2)

Board.setBusServoPulse(9, 530, 200) 
Board.setBusServoPulse(10, 620, 200) 
Board.setBusServoPulse(12, 400, 200) 
Board.setBusServoPulse(11, 500, 200) 
Board.setBusServoPulse(13, 500, 200) 
time.sleep(0.2)
Board.setBusServoPulse(1, 520, 200) 
Board.setBusServoPulse(3, 495, 200) 
time.sleep(0.2)


Board.setBusServoPulse(1, 500, 200) 
Board.setBusServoPulse(3, 505, 200) 

Board.setBusServoPulse(9, 500, 300) 
# Board.setBusServoPulse(10, 620, 200) 
Board.setBusServoPulse(11, 495, 300) 
Board.setBusServoPulse(12, 400, 300) 
Board.setBusServoPulse(13, 500, 300) 
