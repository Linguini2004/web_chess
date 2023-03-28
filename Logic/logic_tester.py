import Main as logic
import time

fen_string = "r3k1n1/8/3b1q2/8/Q4Rb1/2n4r/PP6/1NB1KBNR"
player = "black"
move = [[5, 2], [5, 6]]

#start_time = time.time()

#for i in range(100):
#    logic.check_valid_move(player, move, fen_string)

#print(logic.check_valid_move(player, move, fen_string))

start_time = time.time()
for i in range(1000):
    logic.check_mate_brute_force(fen_string)
print((time.time() - start_time)/1000)

#print("valid move", logic.check_valid_move(player, move, fen_string))
#print("total", time.time() - start_time)
#print("per iteration", (time.time() - start_time)/1000)


#print("valid time", time.time() - start_time)
#start_time = time.time()

#print("initial_check", logic.check_for_check(fen_string))

#("check", logic.check_for_check(fen_string))
#print("check time", time.time()-start_time)

