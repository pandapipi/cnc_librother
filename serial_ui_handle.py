import time

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
import serial_thread as serial_operater
from PyQt5 import uic
import serial_thread
import threading
import system_config as sysconfig

class child_window :
    u_id = ''
    u_passwd = ''
    u_portnamelist = []

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("serial.ui")
        self.serial_handle_total = serial_thread.userial(self)
        ulist = self.serial_handle_total.get_com_list()
        print(ulist)
        if len(ulist) == 0:
            print('无可用串口')
            self.u_portnamelist = []
        else:
            for i in range(0, len(ulist)):
                print(ulist[i])
                self.u_portnamelist.append(ulist[i].name)
        self.ui.cb_discharge_control.addItems(self.u_portnamelist)
        self.ui.cb_move_control.addItems(self.u_portnamelist)
        self.ui.cb_bus_com.addItems(self.u_portnamelist)

        self.ui.cb_comlist.addItems(self.u_portnamelist)
        self.ui.comboBox_Baud.addItem("9600")
        self.ui.comboBox_Baud.addItem("115200")
        self.ui.pb_open.clicked.connect(self.ui_open_com)
        self.ui.pb_shut.clicked.connect(self.ui_close_com)
        self.ui.pb_send.clicked.connect(self.send_data)
        # self.ui.cb_discharge.currentTextChanged.connect(self.changechannal(self.ui.cb_discharge))
        self.ui.pb_set_channal.clicked.connect(self.changechannal)
        # self.serial_handle_total.Signal_Sendmag.connect()

    def ui_open_com(self):
        self.commname = self.ui.cb_comlist.currentText()
        print(self.commname)
        self.serial_handle_total.serial_open(self.commname[3])
        self.serial_handle_total.run()

    def ui_close_com(self):
        self.serial_handle_total.serial_close()#self.commname[3])

        #threading.Thread._Thread__stop(self.serial_handle_total.thread1)

    def ui_update(self,ustring):
        print("ui_update-ustring:{}".format(ustring))

        #ustring = ustring.decode('ascii', 'ignore')  # 以字符串的格式接收需要重新转码
        #ustring = str(ustring, 'utf-8')  # 转换成 'utf-8' 编码
        # if self.ui.checkBox_16.isCheck():
        #     ustring =''.join(['%02X ' % b for b in ustring])
        #
        if self.ui.cb_16_mode.isChecked():
            ustring = ''.join(['%02X ' % b for b in ustring])

        if self.ui.cb_asc_mode.isChecked():
            ustring =ustring.hex()
        if self.ui.cb_Time_add.isChecked():
            ustring = ustring + '  '+'time:'+ str(time.time())

        self.ui.textEdit_rev.append(str(ustring))
    def send_data(self):
        ustring = self.ui.textEdit_send.toPlainText()
        print(ustring)
        #ustring = bytes.fromhex(ustring)
        if self.ui.cb_asc_mode.isChecked():
            self.serial_handle_total.com_tx_buf = ustring.encode('utf-8')
        if self.ui.cb_16_mode.isChecked():
            self.serial_handle_total.com_tx_buf = bytes.fromhex(ustring)
            print(self.serial_handle_total.com_tx_buf)
        try:
            self.serial_handle_total.serial_send_command()
        except:
            pass
    def changechannal(self):
        try:
            # print('start config')
            tx1 = self.ui.cb_discharge_control.currentText()
            tx2 = self.ui.cb_move_control.currentText()
            tx3 = self.ui.cb_bus_com.currentText()
            tx4 = self.ui.le_discharge_data_collection.text()
            tx5 = self.ui.le_relay_control.text()
            tx6 = self.ui.le_system_add.text()
            print(tx1,tx2)
            sysconfig.change_yam_data('Discharge_Com', tx1)
            sysconfig.change_yam_data('Move_Com', tx2)
            sysconfig.change_yam_data('Run_Bus_Com', tx3)
            sysconfig.change_yam_data('DischargeCollectionIP', tx4)
            sysconfig.change_yam_data('none', tx5)
            sysconfig.change_yam_data('SysIP', tx6)


        except:
            print('error')
            pass

    def closeEvent(self, event):
        self.serial_handle_total.serial_close()
if __name__ == '__main__':
    app = QApplication([])
    #app.setWindowIcon(QIcon("icon.ico"))
    stats = child_window ()
    stats.ui.show()
    sys.exit(app.exec_())