from abc import *

class Falcon(ABC):
    def __init__(self):
        self.mine={78,33,10,40,923,42,56,5,75,477,3,56}
    #abstract function        
    def heyThere(self):
        pass
    

class Winter(Falcon):
    def heyThere(self):
        print(self.mine)


win=Winter()
win.heyThere()