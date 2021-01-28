import psutil

class MetaSensor():
    
    def __init__(self, id,type):
        self.id = id
        self.type = type
    
    @abstractmethod
    def getvalue(self):
        return 
    
    def gettype(self):
        return self.type
    
    def getid(self):
        return self.id
    
    def get_cpu_temp(self):
        return psutil.cpu_percent()
    
    def get_memory_usage(self):
        return psutil.virtual_memory().percent
    
    def get_fan_speed(self):
        return psutil.sensors_fan()
    
    def show(self):
        print("{}\t{}\tvalue:{}".format(self.id,self.type,get_value()))