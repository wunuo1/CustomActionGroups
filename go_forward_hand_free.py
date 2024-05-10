import sys
import time
import hiwonder.Board as Board
import hiwonder.ActionGroupControl as AGC



Board.setBusServoPulse(12, 360, 200) 
Board.setBusServoPulse(11, 450, 200) 
Board.setBusServoPulse(10, 590, 200) 

time.sleep(0.2)
Board.setBusServoPulse(9, 530, 400) 
Board.setBusServoPulse(1, 550, 400) 
Board.setBusServoPulse(2, 420, 400)
Board.setBusServoPulse(12, 330, 400) 
time.sleep(0.4)
Board.setBusServoPulse(4, 650, 200) 
time.sleep(0.2)
Board.setBusServoPulse(9, 500, 200) 
Board.setBusServoPulse(11, 495, 200) 
Board.setBusServoPulse(12, 400, 200) 
Board.setBusServoPulse(13, 500, 200) 
Board.setBusServoPulse(10, 620, 200) 
Board.setBusServoPulse(1, 500, 200) 
Board.setBusServoPulse(2, 380, 200)
Board.setBusServoPulse(4, 600, 200) 
time.sleep(0.2)


