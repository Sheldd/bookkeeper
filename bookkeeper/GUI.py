# pylint: disable=missing-module-docstring
import sys
from PySide6.QtWidgets import QApplication  # pylint: disable=no-name-in-module

from bookkeeper.view.presenter import Presenter


if __name__ == '__main__':
    app = QApplication(sys.argv)
    presenter = Presenter('data/budget.db')
    sys.exit(app.exec())
