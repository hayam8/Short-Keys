import shortcutdatabase
from shortcut import Shortcut

"""
The level class takes in a string name for variable, string description for what user should do, list of valid actions
that can be taken by user, and a time limit for how long the level can last
The level class takes in a dictionary with key
"""
class Level:

    #constructor
    def __init__(self, name, des, actions, limit):
        self.name = name
        self.instructions = des
        self.validShortcuts = []
        self.validActions = actions # any action sent in by constructor
        self.timeLimit = limit
        self.setValidShortcuts(actions)
        self.numTargetActions = len(self.validShortcuts)
    
    def setNumTargetActions(self, shortcuts):
        self.numTargetActions = len(shortcuts)

    def setValidShortcuts(self, input):
        shortcuts = []
        for i in input:
            if isinstance(i, Shortcut):
                shortcuts.append(i)
        self.validShortcuts = shortcuts

    def getName(self):
        return self.name

    def getInstructions(self):
        return self.instructions

    def getValidShortcutsList(self):
        return self.validShortcuts

    def getValidShortcuts(self):
        shortcuts = []
        for i in range(len(self.validShortcuts)):
            shortcuts.append(str(self.validShortcuts[i]))
            if(i != (len(self.validShortcuts) - 1)):
                shortcuts.append("\n")
        return ''.join(shortcuts)

    def getAllActions(self):
        return self.validActions

    def getValidActions(self):
        actions = []
        for i in self.validActions:
            if isinstance(i, Shortcut):
               actions.append(i.getKeys())
            else:
                actions.append(i)
        return actions

    def getTimeLimit(self):
        return self.timeLimit

    def getNumTargetActions(self):
        return self.numTargetActions

    #display level info
    def display(self):
        print(self.getName(), "\n" + self.getInstructions(),
              "\nGoal Shortcuts: ", "\n", self.getValidShortcuts(), "\nTarget Number of Actions: ", self.getNumTargetActions(),
              "\nTime Limit: ", self.getTimeLimit(), "sec")

    

    
    def displayLevel(self):
        print(self.getName(), "\n" + self.getInstructions(), 
        "Goal Shortcuts: ", self.getValidShortcuts(), " Target Number of Actions: ", self.getNumTargetActions(),
        " Time Limit: ", self.getTimeLimit(), "sec")