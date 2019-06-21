#!/usr/bin/env python
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QWidget, QBoxLayout

app = QApplication([])
window = QWidget()
layout = QBoxLayout(QBoxLayout.Direction.TopToBottom)

settings_button = QPushButton("Settings")
layout.addWidget(settings_button)

line_display = QLabel("TYPING LINE GOES HERE")
layout.addWidget(line_display)

typing_line = QLineEdit()
layout.addWidget(typing_line)

typing_speed = QLabel("Typing Speed: ??? Characters per minute")
layout.addWidget(typing_speed)

typing_proficiency = QLabel("Proficiency: 0")
layout.addWidget(typing_proficiency)

window.setLayout(layout)
window.show()

app.exec_()
