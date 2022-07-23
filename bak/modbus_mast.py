import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time
# 数据接收端
class ModbusRTU_Master:

    def __init__(self,slaveno,port,bard,startadd,longth):
        self.slaveno = slaveno
        self.port = port
        self.bard = bard
        self.startadd = startadd
        self.longth = longth
        # 设定串口为从站
        # 外置参数包括端口 port = "COM3" 波特率：9600
        self.master = modbus_rtu.RtuMaster(serial.Serial(port=self.port,baudrate=self.bard, bytesize=8, parity='N', stopbits=1))
        self.master.set_timeout(1.0)
        self.master.set_verbose(True)

    # 读保持寄存器
    def AskInterData(self,beginadd,getlongth):
        try:
            read = self.master.execute(self.slaveno, cst.HOLDING_REGISTERS,beginadd, getlongth)  # 这里可以修改需要读取的功能码
            #print(read)
            return (read)
        except Exception as exc:
            print(str(exc))
            return(None)
if __name__ == '__main__':
    umaster =    ModbusRTU_Master(1,'COM2',115200,0,5)
    umaster.AskInterData(0,3)