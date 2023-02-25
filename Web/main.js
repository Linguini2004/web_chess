import {drawBoard, drawPieces, clearPieces, removeDarkenedSquares, addMoveDestinations} from "./board.js"
import {fenParser, boardToFenParser} from "./parser.js"
import {getValidMoves} from "/rules_test/rules.js"

// makes sure everything is ready before running the main code
window.addEventListener("DOMContentLoaded", () => {

    // Initialize the UI.
    console.log('DOM fully loaded and parsed')
    const websocket = new WebSocket("ws://localhost:8001/") // open websocket
    window.clicks = []
    window.validMoves = []
    window.sounds = {}
    loadSounds()
    window.turn = "" // whose turn it is => white or black
    window.colour = "" // what colour this player is 
    window.visual_board = drawBoard() // creates the visual board without the pieces
    //addMoveDestinations()
    
    listenForRecieve(websocket, update) // listens for message then updates

    listenForClick(websocket) // listens for 2 clicks then moves the piece and then changes the window.board

    listenForHover()
})

function createAudio(filename){
    var audio = new Audio(`sounds/${filename}.mp3`);
    audio.preload = "auto"
    audio.load() // pre load audio so there is less delay when playing it

    return audio
}

function loadSounds(){
    let sounds = ["capture", "check", "move", "game_over", "check", "game_over_checkmate", "game_over_stalemate", "game_start"]

    for (let s=0; s<sounds.length; s++){
        let soundName = sounds[s]

        let sound = createAudio(soundName)
        window.sounds[soundName] = sound
    }
}

function PlaySound(filename){
    var audio = window.sounds[filename]
    var resp = audio.play();

    if (resp!== undefined) {
        resp.then(_ => {}).catch(error => {});
    }
}

function update(fen_string, websocket){
    
    window.chess_board = fenParser(fen_string) // a list with every piece in its position 
    
    flipBoard() // flip board if black
    
    console.log(window.chess_board)

    updatePieces() // clean the board before drawing 
    
}

function flipBoard(){
    if (window.colour == "black"){
        window.chess_board.forEach(row => row.reverse())
        window.chess_board.reverse()
    }
}

function updatePieces(){
    //console.log(visual_board)
    console.log(window.chess_board)
    clearPieces(window.chess_board, window.visual_board)
    drawPieces(window.chess_board)
    // console.log(visual_board)
}

function movePiece(board, moves){
    // very basic, has no logic
    //updatePieces(board)
    let start = moves[0]
    let end = moves[1]

    let startx = start[0]
    let starty = start[1]
    let endx = end[0]
    let endy = end[1]

    let movedPiece = board[starty][startx]

    board[starty][startx] = "_"
    board[endy][endx] = movedPiece

    return board
}


function toggleDarkness(square){
    square.add("darken")
}

function checkIfMoveIsValid(column, row){
    let intColumn = parseInt(column, 10)
    let intRow = parseInt(row, 10)
    console.log("column, row", [intColumn, intRow])
    if (isArrayInArray(window.validMoves, [intColumn, intRow])){
        console.log("inside")
        return true
    }
    else{
        return false
    }
}

function isArrayInArray(arr, item){
  var item_as_string = JSON.stringify(item);

  var contains = arr.some(function(ele){
    return JSON.stringify(ele) === item_as_string;
  });
  return contains;
}



function handleLeftClick(websocket){
    window.visual_board.addEventListener("click", ({ target }) => {
        if (window.turn === window.colour){
            if (window.clicks.length < 2) { // if they haven not clicked twice yet
                /*console.log(window.clicks.length)
                console.log("Hello")*/
                var length = target.classList.length
                if (length != 0){ // if 0 this means user has clicked the image not the square itself
                    
                    toggleDarkness(target.classList)

                    var column = target.dataset.col // get column that was clicked
                    var row = target.dataset.row // get row that was clicked
                }
                else{ 
                    let parent = target.parentElement // this gets the parent of the image which is the square

                    toggleDarkness(parent.classList)

                    var column = parent.dataset.col // get column that was clicked
                    var row = parent.dataset.row // get row that was clicked
                    
                }
                if (column === undefined) {
                    return;
                }
                

                window.clicks.push([column, row]) // add click [column, row] to window.clicks
                
                if (window.clicks.length == 1){ // get the valid moves for this first click
                    window.validMoves = getValidMoves(window.chess_board, [parseInt(column, 10), parseInt(row, 10)])  
                    console.log("valid moves", window.validMoves)
                } 
                
            }
        }
        if (window.clicks.length == 2){ // do not use else as windows.clicks is added to when its length is 1 so it becomes 2 but else would't be triggered as it checked before it was added so if statement works better
            console.log("clicks", window.clicks)
            
            // check if attempted clicks(moves) are valid, if not then reset clicks

            if (checkIfMoveIsValid(window.clicks[1][0], window.clicks[1][1])){ // if the move is valid
                PlaySound("move")

                window.chess_board = movePiece(window.chess_board, window.clicks) // move pieces which returns a new board
                flipBoard(window.chess_board) // flip the board before returning it back to server
                let fen_string = boardToFenParser(window.chess_board) // changes the board to a fen string
                sendMoves(websocket, fen_string) // sends info back to server
            }
            else{
                removeDarkenedSquares(window.chess_board, window.visual_board, []) // if they have tried to make a invalid move then clear window.clicks and any darkened squares 
            }
            window.clicks = []

        }
    })
}

function handleRightClick(){
    window.addEventListener('contextmenu', (event) => {
        //event.preventDefault() // stops context menu appearing if user right clicks ontop of the board
        window.clicks = [] // clears clicks
        removeDarkenedSquares(window.chess_board, window.visual_board, []) // re draws the pieces so there are no darkened squares from previous clicks
        console.log("right clicked")       
    })
}

function listenForClick(websocket) { // board is referencing visual board
    handleRightClick() // if right click then clear clicks
    handleLeftClick(websocket) // if left click carry on as normal
}

function listenForHover(){
    window.visual_board.addEventListener("mouseover", (event) => {
        if (window.turn == window.colour){
            var length = event.target.classList.length
            if (length != 0){ // if 0 this means user has clicked the image not the square itself
                var square = event.target

                var column = square.dataset.col // get column that was clicked
            }
            else{ 
                var square = event.target.parentElement // this gets the parent of the image which is the square
            
                var column = square.dataset.col // get column that was clicked
            }
            if (column === undefined) {
                return;
            }
            removeDarkenedSquares(window.chess_board, window.visual_board, window.clicks)
            
            toggleDarkness(square.classList)
        }
    })
}

function reverseClicksIfBlack(){
    let numbersDictionary = {"0": 7, "1": 6, "2": 5, "3": 4, "4": 3, "5": 2, "6": 1, "7": 0}
    
    if (window.colour === "black"){
        let newClicks = []
        for (let i=0; i<window.clicks.length; i++){
            let click = window.clicks[i]
            let column = click[0]
            let row = click[1]
            console.log("click", click)
            let newColumn = numbersDictionary[column.toString()]
            let newRow = numbersDictionary[row.toString()]
            newClicks.push([newColumn, newRow])
        }
        window.clicks = newClicks
        console.log("reversed clicks", window.clicks)
    }   
    
}

function sendMoves(websocket, message){
    websocket.send(message)
    console.log("sent", message)
}


function listenForRecieve(websocket, func){ 
    websocket.onmessage = (event) => {
        let info = JSON.parse(event.data)

        let fen_string = info["fen_string"]
        window.turn = info["turn"]
        window.colour = info["colour"]


        console.log("recieved", event.data)
        console.log("fen_string =>", fen_string, "turn =>", window.turn)
        func(fen_string, websocket) // sets up once fen string is recieved 
    }
}