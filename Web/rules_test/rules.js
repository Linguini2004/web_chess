/* check if a requested move is valid

each type of piece has a class

within the class => function that checks if a move is possible

params = current board state, requested move

return true or false / or set of possible moves */



class Piece{
	fillPossiblePositions(){
		for (let y=0; y<8; y++){
			for (let x=0; x<8; x++){
				this.valid_moves.push([x, y])
			}
		}
	}

	isUpperCase(myString) { 
	  return (myString == myString.toUpperCase()); 
	} 
	
	isLowerCase(myString) { 
	  return (myString == myString.toLowerCase()); 
	} 

	isFriendly(letter){
		console.log("trying to check if ", letter, "is friendly")
		if (this.CASE == "upper"){
			if (this.isUpperCase(letter)){
				return true
			}
			else{return false}
		}
		else if (this.CASE == "lower"){
			if (this.isLowerCase(letter)){
				return true
			}
			else{return false}
		}
	}

	getValidMoves(){
		this.checkMoves()
		return this.valid_moves
	}
}

class Pawn extends Piece{
	constructor(board, piece_position, letter, CASE){
		super()
		this.board = board
		this.row = piece_position[1]
		this.col = piece_position[0]
		this.letter = letter
		this.valid_moves = []
		this.CASE = CASE // upper or lower case
	}

	checkRank(){
		// checks whether the pawn can move 2 squares
		if (this.row == 1 || this.row == 6){
			console.log("on 2nd or 7th rank")
			return true
		}
		else{
			return false
		}
	}

	checkDirectMoves(){
		if (this.checkRank()){
			var radius = 2
		}
		else{
			var radius = 1
		}

		for (let i=1; i<radius+1; i++){
			var row_check = this.row-i
			console.log(this.board[row_check], row_check)
			if (this.board[row_check][this.col] == "_"){

				this.valid_moves.push([this.col, row_check])
			}
		}
	}

	checkTakes(){
		// check if the pawn can take another piece

		// get 2 squares which the pawn can take
		// check if there is are pieces in those 2 squares and if those pieces are friendly
		// remember to check if the pawn is on the side of the board

		let pawnTakeSquares = [[this.row-1, this.col-1], [this.row-1, this.col+1]] // the 2 squares diagonal to pawn
		for (let s=0; s<pawnTakeSquares.length; s++){
			let square = pawnTakeSquares[s] // the square that is diagonal to the pawn
			if (square[0] != 8 && square[1] != 8 && square[0] >= 0 && square[1] >= 0){
				let squarex = square[1]
				let squarey = square[0]

				let piece = this.board[squarey][squarex] // current piece that is in the square that is diagonal to the pawn
				if (piece != "_"){
					if (this.isFriendly(piece) == false){
						this.valid_moves.push([squarex, squarey])
					}
				}	
			}
		}
	}

	getValidMoves(){
		this.checkDirectMoves()
		this.checkTakes()
		// haven't done en passant
		// haven't checked for checks
		return this.valid_moves
	}
}

class Bishop extends Piece{
	constructor(board, piece_position, letter, CASE){
		super()
		this.board = board
		this.row = piece_position[1]
		this.col = piece_position[0]
		this.letter = letter
		this.valid_moves = []
		this.CASE = CASE // upper or lower case
		this.directions = [[1, 1], [-1, -1], [1, -1], [-1, 1]]

	}

	checkMoves(){
		// for each direction the bishop can go in 
		// keep on moving the bishop till you reach a piece  whether it is friendly or enemy !! taking the piece is valid but you stop there 
		for (let d=0; d<this.directions.length; d++){
			let direction = this.directions[d]
			let x = this.col
			let y = this.row
			while (true){
				x += direction[0]
				y += direction[1]
				if (x != 8 && y != 8 && x >= 0 && y >= 0){ // if the requested piece to move is not on the edge of the board
					let encounteredPiece = this.board[y][x]

					if (encounteredPiece != "_"){ // if the requested square is not empty 
						if (this.isFriendly(encounteredPiece)){ // if there is a friendly piece in the way then break loop and go on to next direction
							break
						}
						else{ // if there is an enemy piece in the way then add position to valid moves
							this.valid_moves.push([x, y])
						}
					}
					else{ // if the next square is empty then add it to valid moves
						this.valid_moves.push([x, y])
						
					}
				}
				else{// if it is on the edge of the board break the loop and check the other directions
					break
				}
			}
		}
	}

	
}

class Rook extends Piece{
	constructor(board, piece_position, letter, CASE){
		super()
		this.board = board
		this.row = piece_position[1]
		this.col = piece_position[0]
		this.letter = letter
		this.valid_moves = []
		this.CASE = CASE // upper or lower case
		this.directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
	}

	checkMoves(){
		// for each direction the rook can go in 
		// keep on moving the bishop till you reach a piece  whether it is friendly or enemy !! taking the piece is valid but you stop there 
		for (let d=0; d<this.directions.length; d++){
			let direction = this.directions[d]
			let x = this.col
			let y = this.row
			while (true){
				x += direction[0]
				y += direction[1]
				if (x != 8 && y != 8 && x >= 0 && y >= 0){ // if the requested piece to move is not on the edge of the board
					let encounteredPiece = this.board[y][x]

					if (encounteredPiece != "_"){ // if the requested square is not empty 
						if (this.isFriendly(encounteredPiece)){ // if there is a friendly piece in the way then break loop and go on to next direction
							break
						}
						else{ // if there is an enemy piece in the way then add position to valid moves
							this.valid_moves.push([x, y])
						}
					}
					else{ // if the next square is empty then add it to valid moves
						this.valid_moves.push([x, y])
						
					}
				}
				else{// if it is on the edge of the board break the loop and check the other directions
					break
				}
			}
		}
	}
}

class Queen extends Piece{
	constructor(board, piece_position, letter, CASE){
		super()
		this.board = board
		this.row = piece_position[1]
		this.col = piece_position[0]
		this.letter = letter
		this.valid_moves = []
		this.CASE = CASE // upper or lower case
		this.directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
	}

	checkMoves(){
		// for each direction the rook can go in 
		// keep on moving the bishop till you reach a piece  whether it is friendly or enemy !! taking the piece is valid but you stop there 
		for (let d=0; d<this.directions.length; d++){
			let direction = this.directions[d]
			let x = this.col
			let y = this.row
			while (true){
				x += direction[0]
				y += direction[1]
				if (x != 8 && y != 8 && x >= 0 && y >= 0){ // if the requested piece to move is not on the edge of the board
					let encounteredPiece = this.board[y][x]

					if (encounteredPiece != "_"){ // if the requested square is not empty 
						if (this.isFriendly(encounteredPiece)){ // if there is a friendly piece in the way then break loop and go on to next direction
							break
						}
						else{ // if there is an enemy piece in the way then add position to valid moves
							this.valid_moves.push([x, y])
						}
					}
					else{ // if the next square is empty then add it to valid moves
						this.valid_moves.push([x, y])
						
					}
				}
				else{// if it is on the edge of the board break the loop and check the other directions
					break
				}
			}
		}
	}
}

class King extends Piece{
	constructor(board, piece_position, letter, CASE){
		super()
		this.board = board
		this.row = piece_position[1]
		this.col = piece_position[0]
		this.letter = letter
		this.valid_moves = []
		this.CASE = CASE // upper or lower case
		this.directions = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1, 1]]
	}

		checkMoves(){
		// for each direction the rook can go in 
		// keep on moving the bishop till you reach a piece  whether it is friendly or enemy !! taking the piece is valid but you stop there 
		for (let d=0; d<this.directions.length; d++){
			let direction = this.directions[d]
			let x = this.col
			let y = this.row
			x += direction[0]
			y += direction[1]
			if (x != 8 && y != 8 && x >= 0 && y >= 0){ // if the requested piece to move is not on the edge of the board
				let encounteredPiece = this.board[y][x]

				if (encounteredPiece != "_"){ // if the next square is empty then add it to valid moves
					if (!this.isFriendly(encounteredPiece)){ // if there is an enemy piece in the way then add position to valid moves
						this.valid_moves.push([x, y])
					}
				}
				else{
					this.valid_moves.push([x, y])
					
				}
			}
		}
	}
}

class Knight extends Piece{
	constructor(board, piece_position, letter, CASE){
		super()
		this.board = board
		this.row = piece_position[1]
		this.col = piece_position[0]
		this.letter = letter
		this.valid_moves = []
		this.CASE = CASE // upper or lower case
		this.directions = [[1, 2], [-1, 2], [1, -2], [-1, -2], [-2, 1], [-2, -1], [2, 1], [2, -1]]
	}
	checkMoves(){
		// for each direction the rook can go in 
		// keep on moving the bishop till you reach a piece  whether it is friendly or enemy !! taking the piece is valid but you stop there 
		for (let d=0; d<this.directions.length; d++){
			let direction = this.directions[d]
			let x = this.col
			let y = this.row
			while (true){
				x += direction[0]
				y += direction[1]
				if (x < 8 && y < 8 && x >= 0 && y >= 0){ // if the requested piece to move is not on the edge of the board
					let encounteredPiece = this.board[y][x]

					if (encounteredPiece != "_"){ // if the requested square is not empty 
						if (this.isFriendly(encounteredPiece)){ // if there is a friendly piece in the way then break loop and go on to next direction
							break
						}
						else{ // if there is an enemy piece in the way then add position to valid moves
							this.valid_moves.push([x, y])
						}
					}
					else{ // if the next square is empty then add it to valid moves
						this.valid_moves.push([x, y])
						
					}
				}
				else{// if it is on the edge of the board break the loop and check the other directions
					break
				}
			}
		}
	}
}

function getValidMoves(board, piece_position){
	// create a class for the requested piece
	
	console.log(piece_position)
	let piece = assignClass(board, piece_position)
	console.log(piece)
	// get valid moves from piece
	piece.getValidMoves()
	return piece.valid_moves
}


function assignClass(board, piece_position){
	let row = piece_position[1]
	let col = piece_position[0]

	let pieceDict = {"p": Pawn, "b": Bishop, "r": Rook, "q": Queen, "k": King, "n": Knight} // dictionary with keys of letters with their corresponding class
	let pieceLetter = board[row][col]

	if (pieceLetter.toUpperCase() == pieceLetter){ // if the piece is black, assign it a class with upper
		let piece = new pieceDict[pieceLetter.toLowerCase()](board, piece_position, pieceLetter, "upper")
		return piece
	}
	else{ // if the piece is black, assign it a class with lower
		let piece = new pieceDict[pieceLetter.toLowerCase()](board, piece_position, pieceLetter, "lower")
		return piece
	}	
}

export {getValidMoves}