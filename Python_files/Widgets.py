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
    def __init__(self):
        global nickname
        super().__init__('UI_files/TheoryWidget.ui', 'Теория')

        self.nickname = nickname

        for i in range(1, 59):
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
        global nickname

        user_nick = self.user_nickname.text()
        user_password = self.user_password.text()

        self.error.setStyleSheet("color: rgba(255, 255, 255, 210);")
        self.error.setAlignment(QtCore.Qt.AlignCenter)

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
        self.Exam_Vars = Exam_Vars(self.sender().text())
        self.Exam_Vars.show()
        self.close()

    def go_to_menu(self):
        self.men = Menu()
        self.men.show()
        self.close()


class Exam_Vars_1(AnyWidget): # задания из егэ № 1, 2, 3, 4
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_1.ui', f'Вариант №{egevar}')
        self.egevar = egevar

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
        global otv_perv
        otv_perv.clear()
        otv_perv = [""] * 11

        self.Exam = Exam()
        self.Exam.show()
        self.close()


class Exam_Vars_2(AnyWidget): # задания из егэ № 5, 7
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_2.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        for i in range(5, 8, 2):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i - 4}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i - 4}.setPixmap(Pixmap)')
            eval(f"self.ans_{i - 4}.setText(otv_perv[{i - 1}])")

        self.left.clicked.connect(self.go_to_Exam_Vars_1)
        self.right.clicked.connect(self.go_to_Exam_Vars_3)

    def go_to_Exam_Vars_1(self):
        global otv_perv
        otv_perv[4], otv_perv[6] = self.ans_1.text(), self.ans_3.text()

        self.Exam_Vars_1 = Exam_Vars_1(self.egevar)
        self.Exam_Vars_1.show()
        self.close()

    def go_to_Exam_Vars_3(self):
        global otv_perv
        otv_perv[4], otv_perv[6] = self.ans_1.text(), self.ans_3.text()

        self.Exam_Vars_3 = Exam_Vars_3(self.egevar)
        self.Exam_Vars_3.show()
        self.close()


class Exam_Vars_3(AnyWidget): # задания из егэ № 6, 8, 9
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_3.ui', f'Вариант №{egevar}')
        self.egevar = egevar

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

        self.left.clicked.connect(self.go_to_Exam_Vars_2)
        self.right.clicked.connect(self.go_to_Exam_Vars_4)

    def go_to_Exam_Vars_2(self):
        global otv_perv
        otv_perv[5], otv_perv[7], otv_perv[8] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()

        self.Exam_Vars_2 = Exam_Vars_2(self.egevar)
        self.Exam_Vars_2.show()
        self.close()

    def go_to_Exam_Vars_4(self):
        global otv_perv
        otv_perv[5], otv_perv[7], otv_perv[8] = self.ans_1.text(), self.ans_2.text(), self.ans_3.text()

        self.Exam_Vars_4 = Exam_Vars_4(self.egevar)
        self.Exam_Vars_4.show()
        self.close()


class Exam_Vars_4(AnyWidget): # задания из егэ № 10, 11, 12, 13
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_4.ui', f'Вариант №{egevar}')
        self.egevar = egevar

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
        global ege, pred_ege, otv_perv
        print(ege, pred_ege, otv_perv)

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

        print(ege)


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


class Correct_ans(AnyWidget):
    def __init__(self, exNum, exVar):
        super().__init__('UI_files/Correct_aans.ui', 'Подробное решение')
        self.exNum = exNum
        self.exVar = exVar
        Pixmap = QPixmap(f'ege_po_borbe_tren/var_{exVar}/ans/exer_{exNum}.png')
        self.label.setPixmap(Pixmap)
        self.exNumber.setText(exNum + '.')
        if int(exNum) <= 11:
            self.ok_label.setHidden(True)
            self.add_points.setHidden(True)
            self.ok_label.setEnabled(False)
            self.add_points.setEnabled(False)
        else:
            pass
            # .setChecked(True)

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
        self.exNumber.setText(exNum)
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
        if self.ans.text() == self.answers[self.exVar][self.exNum]:
            self.right_or_no.setText('Верно!')
            pass
        else:
            self.right_or_no.setText('Неправильно!')

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
        self.men = MainMenu()
        self.men.show()
        self.close()

    def go_to_change(self):
        self.cha = ChangeMenu()
        self.cha.show()
        self.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    nickname = 'дима'
    ege = [0] * 18
    pred_ege = [0] * 7
    otv_perv = [""] * 11
    # theo = TheoryWidget()
    ex = Exam_Vars_1(1)
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec_())