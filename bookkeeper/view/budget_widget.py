# pylint: disable=missing-module-docstring
from calendar import monthrange
from datetime import datetime, timedelta

from PySide6.QtWidgets import (  # pylint: disable=no-name-in-module
    QTableWidgetItem,
    QWidget,
)

from bookkeeper.repository.abstract_repository import AbstractRepository
from bookkeeper.models.expense import Expense

from bookkeeper.view.ui.ui_budget_widget import UiBudgetWidget


class BudgetWidget(QWidget):  # pylint: disable=too-few-public-methods
    """
    Виджет для отображения текущих расходов и бюджета
    """
    def __init__(
            self,
            limit: int,
            repo_expense: AbstractRepository[Expense],
    ):
        super().__init__()
        self._limit = limit
        self._repo_expense = repo_expense
        self._ui = UiBudgetWidget()
        self._ui.setup_ui(self)

        self._ui.table_widget.setColumnWidth(0, 270)
        self._ui.table_widget.setColumnWidth(1, 270)

    def update_widget(self):
        """
        Функция для обновления виджета. Вызывается извне, если в базе были изменения.
        """
        current_date = datetime.now()
        count_day_of_month = monthrange(current_date.year, current_date.month)[1]
        all_expenses: list[Expense] = self._repo_expense.get_all()

        first = datetime(current_date.year, current_date.month, current_date.day, 0, 0, 0)
        last = first + timedelta(days=1)
        summa = sum(
            expense.amount for expense in all_expenses
            if first <= expense.expense_date <= last
        )
        self._ui.table_widget.setItem(0, 0, QTableWidgetItem(str(summa)))
        self._ui.table_widget.setItem(0, 1, QTableWidgetItem(str(self._limit)))

        first = first - timedelta(first.weekday())
        last = first + timedelta(days=7)
        summa = sum(
            expense.amount for expense in all_expenses
            if first <= expense.expense_date <= last
        )
        self._ui.table_widget.setItem(1, 0, QTableWidgetItem(str(summa)))
        self._ui.table_widget.setItem(1, 1, QTableWidgetItem(str(self._limit * 7)))

        first = datetime(current_date.year, current_date.month, 1, 0, 0, 0)
        last = first + timedelta(days=count_day_of_month)
        summa = sum(
            expense.amount for expense in all_expenses
            if first <= expense.expense_date <= last
        )
        self._ui.table_widget.setItem(2, 0, QTableWidgetItem(str(summa)))
        self._ui.table_widget.setItem(
            2,
            1,
            QTableWidgetItem(str(self._limit * count_day_of_month)),
        )
