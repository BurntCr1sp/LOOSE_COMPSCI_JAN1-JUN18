import random
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QComboBox, QPushButton, QVBoxLayout, QWidget, QTextEdit, QLabel, QLineEdit

dice = [1,2,3,4,5,6]

print('Roll? (Y/N)')
user = input(':').lower()

if user == 'y':
    r_v1 = random.choice(dice)
    r_v2 = random.choice(dice)
    r_v3 = random.choice(dice)
    r_v4 = random.choice(dice)
    r_v5 = random.choice(dice)
    print(r_v1,r_v2,r_v3,r_v4,r_v5)

    app = QApplication(sys.argv)

    window = QWidget()

    window.setWindowTitle("Yahtzee")

    header = QLabel('You rolled:', window)

    label = QLabel(f"{r_v1}, {r_v2}, {r_v3}, {r_v4}, {r_v5}")

    button = QPushButton('Submit')

    layout = QVBoxLayout()
    layout.setAlignment(Qt.AlignCenter)
    layout.addWidget(header) 
    layout.addWidget(label) 
    layout.addWidget(button)
    window.setLayout(layout)

    window.resize(300, 150)

    window.show()

    sys.exit(app.exec_())