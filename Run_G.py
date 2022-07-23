
import time
class Run_G_Class:

    def __init__(self):
        self.Time_Dict = {}
        self.BegginTime = time.localtime()
        self.StartTime = time.localtime()
        self.EndTime = time.localtime()
    def CutBlank(self,setence):
        try:
            uline1 = setence.replace('  ', ' ')
            uline2 = uline1.replace('   ', ' ')
            uline2 = uline2.replace(';', '')
            uu_list = uline2.split(' ')
        except:
            uu_list = setence
        return uu_list

    def Command_G83(self,name):
        self.Time_Dict[name] = time.time()
    #C220LNH300STEPH200-41 ();
    #G01Z116-H100M04 ();
    def Command_G01(self,setence):
        #setting the condition

        #send run command
        st = setence[2:]
        st = self.CutBlank(st)
        if (len(st) > 1 ):
            if st[0] != 'X' and  st[0] != 'Y' and  st[0] != 'Z'  and st[0] != 'W' :
                return False
            else:

        pass
