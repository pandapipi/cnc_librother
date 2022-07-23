#coding:utf-8
import os
import traceback

from PyQt5.QtGui import QIcon, QPen
from PyQt5.QtWidgets import QApplication, QFileDialog
#import CNC_MAIN
import sys
from PyQt5 import uic, QtWidgets
import  serial_ui_handle  as sui_handle
from PyQt5.QtCore import Qt
import CNC_Conde_Compile as CNC_COMPILE
from PyQt5.QtGui import QPainter, QColor, QFont
import numpy as np
from PyQt5.QtWidgets import *               #导入pyqt的相关文件
#挂件所需要的库
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


#动态显示需要的线程库
import time,threading

#初始化挂件
hear_figure, hear_figure_x = plt.subplots()
canvas = FigureCanvas(hear_figure)

def dynamic_update_figure_data(sleep = 0.01):
    global hear_figure, hear_figure_x
    global thread_hear_flag, hear_pause_flag

    x = np.linspace(0.05, 10, 1000)
    y = np.cos(x)


    while 1:

        plt.plot(x, y, ls="-", lw=2, label="plot figure")
        canvas.draw()
        time.sleep(sleep)




def start_draw():
    #不能用.run()，不然会阻塞运行，不能动态显示
    draw_thread = threading.Thread(target=dynamic_update_figure_data, args=())
    draw_thread.start()


class MainWindow:
    u_id = ''
    u_passwd = ''
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("CNC_MAIN.ui")
        self.ui.pb_file_load.clicked.connect(self.file_load)
        self.ui.pb_code_edit_enable.clicked.connect(self.code_compile_enable_set)
        self.ui.pb_code_save.clicked.connect(self.code_save)
        self.ui.pb_code_compile.clicked.connect(self.code_compile)
        self.ui.tx_code.readOnly = False
    def file_load(self):
        try:
            cnc_file,_=QFileDialog.getOpenFileName(self.ui,'Open file','*\\','CNC files (*.CNC)')

            print(f"filename{cnc_file}")
            f = open(cnc_file,'r', encoding='utf-8')
            with f:
                udata = f.read()
                self.ui.tx_code.setPlainText(udata)
        except Exception as e:
            print(e.args)
            print('==')
            print(traceback.format_exc())

    def code_compile_enable_set(self):
        if self.ui.tx_code.isReadOnly():
            self.ui.tx_code.setReadOnly(False)
        else:
            self.ui.tx_code.setReadOnly(True)
        # self.ui.tx_code.readOnly = not self.ui.tx_code.readOnly
        # if self.ui.tx_code.focusPolicy == Qt.StrongFocus:
        #     self.ui.uitx_code.setFocusPolicy(Qt.NoFocus)
        # else:
        #     self.ui.tx_code.setFocusPolicy(Qt.StrongFocus)
        print(self.ui.tx_code.readOnly)
        print('click ed {}','tx_code')
    def code_save(self):
        file_name,_ = QFileDialog.getSaveFileName(self.ui, "文件保存", "C:\\Users\\Administrator\\Desktop",
                                                "CNC files (*.CNC);;all files(*.*)")
        print (file_name)
        if file_name is not None:
            with open(file=file_name, mode='a+', encoding='utf-8') as file:
                file.write(self.ui.tx_code.toPlainText())
            print('已保存！')
    def code_compile(self):

        uc = CNC_COMPILE.Code_Analysisi()
        print(uc.GrammaticalCheck(self.ui.tx_code.toPlainText()))
        uc.FindDischargeCondition(self.ui.tx_code.toPlainText())
    def update_display(self,position,):
        self.ui.label_X0.setText(position.x)
        self.ui.label_X0.setText(position.y)
        self.ui.label_X0.setText(position.z)
        self.ui.label_X0.setText(position.w)



if __name__ == '__main__':

    app = QApplication([])
    #app.setWindowIcon(QIcon("icon.ico"))
    main_window = MainWindow()

    child_window = sui_handle.child_window()
    main_window.ui.pb_sys_setting.clicked.connect(child_window.ui.show)
    main_window.ui.lh_display.addWidget(canvas)
    main_window.ui.pb_gathing_enable.clicked.connect(start_draw)
    main_window.ui.show()

    sys.exit(app.exec_())
