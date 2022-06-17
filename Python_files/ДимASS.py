class Exam(AnyWidget):
    def __init__(self):
        global nickname
        super().__init__('UI_files/Exam.ui', 'Экзамен')
        self.back.clicked.connect(self.go_to_menu)
        self.nickname = nickname
        for i in range(1, 6):
            eval(f'self.exam_{i}.clicked.connect(self.go_to_EGE)')

    def go_to_EGE(self):
        self.Exam_Vars_1 = Exam_Vars_1(self.sender().text())
        self.Exam_Vars_1.show()
        self.close()

    def go_to_menu(self):
        self.men = Menu()
        self.men.show()
        self.close()


class Exam_Vars_1(AnyWidget):
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_1.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        for i in range(1, 5):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i}.setPixmap(Pixmap)')

        self.var.setText(f"Вариант №{self.egevar}")

        self.back.clicked.connect(self.go_to_Exam)
        self.right.clicked.connect(self.go_to_Exam_Vars_2)

    def go_to_Exam_Vars_2(self):
        self.Exam_Vars_2 = Exam_Vars_2(self.egevar)
        self.Exam_Vars_2.show()
        self.close()

    def go_to_Exam(self):
        self.Exam = Exam()
        self.Exam.show()
        self.close()


class Exam_Vars_2(AnyWidget):
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_2.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        for i in range(5, 8, 2):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i - 4}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i - 4}.setPixmap(Pixmap)')

        self.left.clicked.connect(self.go_to_Exam_Vars_1)
        self.right.clicked.connect(self.go_to_Exam_Vars_3)

    def go_to_Exam_Vars_1(self):
        self.Exam_Vars_1 = Exam_Vars_1(self.egevar)
        self.Exam_Vars_1.show()
        self.close()

    def go_to_Exam_Vars_3(self):
        self.Exam_Vars_3 = Exam_Vars_3(self.egevar)
        self.Exam_Vars_3.show()
        self.close()


class Exam_Vars_3(AnyWidget):
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_3.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_6.png')
        with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_6.png') as img:
            eval(f'self.label_{1}.setFixedSize({img.size[0]}, {img.size[1]})')
        eval(f'self.label_{1}.setPixmap(Pixmap)')

        for i in range(8, 10):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i - 6}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i - 6}.setPixmap(Pixmap)')

        self.left.clicked.connect(self.go_to_Exam_Vars_2)
        self.right.clicked.connect(self.go_to_Exam_Vars_4)

    def go_to_Exam_Vars_2(self):
        self.Exam_Vars_2 = Exam_Vars_2(self.egevar)
        self.Exam_Vars_2.show()
        self.close()

    def go_to_Exam_Vars_4(self):
        self.Exam_Vars_4 = Exam_Vars_4(self.egevar)
        self.Exam_Vars_4.show()
        self.close()


class Exam_Vars_4(AnyWidget):
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars_4.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        for i in range(10, 14):
            Pixmap = QPixmap(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png')
            with PIL.Image.open(f'ege_po_borbe_exam/var_{egevar}/exam_{i}.png') as img:
                eval(f'self.label_{i - 9}.setFixedSize({img.size[0]}, {img.size[1]})')
            eval(f'self.label_{i - 9}.setPixmap(Pixmap)')

        self.left.clicked.connect(self.go_to_Exam_Vars_3)
        self.right.clicked.connect(self.go_to_Exam_Vars_5)

    def go_to_Exam_Vars_3(self):
        self.Exam_Vars_3 = Exam_Vars_3(self.egevar)
        self.Exam_Vars_3.show()
        self.close()

    def go_to_Exam_Vars_5(self):
        self.Exam_Vars_5 = Exam_Vars_5(self.egevar)
        self.Exam_Vars_5.show()
        self.close()


class Exam_Vars_5(AnyWidget):
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


class Exam_Vars_6(AnyWidget):
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


class Exam_Vars_7(AnyWidget):
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
        print("ti lox")


class Exam_Vars_8(AnyWidget):
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


class Exam_Vars_9(AnyWidget):
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