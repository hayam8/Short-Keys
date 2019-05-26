import eel
import shortcutdatabase
from listener import Listener

eel.init('web')
shortcut_list = [
    shortcutdatabase.copy,
    shortcutdatabase.paste,
    shortcutdatabase.cut,
    shortcutdatabase.lockPC
]
current_index = -1

@eel.expose
def startGame():
    return getNextLevel()

@eel.expose
def getNextLevel():
    global current_index
    current_index += 1
    current_shortcut = shortcut_list[current_index]
    print(current_shortcut.getDescription())
    return current_shortcut.getDescription()

@eel.expose
def getEncyclopedia():
    return shortcutdatabase.listOfShortcutsString



eel.start('index.html', size=(1000, 550))
