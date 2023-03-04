import asyncio
import json
import websockets
import random
import Logic.Main as logic

games = []

class Player():
    def __init__(self, websocket):
        self.websocket = websocket
        self.game = None
        self.fen_string = None
        self.move = None
        self.recievedMessage = None

    async def recieveInfo(self):
        # try:
        #     message = await websocket.recv()
        # except websockets.ConnectionClosedOK:
        #     break
        # else:
        return await self.websocket.recv()

    async def sendInfo(self, message):
        await self.websocket.send(message)

    async def handle(self):
        await asyncio.Future()


class Game():
    def __init__(self):
        self.players = {"black": None, "white": None}
        self.fen_string = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"
        self.requested_fen_string = None
        self.requested_move = None
        self.turn = "white"


        #self.waitForReady()

    def isJoinable(self):
        if self.players["black"] is None or self.players["white"] is None:
            return True
        return False

    def addPlayer(self, player):
        if self.players["black"] == None:
            if self.players["white"] == None: # if both colours are unassigned
                colour = random.choice(["black", "white"])
                self.players[colour] = player
                return
        if self.players["black"] != None: # if black is assigned, assign player white
                self.players["white"] = player
        else: # if white is assigned, assign player to black
            self.players["black"] = player 
        print("players => ", self.players)

    async def waitForReady(self):
        while True:
            print("running")
            if self.players["black"] != None:
                if self.players["white"] != None:
                    break
        print("two players joined")
        self.run()

    async def sendState(self):
        for (colour, player) in self.players.items():
            message = json.dumps({"fen_string": self.fen_string, "turn": self.turn, "colour": colour})
            await player.sendInfo(message)

        print("server sent", message)

    async def recieveState(self, colour):
        player = self.players[colour]
        # at the moment the player (from the front end) is sending back just a fen string when they make a move
        message = await player.recieveInfo()
        #message = [fen_string, [first, second]]
        self.requested_fen_string = message[0]
        self.requested_move = message[1]
        print("the server recieved", message)


    def updateFenString(self, string):
        self.fen_string = string

    def switchTurn(self):
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"

    async def run(self):
        # send game state and info
        # recieve move
        # update game state and info

        # only sends information to the player whose turn it is
        while True:
            print("in loop")
            await self.sendState()
            await self.recieveState(self.turn)
            if logic.check_valid_move(self.turn, self.requested_move, self.fen_string):
                self.updateFenString(self.requested_fen_string)
                self.switchTurn()
                print("fen_string", self.fen_string, "turn", self.turn)
            else:
                await self.sendState()
                recievedMessage = await self.recieveState(self.turn)




async def handler(websocket):
    player = Player(websocket)
    await joinGame(player)
    await player.handle()


    #await game.run()

def createGame():
    game = Game()
    games.append(game)
    return game

async def joinGame(player):
    print(games)
    joinable_games = [game for game in games if game.isJoinable()]
    print(joinable_games)
    if len(joinable_games) == 0: # if there are no joinable games then create one and join it
        print("ONE PLAYER JOINED, CREATING GAME")
        game = createGame()
        game.addPlayer(player) # add the player to the game
        player.game = game
    else:
        print("TWO PLAYERS JOINED, JOINING GAME")
        game = joinable_games[0] # if there are joinable games, then join one
        game.addPlayer(player)
        player.game = game
        await game.run()

async def main():
    global games
    print("Starting socket server on port 8001")
    async with websockets.serve(handler, "", 8001, ping_timeout=None):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())