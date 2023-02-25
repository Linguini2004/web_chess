import {getValidMoves} from "./rules.js"

window.addEventListener("DOMContentLoaded", () => {

    // Initialize the UI.
    console.log('DOM fully loaded and parsed')
    let board = [['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
                ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                ['_', '_', '_', '_', '_', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', '_', '_'],
                ['_', '_', '_', '_', '_', '_', '_', '_'],
                ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r']]
    getValidMoves(board, [1, 1]) // x, y starting from top left
})

window.addEventListener('click', (event, target) => {
  console.log(event.button)
})