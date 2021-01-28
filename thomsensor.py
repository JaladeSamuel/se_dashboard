from sensors.sensor import MetaSensor
import numpy as np

class ThomSensor(MetaSensor):
    _metaclass__ = MetaSensor
    
    def __init__(self, id, name):
        super().__init__(id,name)
        
    def getvalue(self):
        return self.get_battery_left()
    
if __name__ == '__main__':
    cfansensor = ThomSensor(0,'string')
    print(cfansensor.getvalue())