from PySide6.QtWidgets import QWidget
from ui_mainwidget import Ui_MainWidget

class MainWidget(QWidget, Ui_MainWidget):
    operator = ""
    val = 0
    display = 0
    locked = False

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.updateDisplay()

        self.button0.clicked.connect(self.button0Clicked)
        self.button1.clicked.connect(self.button1Clicked)
        self.button2.clicked.connect(self.button2Clicked)
        self.button3.clicked.connect(self.button3Clicked)
        self.button4.clicked.connect(self.button4Clicked)
        self.button5.clicked.connect(self.button5Clicked)
        self.button6.clicked.connect(self.button6Clicked)
        self.button7.clicked.connect(self.button7Clicked)
        self.button8.clicked.connect(self.button8Clicked)
        self.button9.clicked.connect(self.button9Clicked)

        self.buttonEnt.clicked.connect(self.buttonEntClicked)
        self.buttonPlus.clicked.connect(self.buttonPlusClicked)
        self.buttonMin.clicked.connect(self.buttonMinClicked)
        self.buttonMul.clicked.connect(self.buttonMulClicked)
        self.buttonDiv.clicked.connect(self.buttonDivClicked)

        self.buttonCom.clicked.connect(self.buttonComClicked)

        self.buttonCCE.clicked.connect(self.buttonCCEClicked)

    def updateDisplay(self):
        self.lcdNumber.display(self.display)

    def button0Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 0
            self.updateDisplay()
    def button1Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 1
            self.updateDisplay()
    def button2Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 2
            self.updateDisplay()
    def button3Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 3
            self.updateDisplay()
    def button4Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 4
            self.updateDisplay()
    def button5Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 5
            self.updateDisplay()
    def button6Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 6
            self.updateDisplay()
    def button7Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 7
            self.updateDisplay()
    def button8Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 8
            self.updateDisplay()
    def button9Clicked(self):
        if not self.locked:
            self.display *= 10
            self.display += 9
            self.updateDisplay()
    def buttonEntClicked(self):
            match self.operator:
                case "+":
                    print("case +")
                    self.display += self.val
                    self.updateDisplay()
                    self.operator = ""
                    self.locked = True
                case "-":
                    print("case -")
                    self.val -= self.display
                    self.display = self.val
                    self.updateDisplay()
                    self.operator = ""
                    self.locked = True
                case "*":
                    print("case *")
                    self.display *= self.val
                    self.updateDisplay()
                    self.operator = ""
                    self.locked = True
                case "/":
                    print("case /")
                    try:
                        self.val /= self.display
                    except:
                        print("Division exception")
                    self.updateDisplay()
                    self.operator = ""
                    self.locked = True
                case _:
                    print("case def")
                    self.val = self.display = 0
                    self.updateDisplay()
                    self.operator = ""
                    self.locked = False


    def buttonPlusClicked(self):
        self.operator = "+"
        self.val = self.display
        self.display = 0
        self.updateDisplay()
    def buttonMinClicked(self):
        self.operator = "-"
        self.val = self.display
        self.display = 0
        self.updateDisplay()
    def buttonMulClicked(self):
        self.operator = "*"
        self.val = self.display
        self.display = 0
        self.updateDisplay()
    def buttonDivClicked(self):
        self.operator = "/"
        self.val = self.display
        self.display = 0
        self.updateDisplay()
    def buttonComClicked(self):
        print("Not yet implemented")
    def buttonCCEClicked(self):
        self.val = self.display = 0
        self.updateDisplay()
        self.operator = ""
        self.locked = False
