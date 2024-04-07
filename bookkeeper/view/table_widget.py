# pylint: disable=missing-module-docstring
from functools import lru_cache

from PySide6.QtWidgets import (  # pylint: disable=no-name-in-module
    QMenu,
    QWidget,
    QTableWidgetItem,
)
from PySide6.QtCore import Qt  # pylint: disable=no-name-in-module
from PySide6.QtGui import QAction  # pylint: disable=no-name-in-module
from bookkeeper.view.ui.ui_table_widget import UiWidgetTable
from bookkeeper.repository.abstract_repository import AbstractRepository
from bookkeeper.models.expense import Expense
from bookkeeper.models.category import Category


class TableWidget(QWidget):  # pylint: disable=too-few-public-methods
    """
    Виджет таблица - для отображения всех операций
    """
    def __init__(
            self,
            repo_categories: AbstractRepository[Category],
            repo_expenses: AbstractRepository[Expense],
    ):
        super().__init__()
        self._cache_expenses_id: dict[int, int] = {}
        self._ui = UiWidgetTable()
        self._ui.setup_ui(self)
        self._ui.table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self._ui.table_widget.customContextMenuRequested.connect(
            self._handle_context_menu,
        )
        self._repo_categories = repo_categories
        self._repo_expenses = repo_expenses

        self._ui.table_widget.setColumnWidth(0, 150)
        self._ui.table_widget.setColumnWidth(1, 80)
        self._ui.table_widget.setColumnWidth(2, 120)
        self._ui.table_widget.setColumnWidth(3, 315)
        self._init_context_menu()

        self.__deleted_row: int | None = None

    def update_table(self):
        """
        Функция для обновления таблицы. Вызывается извне, если в базе были изменения.
        """
        self._cache_expenses_id = {}
        expenses = self._repo_expenses.get_all()
        while self._ui.table_widget.rowCount() > 0:
            self._ui.table_widget.removeRow(0)
        for expense in expenses:
            self._add_expense(expense)

    def _init_context_menu(self):
        self._context_menu = QMenu()
        self._action = QAction('Удалить эту запись')
        self._action.triggered.connect(self._handle_delete_item)
        self._context_menu.addAction(self._action)

    @lru_cache(maxsize=100)
    def _get_name_category_for_id(self, cat_id: int) -> str:
        category = self._repo_categories.get(cat_id)
        return category.name

    def _add_expense(self, expense: Expense):
        count_row = self._ui.table_widget.rowCount()
        self._cache_expenses_id[count_row] = expense.pk
        self._ui.table_widget.insertRow(count_row)
        self._ui.table_widget.setItem(
            count_row,
            0,
            QTableWidgetItem(str(expense.expense_date)),
        )
        self._ui.table_widget.setItem(
            count_row,
            1,
            QTableWidgetItem(str(expense.amount)),
        )
        self._ui.table_widget.setItem(
            count_row,
            2,
            QTableWidgetItem(self._get_name_category_for_id(expense.category))
        )
        self._ui.table_widget.setItem(count_row, 3, QTableWidgetItem(expense.comment))

    def _handle_context_menu(self, pos):
        item = self._ui.table_widget.itemAt(pos)
        self.__deleted_row = item.row()
        self._context_menu.exec_(self._ui.table_widget.mapToGlobal(pos))

    def _handle_delete_item(self):
        expenses_id = self._cache_expenses_id[self.__deleted_row]
        self._repo_expenses.delete(expenses_id)
        del self._cache_expenses_id[self.__deleted_row]
        self._ui.table_widget.removeRow(self.__deleted_row)
