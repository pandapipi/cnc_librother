import time

import  modbus_mast as md_m
import  modbus_slave as md_s
import system_config as sys_con
class Interface_Connect_Relay:
    def __init__(self):
        try:
            self.ConfigHandle = sys_con.SysConfigYaml(sys_con.sys_yaml_file)
        except:
            pass
    def ConnectControl(self):
        try:

            uphase = self.ConfigHandle.p_yaml['RelayMachine']
            self.DischargeMachinePhase = uphase
            print(uphase)
            print(self.ConfigHandle.GetPKey(uphase,'Bord'))

            Port = self.ConfigHandle.GetPKey(uphase,'Port')
            Bord = self.ConfigHandle.GetPKey(uphase,'Bord')
            ADD  = self.ConfigHandle.GetPKey(uphase,'ID')
            Startadd = self.ConfigHandle.GetPKey(uphase,'Startadd')
            DataLongth = self.ConfigHandle.GetPKey(uphase, 'DataLongth')
            BlockName = self.ConfigHandle.GetPKey(uphase, 'BlockName')

            print(type(Bord))
            print(type(DataLongth))
            self.mdControltHandle = md_s.ModbusRTU_Slave(Port,Bord,ADD,BlockName,Startadd,DataLongth)

            return True
        except:
            return None
    def WriteControl(self,Value):

        if(self.mdControltHandle.write(0,Value)):
            return True
        else:
            return False


if __name__ == '__main__':
    si = Interface_Connect_Relay()
    #print(si.ConfigHandle.p_yaml)
    if(si.ConnectControl()):
        print('will write')
        print(si.WriteControl([3,1,1,2,1]))
        print('ok')