import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout
from PyQt5.QtCore import Qt
class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)
        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)
        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        self.setLayout(vbox)
        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()
    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
    def keyPressEvent(self, e):
        l = self.tb.toPlainText().split('\n')
        if e.key() == Qt.Key_Up:
            self.le.setText(str(l[0]))
        elif e.key() == Qt.Key_Down:
            self.le.setText(str(l[len(l) - 1]))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
