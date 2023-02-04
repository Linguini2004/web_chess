function drawBoard(){
    const board = document.querySelector(".board")
    const numRows = 8
    const numCols = 8

    for (let col = 0; col < numCols; col++)
    {
        const column = document.createElement("div")
        column.classList = "col"

        for (let row = 0; row < numRows; row++)
        {
        //const row = document.querySelector(".col")
        const square = document.createElement("div")
        square.dataset.row = row
        square.dataset.col = col
        square.classList = "square"
        // square.addEventListener("click", (e) => { // listens for a click
        //     var length = e.target.classList.length
        //     if (length != 0){ // if 0 this means user has clicked the image not the square itself
        //         e.target.classList.toggle("darken") // toggles the blue css 
        //     }
        //     else{ 
        //         let parent = e.target.parentElement // this gets the parent of the image which is the square
        //         parent.classList.toggle("darken")
        //     }
        // })
        if (row % 2 == col % 2) {
            square.classList.add("white")
        } else {
            square.classList.add("black")
        }
        column.appendChild(square)
        }

        board.append(column)
    }

    const squareWidth = parseInt(getComputedStyle(document.querySelector(".square")).width, 10)

    board.style.maxWidth = numCols * squareWidth // multiplys no. rows by the width of a square => this is set in css

    return board
}


function updatePieces(chess_board, visual_board){
    // sqaure width is a parameter to determine how big the pieces should be
    // board is a list that contains lists of values

    // this for loop iterates through the different squares and removes the image within them

    const all_columns = visual_board.querySelectorAll(".col") // gets all divs with class "col"
    for (let q=0; q<all_columns.length; q++){
        let columns = all_columns[q]
        let squares = columns.childNodes
        //console.log(squares)
        for (let l=0; l<squares.length; l++){
            let current_square = squares[l] // current visual square on the board

            // position of the square on the board
            let squareRow = current_square.dataset["row"] 
            let squareCol = current_square.dataset["col"]

            const squareWidth = parseInt(getComputedStyle(document.querySelector(".square")).width, 10) // gets square width

            // the piece that is meant to be in that position(square)
            let correspondingPiece = chess_board[squareRow][squareCol]
            // if the piece isn't empty
            if (correspondingPiece != "_"){
                let img = current_square.querySelector("img")
                img.remove()
            }
        }
    }
}


function drawPieces(board){
    // sqaure width is a parameter to determine how big the pieces should be
    // board is a list that contains lists of values

    // this for loop iterates through the pieces in the board and adds them to html

    const visual_board = document.querySelector(".board")
    const all_columns = visual_board.querySelectorAll(".col") // gets all divs with class "col"
    for (let q=0; q<all_columns.length; q++){
        let columns = all_columns[q]
        let squares = columns.childNodes
        //console.log(squares)
        for (let l=0; l<squares.length; l++){
            let current_square = squares[l] // current visual square on the board

            // position of the square on the board
            let squareRow = current_square.dataset["row"] 
            let squareCol = current_square.dataset["col"]

            const squareWidth = parseInt(getComputedStyle(document.querySelector(".square")).width, 10) // gets square width

            // the piece that is meant to be in that position(square)
            let correspondingPiece = board[squareRow][squareCol]
            // if the piece isn't empty
            if (correspondingPiece != "_"){
                let filename = getFilenameName(correspondingPiece) // gets filename of that piece(image)
                var image = document.createElement("img") // creates an image for that square
                image.width = squareWidth // sets image width to square width so it fits
                image.src = filename // adds the filename to the source
                current_square.appendChild(image) // adds image to square div
            }
        }
    }


    //console.log(all_columns)
}

function getFilenameName(piece){
    let filename = "pieces/"
    // "_" are checked before this is called so then it doesn't expect to get null in return
    // checks if piece is upper => then it is white
    if (piece.toUpperCase() == piece){
        filename += "w" // means white
        filename += piece.toLowerCase() // changed to lower case because all files are in lower case
        filename += "_forward" // for now white will be facing forward but depends on what colour the player is
        filename += ".svg" // this is the file format
    }
    else{
        filename += "b"
        filename += piece
        filename += "_forward" // for now black will be facing backwards but depends on what colour the player is
        filename += ".svg" // this is the file format
    }

    return filename
}


export {drawBoard, drawPieces, updatePieces}