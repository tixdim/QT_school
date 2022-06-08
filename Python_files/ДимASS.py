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

        self.start_hidden_enabled()

    def start_hidden_enabled(self):
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