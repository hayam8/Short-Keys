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

eel.expose(next);
function next(){
    eel.getNextLevel()(displayLevelDescription)
}
function displayLevelDescription(description){
    var description_text = document.getElementById("description-text")
    description_text.innerHTML = description;
}

function encyclopedia(){
    eel.getEncyclopedia()(displayEncyclopedia)
}

function displayEncyclopedia(enc){
    var encyclopedia = document.getElementById("encyclopedia")
    var welcome_heading = document.getElementById("welcome-heading")
    var start_area = document.getElementById("start-area")
    welcome_heading.style.display = "none"
    start_area.style.display = "none"
    encyclopedia.style.display = "block"
    var tbody = document.createElement("tbody")
    document.getElementById("tab").appendChild(tbody)

    for(var i =0; i < enc[0].length; i++){
        var tr = document.createElement("tr")
        var td_left = document.createElement("td")
        var td_right = document.createElement("td")
        var key = document.createTextNode(enc[0][i])
        var desc = document.createTextNode(enc[1][i])
        td_left.appendChild(key)
        td_right.appendChild(desc)
        tr.appendChild(td_left)
        tr.appendChild(td_right)
        tbody.appendChild(tr)
    }
}

function startLevels(){
    eel.startLevels()
}
