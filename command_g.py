'''
2022.07.13 g01
need send wait for carry out
G01X228-H100M04: translate into two parts :G01X228,G01XH100
Coordinate set mode 'G91X122Y123Z124U125' == 'G91W001' W001 = X122Y123Z124U125
'''
#handle G01Z228-H100M04 (加工到Z-0.772后返回加工点Z1.0);
import Coordinate_Caculater as ccl
import handle_cmc5410 as cn5410
class CommandCNCHandle:
    cmdcharlist = 'CGMHXYZUT'
    ucc = ccl.CNCCoordinate()
    r5410 = cn5410.Cmc5401()
    def StringCommandToArray(self,in_commanc):

        comlist = []
        tmpstring = ''
        if in_commanc[0].isdigit():
            return comlist

        for item in in_commanc:
            if item.isdigit():
                tmpstring = tmpstring + item
            else:
                # print(tmpstring)
                if(len(tmpstring) > 2):
                    comlist.append(tmpstring)
                    tmpstring = ''
                if item in self.cmdcharlist:
                    tmpstring = item
        comlist.append(tmpstring)
        return comlist
    def HandleCNCCommand(self,in_command):
        comdlist = self.StringCommandToArray(in_command)
        print('end:')
        print(comdlist)
        if comdlist[0] == 'G01':
            print('g01 handle')
            axil = comdlist[1][0]
            # axil = self.r5410.check_axil_char(comdlist[1][0])
            #judge its legal,legitimate

            if axil in self.cmdcharlist :
                # print('g01 handle...')
                # print(comdlist[1][1:])
                axil = self.r5410.check_axil_char(comdlist[1][0])
                ud = int(comdlist[1][1:])
                self.ucc.RunMOde = 1
                # print(self.ucc.GetRunData(axil, ud))
                self.r5410.cmdbytes = self.r5410.EndpositionOfInterpolation(axil,ud)
                print(self.r5410.cmdbytes)
        if comdlist[0] == 'G90':
            self.ucc.RunMOde = 0
        if comdlist[0] == 'G91':
            self.ucc.RunMOde = 1
            self.ucc.ReferenceCoordinate = [int(comdlist[1][1:]),int(comdlist[2][1:]),int(comdlist[3][1:]),int(comdlist[4][1:])]
            print(self.ucc.ReferenceCoordinate)

    pass
if __name__ == '__main__':
    # print(StringCommandToArray('C220LNH300STEPH200-93'))
    ucmd = CommandCNCHandle()
    # ucmd.HandleCNCCommand('G01X228-H100M04')# translate into two parts :G01X228,G01XH100
    ucmd.HandleCNCCommand('G91X122Y123Z124U125')  # translate into two parts :G01X228,G01XH100
