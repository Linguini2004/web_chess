function fenParser(fen_string){
	// takes a fen string and returns a board

	var rows = fen_string.split("/")
	var board = []

	const no_rows = rows.length // number of rows

	for (let r=0; r < no_rows; r++){
		let row = rows[r] // current row e.g "rnbqkbnr"
		let split_row = row.split("") // a split row e.g. ["p", "p", "p", "p"]
		let current_list = [] // current list that is going to be added to and then added to the board

		for (let c=0; c < row.length; c++){
			let current_value = row[c]// current value in a row

			// letter = piece (uppercase=white, lowercase=black)
			// number = that length of numbers in "_"

			// checks if letter => compares lowercase to uppercase => if they are different then it is a letter
			if (current_value.toLowerCase() !== current_value.toUpperCase()){
				current_list.push(current_value)
			}
			else {
				// changes number to spaces
				let number = parseInt(current_value, 10)
				for (let i=0; i<number; i++){
					current_list.push("_") // "_" represent a unoccupied cell
				}
			}
		}

		board.push(current_list)

	}
	return board
}

function boardToFenParser(board){
	// takes a board and returns a fen_string
	let fen_string = ""

	for (let r=0; r<board.length; r++){
		// r will cycle through the numbers 0,1,2,3,4,5,6,7
		let current_row = board[r]
		let empty_count = 0 // how many empty values there have been in a row
		for (let c=0; c<board.length; c++){
			// c will cycle through the numbers 0,1,2,3,4,5,6,7
			let current_value = current_row[c]// or current row 
			if (current_value != "_"){
				if (empty_count > 0){
					fen_string += empty_count.toString() // adds the number of empty values in a row there have been 
					empty_count = 0 // sets empty count to zero
				}

				
				fen_string += current_value


				
			}
			else{
				// if the cell or value is empty
				empty_count += 1
				if (c == board.length-1){ // checks if you have reached the end of the row
					fen_string += empty_count.toString()
				}			
			}
		}
		if (r != board.length-1){
			fen_string += "/"

		}
	}
	console.log(fen_string)
	return fen_string
}

export {fenParser, boardToFenParser}