function startGame() {
    var welcome_heading = document.getElementById("welcome-heading")
    var start_area = document.getElementById("start-area")
    var level_description = document.getElementById("level-description")
    var next_button = document.getElementById("next-button")
    welcome_heading.style.display = "none"
    start_area.style.display = "none"
    level_description.style.display = "block"
    eel.startGame()(displayLevelDescription)
    next_button.style.display = "block"
}

//eel.expose(next);
function next(){
    console.log('startGame => js')
    eel.getNextLevel()(displayLevelDescription)
}
function displayLevelDescription(description){
    var description_text = document.getElementById("description-text")
    description_text.innerHTML = description;
}