# 安装：pip3 install pyserial   //python3
import serial
import serial.tools.list_ports
import time
import threading
import PyQt5.QtCore as PQC

def bytesfind(bytes_list,find_str):
    for i in range(len(bytes_list)-len(find_str)):
        if bytes_list[i] == find_str[0] and bytes_list[i+1] == find_str[1]:
            break
    return i
def getusererdata(bytes_list):
    return int.from_bytes(bytes_list, byteorder='little', signed=False)

def get_angle(bytes_list):
    # aa = 0.1
    a = getusererdata(bytes_list)
    print(a)
    aa = a*180/32768
    # print(aa)
    return round(aa,2)
def get_anglespeed(bytes_list):
    # aa = 0.1
    a = getusererdata(bytes_list)
    print(a)
    aa = a*2000/32768
    # print(aa)
    return round(aa,2)
class userial:
    com_rx_buf = ''  # 接收缓冲区
    com_rx_buf = com_rx_buf.encode('utf-8')
    com_tx_buf = ''  # 发送缓冲区
    # COMM = serial.Serial()  # 定义串口对象
    port_list: list  # 可用串口列表
    port_select: list  # 选择好的串口
    COMM = None
    rev_data = ''
    rev_flag = False
    rev_run_flag = False
    angle_x = 0.0
    angle_y = 0.0
    angle_z = 0.0
    anglespeed_x=0.0
    anglespeed_y = 0.0
    anglespeed_z = 0.0

    a_x = ""
    a_y = ""
    a_z = ""

    # 无串口返回0，
    # 返回可用的串口列表
    # Signal_Sendmag = PQC.pyqtSignal(object)

    def __init__(self, stats):
        self._stats = stats
    def get_com_list(self):
        global port_list
        # a = serial.tools.list_ports.comports()
        # print(a)
        self.port_list = list(serial.tools.list_ports.comports())
        # port_list = serial.tools.list_ports.comports()
        return self.port_list

    def set_com_port(self, n=0):

        self.port_select = self.port_list[n]
        return self.port_select.device

    # 打开串口
    def serial_open(self, n=1):
        ucom = 'COM'+str(n)
        self.serial_port = ucom #self.set_com_port(n)

        try:
            self.COMM = serial.Serial(self.serial_port, 9600, timeout=0.01)
            if self.COMM.isOpen():
                self.rev_run_flag = True
                print(self.serial_port, "open success")
                return 0
            else:
                print("open failed")
                return 255
        except:
            print('com is open or error!')
    # 关闭串口
    def serial_close(self):

        self.rev_run_flag = False

        print(self.COMM)
        self.COMM.close()

        print(self.COMM.name + "closed.")

    def set_com_rx_buf(self, buf=''):

        self.com_rx_buf = buf

    def set_com_tx_buf(self, buf=''):

        self.com_tx_buf = buf

    def get_com_rx_buf(self):

        return self.com_rx_buf

    def get_com_tx_buf(self):

        return self.com_tx_buf
    def fenxin(self):
        # p_a = self.rev_data.find('UQ')
        # p_b = self.rev_data.find('UR')
        # p_c = self.rev_data.find('US')
        print(self.rev_data)
        # if p_a >0 :
        #
        #     print(self.rev_data)
        #     self.rev_data = ''


    def thread_com_receive(self, me):
        while True:
            time.sleep(0.05)
            ucoms = me.COMM.readline()
            print(ucoms)

            # if ucoms != b'':
                # self.com_rx_buf += ucoms
                # al = bytesfind(self.com_rx_buf, b'US')
                # print(self.com_rx_buf)
                # bl = len(self.com_rx_buf)
                # print(al)
                # print(bl)
                # self.com_rx_buf = ucoms
                # if bl > al +10:
                        # self.angle_x = get_angle(self.com_rx_buf[al + 2:al + 4])
                        # self.angle_y = get_angle(self.com_rx_buf[al + 4:al + 6])
                        # self.angle_z = get_angle(self.com_rx_buf[al + 6:al + 8])
                        # print(self.angle_x, self.angle_y, self.angle_z)
                        # self.com_rx_buf = ''
                # except Exception as e:
                #     print(e)
                # if al>0:
                    # if len(self.com_rx_buf)-al > al+10:
            #
            #             self.angle_x = get_angle(self.com_rx_buf[al+2:al+4])
            #             self.angle_y = get_angle(self.com_rx_buf[al + 4:al + 6])
            #             self.angle_z = get_angle(self.com_rx_buf[al + 6:al + 8])
            #     print(self.angle_x,self.angle_y,self.angle_z)



            #     try:
            #         al = bytesfind(self.com_rx_buf,b'US')
            #         # bl = bytesfind(self.com_rx_buf, b'UR')
            #         print('a')
            #         if al>0:
            #             if len(self.com_rx_buf[al:]) > al+10:
            #                 # print('hello')
            #                 # print(self.com_rx_buf[al :al + 10])
            #                 # print(self.com_rx_buf[al+2:al+8])
            #                 self.angle_x = get_angle(self.com_rx_buf[al+2:al+4])
            #                 self.angle_y = get_angle(self.com_rx_buf[al + 4:al + 6])
            #                 self.angle_z = get_angle(self.com_rx_buf[al + 6:al + 8])
            #                 print(self.angle_x,self.angle_y,self.angle_z)
            #                 self.com_rx_buf = ''
            #     except Exception as e:
                   # print('ee')
            #print(self.message)
        #while True:
        # if 1:
        #     try:
        #         rx_buf = ''
        #         # rx_buf = rx_buf.encode('utf-8')  # 由于串口使用的是字节，故而要进行转码，否则串口会不识别
        #         rx_buf = self.COMM.read()  # 转化为整型数字
        #         if rx_buf != b'':
        #             time.sleep(0.01)
        #
        #             rx_buf = self.COMM.read_all()
        #             self.com_rx_buf = self.com_rx_buf + rx_buf
        #             self.rev_flag = True
        #             print("串口收到消息:", self.com_rx_buf)
        #             self.com_rx_buf = ''
                    # al = bytesfind(self.com_rx_buf,b'US')
                    # # bl = bytesfind(self.com_rx_buf, b'UR')
                    # print('a')
                    # if al>0:
                    #     if len(self.com_rx_buf[al:]) > al+10:
                    #         # print('hello')
                    #         # print(self.com_rx_buf[al :al + 10])
                    #         # print(self.com_rx_buf[al+2:al+8])
                    #         self.angle_x = get_angle(self.com_rx_buf[al+2:al+4])
                    #         self.angle_y = get_angle(self.com_rx_buf[al + 4:al + 6])
                    #         self.angle_z = get_angle(self.com_rx_buf[al + 6:al + 8])
                    #         print(self.angle_x,self.angle_y,self.angle_z)
                    #         self.com_rx_buf = ''

            #
            # except Exception as e:
            #     print('ee')
            #     pass
                # self.serial_close()
            #if self.rev_run_flag == False:
                #break


    # def serial_encode(addr=0, command=0, param1=0, param0=0):
    #     buf = [addr, command, param1, param0, 0, 0, 0, 0]
    #     print(buf)
    #     return buf

    def serial_send_command(self):

        try:
            ret_len = self.COMM.write(self.com_tx_buf)
            print(ret_len)
        except Exception as E:
            print('Send error'+e)

    def run(self):
        self.thread1 = threading.Thread(target=self.thread_com_receive, args=(me=self)
        self.thread1.start()



if __name__ == '__main__':
    myserial = userial(3)
    myserial.serial_open(4)
    myserial.run()
    # #
    # s1 = b'L\x93'
    # ks =b']UT\x00\x00\x00\x00\x00\x00/\x07\xdf'
    # km = bytesfind(ks,b'US')
    #
    # print(getusererdata(s1))
    #print(get_angle(s1))
    # print(ks[8:10])
    # print(km)

