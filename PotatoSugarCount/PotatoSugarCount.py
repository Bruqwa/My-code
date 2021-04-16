import sys
from potato2 import *

class MyWin(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui=Ui_PotatoSugarCount()
        self.ui.setupUi(self)

        self.ui.Count_button.clicked.connect(self.count_result)

    def count_result(self):
        try:
            mpotato = float(self.ui.Line_potato_input.text())
            msugar = mpotato * 0.08
            vsugar = msugar * 0.06
            spoon = msugar * 0.25
            self.ui.Result1.setText(str(msugar))
            self.ui.Result2.setText(str(vsugar))
            self.ui.Result3.setText(str(spoon))
        except:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle('Ошибка ввода!')
            msg.setText('Введите корректные данные!')
            msg.setIcon(msg.Warning)
            msg.exec()

if __name__=="__main__":
    app=QtWidgets.QApplication(sys.argv)
    myapp=MyWin()
    myapp.show()
    sys.exit(app.exec_())