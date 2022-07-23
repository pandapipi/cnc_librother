# -*- coding: utf_8 -*-
import time

import serial
import modbus_tk
import modbus_tk.defines as cst
from modbus_tk import modbus_rtu
import system_config as sys_con

class User_Modbus_Class:

    def __init__(self,MachineName):
        try:
            self.ConfigHandle = sys_con.SysConfigYaml(sys_con.sys_yaml_file)
            self.MachineName = MachineName
        except:
            pass
    def Connect(self):
        try:

            uphase = self.ConfigHandle.p_yaml[self.MachineName]
            self.Phase = uphase
            print(uphase)
            print(self.ConfigHandle.GetPKey(uphase,'Bord'))

            self.Port = self.ConfigHandle.GetPKey(uphase,'Port')
            self.Bord = self.ConfigHandle.GetPKey(uphase,'Bord')
            self.ID  = self.ConfigHandle.GetPKey(uphase,'ID')
            self.Startadd = self.ConfigHandle.GetPKey(uphase,'Startadd')
            self.DataLongth = self.ConfigHandle.GetPKey(uphase, 'DataLongth')
            self.BlockName = self.ConfigHandle.GetPKey(uphase, 'BlockName')



            #设定串口为从站
            self.master = modbus_rtu.RtuMaster(serial.Serial(port=self.Port,
            baudrate=self.Bord, bytesize=8, parity='N', stopbits=1, xonxoff=0))
            self.master.set_timeout(5.0)
            self.master.set_verbose(True)
            print('wait...')
            #读保持寄存器 03H 1站号 地址2700 长度0-42

        except Exception as exc:
            print(str(exc))

    def ReadReg(self,StartAdd,ByteLongth):
        try:
            ret = self.master.execute(self.ID, cst.READ_HOLDING_REGISTERS, StartAdd, ByteLongth)  # 这里可以修改需要读取的功能码
            print(ret)
            return list(ret)
        except Exception as exc:
            print(str(exc))
            return False

    def ReadRelay(self,StartAdd,ByteLongth):
        try:
            ret = self.master.execute(self.ID, cst.READ_COILS, StartAdd, ByteLongth)  # 这里可以修改需要读取的功能码
            print(ret)
            return list(ret)

        except Exception as exc:
            print(str(exc))
            return False

    # # 单个读写寄存器操作 06H
    def WriteSignalReg(self,StartAdd,Value):
        try:
            self.master.execute(self.ID, cst.WRITE_SINGLE_REGISTER, StartAdd, output_value=Value)
            return True
        except Exception as exc:
            print(str(exc))
            return False


    # # 写寄存器地址为0的线圈寄存器，写入内容为0（位操作） 05H
    def WriteSignalCOIL(self,StartAdd,Value):
        print('will operater{}-{}',StartAdd,Value)
        try:
            self.master.execute(self.ID, cst.WRITE_SINGLE_COIL, StartAdd, output_value=Value)
            return True
        except Exception as exc:
            print(str(exc))
            return False



    # # 多个寄存器读写操作 10H
    # # 写寄存器起始地址为0的保持寄存器，操作寄存器个数为4 output_value=[20, 21, 22, 23]))
    # logger.info(master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 11, output_value=[20, 21, 22, 23]))
    # 反馈：01 10 00 0B 00 04 08 00 14 00 15 00 16 00 17 AB A9

    def WriteMultipleRegisters(self,StartAdd,Value):
        try:
            self.master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, StartAdd, output_value=Value)
            return True
        except Exception as exc:
            print(str(exc))
            return False

if __name__ == "__main__":
    m = User_Modbus_Class('TouchTestMachine')
    m.Connect()
    for i in range(4):
        if(    m.WriteSignalCOIL(2,1)):
            print('ok..')
        #time.sleep(1000)
        if(m.WriteSignalCOIL(2, 0)):
            print('ok...')
    # if(m.ReadReg(1,2)):
    #     print('Ok')
    # else:
    #     print("error")
    # m.WriteSignalReg(1,0x1234)
    # time.sleep(1)
    # m.WriteMultipleRegisters(1,[2,3,4])
    # time.sleep(1)
    # m.ReadReg(1,2)

    # m = User_Modbus_Class('RelayMachine')
    # m.Connect()
    # m.WriteSignalCOIL()