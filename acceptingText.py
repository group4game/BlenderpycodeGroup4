import bge
from bge import logic
path = logic.expandPath("//datafile.txt")

def main():

    cont = bge.logic.getCurrentController()
    own = cont.owner
    
    file = open(path, 'w')
    keyEvents = bge.logic.keyboard.events
    
    hitKeys = [k for k in keyEvents \
                    if keyEvents[k] == bge.logic.KX_INPUT_JUST_ACTIVATED]
                    
    if hitKeys != []:
        print(hitKeys[0])
        key = bge.events.EventToCharacter(hitKeys[0], False)
        print(key)
        if len(own.text) < 10:
            own.text += key
        
    file.write(own.text)
    

main()

