function startGame() {
    var welcome_heading = document.getElementById("welcome-heading")
    var start_area = document.getElementById("start-area")
    var level_description = document.getElementById("level-description")
    welcome_heading.style.display = "none"
    start_area.style.display = "none"
    level_description.style.display = "block"
    eel.startGame('started')(displayLevelDescription)
}

function displayLevelDescription(description){
    var description_text = document.getElementById("description-text")
    description_text.innerHTML = description;
}