import sys
import dem1
from PyQt5.QtWidgets import QApplication, QMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建QApplication 代表整个应用程序 固定写法
    mainWindow = QMainWindow()  # 创建 mainWindow对象
    ui = dem1.Ui_MainWindow()  # 创建Ui_MainWindow类实例化
    ui.setupUi(mainWindow)     # 向主窗口添加控件
    mainWindow.show()
    sys.exit(app.exec_())      # 进入主循环

