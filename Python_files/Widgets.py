import os, shutil, PIL.Image
import sys, json

from PyQt5.QtGui import QPixmap, QPainter, QColor, QIcon, QFont, QMovie
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


class Zastavka(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI_files/zast.ui', self)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(600, 600)


        gif = QtGui.QMovie(f"gif/1")
        self.label.setMovie(gif)
        gif.start()

    def keyPressEvent(self, a0: QtGui.QKeyEvent):
        self.log = Login()
        self.log.show()
        self.close()


class TheoryWidget(AnyWidget):
    def __init__(self):
        global nickname
        super().__init__('UI_files/TheoryWidget.ui', 'Теория')

        self.nickname = nickname

        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
                  27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48,
                  50, 51, 52, 53, 54, 55, 56, 57, 58]:
            pixmap = QPixmap(f'ege_po_borbe_theory/theory_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_theory/theory_{i}.png') as img:
                eval(f'self.label_{i}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i}.setPixmap(pixmap)')

        self.back.clicked.connect(self.go_to_menu)

    def go_to_menu(self):
        self.mai = Menu()
        self.mai.show()
        self.close()


class MainMenu(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/menu_with_menu.ui', ' ')

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
        self.anonim.clicked.connect(self.anonim_sign_in)

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

        self.pb_eye_active.setGeometry(350, 250, 21, 21)

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
        global nickname

        user_nick = self.user_nickname.text()
        user_password = self.user_password.text()

        self.error.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.error.setAlignment(QtCore.Qt.AlignCenter)

        try:
            with open("users.json", "r", encoding="utf-8") as read_file:
                users = json.load(read_file)

            if user_nick in users:
                if users[user_nick]["password"] == user_password:
                    nickname = user_nick
                    self.glavn_menu = MainMenu()
                    self.glavn_menu.show()
                    self.close()
                else:
                    if user_password == "":
                        self.error.setText("Заполните пароль!")
                    else:
                        self.error.setText("Вы ввели неправильный пароль!")
            else:
                self.error.setText("Такого никнейма нет!")
        except Exception:
            self.error.setText("Такого никнейма нет!")

    def anonim_sign_in(self):
        global nickname
        nickname = "anonymous_228_337.on@qwe"

        self.glavn_menu = MainMenu()
        self.glavn_menu.show()
        self.close()


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
                "password": user_password_1,
                "tren": {
                    "1": [0 for i in range(11)],
                    "2": [0 for i in range(11)],
                    "3": [0 for i in range(11)],
                    "4": [0 for i in range(11)],
                    "5": [0 for i in range(11)]
                }
            }

            with open("users.json", "w", encoding="utf-8") as write_file:
                json.dump(users, write_file, indent=4, ensure_ascii=False)

            self.signin = Login()
            self.signin.show()
            self.close()


class Spravka(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/Spravka.ui', 'Справка')
        self.back.clicked.connect(self.go_to_main_menu)

    def go_to_main_menu(self):
        self.Main = MainMenu()
        self.Main.show()
        self.close()


class Exam(AnyWidget): # меню с предложенными вариантами
    def __init__(self):
        global nickname
        super().__init__('UI_files/Exam.ui', 'Экзамен')
        self.back.clicked.connect(self.go_to_menu)
        self.nickname = nickname
        for i in range(1, 6):
            eval(f'self.exam_{i}.clicked.connect(self.go_to_EGE)')

    def go_to_EGE(self):
        global ege, pred_ege, otv_perv
        ege.clear()
        pred_ege.clear()
        otv_perv.clear()
        ege = [0] * 18
        pred_ege = [0] * 7
        otv_perv = [""] * 11

        self.Exam_Vars_1 = Exam_Vars_1(self.sender().text())
        self.Exam_Vars_1.show()
        self.close()

    def go_to_menu(self):
        self.men = Menu()
        self.men.show()
        self.close()


class Exam_Vars_1(AnyWidget): # задания из егэ № 1, 2, 3, 4
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_1.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        if self.egevar == "3":
            self.ans_1.setGeometry(1060, 100, 211, 61)
            self.label_2.setGeometry(100, 230, 0, 0)
            self.ans_2.setGeometry(1060, 280, 211, 61)
            self.label_3.setGeometry(100, 480, 0, 0)
            self.ans_3.setGeometry(1060, 480, 211, 61)
            self.ans_4.setGeometry(1060, 620, 211, 61)

        elif self.egevar == "4":
            self.ans_1.setGeometry(1060, 100, 211, 61)
            self.label_2.setGeometry(100, 260, 0, 0)
            self.ans_2.setGeometry(1060, 260, 211, 61)
            self.label_3.setGeometry(100, 420, 0, 0)
            self.ans_3.setGeometry(1060, 420, 211, 61)
            self.label_4.setGeometry(100, 590, 0, 0)
            self.ans_4.setGeometry(1060, 590, 211, 61)

        elif self.egevar == "5":
            self.label_2.setGeometry(100, 230, 0, 0)
            self.ans_2.setGeometry(1060, 240, 211, 61)
            self.label_3.setGeometry(100, 400, 0, 0)
            self.ans_3.setGeometry(1060, 410, 211, 61)
            self.label_4.setGeometry(100, 610, 0, 0)
            self.ans_4.setGeometry(1060, 610, 211, 61)

        for i in range(1, 5):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i}.setPixmap(Pixmap)')
            eval(f"self.ans_{i}.setText(otv_perv[{i - 1}])")

        self.var.setText(f"Вариант №{self.egevar}")

        self.back.clicked.connect(self.go_to_Exam)
        self.right.clicked.connect(self.go_to_Exam_Vars_2)

    def go_to_Exam_Vars_2(self):
        global otv_perv
        otv_perv[0], otv_perv[1], otv_perv[2], otv_perv[3] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text(), self.ans_4.text()

        self.Exam_Vars_2 = Exam_Vars_2(self.egevar)
        self.Exam_Vars_2.show()
        self.close()

    def go_to_Exam(self):
        self.Exam = Exam()
        self.Exam.show()
        self.close()


class Exam_Vars_2(AnyWidget): # задания из егэ № 5, 7
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_2.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        if self.egevar == "1":
            self.label_3.setGeometry(120, 250, 0, 0)
            self.ans_3.setGeometry(1060, 450, 211, 61)

            for i in range(5, 8, 2):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 4}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 4}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 4}.setText(otv_perv[{i - 1}])")

            self.label_2.setEnabled(False)
            self.label_2.setHidden(True)
            self.ans_2.setEnabled(False)
            self.ans_2.setHidden(True)

        elif self.egevar == "2":
            self.label_3.setGeometry(120, 590, 0, 0)
            self.ans_3.setGeometry(1060, 610, 211, 61)

            for i in range(5, 8):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 4}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 4}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 4}.setText(otv_perv[{i - 1}])")

        elif self.egevar == "3":
            self.label_1.setGeometry(120, 40, 0, 0)
            self.ans_1.setGeometry(1060, 90, 211, 61)

            self.label_3.setGeometry(120, 300, 0, 0)
            self.ans_3.setGeometry(1060, 380, 211, 61)

            self.label_2.setGeometry(120, 590, 0, 0)
            self.ans_2.setGeometry(1060, 620, 211, 61)

            for i in range(5, 8, 2):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 4}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 4}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 4}.setText(otv_perv[{i - 1}])")

            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_8.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_8.png') as img:
                eval(f'self.label_2.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_2.setPixmap(Pixmap)')
            eval(f"self.ans_2.setText(otv_perv[{7}])")

        elif self.egevar == "4":
            self.label_1.setGeometry(120, 50, 0, 0)
            self.ans_1.setGeometry(1060, 65, 211, 61)

            self.label_2.setGeometry(120, 190, 0, 0)
            self.ans_2.setGeometry(1060, 280, 211, 61)

            self.label_3.setGeometry(120, 570, 0, 0)
            self.ans_3.setGeometry(1060, 625, 211, 61)

            for i in range(5, 8):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 4}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 4}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 4}.setText(otv_perv[{i - 1}])")

        elif self.egevar == "5":
            self.label_1.setGeometry(120, 50, 0, 0)
            self.ans_1.setGeometry(1060, 75, 211, 61)

            self.label_2.setGeometry(120, 350, 0, 0)
            self.ans_2.setGeometry(1060, 390, 211, 61)

            self.label_3.setEnabled(False)
            self.label_3.setHidden(True)
            self.ans_3.setEnabled(False)
            self.ans_3.setHidden(True)

            for i in range(5, 7):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 4}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 4}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 4}.setText(otv_perv[{i - 1}])")

        self.left.clicked.connect(self.go_to_Exam_Vars_1)
        self.right.clicked.connect(self.go_to_Exam_Vars_3)

    def go_to_Exam_Vars_1(self):
        global otv_perv
        if self.egevar in "1":
            otv_perv[4], otv_perv[6] = self.ans_1.text(), self.ans_3.text()
        elif self.egevar in "24":
            otv_perv[4], otv_perv[5], otv_perv[6] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()
        elif self.egevar == "3":
            otv_perv[4], otv_perv[7], otv_perv[6] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()
        else:
            otv_perv[4], otv_perv[5] = self.ans_1.text(), self.ans_2.text()

        self.Exam_Vars_1 = Exam_Vars_1(self.egevar)
        self.Exam_Vars_1.show()
        self.close()

    def go_to_Exam_Vars_3(self):
        global otv_perv
        if self.egevar in "1":
            otv_perv[4], otv_perv[6] = self.ans_1.text(), self.ans_3.text()
        elif self.egevar in "24":
            otv_perv[4], otv_perv[5], otv_perv[6] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()
        elif self.egevar == "3":
            otv_perv[4], otv_perv[7], otv_perv[6] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()
        else:
            otv_perv[4], otv_perv[5] = self.ans_1.text(), self.ans_2.text()

        self.Exam_Vars_3 = Exam_Vars_3(self.egevar)
        self.Exam_Vars_3.show()
        self.close()


class Exam_Vars_3(AnyWidget): # задания из егэ № 6, 8, 9
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_3.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        if self.egevar == "1":
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_6.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_6.png') as img:
                eval(f'self.label_1.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_1.setPixmap(Pixmap)')
            eval(f"self.ans_1.setText(otv_perv[5])")

            for i in range(8, 10):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 6}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 6}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 6}.setText(otv_perv[{i - 1}])")

        elif self.egevar == "2":
            self.label_1.setEnabled(False)
            self.label_1.setHidden(True)
            self.ans_1.setEnabled(False)
            self.ans_1.setHidden(True)

            self.label_2.setGeometry(100, 70, 0, 0)
            self.ans_2.setGeometry(1060, 130, 211, 61)

            self.label_3.setGeometry(100, 320, 0, 0)
            self.ans_3.setGeometry(1060, 380, 211, 61)

            for i in range(8, 10):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 6}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 6}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 6}.setText(otv_perv[{i - 1}])")

        elif self.egevar == "3":
            self.label_1.setGeometry(100, 40, 0, 0)
            self.ans_1.setGeometry(1060, 100, 211, 61)
            self.label_2.setGeometry(100, 390, 0, 0)
            self.ans_2.setGeometry(1060, 420, 211, 61)

            self.label_3.setEnabled(False)
            self.label_3.setHidden(True)
            self.ans_3.setEnabled(False)
            self.ans_3.setHidden(True)

            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_6.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_6.png') as img:
                eval(f'self.label_1.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_1.setPixmap(Pixmap)')
            eval(f"self.ans_1.setText(otv_perv[5])")

            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_9.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_9.png') as img:
                eval(f'self.label_2.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_2.setPixmap(Pixmap)')
            eval(f"self.ans_2.setText(otv_perv[8])")

        elif self.egevar == "4":
            self.label_1.setGeometry(100, 80, 0, 0)
            self.ans_1.setGeometry(1060, 120, 211, 61)
            self.label_2.setGeometry(100, 330, 0, 0)
            self.ans_2.setGeometry(1060, 360, 211, 61)

            self.label_3.setEnabled(False)
            self.label_3.setHidden(True)
            self.ans_3.setEnabled(False)
            self.ans_3.setHidden(True)

            for i in range(8, 10):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 7}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 7}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 7}.setText(otv_perv[{i - 1}])")

        elif self.egevar == "5":
            self.label_1.setGeometry(100, 40, 0, 0)
            self.ans_1.setGeometry(1060, 80, 211, 61)
            self.label_2.setGeometry(100, 380, 0, 0)
            self.ans_2.setGeometry(1060, 405, 211, 61)
            self.label_3.setGeometry(100, 540, 0, 0)
            self.ans_3.setGeometry(1060, 550, 211, 61)

            for i in range(7, 10):
                Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
                with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                    eval(f'self.label_{i - 6}.setFixedSize({img.size[0]}, {img.size[1]})')
                eval(f'self.label_{i - 6}.setPixmap(Pixmap)')
                eval(f"self.ans_{i - 6}.setText(otv_perv[{i - 1}])")

        self.left.clicked.connect(self.go_to_Exam_Vars_2)
        self.right.clicked.connect(self.go_to_Exam_Vars_4)

    def go_to_Exam_Vars_2(self):
        global otv_perv
        if self.egevar == "1":
            otv_perv[5], otv_perv[7], otv_perv[8] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()
        elif self.egevar == "2":
            otv_perv[7], otv_perv[8] = self.ans_2.text(), self.ans_3.text()
        elif self.egevar == "3":
            otv_perv[5], otv_perv[8] = self.ans_1.text(), self.ans_2.text()
        elif self.egevar == "4":
            otv_perv[7], otv_perv[8] = self.ans_1.text(), self.ans_2.text()
        else:
            otv_perv[6], otv_perv[7], otv_perv[8] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()

        self.Exam_Vars_2 = Exam_Vars_2(self.egevar)
        self.Exam_Vars_2.show()
        self.close()

    def go_to_Exam_Vars_4(self):
        global otv_perv
        if self.egevar == "1":
            otv_perv[5], otv_perv[7], otv_perv[8] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()
        elif self.egevar == "2":
            otv_perv[7], otv_perv[8] = self.ans_2.text(), self.ans_3.text()
        elif self.egevar == "3":
            otv_perv[5], otv_perv[8] = self.ans_1.text(), self.ans_2.text()
        elif self.egevar == "4":
            otv_perv[7], otv_perv[8] = self.ans_1.text(), self.ans_2.text()
        else:
            otv_perv[6], otv_perv[7], otv_perv[8] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()

        self.Exam_Vars_4 = Exam_Vars_4(self.egevar)
        self.Exam_Vars_4.show()
        self.close()


class Exam_Vars_4(AnyWidget): # задания из егэ № 10, 11, 12, 13
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_4.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        if self.egevar == "2":
            self.label_1.setGeometry(100, 70, 0, 0)
            self.ans_1.setGeometry(1060, 90, 211, 61)

            self.label_2.setGeometry(100, 250, 0, 0)
            self.ans_2.setGeometry(1060, 270, 211, 61)

            self.label_5.setGeometry(50, 360, 1301, 71)
            self.label_3.setGeometry(100, 460, 0, 0)
            self.label_4.setGeometry(100, 640, 0, 0)

        elif self.egevar == "3":
            self.label_1.setGeometry(100, 70, 0, 0)
            self.ans_1.setGeometry(1060, 70, 211, 61)

            self.label_2.setGeometry(100, 230, 0, 0)
            self.ans_2.setGeometry(1060, 235, 211, 61)

            self.label_5.setGeometry(50, 360, 1301, 71)
            self.label_3.setGeometry(100, 440, 0, 0)
            self.label_4.setGeometry(100, 580, 0, 0)

        elif self.egevar == "4":
            self.label_1.setGeometry(100, 30, 0, 0)
            self.ans_1.setGeometry(1060, 60, 211, 61)

            self.label_2.setGeometry(100, 290, 0, 0)
            self.ans_2.setGeometry(1060, 280, 211, 61)

            self.label_5.setGeometry(50, 390, 1301, 71)
            self.label_3.setGeometry(100, 490, 0, 0)
            self.label_4.setGeometry(100, 610, 0, 0)

        elif self.egevar == "5":
            self.label_1.setGeometry(100, 30, 0, 0)
            self.ans_1.setGeometry(1060, 80, 211, 61)

            self.label_2.setGeometry(100, 315, 0, 0)
            self.ans_2.setGeometry(1060, 305, 211, 61)

            self.label_5.setGeometry(50, 370, 1301, 71)
            self.label_3.setGeometry(100, 450, 0, 0)
            self.label_4.setGeometry(100, 570, 0, 0)

        for i in range(10, 14):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i - 9}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i - 9}.setPixmap(Pixmap)')
            if i in [10, 11]:
                eval(f"self.ans_{i - 9}.setText(otv_perv[{i - 1}])")

        self.left.clicked.connect(self.go_to_Exam_Vars_3)
        self.right.clicked.connect(self.go_to_Exam_Vars_5)

    def go_to_Exam_Vars_3(self):
        global otv_perv
        otv_perv[9], otv_perv[10] = self.ans_1.text(), self.ans_2.text()

        self.Exam_Vars_3 = Exam_Vars_3(self.egevar)
        self.Exam_Vars_3.show()
        self.close()

    def go_to_Exam_Vars_5(self):
        global otv_perv
        otv_perv[9], otv_perv[10] = self.ans_1.text(), self.ans_2.text()

        self.Exam_Vars_5 = Exam_Vars_5(self.egevar)
        self.Exam_Vars_5.show()
        self.close()


class Exam_Vars_5(AnyWidget): # задания из егэ № 14, 15, 16
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_5.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        if self.egevar == "2":
            self.label_1.setGeometry(160, 100, 0, 0)
            self.label_2.setGeometry(160, 240, 0, 0)
            self.label_3.setGeometry(160, 550, 0, 0)

        elif self.egevar == "3":
            self.label_1.setGeometry(160, 80, 0, 0)
            self.label_2.setGeometry(160, 260, 0, 0)
            self.label_3.setGeometry(160, 520, 0, 0)

        elif self.egevar == "4":
            self.label_1.setGeometry(160, 80, 0, 0)
            self.label_2.setGeometry(160, 265, 0, 0)
            self.label_3.setGeometry(160, 520, 0, 0)

        elif self.egevar == "5":
            self.label_1.setGeometry(160, 60, 0, 0)
            self.label_2.setGeometry(160, 160, 0, 0)
            self.label_3.setGeometry(160, 500, 0, 0)

        for i in range(14, 17):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i - 13}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i - 13}.setPixmap(Pixmap)')

        self.left.clicked.connect(self.go_to_Exam_Vars_4)
        self.right.clicked.connect(self.go_to_Exam_Vars_6)

    def go_to_Exam_Vars_4(self):
        self.Exam_Vars_4 = Exam_Vars_4(self.egevar)
        self.Exam_Vars_4.show()
        self.close()

    def go_to_Exam_Vars_6(self):
        self.Exam_Vars_6 = Exam_Vars_6(self.egevar)
        self.Exam_Vars_6.show()
        self.close()


class Exam_Vars_6(AnyWidget): # задания из егэ № 17, 18
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_6.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        if self.egevar == "2":
            self.label_1.setGeometry(160, 100, 0, 0)
            self.label_2.setGeometry(160, 350, 0, 0)

        elif self.egevar == "4":
            self.label_1.setGeometry(160, 100, 0, 0)
            self.label_2.setGeometry(160, 390, 0, 0)

        for i in range(17, 19):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i - 16}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i - 16}.setPixmap(Pixmap)')

        self.left.clicked.connect(self.go_to_Exam_Vars_5)
        self.save.clicked.connect(self.go_to_Exam_Vars_7)

    def go_to_Exam_Vars_5(self):
        self.Exam_Vars_5 = Exam_Vars_5(self.egevar)
        self.Exam_Vars_5.show()
        self.close()

    def go_to_Exam_Vars_7(self):
        self.Exam_Vars_7 = Exam_Vars_7(self.egevar)
        self.Exam_Vars_7.show()
        self.close()


class Exam_Vars_7(AnyWidget): # меню для перехода к оценке второй части
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_7.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        self.back.clicked.connect(self.go_to_Exam_Vars_6)
        self.krit.clicked.connect(self.go_to_krit)
        self.itogi.clicked.connect(self.go_to_itogi)

        for i in range(7):
            eval(f'self.ex_{i + 12}.clicked.connect(self.go_to_Razb)')

    def go_to_Exam_Vars_6(self):
        self.Exam_Vars_6 = Exam_Vars_6(self.egevar)
        self.Exam_Vars_6.show()
        self.close()

    def go_to_krit(self):
        self.Exam_Vars_8 = Exam_Vars_8(self.egevar)
        self.Exam_Vars_8.show()
        self.close()

    def go_to_Razb(self):
        self.Exam_Vars_9 = Exam_Vars_9(self.egevar, self.sender().text())
        self.Exam_Vars_9.show()
        self.close()

    def go_to_itogi(self):
        global ege, otv_perv

        with open("ege_po_borbe_exam/otvete.json", "r", encoding="utf-8") as f:
            otvete = json.load(f)[f"var_{self.egevar}"]

        for i in range(11):
            try:
                if "," in otv_perv[i]:
                    otv_perv[i] = otv_perv[i].replace(",", ".")
                if float(otvete[str(i + 1)]) == float(otv_perv[i]):
                    ege[i] = 1
            except Exception:
                ege[i] = 0

        self.Exam_Vars_10 = Exam_Vars_10(self.egevar)
        self.Exam_Vars_10.show()
        self.close()


class Exam_Vars_8(AnyWidget): # критерии
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_8.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        for i in range(7):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/crit_{i + 12}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/crit_{i + 12}.png') as img:
                eval(f'self.label_{i + 1}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i + 1}.setPixmap(Pixmap)')

        self.back.clicked.connect(self.go_to_Exam_Vars_7)

    def go_to_Exam_Vars_7(self):
        self.Exam_Vars_7 = Exam_Vars_7(self.egevar)
        self.Exam_Vars_7.show()
        self.close()


class Exam_Vars_9(AnyWidget): # оценка заданий второй части
    def __init__(self, egevar, number):
        super().__init__('UI_files/Exam_Vars_9.ui', f'Вариант №{egevar}')
        self.egevar = egevar
        self.number = number

        self.text.setText(f"Решение задания №{number}")

        Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/resh_{number}.png')
        self.label.setPixmap(Pixmap)

        if self.number in ("13", "16"):
            self.rb_5.setHidden(True)
            self.rb_5.setEnabled(False)
        elif self.number in ["12", "14", "15"]:
            self.rb_5.setHidden(True)
            self.rb_5.setEnabled(False)
            self.rb_4.setHidden(True)
            self.rb_4.setEnabled(False)

        for i in range(5):
            eval(f"self.rb_{i + 1}.toggled.connect(self.onClicked)")

        eval(f"self.rb_{ege[int(self.number) - 1] + 1}.setChecked(True)")

        self.back.clicked.connect(self.go_to_Exam_Vars_7)
        self.save.clicked.connect(self.save_and_goex)

    def onClicked(self):
        global pred_ege
        radioButton = self.sender()
        if radioButton.isChecked():
            pred_ege[int(self.number) - 12] = int(radioButton.text())

    def save_and_goex(self):
        global pred_ege, ege
        ege[int(self.number) - 1] = pred_ege[int(self.number) - 12]
        self.Exam_Vars_7 = Exam_Vars_7(self.egevar)
        self.Exam_Vars_7.show()
        self.close()

    def go_to_Exam_Vars_7(self):
        self.Exam_Vars_7 = Exam_Vars_7(self.egevar)
        self.Exam_Vars_7.show()
        self.close()


class Exam_Vars_10(AnyWidget): # итоговый результат
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_10.ui', f'Вариант №{egevar}')
        self.egevar = egevar
        self.UI()

    def UI(self):
        self.var.setText(f"Результат выполнения {self.egevar} варианта")
        self.var.setStyleSheet('color:#ffffff;')

        with open("ege_po_borbe_exam/otvete.json", "r", encoding="utf-8") as f:
            otvete = json.load(f)[f"var_{self.egevar}"]

        for i in range(1, 12):
            eval(f"self.ans_{i}.setText(str({otvete[str(i)]}))")

            eval(f"self.u_ans_{i}.setText(str({otv_perv[i - 1]}))")
            if otv_perv[i - 1].replace(" ", "") == "":
                eval(f"self.u_ans_{i}.setStyleSheet('color: #ffffff; border-style: solid; "
                    f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                    f"border-bottom-width: 1px; border-left-width: 1px;')")
            elif ege[i - 1] == 0:
                eval(f"self.u_ans_{i}.setStyleSheet('background-color: rgba(255, 0, 0, 155); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")
            else:
                eval(f"self.u_ans_{i}.setStyleSheet('background-color: rgba(50, 205, 50, 180); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")

        max_vt_chast = {12: 2, 13: 3, 14: 2, 15: 2, 16: 3, 17: 4, 18: 4}

        for i in range(12, 19):
            eval(f"self.u_point_{i}.setText(str({ege[i - 1]}))")
            if ege[i - 1] == 0:
                eval(f"self.u_point_{i}.setStyleSheet('background-color: rgba(255, 0, 0, 155); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")
            elif ege[i - 1] == max_vt_chast[i]:
                eval(f"self.u_point_{i}.setStyleSheet('background-color: rgba(50, 205, 50, 180); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")
            else:
                eval(f"self.u_point_{i}.setStyleSheet('background-color: rgba(255, 215, 0, 175); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")

        perevod_points = [6, 11, 17, 22, 27, 34, 40, 46, 52, 58, 64, 66, 68, 70, 72, 74, 76, 78,
                          80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 100, 100]
        if sum(ege) == 0:
            self.itog_point = 0
        else:
            self.itog_point = perevod_points[sum(ege) - 1]

        if self.itog_point % 10 == 1 and self.itog_point != 11:
            self.text = "балл"
        elif (self.itog_point % 10 == 2 and self.itog_point != 12) or (self.itog_point % 10 == 3 and self.itog_point != 13) or \
                (self.itog_point % 10 == 4 and self.itog_point != 14):
            self.text = "балла"
        else:
            self.text = "баллов"

        self.resh_zad = sum([1 if i > 0 else 0 for i in ege])

        if self.itog_point >= 27:
            proyden_porog = "пройден"
            color = "rgba(50, 205, 50, 225)"
        else:
            proyden_porog = "не пройден"
            color = "rgba(255, 0, 0, 195)"

        if self.resh_zad == 1:
            self.text_zad = "задание"
        elif self.resh_zad in [2, 3, 4]:
            self.text_zad = "задания"
        else:
            self.text_zad = "заданий"

        perv_ballov = sum(ege)
        if perv_ballov % 10 == 1 and perv_ballov != 11:
            self.text_perv_ballov = "первичный балл"
        elif (perv_ballov % 10 == 2 and perv_ballov != 12) or (perv_ballov % 10 == 3 and perv_ballov != 13)\
                or (perv_ballov % 10 == 4 and perv_ballov != 14):
            self.text_perv_ballov = "первичных балла"
        else:
            self.text_perv_ballov = "первичных баллов"

        self.itogo.setText(f"Вы набрали {self.itog_point} {self.text} из 100")
        self.porog.setText(f'''<html><head/><body>
            <p>Решено {self.resh_zad} {self.text_zad} из 18, набрано {sum(ege)} {self.text_perv_ballov}, </p>
            <p>что соответствует {self.itog_point} баллам по стобалльной шкале.</p>
            <p>В 2022 году порог для получения аттестата </p>
            <p>составляет 27 баллов, <span style="text-decoration: underline;color: {color}">порог {proyden_porog}.</span></p>
            </body></html>''')

        self.bt_prof.clicked.connect(self.go_to_Profile)
        self.back.clicked.connect(self.go_to_Exam_Vars_7)
        self.resh_per.clicked.connect(self.go_to_Exam_Vars_11)

    def go_to_Exam_Vars_7(self):
        self.Exam_Vars_7 = Exam_Vars_7(self.egevar)
        self.Exam_Vars_7.show()
        self.close()

    def go_to_Exam_Vars_11(self):
        self.Exam_Vars_11 = Exam_Vars_11(self.egevar)
        self.Exam_Vars_11.show()
        self.close()

    def go_to_Profile(self):
        if nickname != "anonymous_228_337.on@qwe":
            with open("users.json", "r", encoding="utf-8") as read_file:
                users = json.load(read_file)

            info_var = {"var": self.egevar, "vsego_points": self.itog_point, "text": self.text,
                        "resh_zad": self.resh_zad, "text_perv_ballov": self.text_perv_ballov,
                        "text_zad": self.text_zad, "ege": ege}

            for i in range(1, 12):
                info_var[i] = otv_perv[i - 1]
            for i in range(12, 19):
                info_var[i] = ege[i - 1]

            if 'vars' in users[nickname]:
                users[nickname]["vars"][len(users[nickname]["vars"]) + 1] = info_var
            else:
                users[nickname]["vars"] = {"1": info_var}

            with open("users.json", "w", encoding="utf-8") as write_file:
                json.dump(users, write_file, indent=4, ensure_ascii=False)

        self.Profile = Profile()
        self.Profile.show()
        self.close()


class Exam_Vars_11(AnyWidget): # меню с предложенными номерами заданий
    def __init__(self, egevar):
        global nickname
        super().__init__('UI_files/Exam_Vars_11.ui', 'Экзамен')

        self.egevar = egevar

        for i in range(1, 12):
            eval(f'self.exam_{i}.clicked.connect(self.go_to_Resh)')

        self.back.clicked.connect(self.go_to_Exam_Vars_10)

    def go_to_Resh(self):
        self.Exam_Vars_12 = Exam_Vars_12(self.egevar, self.sender().text())
        self.Exam_Vars_12.show()
        self.close()

    def go_to_Exam_Vars_10(self):
        self.Exam_Vars_10 = Exam_Vars_10(self.egevar)
        self.Exam_Vars_10.show()
        self.close()


class Exam_Vars_12(AnyWidget): # разбор первой части
    def __init__(self, egevar, number):
        super().__init__('UI_files/Exam_Vars_12.ui', f'Вариант №{egevar}')
        self.egevar = egevar
        self.number = number

        self.label.setText(f"Решения задания №{self.number}")

        Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/razb_{self.number}.png')
        with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/razb_{self.number}.png') as img:
            eval(f'self.label_1.setFixedSize({img.size[0]}, {img.size[1]})')
        eval(f'self.label_1.setPixmap(Pixmap)')

        self.back.clicked.connect(self.go_to_Exam_Vars_11)

    def go_to_Exam_Vars_11(self):
        self.Exam_Vars_11 = Exam_Vars_11(self.egevar)
        self.Exam_Vars_11.show()
        self.close()


class Info_Vars(AnyWidget):
    def __init__(self, popitka, egevar):
        super().__init__('UI_files/Exam_Vars_10.ui', f'Вариант №{egevar}')
        self.popitka = popitka
        self.egevar = egevar
        self.UI()

    def UI(self):
        self.var.setText(f"Результат выполнения {self.egevar} варианта")
        self.var.setStyleSheet('color:#ffffff;')

        with open("ege_po_borbe_exam/otvete.json", "r", encoding="utf-8") as f:
            otvete = json.load(f)[f"var_{self.egevar}"]

        with open("users.json", "r", encoding="utf-8") as read_file:
            info = json.load(read_file)[nickname]["vars"][str(self.popitka)]

        self.itog_point, self.text, self.resh_zad, self.text_perv_ballov, self.text_zad, self.ege_var = info["vsego_points"], \
            info["text"], info["resh_zad"], info["text_perv_ballov"], info["text_zad"], info["ege"],

        for i in range(1, 12):
            eval(f"self.ans_{i}.setText(str({otvete[str(i)]}))")

            eval(f"self.u_ans_{i}.setText(str({info[str(i)]}))")
            if info[str(i)].replace(" ", "") == "":
                eval(f"self.u_ans_{i}.setStyleSheet('color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")
            elif self.ege_var[i - 1] == 0:
                eval(f"self.u_ans_{i}.setStyleSheet('background-color: rgba(255, 0, 0, 155); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")
            else:
                eval(f"self.u_ans_{i}.setStyleSheet('background-color: rgba(50, 205, 50, 180); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")

        max_vt_chast = {12: 2, 13: 3, 14: 2, 15: 2, 16: 3, 17: 4, 18: 4}

        for i in range(12, 19):
            eval(f"self.u_point_{i}.setText(str({self.ege_var[i - 1]}))")
            if self.ege_var[i - 1] == 0:
                eval(f"self.u_point_{i}.setStyleSheet('background-color: rgba(255, 0, 0, 155); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")
            elif self.ege_var[i - 1] == max_vt_chast[i]:
                eval(f"self.u_point_{i}.setStyleSheet('background-color: rgba(50, 205, 50, 180); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")
            else:
                eval(f"self.u_point_{i}.setStyleSheet('background-color: rgba(255, 215, 0, 175); "
                     f"color: #ffffff; border-style: solid; "
                     f"border-color: black;border-top-width: 0px; border-right-width: 1px; "
                     f"border-bottom-width: 1px; border-left-width: 1px;')")

        perevod_points = [6, 11, 17, 22, 27, 34, 40, 46, 52, 58, 64, 66, 68, 70, 72, 74, 76, 78,
                          80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100, 100, 100]

        if self.itog_point >= 27:
            proyden_porog = "пройден"
            color = "rgba(50, 205, 50, 225)"
        else:
            proyden_porog = "не пройден"
            color = "rgba(255, 0, 0, 195)"

        self.itogo.setText(f"Вы набрали {self.itog_point} {self.text} из 100")
        self.porog.setText(f'''<html><head/><body>
            <p>Решено {self.resh_zad} {self.text_zad} из 18, набрано {sum(self.ege_var)} {self.text_perv_ballov}, </p>
            <p>что соответствует {self.itog_point} баллам по стобалльной шкале.</p>
            <p>В 2022 году порог для получения аттестата </p>
            <p>составляет 27 баллов, <span style="text-decoration: underline;color: {color}">порог {proyden_porog}.</span></p>
            </body></html>''')

        self.back.clicked.connect(self.go_to_Profile)
        self.bt_prof.setEnabled(False)
        self.bt_prof.setHidden(True)

    def go_to_Profile(self):
        self.pro = Profile()
        self.pro.show()
        self.close()


class Correct_ans(AnyWidget):
    def __init__(self, exNum, exVar):
        super().__init__('UI_files/Correct_aans.ui', 'Подробное решение')
        self.exNum = exNum
        self.exVar = exVar
        Pixmap = QPixmap(f'ege_po_borbe_tren/var_{exVar}/ans/exer_{exNum}.png')
        self.label.setPixmap(Pixmap)
        self.exNumber.setText(f"Тип задания №{exNum}")

        self.back.clicked.connect(self.go_to_ex)

    def go_to_ex(self):
        self.ex = Exercise(self.exNum, self.exVar)
        self.ex.show()
        self.close()


class Exercise(AnyWidget):
    def __init__(self, exNum, exVar):
        super().__init__('UI_files/Exercise.ui', ' ')
        self.exNum = exNum
        self.exVar = exVar
        Pixmap = QPixmap(f'ege_po_borbe_tren/var_{exVar}/exer_{exNum}.png')
        with PIL.Image.open(f'ege_po_borbe_tren/var_{exVar}/exer_{exNum}.png') as img:
            self.label.setFixedSize(*img.size)
        self.exNumber.setText(f"Тип задания №{exNum}")
        self.label.setPixmap(Pixmap)

        if int(exNum) <= 11:
            self.second_part.setHidden(True)
        else:
            self.ans.setEnabled(False)
            self.ans.setHidden(True)
            self.check_ans.setHidden(True)
            self.check_ans.setEnabled(False)

        self.check_ans.clicked.connect(self.check_answer)
        self.back.clicked.connect(self.go_to_Tren_Variants)
        self.see_right.clicked.connect(self.go_to_correct_ans)

    def check_answer(self):
        with open("ege_po_borbe_tren/answers.json", 'r', encoding="utf-8") as read_file:
            ans = json.load(read_file)
            if self.ans.text().replace(',', '.') == str(ans[f'var_{self.exVar}'][self.exNum]):
                self.right_or_no.setText('Правильно!')

                with open("users.json", "r", encoding="utf-8") as read_file:
                    users = json.load(read_file)
                users[nickname]["tren"][str(self.exVar)][int(self.exNum) - 1] = 1

            else:
                self.right_or_no.setText('Неправильно!')

                with open("users.json", "r", encoding="utf-8") as read_file:
                    users = json.load(read_file)
                users[nickname]["tren"][str(self.exVar)][int(self.exNum) - 1] = 2

        with open("users.json", "w", encoding="utf-8") as write_file:
            json.dump(users, write_file, indent=4, ensure_ascii=False)


    def go_to_correct_ans(self):
        self.cor = Correct_ans(self.exNum, self.exVar)
        self.cor.show()
        self.close()

    def go_to_Tren_Variants(self):
        self.Tren = Tren_Variants(self.exNum)
        self.Tren.show()
        self.close()


class Tren_Variants(AnyWidget):
    def __init__(self, exer):
        global nickname
        super().__init__('UI_files/Tren_Vars.ui', 'Выбор варианта')
        self.exer = exer
        self.nickname = nickname

        if nickname != "anonymous_228_337.on@qwe":
            ok_pix = QPixmap('Images/Ok.png')
            not_ok_pix = QPixmap('Images/notOk.png')
            if int(exer) <= 11:
                with open("users.json", 'r', encoding="utf-8") as ab:
                    users = json.load(ab)
                    for i in range(1, 6):
                        if users[self.nickname]['tren'][str(i)][int(self.exer) - 1] == 1:
                            eval(f'self.ex_complited_{i}.setPixmap(ok_pix)')
                        elif users[self.nickname]['tren'][str(i)][int(self.exer) - 1] == 2:
                            eval(f'self.ex_complited_{i}.setPixmap(not_ok_pix)')

        self.back.clicked.connect(self.go_to_Tren)
        for i in range(1, 6):
            eval(f'self.var_{i}.clicked.connect(self.go_to_exercise)')

    def go_to_exercise(self):
        self.exer = Exercise(self.exer, self.sender().text())
        self.exer.show()
        self.close()

    def go_to_Tren(self):
        self.Tren = Tren()
        self.Tren.show()
        self.close()


class Tren(AnyWidget):
    def __init__(self):
        global nickname
        super().__init__('UI_files/Tren.ui', 'Выбор задания')
        self.back.clicked.connect(self.go_to_menu)
        self.nickname = nickname
        for i in range(1, 19):
            eval(f'self.exercise_{i}.clicked.connect(self.go_to_Tren_variants)')

    def go_to_Tren_variants(self):
        self.Tren_vars = Tren_Variants(self.sender().text())
        self.Tren_vars.show()
        self.close()

    def go_to_menu(self):
        self.men = Menu()
        self.men.show()
        self.close()


class Menu(AnyWidget):
    def __init__(self):
        super().__init__('UI_files/Menu.ui', 'Меню')
        self.Theo_btn.clicked.connect(self.go_to_Theo)
        self.Exam_btn.clicked.connect(self.go_to_Exam)
        self.Tren_btn.clicked.connect(self.go_to_Tren)
        self.back.clicked.connect(self.go_to_main)

    def go_to_main(self):
        self.mai = MainMenu()
        self.mai.show()
        self.close()

    def go_to_Theo(self):
        global theo

        theo.show()
        self.close()

    def go_to_Exam(self):
        self.exam = Exam()
        self.exam.show()
        self.close()

    def go_to_Tren(self):
        self.tren = Tren()
        self.tren.show()
        self.close()


class ChangeMenu(AnyWidget):
    def __init__(self):
        global nickname
        super().__init__('UI_files/ChangeMenu.ui', 'Изменить профиль')
        self.nickname = nickname
        self.pb_eye_active_1.setHidden(True)
        self.pb_eye_active_2.setHidden(True)

        if os.path.exists(f'users_avatars/{self.nickname}_img.png'):
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.nickname}_img.png);'
                                         f' border-radius: 60px')

        elif os.path.exists(f'users_avatars/{self.nickname}_img.jpg'):
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.nickname}_img.jpg);'
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
            user_file = json.load(read_file)[f'{self.nickname}']
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

            users[self.nickname] = {
                "name": user_name,
                "surname": user_surname,
                "password": user_password_1
            }

            with open("users.json", "w", encoding="utf-8") as write_file:
                json.dump(users, write_file, indent=4, ensure_ascii=False)

    def go_to_profile(self):
        self.pro = Profile()
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
                os.remove(f'users_avatars/{self.nickname}_img.jpg')
            except:
                try:
                    os.remove(f'users_avatars/{self.nickname}_img.png')
                except:
                    pass
            shutil.copy(file_url, "users_avatars")
            os.rename(f'users_avatars/{file_url[-1 * file_url[::-1].find("/"):]}',
                      f'users_avatars/{self.nickname}_img.{file_url[-3:]}')

            self.user_icon.setStyleSheet(f'border-radius:60px;'
                                         f'border-image: url(users_avatars/{self.nickname}_img.{file_url[-3:]})')
        except:
            pass


class Profile(AnyWidget):
    def __init__(self):
        global nickname
        super().__init__('UI_files/Profile.ui', 'Профиль')
        self.nickname = nickname

        if nickname != "anonymous_228_337.on@qwe":
            with open("users.json", "r", encoding="utf-8") as read_file:
                user_data = json.load(read_file)[self.nickname]

            self.user_FI.setText(f'{user_data["name"]} {user_data["surname"]}')
            self.user_nickname.setText(self.nickname)

            self.widget = QWidget()
            self.num = 49
            self.vbox = QVBoxLayout()
            self.vbox.setGeometry(QRect(0, 0, 1341, 1000))

            if os.path.exists(f'users_avatars/{self.nickname}_img.png'):
                self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.nickname}_img.png);'
                                             f' border-radius: 60px')

            elif os.path.exists(f'users_avatars/{self.nickname}_img.jpg'):
                self.user_icon.setStyleSheet(f'border-image: url(users_avatars/{self.nickname}_img.jpg);'
                                             f' border-radius: 60px')

            else:
                self.user_icon.setStyleSheet(f'border-image: url(users_avatars/standart_image.png);'
                                             f' border-radius: 60px')

            if "vars" in user_data:
                for i in range(len(user_data["vars"])):
                    points = str(user_data["vars"][str(i + 1)]["vsego_points"])
                    if points in "07":
                        a = 69
                    elif points != "100":
                        a = 67
                    else:
                        a = 65

                    btn = QPushButton(f'  Попытка №{i + 1}' + ' ' * a + f'{points}/100')
                    btn.setFont(QFont('MS Shell Dlg 2', 30))
                    btn.setMaximumSize(QSize(1300, 120))
                    btn.setMinimumSize(QSize(1300, 120))

                    if user_data["vars"][str(i + 1)]["vsego_points"] < 27:
                        btn.setStyleSheet('background-color: rgba(223, 116, 153, 230); color: '
                                          'rgba(255, 255, 255, 150); text-align: left; border-radius: 25px')
                    else:
                        btn.setStyleSheet('background-color: rgba(158, 241, 162, 240); color: '
                                          'rgba(255, 255, 255, 150); text-align: left; border-radius: 25px')

                    btn.clicked.connect(self.go_to_Info_Var)
                    self.vbox.addWidget(btn)

                self.vbox.setSpacing(20)
                self.widget.setLayout(self.vbox)
                self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                self.scrollArea.setWidgetResizable(True)
                self.scrollArea.setWidget(self.widget)

                self.no_vars.setEnabled(False)
                self.no_vars.setHidden(True)

            else:
                self.variants.setEnabled(False)
                self.variants.setHidden(True)

        else:
            self.user_nickname.setText("Аноним")
            self.user_icon.setStyleSheet(f'border-image: url(users_avatars/standart_image.png); '
                                         f'border-radius: 60px')
            self.variants.setEnabled(False)
            self.variants.setHidden(True)

            self.user_icon.setGeometry(110, 50, 131, 121)
            self.user_nickname.setGeometry(50, 190, 251, 71)

            self.no_vars.setText('''<html><head/><body>
            <p align="center">Ваши попытки не доступны!</p>
            <p align="center">Войдите в свой аккаунт для этого!</p>
            </body></html>''')
            self.no_vars.setStyleSheet("font-size: 40px; color: rgba(255, 255, 255, 210);")

        self.change_btn.clicked.connect(self.go_to_change)
        self.back.clicked.connect(self.go_to_main_menu)

    def go_to_Info_Var(self):
        popitka = int(self.sender().text().split()[1].split("№")[-1])

        with open("users.json", "r", encoding="utf-8") as read_file:
            ege_va = json.load(read_file)[self.nickname]["vars"][str(popitka)]["var"]

        self.Info_Vars = Info_Vars(popitka, int(ege_va))
        self.Info_Vars.show()
        self.close()

    def go_to_main_menu(self):
        self.men = MainMenu()
        self.men.show()
        self.close()

    def go_to_change(self):
        if nickname == "anonymous_228_337.on@qwe":
            self.no_vars.setText('''<html><head/><body>
                        <p align="center">Вы не можете изменять данные профиля!</p>
                        <p align="center">Войдите в свой аккаунт для этого!</p>
                        </body></html>''')
            self.no_vars.setStyleSheet("font-size: 40px; color: rgba(255, 255, 255, 210);")
        else:
            self.cha = ChangeMenu()
            self.cha.show()
            self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # anonymous_228_337.on@qwe - anonim nick
    nickname = ''
    ege, pred_ege, otv_perv = [0] * 18, [0] * 7, [""] * 11
    theo = TheoryWidget()
    ex = Zastavka()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())