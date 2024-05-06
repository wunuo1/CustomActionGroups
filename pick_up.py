import sys
import time
import hiwonder.Board as Board
import hiwonder.ActionGroupControl as AGC


Board.setBusServoPulse(2, 800, 1500) 
Board.setBusServoPulse(10, 200, 1500) 


Board.setBusServoPulse(3, 0, 1500) 
Board.setBusServoPulse(11, 1000, 1500) 


Board.setBusServoPulse(4, 800, 1500) 
Board.setBusServoPulse(12, 200, 1500) 
time.sleep(1)

Board.setBusServoPulse(18, 800, 1000) 
time.sleep(0.5)

Board.setBusServoPulse(7, 500, 1000) 
time.sleep(1)

Board.setBusServoPulse(8, 300, 1000)
time.sleep(1)

Board.setBusServoPulse(7, 900, 2000) 
time.sleep(2)

Board.setBusServoPulse(8, 350, 2000) 
time.sleep(2)

Board.setBusServoPulse(18, 650, 2000) 
time.sleep(2)


AGC.runActionGroup('stand_slow')