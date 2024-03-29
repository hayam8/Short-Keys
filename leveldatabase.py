import shortcutdatabase as db
from level import Level

#level params: name, instructions, valid shortcuts, time limit

level1Des = "Copy all of the text from the current window and then paste it into the Notepad application"
level1Actions = ['createUserMongoDB - Notepad', db.getShortcutByName("selectAll"), db.getShortcutByName("copy"), 'Untitled - Notepad', db.getShortcutByName("paste")]
level1 = Level("Level 1", level1Des, level1Actions, 10)
"""
level1Description = "Open the Notepad application"
level1Actions = [shortcutdatabase.openSearch, 'n', 'o', 't', 'e','p', 'a', 'd', 'Enter']
level1 = Level("Level 1", level1Description, level1Actions, 5)

level2Description = "Pin the application to the left side of the screen"
level2Shortcuts = [shortcutdatabase.pinLeft]
level2 = Level("Level 2", level2Description, level2Shortcuts, 5)

level3Description = "Copy all the text from the open window \n 2. Paste it in a notepad document"
level3Shortcuts = [shortcutdatabase.selectAll, shortcutdatabase.copy, shortcutdatabase.openSearch, shortcutdatabase.paste]
level3 = Level("Level 3", level3Description, level3Shortcuts, 5)

level4Description = "1. Open a Firefox window \n2. Open a new window \n3. Close that window \n4. Open a private window \n5. Navigate to the URL bar \n6. Go to www.celinedion.com"
level4Shortcuts = [shortcutdatabase.openSearch, shortcutdatabase.openNewWindow, shortcutdatabase.closeTab, shortcutdatabase.openPrivateWindow, shortcutdatabase.moveCursorToURLBar]
level4 = Level("Level 4", level4Description, level4Shortcuts, 5)
"""

"""
# building level1 tasks dictionary <<str>Task Description: <list> shortcuts/keys>
level1tasks = {"Open the Notepad application": [shortcutdatabase.openSearch, 'n', 'o', 't', 'e','p', 'a', 'd', 'Enter'],
               "Pin this application to the left side of the screen": [shortcutdatabase.maximizeToLeft],
               "Maximize this window": [shortcutdatabase.maximize],
               "Open a new text file": [shortcutdatabase.openNewWindow],
               "Close the application": [shortcutdatabase.closeWindow]
               }
"""
"""

level1Description = "Open the Notepad application"
level1Actions = [shortcutdatabase.openSearch, 'n', 'o', 't', 'e','p', 'a', 'd', 'Enter']
level1 = Level("Level 1", level1Description, level1Actions, 5)

level2Description = "Pin this application to the left side of the screen"
level2Shortcuts = [shortcutdatabase.maximizeToLeft]
level2 = Level("Level 2", level2Description, level2Shortcuts, 5)

level3Description = "Maximize this window"
level3Shortcuts = [shortcutdatabase.maximize]
level3 = Level("Level 3", level3Description, level3Shortcuts, 5)

task4Description = "Open a new text file"
task4Shortcuts = [shortcutdatabase.openNewWindow]
task4 = Level("Task 4", task4Description, task4Shortcuts, 5)

task5Description = "Close the application"
task5Shortcuts = [shortcutdatabase.closeWindow]
task5 = Level("Task 5", task5Description, task5Shortcuts, 5)

level4Description = "Shrink this window"
level4Shortcuts = [shortcutdatabase.minimize]
level4 = Level("Level 4", level4Description, level4Shortcuts, 5)

level5Description = "Tab through all your open windows using Alt-Tab"
level5Shortcuts = [shortcutdatabase.switchTabs]
level5  = Level("Level 5", level5Description, level5Shortcuts, 5)

level6Description = "Tab through all your open windows using CRTL-Alt-Tab"
level6Shortcuts = [shortcutdatabase.switchBetweenAllTabs]
level6  = Level("Level 6", level6Description, level6Shortcuts, 5)
"""
"""
levelNTask1 =
levelNTask2=
levelNTask3 =
levelNTask4 =
levelNTask5 =

levelNTasks = {


}
"""

"""
level database tests
"""
#print(level1.getValidActions())
#print('Win' in level1.getValidActions())