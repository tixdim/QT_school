import sys
from PyQt5.QtGui import QPixmap, QPainter, QColor, QIcon
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QButtonGroup


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
        super().__init__('menu_with_menu.ui', 'Меню (название переделать)')
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
        uic.loadUi('LogIn.ui', self)
        img = QPixmap('1.jpg')
        self.imageLabel.setPixmap(img)


class Spravka(AnyWidget):
    def __init__(self):
        super().__init__('Spravka.ui', 'Справка')


class Menu(AnyWidget):
    def __init__(self):
        super().__init__('Menu.ui', 'Меню')


class Profile(AnyWidget):
    def __init__(self):
        super().__init__('Profile.ui', 'Профиль')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Spravka()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())
