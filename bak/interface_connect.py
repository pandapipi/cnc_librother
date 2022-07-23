import time

import  modbus_mast as md_m
import  modbus_slave as md_s
import system_config as sys_con
class Interface_Connect:
    def __init__(self):
        try:
            self.ConfigHandle = sys_con.SysConfigYaml(sys_con.sys_yaml_file)
        except:
            pass
    def ConnectDischargeControl(self):
        try:

            uphase = self.ConfigHandle.p_yaml['DischargeMachine']
            self.DischargeMachinePhase = uphase
            print(uphase)
            print(self.ConfigHandle.GetPKey(uphase,'Bord'))

            Port = self.ConfigHandle.GetPKey(uphase,'Port')
            Bord = self.ConfigHandle.GetPKey(uphase,'Bord')
            ADD  = self.ConfigHandle.GetPKey(uphase,'Add')
            Startadd = self.ConfigHandle.GetPKey(uphase,'Startadd')
            DataLongth = self.ConfigHandle.GetPKey(uphase, 'DataLongth')
            BlockName = self.ConfigHandle.GetPKey(uphase, 'BlockName')

            print(type(Bord))
            print(type(DataLongth))
            self.uConnecDischargeControltHandle = md_s.ModbusRTU_Slave(Port,Bord,ADD,BlockName,Startadd,DataLongth)

            return True
        except:
            return None
    def WriteDischargeControl(self,Value):
        if( self.uConnecDischargeControltHandle.write(0,Value)):
            return True
        else:
            return False
    def SetDischarge(self):
        #shut channal first
        if(~self.WriteDischargeControl([0x3000])):
            return False
        time.sleep(2)
        if(~self.WriteDischargeControl([0x1000+self.ConfigHandle.GetPKey(self.DischargeMachinePhase,'PWM_LOW')])):
            return False
        time.sleep(2)
        if(~self.WriteDischargeControl([0x2000 + self.ConfigHandle.GetPKey(self.DischargeMachinePhase, 'PWM_HIGH')])):
            return False
        time.sleep(2)
        if(~self.WriteDischargeControl([0x3000 + self.ConfigHandle.GetPKey(self.DischargeMachinePhase, 'Channal')])):
            return False
        return True

if __name__ == '__main__':
    si = Interface_Connect()
    #print(si.ConfigHandle.p_yaml)
    if(si.ConnectDischargeControl()):
        print('will write')
        print(si.WriteDischargeControl([1,2,4]))
        print('ok')
        si.SetDischarge()