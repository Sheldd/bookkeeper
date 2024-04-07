# pylint: disable=missing-module-docstring
from PySide6.QtWidgets import QMainWindow, QWidget  # pylint: disable=no-name-in-module

from bookkeeper.view.add_widget import AddWidget
from bookkeeper.view.UI_budget import UI_Budget
from bookkeeper.view.UI_table import UI_Table


class UI_BasicWindow(QMainWindow):  # pylint: disable=too-few-public-methods
    """
    Виджет главного окна, просто содержит и отрисовывает все части интерфейса
    """
    def __init__(
            self,
            table_widget: UI_Table,
            budget_widget: UI_Budget,
            add_widget: AddWidget,
    ):
        super().__init__()
        self.setFixedSize(680, 800)
        self.setWindowTitle('The Bookkeeper App')

        central_widget: QWidget = QWidget(self)
        central_widget.setGeometry(0, 0, self.width(), self.height())
        height = 5
        self._table = table_widget
        self._table.setParent(central_widget)
        self._table.setGeometry(5, height, self._table.width(), self._table.height())

        height += self._table.height() + 25
        self._budget = budget_widget
        self._budget.setParent(central_widget)
        self._budget.setGeometry(5, height, self._budget.width(), self._budget.height())

        height += self._budget.height() + 55
        self._add_widget = add_widget
        self._add_widget.setParent(central_widget)
        self._add_widget.setGeometry(
            5,
            height,
            self._add_widget.width(),
            self._add_widget.height(),
        )

        self.setCentralWidget(central_widget)
        self.show()
