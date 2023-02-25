window.addEventListener("DOMContentLoaded", () => {

    // Initialize the UI.
    console.log('DOM fully loaded and parsed')

    checkForFindGame()
    
})

function checkForFindGame(){
    document.querySelector("#find_game").addEventListener("click", function (){PlaySound("check")}) 
}

function PlaySound(filename){
    var audio = new Audio(`${filename}.mp3`);
    audio.play();

    var resp = audio.play();

    if (resp!== undefined) {
        resp.then(_ => {}).catch(error => {});
    }
}