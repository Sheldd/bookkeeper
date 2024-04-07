# pylint: disable=missing-module-docstring
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.sqlite_repository import SQLiteRepository

from bookkeeper.view.add_widget import AddWidget
from bookkeeper.view.budget_widget import BudgetWidget
from bookkeeper.view.budget_mainwindow import BudgetMainWindow
from bookkeeper.view.category_widget import CategoryWidget
from bookkeeper.view.table_widget import TableWidget


class Presenter:
    """
    Класс Presenter, который создает  репозитории и GUI
    и обновляет виджеты.
    """
    def __init__(self, db_file: str):
        self._expense_repo = SQLiteRepository[Expense](db_file, Expense)
        self._category_repo = SQLiteRepository[Category](db_file, Category)

        self._table_widget = TableWidget(self._category_repo, self._expense_repo)
        self._table_widget.update_table()

        self._budget = BudgetWidget(limit=5000, repo_expense=self._expense_repo)
        self._budget.update_widget()

        self._add_widget = AddWidget(
            self._category_repo,
            self._expense_repo,
            self.open_category_inspector,
            self.add_new_expense,
        )
        self._category_inspector_closed()

        self._main_window = BudgetMainWindow(
            self._table_widget,
            self._budget,
            self._add_widget,
        )

        self._category_inspector = CategoryWidget(
            self._category_repo,
            self._category_inspector_closed,
        )

        self._main_window.show()

    def open_category_inspector(self):
        """
        Промежуточная фнкция, вызывающаяся при добавлении 
        категории в виджете (нажатие кнопки)
        """
        self._category_inspector.show_widget()

    def _category_inspector_closed(self):
        self._add_widget.update_widget()

    def add_new_expense(self):
        """
        Промежуточная функция для связи кнопки добавления трат
        и обновления данных в виджете.
        """
        self._table_widget.update_table()
        self._budget.update_widget()
