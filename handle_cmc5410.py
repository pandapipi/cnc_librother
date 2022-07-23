'''
base:cmc5410软件函数库开发手册
XY 轰 2 轰直线插补：
収生数据代码为：
22 01 00 00 27 10 X 轰插补结束点 10000；
22 02 00 00 4E 20 Y 轰结束插补点 20000；
23 01 02 収送 2 轰直线插补命令

'''
class Cmc5401:
    axildef_dict ={'x':1,'y':2,'z':4,'u':8,'F':0x0F}
    cmdstring = ''
    cmdbytes=bytes()
    #设定范围
    def check_axil_char(self,in_char):
        x = in_char
        if in_char == 'X':
            x = 'x'
        if in_char == 'Y':
            x = 'y'
        if in_char == 'Z':
            x = 'z'
        if in_char == 'U':
            x = 'u'
        return x
    def get_hex_from_data(self,in_data,w):
        a = 0
        if w == 0:
         a = in_data & 0xff
        if w == 1:
            a = (in_data >> 8) & 0xff
        if w == 2:
            a = (in_data >> 16) & 0xff
        if w == 3:
            a = (in_data >> 24) & 0xff
        return a
    #设定范围：
    def setlimitzoon(self,axil,in_data):
    
        cmd = []
        x = self.check_axil_char(axil)
        if not (x in self.axildef_dict):
            return cmd
    
        cmd.append( 0x01)
        cmd.append(self.axildef_dict[x])
        cmd.append(self.get_hex_from_data(in_data,3))
        cmd.append(self.get_hex_from_data(in_data,2))
        cmd.append(self.get_hex_from_data(in_data,1))
        cmd.append(self.get_hex_from_data(in_data,0))
    
        return cmd
    
    #设定初始速度和驱劢速度
    def setspeed(self,axil,start_speed,driver_speed):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
    
        cmd.append( 0x02)
        cmd.append(self,self.axildef_dict[x])
        cmd.append(self.get_hex_from_data(start_speed,1))
        cmd.append(self.get_hex_from_data(start_speed,0))
        cmd.append(self.get_hex_from_data(driver_speed,1))
        cmd.append(self.get_hex_from_data(driver_speed,0))
        return cmd
    #设定设定加/减速度
    def setspeed(self,axil,add_speed,dec_speed):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
    
        cmd.append( 0x03)
        cmd.append(self,self.axildef_dict[x])
        cmd.append(self.get_hex_from_data(add_speed,1))
        cmd.append(self.get_hex_from_data(add_speed,0))
        cmd.append(self.get_hex_from_data(dec_speed,1))
        cmd.append(self.get_hex_from_data(dec_speed,0))
        return cmd

    # 设置输出脉冲模式
    def setPulseOutMode(self, axil, mode):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd

        cmd.append(0x07)
        cmd.append(self, self.axildef_dict[x])
        cmd.append(mode)#0-双脉冲；1-方向脉冲，方向逡辑申平为低；2-方向脉冲，方向逡辑申平为高。

        return cmd
    #正向定长驱劢
    def RunPositivePulse(self,axil,pulse):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
    
        cmd.append( 0x0d)
    
        cmd.append(self,self.axildef_dict[x])
    
        cmd.append(self.get_hex_from_data(pulse,3))
        cmd.append(self.get_hex_from_data(pulse,2))
        cmd.append(self.get_hex_from_data(pulse,1))
        cmd.append(self.get_hex_from_data(pulse,0))
        # print(cmd)
        # ab = bytes(cmd)
        # print(ab)
        return cmd

    # 负向定长驱劢
    def RunNegetivePulse(self,axil,in_data):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
    
        cmd.append( 0x0e)
    
        cmd.append(self,self.axildef_dict[x])
        cmd.append(self.get_hex_from_data(in_data,3))
        cmd.append(self.get_hex_from_data(in_data,2))
        cmd.append(self.get_hex_from_data(in_data,1))
        cmd.append(self.get_hex_from_data(in_data,0))

        return cmd
    #设定逡辑位置计数器值,清 X 轰逡辑位置计数器:11 01 00 00 00 0
    def set_axillogiccounterreg(self,axil,in_data):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
    
        cmd.append( 0x11)
    
        cmd.append(self,self.axildef_dict[x])
        cmd.append(self.get_hex_from_data(in_data,3))
        cmd.append(self.get_hex_from_data(in_data,2))
        cmd.append(self.get_hex_from_data(in_data,1))
        cmd.append(self.get_hex_from_data(in_data,0))

        return cmd
    #设定实际位置计数器
    def set_axilRealcounterreg(self,axil,in_data):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
    
        cmd.append( 0x12)
    
        cmd.append(self,self.axildef_dict[x])
        cmd.append(self.get_hex_from_data(in_data,3))
        cmd.append(self.get_hex_from_data(in_data,2))
        cmd.append(self.get_hex_from_data(in_data,1))
        cmd.append(self.get_hex_from_data(in_data,0))
        # print(cmd)
        # ab = bytes(cmd)
        # print(ab)
        return cmd
    #启劢软限位
    def Enable_SoftLimit(self,axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
        cmd.append(0x16)
        cmd.append(self.axildef_dict[x])
        cmd.append(0x01)
        return cmd
    #禁止软限位
    def Disable_SoftLimit(self,axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self,x in self.axildef_dict):
            return cmd
        cmd.append(0x17)
        cmd.append(self.axildef_dict[x])
        cmd.append(0x01)
        return cmd

    #获取当前逡辑位置计数器值
    def Read_Logic_Counter(self,axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self, x in self.axildef_dict):
            return cmd
        cmd.append(0x1a)
        cmd.append(self.axildef_dict[x])
        return cmd
    #获取当前实际位置计数器值
    def Read_Real_Counter(self,axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self, x in self.axildef_dict):
            return cmd
        cmd.append(0x1b)
        cmd.append(self.axildef_dict[x])
        return cmd
    #速停止：1F
    def DecStop(self, axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self, x in self.axildef_dict):
            return cmd
        cmd.append(0x1f)
        cmd.append(self.axildef_dict[x])
        return cmd
    #立即停止:20
    def ImmediatelyStop(self, axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self, x in self.axildef_dict):
            return cmd
        cmd.append(0x20)
        cmd.append(self.axildef_dict[x])
        return cmd
    #恒定速度插补：设置为恒速插补时要设置好各轰的范围。21 示例：恒速 2 轰插补 21 01
    def NormalSpeedInterpolation(self, mode):
        # x = self.check_axil_char(axil)
        cmd = []
        # if not (self, x in self.axildef_dict):
        #     return cmd
        cmd.append(0x21)
        cmd.append(mode)#模式设置：0-恒速插补模式无效；1-2 轰恒速插补；2-设置无效；3-3 轰恒速插补
        # cmd.append(self.axildef_dict[x])
        return cmd
    #设定插补结束点
    def EndpositionOfInterpolation(self, axil,in_data):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self, x in self.axildef_dict):
            return cmd
        cmd.append(0x22)
        cmd.append(self.axildef_dict[x])
        cmd.append(self.get_hex_from_data(in_data,3))
        cmd.append(self.get_hex_from_data(in_data,2))
        cmd.append(self.get_hex_from_data(in_data,1))
        cmd.append(self.get_hex_from_data(in_data,0))
        return cmd
    #2 axil直线插补 23
    def DoubleAxilInterpolation(self,axil1,axil2):
        x = self.check_axil_char(axil1)
        y = self.check_axil_char(axil2)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
        if not (y in self.axildef_dict):
            return cmd
        cmd.append(0x23)
        cmd.append(self.axildef_dict[x])
        cmd.append(self.axildef_dict[y])

        return cmd
    #设定圆弧插补圆心
    def SetCirleInterpolationCenter(self,axil,in_data):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd

        cmd.append(0x25)
        cmd.append(self.axildef_dict[x])
        cmd.append(self.get_hex_from_data(in_data, 3))
        cmd.append(self.get_hex_from_data(in_data, 2))
        cmd.append(self.get_hex_from_data(in_data, 1))
        cmd.append(self.get_hex_from_data(in_data, 0))

        return cmd
    #2axil顺时针圆弧插补
    def SetCircleInterpolationClockwise(self,axil1,axil2):
        x = self.check_axil_char(axil1)
        y = self.check_axil_char(axil2)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
        if not (y in self.axildef_dict):
            return cmd
        cmd.append(0x26)
        cmd.append(self.axildef_dict[x])
        cmd.append(self.axildef_dict[y])
        return cmd
    #2axil逆时针圆弧插补
    def SetCircleInterpolationClockwise(self,axil1,axil2):
        x = self.check_axil_char(axil1)
        y = self.check_axil_char(axil2)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
        if not (y in self.axildef_dict):
            return cmd
        cmd.append(0x27)
        cmd.append(self.axildef_dict[x])
        cmd.append(self.axildef_dict[y])
        return cmd
    #使能硬件限位功
    def Enable_HardwareLimit(self,axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (x in self.axildef_dict):
            return cmd
        cmd.append(0x38)
        cmd.append(self.axildef_dict[x])
        cmd.append(0x00)#：0-立即停止，1-减速停
        cmd.append(0x00)#-正限位有效逡辑申平：0-低申平，1-高申平
        cmd.append(0x00)#-正限位有效逡辑申平：0-低申平，1-高申平
        return cmd
    #判断轰驱劢是否停止
    def Ask_Axil_Run_Stop(self,axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self,x in self.axildef_dict):
            return cmd
        cmd.append(0x39)
        cmd.append(self.axildef_dict[x])
        return cmd
    #使能自劢回原点执行的 Step
    def Homing(self, axil,dr):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self, x in self.axildef_dict):
            return cmd
        cmd.append(0x40)
        cmd.append(self.axildef_dict[x])
        cmd.append(dr)
        cmd.append(0x01)
        return cmd
    #使能回原点结束清除逡辑/实际位置计数器
    def HomingAndSetZero(self, axil):
        x = self.check_axil_char(axil)
        cmd = []
        if not (self, x in self.axildef_dict):
            return cmd
        cmd.append(0x48)
        cmd.append(self.axildef_dict[x])
        return cmd
if __name__ == '__main__':
    cnc1 =  Cmc5401()
    #print(cnc1.ImmediatelyStop('x'))
    '''
    XY 轰 2 轰直线插补：
    収生数据代码为：
    22 01 00 00 27 10 X 轰插补结束点 10000；
    22 02 00 00 4E 20 Y 轰结束插补点 20000；
    23 01 02 収送 2 轰直线插补命令'''
    print(cnc1.EndpositionOfInterpolation('x',10000))
    print(cnc1.EndpositionOfInterpolation('y', 20000))
    print(cnc1.DoubleAxilInterpolation('x','y'))
    '''
    XY 轰顺时针圆弧插补插补：

    22 01 00 00 27 10 X 轰插补结束点 10000；
    22 02 00 00 4E 20 Y 轰结束插补点 20000；
    25 01 00 00 13 88 X 轰圆心坐标
     CMC5401 软件函数库开发手册
     第 85 页 共 90 页
    25 02 00 00 00 00 Y 轰圆心坐标
    26 01 02 収送 2 轰顺时针圆弧插补命令

    '''

