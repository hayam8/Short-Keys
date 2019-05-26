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
listener = Listener('user_output.txt', shortcut_list)
@eel.expose
def startGame():
    listener.start()
    return getNextLevel()

@eel.expose
def getNextLevel():
    global current_index
    current_index += 1
    current_shortcut = shortcut_list[current_index]
    return current_shortcut.getDescription()


eel.start('index.html', size=(1000, 550))
