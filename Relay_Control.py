
'''
this use modbus slave  mode:1
'''
import Parameter_Define_Class as pdc
import system_config as sys_con
import User_Modbus as u_md

class Realy_Define(object):
    def __init__(self):
        try:
            self.ConfigHandle = sys_con.SysConfigYaml(sys_con.sys_yaml_file)
            up = self.ConfigHandle.p_yaml['RelayMachine']
            # print(uphase)
            self.uphase = self.ConfigHandle.GetPKey(up, 'RelayDefine')
            self._keys = list(self.uphase.keys())
            self._values = list(self.uphase.values())
            # print(self.__keys)
            # print(self.__values)

        except:
            pass
        # print(uup.keys())
        self.uc = pdc.Parameters(self._keys)
        #print((self.__values)
        self.uc.load_vals(self._values)
        # self.uc
class Relay_Control:

    def __init__(self):
        self.ud = Realy_Define()
        self.md_handle = u_md.User_Modbus_Class('RelayMachine')
        self.md_handle.Connect()
    def Turn_On(self,operater_name):
        #find position
        ps = self.ud.uphase[operater_name][0]
        ps_int = int(ps)
        # if(type(ps)=='str'):
        #     ps_int = int(ps)
        # else:
        #     ps_int = ps
        self.md_handle.WriteSignalCOIL(ps_int,1)
        print(ps)
        # send_out
        #wirte back

if __name__ == "__main__":
    # k = Realy_Define()
    # # print(k.SW_AlarmPowver)
    # k.uc.print_all()
    # print(k.uc.SW_AlarmPowver)
    k = Relay_Control()
    k.Turn_On('SW_AlarmPowver')