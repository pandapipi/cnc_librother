import time

import User_Modbus as u_mod

class Interface_Setting_Discharge:
    def __init__(self):
        try:
            self.ConfigPhaseName = 'DischargeMachine'
            self.userHandle = u_mod.User_Modbus_Class(self.ConfigPhaseName)

            self.userHandle.Connect()

            self.pwm_low = self.userHandle.ConfigHandle.GetPKey(self.userHandle.Phase,'PWM_LOW')
            print(self.pwm_low)
            self.pwm_high = self.userHandle.ConfigHandle.GetPKey(self.userHandle.Phase, 'PWM_HIGH')
            print(self.pwm_high)
            self.pwm_channal = self.userHandle.ConfigHandle.GetPKey(self.userHandle.Phase, 'Channal')
            print(self.pwm_channal)
            self.pwm_votage_switch = self.userHandle.ConfigHandle.GetPKey(self.userHandle.Phase, 'PulseVotageSwitch')
            print('config {}',self.pwm_votage_switch)

        except:
            pass

    def WriteControl(self):

       if not self.userHandle.WriteSignalReg(0,0x3000):
           return False
       if not self.userHandle.WriteSignalReg(0,0x1000+self.pwm_low):
           return False
       print(self.pwm_high)
       if not self.userHandle.WriteSignalReg(0,0x2000+self.pwm_high):
           return False
       if not self.userHandle.WriteSignalReg(0, 0x3000 + self.pwm_channal):
           return False
       return True
    def AskLimitInput(self):
        self.userHandle.ReadReg(0,2)

if __name__ == '__main__':
    si = Interface_Setting_Discharge()
    print('...')
    if not si == None:
        si.WriteControl()
        si.AskLimitInput()
