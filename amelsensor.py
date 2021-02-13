from sensors.sensor import MetaSensor
import numpy as np

class AmelSensor(MetaSensor):
    _metaclass__ = MetaSensor
    
    def __init__(self, id, name):
        super().__init__(id,name)
        
    def getvalue(self):
        return self.get_memory_usage()
    
        