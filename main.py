from generate_image import generate_image
from PyQt5.QtWidgets import (
   QApplication, QWidget, QLineEdit,
   QLabel, QPushButton, QListWidget)
from PyQt5.QtGui import QPixmap
from get_quote import get_quote
from form_text import format_text

print(len("Пора было понять, что с ходом событий шутки плохи. В жизни существует порядок, который нелегко нарушить."))

class GetQuote(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(840, 580)

        self.button_generate = QPushButton("Сгенерировать", self)
        self.button_generate.setGeometry(12, 442, 274, 60)
        self.button_generate.setStyleSheet("font: 32px")
        self.button_generate.clicked.connect(self.set_quote)

        self.label_for_image = QLabel("", self)
        self.label_for_image.setGeometry(375, 15, 600, 400)

        self.image = QPixmap("")
        self.label_for_image.setPixmap(self.image)
        self.label_for_image.show()

        self.label_quote = QLabel("", self)
        self.label_quote.setGeometry(10, 520, 820, 55)

        self.initUI()

    def initUI(self):
        pass

    def set_quote(self):
        quote = get_quote()
        generate_image(quote)

        self.image = QPixmap("image.jpg")
        self.label_for_image.setPixmap(self.image)
        self.label_for_image.show()

        self.label_quote.setText(format_text(quote, 105))


app = QApplication([])
ex = GetQuote()
ex.show()
app.exec()
