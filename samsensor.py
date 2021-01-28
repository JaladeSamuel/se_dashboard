from sensors.sensor import MetaSensor
import numpy as np

class SamSensor(MetaSensor):
    
    __metaclass__ = MetaSensor
    def __init__(self, id, name):
        super().__init__(id,name)
    
    def getvalue(self):
        return np.random.random_sample()
    

if __name__ == '__main__':
    rasp = samsensor(0,'float')
    print(rasp.getvalue())