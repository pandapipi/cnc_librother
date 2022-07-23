from PyQt5.QtCore import *
#定义信号相关
class MyTypeSignal(QObject):
    #定义一个信号变量，1个参数
    sendmag=pyqtSignal(object)
    #发射函数
    def run(self):
        self.sendmag.emit('Hello')
#定义槽
class MySlot(QObject):
    #定义槽函数，参数msg用来表示信号变量的值
    def get(self,msg):
        print("信息"+msg)

#主函数
if __name__ == '__main__':
    send=MyTypeSignal()
    slot=MySlot()
    send.sendmag.connect(slot.get)#将信号变量与槽函数连接
    send.run()#运行发射函数，进行信号发射
