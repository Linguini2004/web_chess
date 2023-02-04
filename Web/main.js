import {drawBoard, drawPieces, updatePieces} from "./board.js"
import {fenParser, boardToFenParser} from "./parser.js"

// makes sure everything is ready before running the main code
window.addEventListener("DOMContentLoaded", () => {

    // Initialize the UI.
    console.log('DOM fully loaded and parsed')
    const websocket = new WebSocket("ws://localhost:8001/") // open websocket
    window.clicks = []
    const visual_board = drawBoard() // creates the visual board without the pieces

    
    listenForRecieve(websocket, update) // listen for initial message


    listenForClick(visual_board, websocket) // listens for 2 clicks then moves the piece and then changes the window.board

})

function update(fen_string, websocket){
    window.chess_board = fenParser(fen_string) // a list with every piece in its position 
    
    console.log(chess_board)
    //console.log(window.chess_board)

    drawPieces(window.chess_board) // draws pieces onto  visual board
    //setTimeout(main, 3000, websocket, fen_string, board)
    //boardToFenParser(board)
    

}

function main(fen_string ,websocket){
    

    //updatePieces(current_board) // removes images from cells
    console.log("updating")
    let new_board = fenParser(fen_string)
    drawPieces(new_board)

    sendMoves(websocket, fen_string) // sends info back to server
}

// function sendMoves(board, websocket) {
//     board.addEventListener("click", ({ target }) => {
//     var length = target.classList.length
//     if (length != 0){ // if 0 this means user has clicked the image not the square itself
//         const column = target.dataset.col
//         const row = target.dataset.row

//         if (column === undefined) {
//             return;
//         }
//         const event = {
//             type: "play",
//             column: parseInt(column, 10),
//             row: parseInt(row, 10)
//         }
//         websocket.send(JSON.stringify(event))
    
//     }
//     else{ 
//         let parent = target.parentElement // this gets the parent of the image which is the square

//         const column = parent.dataset.col
//         const row = parent.dataset.row
//         if (column === undefined) {
//             return;
//         }
//         const event = {
//             type: "play",
//             column: parseInt(column, 10),
//             row: parseInt(row, 10)
//         }
//         websocket.send(JSON.stringify(event)) // turns event into a json format
        
//     }
//     }) 
// }

function cleanup(visual_board){
    //console.log(visual_board)
    console.log(window.chess_board)
    updatePieces(window.chess_board, visual_board)
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
    square.toggle("darken")
}


function listenForClick(visual_board, websocket) { // board is referencing visual board
    
    // console.log("listen for click called", window.clicks)
    visual_board.addEventListener("click", ({ target }) => {
    console.log(window.clicks.length)
    if (window.clicks.length < 2) { // if they haven not clicked twice yet
        /*console.log(window.clicks.length)
        console.log("Hello")*/
        var length = target.classList.length
        if (length != 0){ // if 0 this means user has clicked the image not the square itself
            
            toggleDarkness(target.classList)

            const column = target.dataset.col // get column that was clicked
            const row = target.dataset.row // get row that was clicked

            if (column === undefined) {
                return;
            }
            //console.log("column, row", column, row)
            window.clicks.push([column, row])
        
        }
        else{ 
            let parent = target.parentElement // this gets the parent of the image which is the square

            toggleDarkness(parent.classList)

            const column = parent.dataset.col // get column that was clicked
            const row = parent.dataset.row // get row that was clicked
            if (column === undefined) {
                return;
            }
            //console.log("column, row", column, row)
            window.clicks.push([column, row])
        }
    }
    if (window.clicks.length == 2){ // do not use else as windows.clicks is added to when its length is 1 so it becomes 2 but else would't be triggered as it checked before it was added so if statement works better
        // if they have clicked twice#

        console.log(window.clicks)
        
        
        // console.log("pressed twice", window.clicks)
        console.log(visual_board)
        cleanup(visual_board)
        window.chess_board = movePiece(window.chess_board, window.clicks) // move pieces which returns a new board
        let fen_string = boardToFenParser(chess_board) // changes the board to a fen string
        sendMoves(websocket, fen_string) // sends info back to server

        window.clicks = []

    }

    }) 
}


function sendMoves(websocket, message){
    websocket.send(message)
    console.log("sent", message)
}


function listenForRecieve(websocket, func){ 
    websocket.onmessage = (event) => {
        console.log("recieved", event.data)
        func(event.data, websocket) // sets up once fen string is recieved 
    }
}