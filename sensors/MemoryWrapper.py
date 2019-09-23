from sensor_wrapper import SensorWrapper
import psutil

class MemoryWrapper(SensorWrapper):
    _key = 'memory'

    def __init__(self):
        SensorWrapper.__init__(self)

    def get_data(self):
        msg = {}
        # Get memory in use and add to msg, using bit shift operator to represent in MB
        msg["memory_used"] = psutil.virtual_memory().used >> 20
        return msg

    def get_info(self):
        return psutil.virtual_memory()