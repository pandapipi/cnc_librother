import Parameter_Define_Class as pdc
import system_config as sys_con


class Realy_Define(object):
    def __init__(self):
        try:
            self.ConfigHandle = sys_con.SysConfigYaml(sys_con.sys_yaml_file)
            uphase = self.ConfigHandle.p_yaml['RelayMachine']
            # print(uphase)
            uup = self.ConfigHandle.GetPKey(uphase, 'RelayDefine')
            self.__keys = list(uup.keys())
            self.__values = list(uup.values())
            # print(self.__keys)
            # print(self.__values)
        except:
            pass
        # print(uup.keys())
        self.uc = pdc.Parameters(self.__keys)
        #print((self.__values)
        self.uc.load_vals(self.__values)
        # self.uc
if __name__ == "__main__":
    k = Realy_Define()
    # print(k.SW_AlarmPowver)
    k.uc.print_all()
    print(k.uc.SW_AlarmPowver)