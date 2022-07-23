
class CNCCoordinate:
    #绝对坐标,单位um
    BaseCoordinate = [0,0,0,0]
    ReferenceCoordinate = [5,5,5,5]
    LimitZone = [1000,1000,1000,1000]
    RunMOde = 0 #0:绝对坐标，1：相对坐标
    def GetRunData(self,axil,aimps):
        rt = 0
        if self.RunMOde == 0:
            if axil == 'x':
              rt = aimps - self.BaseCoordinate[0]
            if axil == 'y':
              rt = aimps - self.BaseCoordinate[1]
            if axil == 'z':
              rt = aimps - self.BaseCoordinate[2]
            if axil == 'u':
              rt = aimps - self.BaseCoordinate[3]


        if self.RunMOde == 1:
            if axil == 'x':
                rt = aimps + self.ReferenceCoordinate[0] - self.BaseCoordinate[0]
            if axil == 'y':
                rt = aimps + self.ReferenceCoordinate[1] - self.BaseCoordinate[1]
            if axil == 'z':
                rt = aimps + self.ReferenceCoordinate[2] - self.BaseCoordinate[2]
            if axil == 'u':
                rt = aimps + self.ReferenceCoordinate[3] - self.BaseCoordinate[3]
        return rt
if __name__ == '__main__':
    uc = CNCCoordinate()

    print(uc.GetRunData('x',123))
    uc.RunMOde = 1
    print(uc.GetRunData('x', 123))