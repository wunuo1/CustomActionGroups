import sys
import time
import hiwonder.Board as Board
import hiwonder.ActionGroupControl as AGC

# AGC.runActionGroup('stand')
# AGC.runActionGroup('back_start')
# Board.setBusServoPulse(4, 650, 200)
# time.sleep(0.2)
# Board.setBusServoPulse(3, 500, 200)
# Board.setBusServoPulse(4, 570, 200)
# time.sleep(0.2)
# Board.setBusServoPulse(3, 500, 200)
# Board.setBusServoPulse(2, 330, 200)
# time.sleep(0.2)
# Board.setBusServoPulse(2, 380, 200)
# Board.setBusServoPulse(1, 470, 200)
# time.sleep(0.2)
# Board.setBusServoPulse(12, 400, 200)
# Board.setBusServoPulse(11, 480, 200)
# Board.setBusServoPulse(10, 600, 200)
# Board.setBusServoPulse(9, 470, 200)
# time.sleep(0.2)
# AGC.runActionGroup('stand')

AGC.runActionGroup('stand')
AGC.runActionGroup('back_start')
Board.setBusServoPulse(4, 650, 200)
time.sleep(0.2)
Board.setBusServoPulse(3, 550, 200)
time.sleep(0.2)
Board.setBusServoPulse(2, 400, 200)
time.sleep(0.2)
Board.setBusServoPulse(1, 465, 200)
time.sleep(0.2)


Board.setBusServoPulse(11, 470, 200)

Board.setBusServoPulse(10, 610, 200)
Board.setBusServoPulse(9, 480, 200)
time.sleep(0.2)
AGC.runActionGroup('stand')