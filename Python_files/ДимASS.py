class Exam(AnyWidget): # меню с предложенными вариантами
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