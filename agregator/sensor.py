import numpy as np
import time 
class Sensor():
    
    def __init__(self, id,type,localisation):
        self.id = id
        self.type = type
        self.localisation = localisation
        self.data = []

    def clear_buffer(self):
        self.data = []

    def getvalue(self):
        for i in range(10):
            self.data.append(19.5 + np.random.rand())
        return self.data

    
    def gettype(self):
        return self.type
    
    def getid(self):
        return self.id

    def getlocalisation(self):
        return self.localisation
    
