from sensors.sensor import MetaSensor
import numpy as np

class samsensor(MetaSensor):
    def __init__(self, *args):
        super(MetaSensor, self).__init__(*args)
    
    def getvalue(args):
        # TODO raspsensor
        return np.random.random_sample()
    

if __name__ == '__main__':
    rasp = samsensor("ta","mere")
    print(rasp.getvalue())
    
        
        