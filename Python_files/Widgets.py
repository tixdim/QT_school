import os, shutil, PIL.Image
import sys, json
from PyQt5.QtGui import QPixmap, QPainter, QColor, QIcon, QFont
from PyQt5.QtCore import Qt, QSize, QRect
from PyQt5 import uic, QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QButtonGroup,\
    QVBoxLayout, QScrollArea, QGraphicsDropShadowEffect, QFileDialog, QLineEdit, QTabWidget


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


class TheoryWidget(AnyWidget):
    def __init__(self, nickname):
        global Images_size
        global Pixmaps
        super().__init__('UI_files/TheoryWidget.ui', 'Теория')

        self.nickname = nickname

        for i in range(1, 59):

            eval(f'self.label_{i}.setFixedSize({Images[i - 1][0]}, {Images[i - 1][1]})')
            eval(f'self.label_{i}.setPixmap(Pixmaps[i - 1])')

        self.back.clicked.connect(self.go_to_menu)

    def go_to_menu(self):
        self.mai = Menu(self.nickname)
        self.mai.show()
        self.close()


class MainMenu(AnyWidget):
    def __init__(self, nickname):
        super().__init__('UI_files/menu_with_menu.ui', 'Меню (название переделать)')
        self.nicname = nickname

        self.Spravka_btn.clicked.connect(self.go_to_spravka)
        self.Menu_btn.clicked.connect(self.go_to_menu)
        self.Profile_btn.clicked.connect(self.go_to_profile)
        self.Exit_btn.clicked.connect(self.go_to_login)

    def go_to_spravka(self):
        self.spr = Spravka(self.nicname)
        self.spr.show()
        self.close()

    def go_to_menu(self):
        self.men = Menu(self.nicname)
        self.men.show()
        self.close()

    def go_to_profile(self):
        self.pro = Profile(self.nicname)
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

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(520, 600)

        self.back.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                        color=QtGui.QColor(234, 221, 186, 100)))
        self.front.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                         color=QtGui.QColor(105, 118, 132, 100)))
        self.pb_login.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3,
                                                                            color=QtGui.QColor(105, 118, 132, 100)))

        self.pb_close.clicked.connect(self.exit)
        self.pb_login.clicked.connect(self.sign_in)
        self.pb_regist.clicked.connect(self.sign_up)

        self.pb_eye_not.clicked.connect(self.off_pass)
        self.pb_eye_active.clicked.connect(self.on_pass)

        self.start_hidden_enabled()

    def start_hidden_enabled(self):
        self.pb_eye_active.setHidden(True)
        self.pb_eye_active.setEnabled(False)
        self.pb_eye_not.setHidden(False)
        self.pb_eye_not.setEnabled(True)

    def off_pass(self):
        self.user_password.setEchoMode(QLineEdit.Normal)
        self.pb_eye_not.setHidden(True)
        self.pb_eye_not.setEnabled(False)

        self.pb_eye_active.setHidden(False)
        self.pb_eye_active.setEnabled(True)

        self.pb_eye_active.setGeometry(350, 270, 21, 21)

        self.user_nickname.setEnabled(False)
        self.user_password.setEnabled(False)

        self.user_nickname.setEnabled(True)
        self.user_password.setEnabled(True)

    def on_pass(self):
        self.user_password.setEchoMode(QLineEdit.Password)
        self.pb_eye_active.setHidden(True)
        self.pb_eye_active.setEnabled(False)

        self.pb_eye_not.setHidden(False)
        self.pb_eye_not.setEnabled(True)

        self.user_nickname.setEnabled(False)
        self.user_password.setEnabled(False)

        self.user_nickname.setEnabled(True)
        self.user_password.setEnabled(True)

    def exit(self):
        sys.exit()

    def sign_up(self):
        self.regist = Regist()
        self.regist.show()
        self.close()

    def sign_in(self):
        user_nick = self.user_nickname.text()
        user_password = self.user_password.text()

        self.error.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.error.setAlignment(QtCore.Qt.AlignCenter)

        with open("users.json", "r", encoding="utf-8") as read_file:
            users = json.load(read_file)

        if user_nick in users:
            if users[user_nick]["password"] == user_password:
                self.glavn_menu = MainMenu(user_nick)
                self.glavn_menu.show()
                self.close()
            else:
                if user_password == "":
                    self.error.setText("Заполните пароль!")
                else:
                    self.error.setText("Вы ввели неправильный пароль!")
        else:
            self.error.setText("Такого никнейма нет!")


class Regist(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_files/SignUp.ui', self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(520, 600)

        self.back.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                        color=QtGui.QColor(234, 221, 186, 100)))
        self.front.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0,
                                                                         color=QtGui.QColor(105, 118, 132, 100)))
        self.pb_regist.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3,
                                                                            color=QtGui.QColor(105, 118, 132, 100)))

        self.pb_close.clicked.connect(self.exit)
        self.pb_back.clicked.connect(self.per_back)
        self.pb_regist.clicked.connect(self.sign_up)

        self.pb_eye_not_1.clicked.connect(self.off_pass_1)
        self.pb_eye_active_1.clicked.connect(self.on_pass_1)
        self.pb_eye_not_2.clicked.connect(self.off_pass_2)
        self.pb_eye_active_2.clicked.connect(self.on_pass_2)

        self.pb_eye_active_1.setHidden(True)
        self.pb_eye_active_1.setEnabled(False)
        self.pb_eye_not_1.setHidden(False)
        self.pb_eye_not_1.setEnabled(True)

        self.pb_eye_active_2.setHidden(True)
        self.pb_eye_active_2.setEnabled(False)
        self.pb_eye_not_2.setHidden(False)
        self.pb_eye_not_2.setEnabled(True)

    def off_pass_1(self):
        self.password_1.setEchoMode(QLineEdit.Normal)
        self.pb_eye_not_1.setHidden(True)
        self.pb_eye_not_1.setEnabled(False)

        self.pb_eye_active_1.setHidden(False)
        self.pb_eye_active_1.setEnabled(True)

        self.pb_eye_active_1.setGeometry(350, 320, 21, 21)

        self.nickname.setEnabled(False)
        self.name.setEnabled(False)
        self.surname.setEnabled(False)
        self.password_1.setEnabled(False)
        self.password_2.setEnabled(False)

        self.nickname.setEnabled(True)
        self.name.setEnabled(True)
        self.surname.setEnabled(True)
        self.password_1.setEnabled(True)
        self.password_2.setEnabled(True)

    def on_pass_1(self):
        self.password_1.setEchoMode(QLineEdit.Password)
        self.pb_eye_active_1.setHidden(True)
        self.pb_eye_active_1.setEnabled(False)

        self.pb_eye_not_1.setHidden(False)
        self.pb_eye_not_1.setEnabled(True)

        self.nickname.setEnabled(False)
        self.name.setEnabled(False)
        self.surname.setEnabled(False)
        self.password_1.setEnabled(False)
        self.password_2.setEnabled(False)

        self.nickname.setEnabled(True)
        self.name.setEnabled(True)
        self.surname.setEnabled(True)
        self.password_1.setEnabled(True)
        self.password_2.setEnabled(True)

    def off_pass_2(self):
        self.password_2.setEchoMode(QLineEdit.Normal)
        self.pb_eye_not_2.setHidden(True)
        self.pb_eye_not_2.setEnabled(False)

        self.pb_eye_active_2.setHidden(False)
        self.pb_eye_active_2.setEnabled(True)

        self.pb_eye_active_2.setGeometry(350, 380, 21, 21)

        self.nickname.setEnabled(False)
        self.name.setEnabled(False)
        self.surname.setEnabled(False)
        self.password_1.setEnabled(False)
        self.password_2.setEnabled(False)

        self.nickname.setEnabled(True)
        self.name.setEnabled(True)
        self.surname.setEnabled(True)
        self.password_1.setEnabled(True)
        self.password_2.setEnabled(True)

    def on_pass_2(self):
        self.password_2.setEchoMode(QLineEdit.Password)
        self.pb_eye_active_2.setHidden(True)
        self.pb_eye_active_2.setEnabled(False)

        self.pb_eye_not_2.setHidden(False)
        self.pb_eye_not_2.setEnabled(True)

        self.nickname.setEnabled(False)
        self.name.setEnabled(False)
        self.surname.setEnabled(False)
        self.password_1.setEnabled(False)
        self.password_2.setEnabled(False)

        self.nickname.setEnabled(True)
        self.name.setEnabled(True)
        self.surname.setEnabled(True)
        self.password_1.setEnabled(True)
        self.password_2.setEnabled(True)

    def exit(self):
        sys.exit()

    def per_back(self):
        self.signin = Login()
        self.signin.show()
        self.close()

    def sign_up(self):
        user_nick = self.nickname.text()
        user_name = self.name.text()
        user_surname = self.surname.text()
        user_password_1 = self.password_1.text()
        user_password_2 = self.password_2.text()

        self.error.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.error.setAlignment(QtCore.Qt.AlignCenter)

        if len(user_nick) == 0 or len(user_name) == 0 or len(user_surname) == 0:
            self.error.setText("Вы заполнили не все поля!")

        elif len(user_password_1) < 6 or len(user_password_2) < 6:
            self.error.setText("Длина пароля должна быть больше 6 символов!")

        elif user_password_1 != user_password_2:
            self.error.setText("Пароли не совпадают!")

        else:
            self.error.setText("")

            if not os.path.isfile("users.json"):
                with open("users.json", "w", encoding="utf-8") as write_file:
                    json.dump({}, write_file, indent=4, ensure_ascii=False)

            with open("users.json", "r", encoding="utf-8") as read_file:
                users = json.load(read_file)

            if user_nick in users:
                self.error.setText("Извините, такой никнейм уже занят!")
                return

            users[user_nick] = {
                "name": user_name,
                "surname": user_surname,
                "password": user_password_1
            }

            with open("users.json", "w", encoding="utf-8") as write_file:
                json.dump(users, write_file, indent=4, ensure_ascii=False)

            self.signin = Login()
            self.signin.show()
            self.close()


class Spravka(AnyWidget):
    def __init__(self, nickname):
        super().__init__('UI_files/Spravka.ui', 'Справка')
        self.nicname = nickname
        self.back.clicked.connect(self.go_to_main_menu)

    def go_to_main_menu(self):
        self.Main = MainMenu(self.nicname)
        self.Main.show()
        self.close()


class Exam(AnyWidget):
    def __init__(self, nickname):
        super().__init__('UI_files/Exam.ui', 'Экзамен')
        self.back.clicked.connect(self.go_to_menu)
        self.nickname = nickname

    def go_to_menu(self):
        self.men = Menu(self.nickname)
        self.men.show()
        self.close()


class Tren(AnyWidget):
    def __init__(self, nickname):
        super().__init__('UI_files/Tren.ui', 'Тренажер')
        self.back.clicked.connect(self.go_to_menu)
        self.nickname = nickname

    def go_to_menu(self):
        self.men = Menu(self.nickname)
        self.men.show()
        self.close()


class Menu(AnyWidget):
    def __init__(self, nickname):
        super().__init__('UI_files/Menu.ui', 'Меню')
        self.nickname = nickname
        self.Theo_btn.clicked.connect(self.go_to_Theo)
        self.Exam_btn.clicked.connect(self.go_to_Exam)
        self.Tren_btn.clicked.connect(self.go_to_Tren)
        self.back.clicked.connect(self.go_to_main)

    def go_to_main(self):
        self.mai = MainMenu(self.nickname)
        self.mai.show()
        self.close()

    def go_to_Theo(self):
        self.the = TheoryWidget(self.nickname)
        self.the.show()
        self.close()

    def go_to_Exam(self):
        self.exam = Exam(self.nickname)
        self.exam.show()
        self.close()

    def go_to_Tren(self):
        self.tren = Tren(self.nickname)
        self.tren.show()
        self.close()


class ChangeMenu(AnyWidget):
    def __init__(self, nickname):
        super().__init__('UI_files/ChangeMenu.ui', 'Изменить профиль')
        self.nicname = nickname
        self.pb_eye_active_1.setHidden(True)
        self.pb_eye_active_2.setHidden(True)

        if os.path.exists(f'users_avatars/{self.nicname}_img.png'):
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.nicname}_img.png);'
                                         f' border-radius: 60px')

        elif os.path.exists(f'users_avatars/{self.nicname}_img.jpg'):
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.nicname}_img.jpg);'
                                         f' border-radius: 60px')
        else:
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/standart_image.png);'
                                         f' border-radius: 60px')

        self.image_change_btn.clicked.connect(self.change_img)
        self.back.clicked.connect(self.go_to_profile)
        self.acept.clicked.connect(self.accept)
        self.pb_eye_not_1.clicked.connect(self.off_pass_1)
        self.pb_eye_active_1.clicked.connect(self.on_pass_1)
        self.pb_eye_not_2.clicked.connect(self.off_pass_2)
        self.pb_eye_active_2.clicked.connect(self.on_pass_2)

    def off_pass_1(self):
        self.password_1.setEchoMode(QLineEdit.Normal)
        self.pb_eye_not_1.setHidden(True)
        self.pb_eye_not_1.setEnabled(False)

        self.pb_eye_active_1.setHidden(False)
        self.pb_eye_active_1.setEnabled(True)

        self.pb_eye_active_1.setGeometry(870, 435, 30, 30)

        self.name.setEnabled(False)
        self.surname.setEnabled(False)
        self.password_1.setEnabled(False)
        self.password_2.setEnabled(False)
        self.image_change_btn.setEnabled(False)

        self.image_change_btn.setEnabled(True)
        self.name.setEnabled(True)
        self.surname.setEnabled(True)
        self.password_1.setEnabled(True)
        self.password_2.setEnabled(True)

    def on_pass_1(self):
        self.password_1.setEchoMode(QLineEdit.Password)
        self.pb_eye_active_1.setHidden(True)
        self.pb_eye_active_1.setEnabled(False)

        self.pb_eye_not_1.setHidden(False)
        self.pb_eye_not_1.setEnabled(True)

        self.name.setEnabled(False)
        self.surname.setEnabled(False)
        self.password_1.setEnabled(False)
        self.password_2.setEnabled(False)
        self.image_change_btn.setEnabled(False)

        self.image_change_btn.setEnabled(True)
        self.name.setEnabled(True)
        self.surname.setEnabled(True)
        self.password_1.setEnabled(True)
        self.password_2.setEnabled(True)

    def off_pass_2(self):
        self.password_2.setEchoMode(QLineEdit.Normal)
        self.pb_eye_not_2.setHidden(True)
        self.pb_eye_not_2.setEnabled(False)

        self.pb_eye_active_2.setHidden(False)
        self.pb_eye_active_2.setEnabled(True)

        self.pb_eye_active_2.setGeometry(870, 535, 30, 30)

        self.name.setEnabled(False)
        self.surname.setEnabled(False)
        self.password_1.setEnabled(False)
        self.password_2.setEnabled(False)
        self.image_change_btn.setEnabled(False)

        self.image_change_btn.setEnabled(True)
        self.name.setEnabled(True)
        self.surname.setEnabled(True)
        self.password_1.setEnabled(True)
        self.password_2.setEnabled(True)

    def on_pass_2(self):
        self.password_2.setEchoMode(QLineEdit.Password)
        self.pb_eye_active_2.setHidden(True)
        self.pb_eye_active_2.setEnabled(False)

        self.pb_eye_not_2.setHidden(False)
        self.pb_eye_not_2.setEnabled(True)

        self.name.setEnabled(False)
        self.surname.setEnabled(False)
        self.password_1.setEnabled(False)
        self.password_2.setEnabled(False)
        self.image_change_btn.setEnabled(False)

        self.image_change_btn.setEnabled(True)
        self.name.setEnabled(True)
        self.surname.setEnabled(True)
        self.password_1.setEnabled(True)
        self.password_2.setEnabled(True)

    def accept(self):
        user_name = self.name.text()
        user_surname = self.surname.text()
        user_password_1 = self.password_1.text()
        user_password_2 = self.password_2.text()
        with open("users.json", "r", encoding="utf-8") as read_file:
            user_file = json.load(read_file)[f'{self.nicname}']
            if user_name:
                pass
            else:
                user_name = user_file['name']
            if user_surname:
                pass
            else:
                user_surname = user_file['surname']
            if user_password_1 or user_password_2:
                pass
            else:
                user_password_1 = user_password_2 = user_file['password']

        self.error.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.error.setAlignment(QtCore.Qt.AlignCenter)

        if len(user_name) == 0 or len(user_surname) == 0:
            self.error.setText("Вы заполнили не все поля!")

        elif len(user_password_1) < 6 or len(user_password_2) < 6:
            self.error.setText("Длина пароля должна быть больше 6 символов!")

        elif user_password_1 != user_password_2:
            self.error.setText("Пароли не совпадают!")

        else:
            self.error.setText("Ваши данные сохранены")
            self.name.setText('')
            self.surname.setText('')
            self.password_1.setText('')
            self.password_2.setText('')

            if not os.path.isfile("users.json"):
                with open("users.json", "w", encoding="utf-8") as write_file:
                    json.dump({}, write_file, indent=4, ensure_ascii=False)

            with open("users.json", "r", encoding="utf-8") as read_file:
                users = json.load(read_file)

            users[self.nicname] = {
                "name": user_name,
                "surname": user_surname,
                "password": user_password_1
            }

            with open("users.json", "w", encoding="utf-8") as write_file:
                json.dump(users, write_file, indent=4, ensure_ascii=False)

    def go_to_profile(self):
        self.pro = Profile(self.nicname)
        self.pro.show()
        self.close()

    def change_img(self):
        try:
            file = QFileDialog.getOpenFileUrl(self,
                                              caption='Выбрать картинку',
                                              filter='Картинка (*.jpg);;Картинка (*.png)')[0]
            file_url = file.url()[8:]
            if not file_url:
                raise BaseException
            try:
                os.remove(f'users_avatars/{self.nicname}_img.jpg')
            except:
                try:
                    os.remove(f'users_avatars/{self.nicname}_img.png')
                except:
                    pass
            shutil.copy(file_url, "users_avatars")
            os.rename(f'users_avatars/{file_url[-1 * file_url[::-1].find("/"):]}',
                      f'users_avatars/{self.nicname}_img.{file_url[-3:]}')

            self.user_icon.setStyleSheet(f'border-radius:60px;'
                                         f'border-image: url(users_avatars/{self.nicname}_img.{file_url[-3:]})')
        except:
            pass


class Profile(AnyWidget):
    def __init__(self, nickname):
        super().__init__('UI_files/Profile.ui', 'Профиль')
        self.nicname = nickname
        with open("users.json", "r", encoding="utf-8") as read_file:
            user_data = json.load(read_file)[self.nicname]
            self.user_FI.setText(f'{user_data["name"]} {user_data["surname"]}')
            self.user_nickname.setText(self.nicname)
        self.widget = QWidget()
        self.num = 49
        self.vbox = QVBoxLayout()
        self.vbox.setGeometry(QRect(0, 0, 1341, 1000))

        if os.path.exists(f'users_avatars/{self.nicname}_img.png'):
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.nicname}_img.png);'
                                         f' border-radius: 60px')

        elif os.path.exists(f'users_avatars/{self.nicname}_img.jpg'):
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.nicname}_img.jpg);'
                                         f' border-radius: 60px')
        else:
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/standart_image.png);'
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
        self.back.clicked.connect(self.go_to_main_menu)

    def go_to_main_menu(self):
        self.men = MainMenu(self.nicname)
        self.men.show()
        self.close()

    def go_to_change(self):
        self.cha = ChangeMenu(self.nicname)
        self.cha.show()
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Pixmaps = [QPixmap(f'ege_po_borbe_theory/theory_{i}.png') for i in range(1, 59)]
    Images = []
    for i in range(1, 59):
        with PIL.Image.open(f'ege_po_borbe_theory/theory_{i}.png') as img:
            Images.append(img.size)
    ex = TheoryWidget("ДимASSS")
    # ex = Login()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())