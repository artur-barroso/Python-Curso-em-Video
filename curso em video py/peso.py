import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")
        self.setGeometry(100, 100, 300, 400)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.layout.addWidget(self.display)

        buttons_layout = QVBoxLayout()
        self.layout.addLayout(buttons_layout)

        buttons = [
            ('7', '8', '9', '/'),
            ('4', '5', '6', '*'),
            ('1', '2', '3', '-'),
            ('C', '0', '=', '+'),
        ]

        for row in buttons:
            row_layout = QHBoxLayout()
            buttons_layout.addLayout(row_layout)
            for btn_text in row:
                btn = QPushButton(btn_text)
                btn.clicked.connect(lambda state, text=btn_text: self.on_btn_click(text))
                row_layout.addWidget(btn)

    def on_btn_click(self, text):
        if text == 'C':
            self.display.clear()
        elif text == '=':
            try:
                result = eval(self.display.text())
                self.display.setText(str(result))
            except Exception as e:
                self.display.setText("Error")
        else:
            current = self.display.text()
            self.display.setText(current + text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc = Calculadora()
    calc.show()
    sys.exit(app.exec_())
