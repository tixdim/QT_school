import os, shutil
import sys, json
from PyQt5.QtGui import QPixmap, QPainter, QColor, QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QButtonGroup,\
    QVBoxLayout, QScrollArea, QGraphicsDropShadowEffect, QFileDialog, QLineEdit


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
        uic.loadUi('UI_files/SignIn.ui', self)

        self.back.setStyleSheet("background-color: #ffc0cb; border-radius: 25px;")
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(521, 600)

        self.back.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                        color=QtGui.QColor(234, 221, 186, 100)))
        self.front.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                         color=QtGui.QColor(105, 118, 132, 100)))
        self.pb_login.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3,
                                                                            color=QtGui.QColor(105, 118, 132, 100)))

        self.pb_close.clicked.connect(self.exit)
        self.pb_login.clicked.connect(self.log_in_menu)

    def exit(self):
        sys.exit()

    def log_in_menu(self):
        # проверка на правильность пароля и логина

        self.glavn_menu = MenuWithMenu()
        self.glavn_menu.show()
        self.close()


class Spravka(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/Spravka.ui', 'Справка')


class Menu(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/Menu.ui', 'Меню')


class ChangeMenu(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/ChangeMenu.ui', 'Изменить профиль')
        self.user_name = 'ДимASSS'    # json

        if os.path.exists(f'users_avatars/{self.user_name}_img.png'):
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.user_name}_img.png);'
                                         f' border-radius: 60px')

        else:
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.user_name}_img.jpg);'
                                         f' border-radius: 60px')

        self.image_change_btn.clicked.connect(self.change_img)

    def change_img(self):
        try:
            file = QFileDialog.getOpenFileUrl(caption='Выберите картинку')[0]
            file_url = file.url()[8:]
            if not file_url:
                raise BaseException
            try:
                os.remove(f'users_avatars/{self.user_name}_img.jpg')
            except:
                try:
                    os.remove(f'users_avatars/{self.user_name}_img.png')
                except:
                    pass
            shutil.copy(file_url, "users_avatars")
            os.rename(f'users_avatars/{file_url[-1 * file_url[::-1].find("/"):]}',
                      f'users_avatars/{self.user_name}_img.{file_url[-3:]}')

            self.user_icon.setStyleSheet(f'border-radius:60px;'
                                         f'border-image: url(users_avatars/{self.user_name}_img.{file_url[-3:]})')
        except:
            pass


class Profile(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/Profile.ui', 'Профиль')
        self.widget = QWidget()
        self.num = 49
        self.user_name = 'ДимASSS'            # переделать 100 проц (через json файл)
        self.vbox = QVBoxLayout()
        self.vbox.setGeometry(QRect(0, 0, 1341, 1000))

        if os.path.exists(f'users_avatars/{self.user_name}_img.png'):
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.user_name}_img.png);'
                                         f' border-radius: 60px')

        else:
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.user_name}_img.jpg);'
                                         f' border-radius: 60px')

        for i in range(1, 50):
            font = QFont('MS Shell Dlg 2', 30)
            btn = QPushButton(f'  Вариант {i}')
            btn.setFont(font)
            btn.setMaximumSize(QSize(1300, 120))
            btn.setMinimumSize(QSize(1300, 120))
            if i % 2 == 1:
                btn.setStyleSheet('background-color: rgba(223, 116, 153, 150); color: '
                                  'rgba(255, 255, 255, 150); text-align: left;'
                                  'border-radius: 25px')
            else:
                btn.setStyleSheet('background-color: rgba(158, 241, 162, 200); color: '
                                  'rgba(255, 255, 255, 150); text-align: left;'
                                  'border-radius: 25px')
            self.vbox.addWidget(btn)

        self.vbox.setSpacing(20)
        self.widget.setLayout(self.vbox)
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.widget)
        self.change_btn.clicked.connect(self.go_to_change)

    def go_to_change(self):
        self.cha = ChangeMenu()
        self.cha.show()
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Profile()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())