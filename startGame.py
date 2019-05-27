import eel
import shortcutdatabase
from listener import Listener
from levellistener import LevelListener
import leveldatabase
#from pywin32 import win32api
#from win32api import win32gui

eel.init('web')
shortcut_list = shortcutdatabase.getAllShortcuts()
current_index = -1
level = leveldatabase.level1

@eel.expose
def startGame():
    listener = Listener('user_output.txt', shortcut_list)
    listener.start()
    return getNextLevel()

@eel.expose
def getNextLevel():
    global current_index
    current_index += 1
    current_shortcut = shortcut_list[current_index]
    return current_shortcut.getDescription()

@eel.expose
def getEncyclopedia():
    list_shortcuts = shortcutdatabase.getAllShortcutsString()
    shortcut_keys = []
    shortcut_descriptions = []
    for i in list_shortcuts:
        items = i.split("=")
        shortcut_keys.append(items[0])
        shortcut_descriptions.append(items[1])

    return [shortcut_keys, shortcut_descriptions]


@eel.expose
def startLevels():
    level_listener = LevelListener('user_output_levels.txt', level)
    level_listener.start()


eel.start('index.html')