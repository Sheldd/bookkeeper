# pylint: disable=missing-module-docstring
from typing import Callable

from PySide6.QtWidgets import QWidget  # pylint: disable=no-name-in-module

from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category
from bookkeeper.repository.abstract_repository import AbstractRepository

from bookkeeper.view.ui.ui_add_widget import UiAddWidget


class AddWidget(QWidget):  # pylint: disable=too-few-public-methods
    """
    Виджет для добавления операций
    """
    def __init__(
            self,
            repo_categories: AbstractRepository[Category],
            repo_expenses: AbstractRepository[Expense],
            handler_show_category: Callable,
            handler_add_expense: Callable,
    ):
        super().__init__()
        self._repo_categories = repo_categories
        self._repo_expenses = repo_expenses
        self._open_button_category = handler_show_category
        self._handler_add_expense = handler_add_expense
        self._cache_categories: dict[str, int] = {}
        self._ui = UiAddWidget()
        self._ui.setup_ui(self)
        self._ui.pb_add_category.clicked.connect(self._handler_button_category)
        self._ui.pb_add_item.clicked.connect(self._handler_button_add)

    def _handler_button_category(self):
        self._open_button_category()

    def update_widget(self):
        """
        Функция для обновления виджета. Вызывается извне, если в базе были изменения.
        """
        categories: list[Category] = self._repo_categories.get_all()
        self._cache_categories = {
            category.name: category.pk for category in categories
        }
        self._ui.cmb_category.clear()
        self._ui.cmb_category.addItems(self._cache_categories.keys())

    def _handler_button_add(self):
        price: int = self._ui.spb_amount.value()
        self._ui.spb_amount.setValue(0)

        expense = self._ui.date_time_edit.dateTime()
        category_name = self._ui.cmb_category.currentText()
        commentary = self._ui.txt_comment.toPlainText()

        expense = Expense(
            amount=price,
            category=self._cache_categories[category_name],
            expense_date=expense.toPython(),
            comment=commentary
        )
        self._repo_expenses.add(expense)
        self._handler_add_expense()
