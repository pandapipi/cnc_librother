import threading
from PyQt5.QtWidgets import QApplication, QMainWindow
#import CNC_MAIN
import sys
from PyQt5 import uic
class thread_class_test(threading.Thread):

    def __init__(self,parent):
        threading.Thread.__init__(self)
        self.parent = parent

    def run(self):
         print ("运行线程:", threading.current_thread().ident)

class Stats:
    u_id = ''
    u_passwd = ''
    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = uic.loadUi("serial.ui")
        print("主线程id:", threading.current_thread().ident)

        self.thread_class = thread_class_test(self)
        self.thread_class.start()

    #self.ui.pushButton.clicked.connect(self.click_success)

    def closeEvent(self, event):
        print("窗体关闭")

if __name__ == '__main__':
    app = QApplication([])
    #app.setWindowIcon(QIcon("icon.ico"))
    stats = Stats()
    stats.ui.show()
    sys.exit(app.exec_())