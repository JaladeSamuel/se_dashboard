import psutil
import geocoder

class MetaSensor():
    
    def __init__(self, id,type):
        self.id = id
        self.type = type
    
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
        return psutil.sensors_fans()
    
    def get_battery_left(self):
        return str(psutil.sensors_battery().secsleft/60).format("%d") + 'min'
    
    def get_is_plugged(self):
        return psutil.sensors_battery().power_plugged
    
    def get_gps(self):
        g = geocoder.ip('me')
        print(g.latlng)
        return g.latlng
    
    def show(self):
        print("{}\t{}\tvalue:{}".format(self.id,self.type,get_value()))