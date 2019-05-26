import eel
import leveldatabase

eel.init('web')

@eel.expose
def startGame(data):
    print(data)
    return "level description"


eel.start('index.html', size=(1000, 600))
