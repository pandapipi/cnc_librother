import time

import  modbus_mast as md_m
import  modbus_slave as md_s
import system_config as sys_con
class Interface_Connect_TouchTestMachine:
    def __init__(self):
        try:
            self.ConfigHandle = sys_con.SysConfigYaml(sys_con.sys_yaml_file)
        except:
            pass
    def ConnectControl(self):
        try:

            uphase = self.ConfigHandle.p_yaml['TouchTestMachine']
            self.DischargeMachinePhase = uphase
            print(uphase)
            print(self.ConfigHandle.GetPKey(uphase,'Bord'))

            Port = self.ConfigHandle.GetPKey(uphase,'Port')
            Bord = self.ConfigHandle.GetPKey(uphase,'Bord')
            ID  = self.ConfigHandle.GetPKey(uphase,'ID')
            Startadd = self.ConfigHandle.GetPKey(uphase,'Startadd')
            DataLongth = self.ConfigHandle.GetPKey(uphase, 'DataLongth')
            BlockName = self.ConfigHandle.GetPKey(uphase, 'BlockName')

            print(type(Bord))
            print(type(DataLongth))
            self.mdControltHandle = md_m.ModbusRTU_Master(ID,Port,Bord,Startadd,DataLongth)

            return True
        except:
            return None
    def AskAdd(self,beginadd,getlongth):

            return self.mdControltHandle.AskInterData(beginadd,getlongth)


if __name__ == '__main__':
    si = Interface_Connect_TouchTestMachine()
    #print(si.ConfigHandle.p_yaml)
    if(si.ConnectControl()):
        print('will write')
        print(si.AskAdd(0,3))
        print('ok')