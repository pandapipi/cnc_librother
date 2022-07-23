'''
这里块定义，读写一定要一样多。
设定多少长度，每次写得固定多少长度。要不会冲掉其它位置数据。
!!!!!!!!!!!!!利用Modbus 工具 模拟数据发送 和 接收  【注意】：modbus poll 设置中的数据长度一定要和程序中推送的长度一致 ，在这个问题上浪费了好长时间 哎 !!!!!!!!!!!!!!!!
modebus pull re 03
'''
import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import time
class ModbusRTU_Slave:
    def __init__(self,port,bard,slave_no,blockname,startadd,longth):

        self.port = port
        self.bard = bard
        self.slave_no = slave_no
        self.blockname = blockname
        self.startadd = startadd
        self.longth = longth
        # # 设定串口为从站
        # # 外置参数包括端口 port = "COM3" 波特率：9600
        self.server = modbus_rtu.RtuServer(serial.Serial(port=port, baudrate=bard, bytesize=8, parity='N', stopbits=1))
        self.server.start()
        print("runing...")
        self.SSLAVE1 = self.server.add_slave(1)
        self.SSLAVE1.add_block('A', cst.HOLDING_REGISTERS, 0, self.longth)  # 地址0，长度4
        print('config ok')
    def write(self,StartAdd,Value):
       try:
           self.SSLAVE1.set_values(self.blockname, StartAdd, Value)  # 改变在地址0处的寄存器的值):
           return (True)

       except:
           print('config error!')
           return(False)

if __name__ == '__main__':
    um = ModbusRTU_Slave('COM2',115200,1,'A',0,5)
    um.write(0,[4,5])
