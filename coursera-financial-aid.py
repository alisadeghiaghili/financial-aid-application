# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 17:49:27 2023

@author: sadeghi.a
"""

import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QHBoxLayout, QMessageBox, QApplication

class FinancialAidApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Coursera Financial Aid Application')
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        self.field_label = QLabel('Enter the field name:')
        self.field_input = QLineEdit()

        self.course_label = QLabel('Enter the course name:')
        self.course_input = QLineEdit()

        self.institute_label = QLabel('Enter the institute name:')
        self.institute_input = QLineEdit()

        self.result_label = QLabel('Result:')
        self.result_output = QTextEdit()
        self.result_output.setReadOnly(True)

        submit_button = QPushButton('Genarate')
        submit_button.clicked.connect(self.process_application)

        copy_part1_button = QPushButton('Copy Part 1')
        copy_part1_button.clicked.connect(self.copy_part1_to_clipboard)

        copy_part2_button = QPushButton('Copy Part 2')
        copy_part2_button.clicked.connect(self.copy_part2_to_clipboard)

        clear_button = QPushButton('Clear')
        clear_button.clicked.connect(self.clear_inputs)

        button_layout = QHBoxLayout()
        button_layout.addWidget(submit_button)
        button_layout.addWidget(copy_part1_button)
        button_layout.addWidget(copy_part2_button)
        button_layout.addWidget(clear_button)

        layout.addWidget(self.field_label)
        layout.addWidget(self.field_input)
        layout.addWidget(self.course_label)
        layout.addWidget(self.course_input)
        layout.addWidget(self.institute_label)
        layout.addWidget(self.institute_input)
        layout.addLayout(button_layout)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_output)

        self.setLayout(layout)

    def process_application(self):
        field = self.field_input.text()
        courseName = self.course_input.text()
        instituteName = self.institute_input.text()

        # Capitalize the first letter of field and instituteName, lowercase courseName
        field = field.capitalize()
        courseName = courseName.lower()
        instituteName = instituteName.capitalize()

        part1 = f"I am a diligent and ambitious student hailing from a developing nation, deeply passionate about the field of {field}. "\
            "Regrettably, the educational resources and opportunities in my current college fall short of the standards "\
            "necessary for a comprehensive understanding of this discipline. Therefore, my pursuit of a promising career "\
            f"in the future hinges upon enrolling in the {courseName} course. Given my student status and the prohibitions "\
            "on part-time employment within my college, I am confronted with the stark reality that I lack the financial "\
            "means to cover the expenses associated with this esteemed course. Financial Aid, in this context, is not just a "\
            "mere option; it is the lifeline that can bridge the chasm between my aspirations and reality."\
            "\n\nThe course in question represents an invaluable opportunity for me to acquire in-depth knowledge and "\
            f"expertise in {field}. Not only will it equip me with practical skills and insights, but it will also "\
            "nurture my intellectual curiosity and analytical abilities. This course holds the potential to be a "\
            "transformative force in my educational journey, and its impact will reverberate throughout my career. "\
            "Furthermore, it promises to provide me with a globally recognized certificate, a testament to my "\
            f"dedication and competence in {field}. The acquisition of this certificate will undoubtedly elevate my "\
            "professional profile and open doors to a world of opportunities."\
            "\n\nMy enthusiasm for this course knows no bounds. It is not just about acquiring knowledge but about "\
            "improving lives, including mine. It is about realizing the dreams that I have nurtured since my formative "\
            "years. Coursera, as a platform, has garnered widespread acclaim and trust among my peers and mentors. "\
            "Their resounding endorsements have ignited a fire within me, compelling me to embark on this educational "\
            "journey with unwavering determination and enthusiasm. I believe that with Financial Aid, I can fully "\
            "devote myself to this course without sacrificing my basic needs and secure a brighter future."

        part2 = f"{field} is in high demand, and I want to complete the "\
                f"{courseName} Course at {instituteName}. This course will enhance my job prospects "\
                "after graduation from my institute. It will help me excel in "\
                f"{field} and give me an advantage over my competitors. A "\
                "verified certificate will add credibility to the certificate I receive "\
                "from this course. I plan to complete all assignments on or before the deadlines, "\
                "as I have done in previous Signature Track Courses. As mentioned earlier, "\
                "Coursera has not only been recommended by my student peers but also by our "\
                "college faculty. Following their prestigious advice, I am "\
                "eager to gain more knowledge and refine my skills through this course. "\
                "Additionally, I intend to actively participate in Discussion Forums, which I believe "\
                "will complement my learning. I also plan to grade assignments that are peer-reviewed, "\
                "which I consider to be an invaluable learning opportunity."

        application_text = part1 + '\n' + '=' * 60 + '\n' + part2
        self.result_output.setPlainText(application_text)

    def copy_part1_to_clipboard(self):
        part1_text = self.result_output.toPlainText().split('=' * 60)[0]
        clipboard = QApplication.clipboard()
        clipboard.setText(part1_text)
        QMessageBox.information(self, 'Copy Part 1', 'Part 1 has been copied to clipboard.')

    def copy_part2_to_clipboard(self):
        part2_text = self.result_output.toPlainText().split('=' * 60)[1]
        clipboard = QApplication.clipboard()
        clipboard.setText(part2_text)
        QMessageBox.information(self, 'Copy Part 2', 'Part 2 has been copied to clipboard.')

    def clear_inputs(self):
        self.field_input.clear()
        self.course_input.clear()
        self.institute_input.clear()
        self.result_output.clear()

def main():
    app = QApplication(sys.argv)
    window = FinancialAidApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
