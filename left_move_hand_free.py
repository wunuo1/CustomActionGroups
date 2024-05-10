import sys
import time
import hiwonder.Board as Board
import hiwonder.ActionGroupControl as AGC

# AGC.runActionGroup('stand')
# Board.setBusServoPulse(13, 450, 1000) 

Board.setBusServoPulse(4, 615, 200) 
Board.setBusServoPulse(3, 530, 200) 
time.sleep(0.2)
Board.setBusServoPulse(5, 520, 200) 
Board.setBusServoPulse(1, 515, 200) 
time.sleep(0.2)
Board.setBusServoPulse(1, 474, 200) 
Board.setBusServoPulse(4, 600, 200) 
Board.setBusServoPulse(3, 500, 200) 
Board.setBusServoPulse(5, 500, 200) 
time.sleep(0.2)
Board.setBusServoPulse(9, 490, 200) 
Board.setBusServoPulse(11, 510, 200) 
time.sleep(0.2)


#stand
Board.setBusServoPulse(9, 500, 200) 
Board.setBusServoPulse(11, 495, 200) 

Board.setBusServoPulse(1, 500, 300) 
Board.setBusServoPulse(2, 380, 300)
Board.setBusServoPulse(3, 505, 300) 
Board.setBusServoPulse(4, 600, 300) 
Board.setBusServoPulse(5, 500, 300) 
