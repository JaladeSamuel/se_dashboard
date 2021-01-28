from sensors.sensor import MetaSensor
import numpy as np

class SelimSensor(MetaSensor):
    _metaclass__ = MetaSensor
    
    def __init__(self, id, name):
        super().__init__(id,name)
        
    def getvalue(self):
        return self.get_cpu_temp()
    
if __name__ == '__main__':
    ctempsensor = SelimSensor(0,'float')
    print(ctempsensor.getvalue())
        