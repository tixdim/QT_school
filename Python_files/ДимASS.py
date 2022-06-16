class Exam(AnyWidget):
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


class Correct_ans(AnyWidget):
    def __init__(self, exNum, exVar):
        super().__init__('UI_files/Correct_ans.ui', 'Подробное решение')
        self.exNum = exNum
        self.exVar = exVar
        Pixmap = QPixmap(f'ege_po_borbe_tren/var_{exVar}/ans/exer_{exNum}.png')
        self.exNumber.setText(exNum + '.')
        self.back.clicked.connect(self.go_to_ex)
        self.label.setPixmap(Pixmap)

    def go_to_ex(self):
        self.ex = Exercise(self.exNum, self.exVar)
        self.ex.show()


class Exam_Vars(AnyWidget):
    def __init__(self, egevar):
        super().__init__('UI_files/Exam_Vars.ui', f'Вариант №{egevar}')
        self.egevar = egevar

        # Pixmap = QPixmap(f'ege_po_borbe_tren/var_{exVar}/exer_{exNum}.png')
        # # with PIL.Image.open(f'ege_po_borbe_tren/var_{exVar}/exer_{exNum}.png') as img:
        # #     self.label.setFixedSize(*img.size)
        # self.exNumber.setText(exNum)
        # self.label.setPixmap(Pixmap)

        self.back.clicked.connect(self.go_to_Exam)

    def go_to_Exam(self):
        self.Exam = Exam()
        self.Exam.show()
        self.close()