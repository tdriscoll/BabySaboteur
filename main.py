from PyQt4.QtGui import QApplication
import sys
from production.presenter import Presenter
from display.view import View
from questions.easy_questions import questions


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Baby Saboteur")
    presenter = Presenter(View(), questions)
    presenter.initialize()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()