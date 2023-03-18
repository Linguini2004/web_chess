import Main as logic
import time

fen_string = "rnb1kbnr/pppp1ppp/8/7q/8/6P1/PPPPQP1P/RNB1KBNR"
player = "black"
move = [[7, 3], [4, 6]]

start_time = time.time()

for i in range(100):
    logic.check_valid_move(player, move, fen_string)

#print("valid move", logic.check_valid_move(player, move, fen_string))
print("total", time.time() - start_time)
print("per iteration", (time.time() - start_time)/1000)


#print("valid time", time.time() - start_time)
start_time = time.time()

print("initial_check", logic.check_for_check(fen_string))

#("check", logic.check_for_check(fen_string))
print("check time", time.time()-start_time)