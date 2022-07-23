# 安装：pip3 install pyserial   //python3
import serial
import serial.tools.list_ports
import time
import threading
import PyQt5.QtCore as PQC


class userial:
    com_rx_buf = ''  # 接收缓冲区
    com_tx_buf = ''  # 发送缓冲区
    # COMM = serial.Serial()  # 定义串口对象
    port_list: list  # 可用串口列表
    port_select: list  # 选择好的串口
    COMM = None
    rev_data = ''
    rev_flag = False
    rev_run_flag = False
    angle_x = ""
    angle_y = ""
    angle_z = ""
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

    def thread_com_receive(self):

        while True:
            try:
                rx_buf = ''
                rx_buf = self.COMM.read()  # 转化为整型数字
                if rx_buf != b'':
                    time.sleep(0.01)
                    rx_buf = rx_buf + self.COMM.read_all()
                    print("串口收到消息:", rx_buf)
                    self.rev_data = rx_buf
                    self.rev_flag = True
                    # self.Signal_Sendmag.emit(rx_buf)
                    #self._stats.ui_update(rx_buf)
                time.sleep(0.01)
            except Exception as e:
                pass
                # self.serial_close()
            if self.rev_run_flag == False:
                break


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
        self.thread1 = threading.Thread(target=self.thread_com_receive)
        self.thread1.start()


if __name__ == '__main__':
    myserial = userial(3)
    # ulist = myserial.get_com_list()
    # print(ulist)
    #
    # if len(ulist) == 0:
    #     print('无可用串口')
    # else:
    #
    #     for i in range(0, len(ulist)):
    #
    #         print(ulist[i].name)
    #myserial.com_tx_buf = 'sendok'
    myserial.serial_open(4)
    # len = ulistport_list.__len__()
    # ulist.device =ulist.port_list[0].device
    # print(len, ulist.device)
    # myserial.serial_close()
    #myserial.serial_send_command()
    myserial.run()

    # 以下语句为阻止主线程结束退出，如果主线程结束，那么其附带的子线程也会随之强制结束
    # while True:
    #     time.sleep(3000)

