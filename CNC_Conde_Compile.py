import queue

import Parameter_Define_Class as Para_Define

class Code_Analysisi:

    def __init__(self):
        # #定义一个条件字典
        self.M_Condition={}
        # #定义一个子程序字黄,save name,star_ps,end_ps
        self.M_Runsub_Dict = {}

        self.u_main_start_ps = None
        self.u_main_end_ps = None



        # self.M_Runsub = #queue.Queue()
        # self.M_RunMain = queue.Queue()

        #define deep dict
        self.M_Deep ={}
        self.Dis_CondNameList  = ['_ON', '_OFF', '_IP', '_PL', '_V', '_HP', '_PP', '_AL', '_OC', '_LD']
        # va_data = ['50', '20', '30', '-', '500', '1', '5', '3', '4', '6']
        # print(self.Dis_CondNameList)
        self.Dis_Condition = Para_Define.Parameters(self.Dis_CondNameList)
        self.Machining_CondNameList = ['_ON', '_MA', '_SV', '_UP', '_C', '_S', '_LN', '_STEP', '_L', '_LP']
        # va_data = ['50', '20', '30', '-', '500', '1', '5', '3', '4', '6']
        self.Mahining_Condition = Para_Define.Parameters(self.Machining_CondNameList)
        # X Y Z W
        self.Run_Axis = ['Direction','Step','Min','Max']
    def AddCondition(self,ConditionText):
        try:
            name = ConditionText[0]


            self.Dis_Condition.load_vals(ConditionText[1])

            self.Mahining_Condition.load_vals(ConditionText[2])
            # print('first part:{},{},{}',name,self.Dis_Condition.get_vals(),self.Mahining_Condition.get_vals())
            self.M_Condition[name] = [self.Dis_Condition.get_vals(),self.Mahining_Condition.get_vals()]
        except Exception as e:
            print(e)
    def GenerateCondition(self,name,uc1,uc2):
        try:
            ucd = name
            for items in uc1:
                ucd = ucd +' '
                ucd = ucd + items
        except:
            return None
    def DispartCondtion(self,line):
        try :
            line1 = line.replace('  ', ' ')
            line2 = line1.replace('   ', ' ')
            line2 = line2.replace(';', '')
            uulist = line2.split(' ')

            uname = uulist[0]

            uulist.pop(0)
            uulist.pop(0)
            # print(uulist)
            # for i in range(len(uulist)):
            #    print('list{}:{}',i,uulist[i])
            # ['_ON', '_OFF', '_IP', '_PL', '_V', '_HP', '_PP', '_AL', '_OC', '_LD']
            # ['_ON', '_MA', '_SV', '_UP', '_C', '_S', '_LN', '_STEP', '_L', '_LP']
            va_data = ['50', '20', '30', '-', '500', '1', '5', '3', '4', '6']
            va_data[0] = uulist[0]  # on
            va_data[1] = uulist[1]  # off
            va_data[2] = uulist[3]  # ip
            va_data[3] = uulist[9]  # pl
            va_data[4] = uulist[10]  # v
            va_data[5] = uulist[11]  # hp
            va_data[6] = uulist[12]  # pp

            # va_data[7] = uulist[12] #AL
            # va_data[8] = uulist[12]  # OC
            # va_data[9] = uulist[12]  # ld
            # ['_ON', '_MA', '_SV', '_UP', '_C', '_S', '_LN', '_STEP', '_L', '_LP']
            vb_data = ['50', '20', '30', '-', '500', '1', '5', '3', '4', '6']
            # vb_data[0] = uulist[0] #on
            vb_data[1] = uulist[2]  # ma
            vb_data[2] = uulist[4]  # sv
            vb_data[3] = uulist[5]  # up
            vb_data[4] = uulist[13]  # c
            vb_data[5] = uulist[14]  # s
            vb_data[6] = uulist[7]  # ln
            vb_data[7] = uulist[8]  # step
            vb_data[8] = uulist[15]  # l
            vb_data[9] = uulist[12]  # lp
            #print(uname, va_data, vb_data)
            return (uname, va_data, vb_data)
        except Exception as e:
            print(e)
            return None
    def FindDischargeCondition(self,utext):
        u_main_start_ps = None
        u_main_end_ps = None

        try:
            ulinelist = utext.split('\n')
        except:
            pass
        # print(ulist)


        for i in range(len(ulinelist)):
            try:
                uline = ulinelist[i].strip()
            except:
                pass
            try:
                # print(uline[0])
                if (uline[0] == 'C') and (uline.find(' = ') > -1):
                    a = self.DispartCondtion(uline)
                    self.AddCondition(a)

                    #thies is deep handle
                if (uline[0] == 'H') and (uline.find(' = ') > -1):
                    uline1 = uline.replace('  ', ' ')
                    uline2 = uline1.replace('   ', ' ')
                    uline2 = uline2.replace(';', '')
                    uu_list = uline2.split(' ')

                    if(uu_list[1]) == '=':
                        name = uu_list[0]
                        deep_parameter = self.Collation_Deep_Parameter(uu_list[2])
                        self.M_Deep[name] = deep_parameter
                #子程序序号
                if (uline[0] == 'G') and (uline[1].isdigit()):
                    if not self.u_main_start_ps:
                        self.u_main_start_ps = i
                        #ulinelist.index(uline)
                        # print(u_main_start_ps, u_main_end_ps)

                if (uline[0] == 'N') and (uline[1].isdigit()):
                    if not u_main_end_ps:
                        self.u_main_end_ps = i
                        #ulinelist.index(uline)
                        # print(u_main_start_ps, u_main_end_ps)
                        #
                        # for ms in range(self.u_main_start_ps,self.u_main_end_ps):
                        #     self.M_RunMain.put(ulinelist[ms])
                    sub_name = uline
                    sub_name = self.CutComment(sub_name)
                    sub_start_ps = i
                    #ulinelist.index(uline)
                    self.M_Runsub_Dict[sub_name]=[sub_start_ps,sub_start_ps]
                    # print('start position:',sub_start_ps)
                    #Collation the name,cut the annotation
                if uline.find('M99') > -1:
                    v = self.M_Runsub_Dict[sub_name]
                    v[1] = i
                    self.M_Runsub_Dict[sub_name] = v
                # if uline.find('M99') > -1 :
                #     print(uline)
                #     print(sub_start_ps)
                #     print(ulinelist[sub_start_ps:])
                #     sub_end_ps = ulinelist[sub_start_ps:].index(uline)
                #     print('end position:', sub_end_ps)
                #     if sub_end_ps > sub_start_ps:
                #
                #         self.M_Runsub_Dict[sub_name]=[sub_start_ps,sub_end_ps]
                #         sub_start_ps = None
            except:
                pass

        print('this is all')
        # print(self.M_Condition)
        # print(self.M_Deep)
        # #print(self.M_RunMain)
        # for i in range(self.M_RunMain.qsize()):
        #     print(self.M_RunMain.get())
        # print(self.M_RunMain.qsize())
        print(self.M_Runsub_Dict)
            # print(line)
            # print(type(line))
            # if(line[0]=='C'):
            #     print('find C')
            # if(line[0] == 'C') and (line.find(' = ')>-1):
            #     # uc = self.DispartCondtion(line)
            #     print('Dispart ok ..')
                # print(uc)
                # self.AddCondition(uc)
                # print(self.M_Condition)
                # print('Find Condition ..')



    def Collation_Deep_Parameter(self,ustr):
        # print(ustr,len(ustr))
        if(ustr[0] != '+') and (ustr[0] != '-'):
            return None
        if(len(ustr))<9:
            return None
        # print(ustr[0:9])
        return ustr[0:9]
        # for i in range(1,len(ustr)):
        #     if ~ustr[i].isdigit():
        #         if(i>2) and (i<8):



    def CutComment(self,uComment):
        p1 = uComment.find('(')
        if(p1>2):
            return uComment[:p1-1]
        if(p1<2):
            return False
        return uComment
    def GrammaticalCheck(self,ustr):
        #每行要有;,由于使用;来分段，帮这里不能这样检，先不考虑
        # lines = ustr.split('\n')
        # print(lines)
        # print('.')
        lines = ustr.split(';')
        #
        # if(len(lines)!= len(liness)):
        #     ret = 'E setence error--'+ str(len(lines))+'---'+ str(len(liness))
        #     return ret
        # print('..')
        # for line in liness:
        #     l = len(line)
        #
        #     if line[l-1] != ';':
        #         ret = 'Error' + line + 'need:;'
        #         print(line)
        #         print('The longth:', line[l - 1])
        #         return ret
        #mast exist M02
        ret = 'Check Error'
        for line in lines:
            if line == 'M02':
                ret = 'Check Ok!'
        # if exist sub program,must exit M90
        ret = 'Check Error'
        for line in lines:
            if (line[0] == 'N') and (line[1].isdigit()):
                #start this position to find M90,but not over pass sub program sn
                print('Will find the end Command.')
        return ret

if __name__ == '__main__':
    obj1 = Code_Analysisi()

