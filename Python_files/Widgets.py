import sys
from PyQt5.QtGui import QPixmap, QPainter, QColor, QIcon, QFont
from PyQt5 import uic, QtCore
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QButtonGroup,\
    QVBoxLayout, QScrollArea


class AnyWidget(QWidget):
    def __init__(self, ui_file, name):
        super().__init__()

        self.img = QPixmap('1.jpg')
        self.imageLabel = QLabel(self)
        self.imageLabel.move(0, 0)
        self.imageLabel.resize(1400, 800)
        self.imageLabel.setPixmap(self.img)

        uic.loadUi(ui_file, self)

        self.setWindowTitle(name)
        self.setFixedSize(1400, 800)


class MenuWithMenu(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/menu_with_menu.ui', 'Меню (название переделать)')
        self.Spravka_btn.clicked.connect(self.go_to_spravka)
        self.Menu_btn.clicked.connect(self.go_to_menu)
        self.Profile_btn.clicked.connect(self.go_to_profile)
        self.Exit_btn.clicked.connect(self.go_to_login)

    def go_to_spravka(self):
        self.spr = Spravka()
        self.spr.show()
        self.close()

    def go_to_menu(self):
        self.men = Menu()
        self.men.show()
        self.close()

    def go_to_profile(self):
        self.pro = Profile()
        self.pro.show()
        self.close()

    def go_to_login(self):
        self.log = Login()
        self.log.show()
        self.close()


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_files/LogIn.ui', self)

        self.back.setStyleSheet("background-color: #ffc0cb; border-radius: 25px;")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


class Spravka(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/Spravka.ui', 'Справка')


class Menu(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/Menu.ui', 'Меню')


class Profile(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/Profile.ui', 'Профиль')
        self.widget = QWidget()
        self.vbox = QVBoxLayout()

        for i in range(1, 50):
            font = QFont('MS Shell Dlg 2', 30)
            btn = QPushButton(f'Вариант {i}')
            btn.setFont(font)
            if i % 2 == 1:
                btn.setStyleSheet('background-color: rgba(223, 116, 153, 150); color: '
                                  'rgba(255, 255, 255, 150); text-align: left;')
            else:
                btn.setStyleSheet('background-color: rgba(158, 241, 162, 200); color: '
                                  'rgba(255, 255, 255, 150); text-align: left;')
            self.vbox.addWidget(btn)

        self.vbox.setSpacing(20)
        self.widget.setLayout(self.vbox)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Profile()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
