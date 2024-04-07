# pylint: disable=missing-module-docstring
from typing import Callable

from PySide6.QtWidgets import (  # pylint: disable=no-name-in-module
    QWidget,
    QTreeWidgetItem,
)

from bookkeeper.view.ui.ui_category_widget import UiCategoryWidget
from bookkeeper.models.category import Category
from bookkeeper.repository.abstract_repository import AbstractRepository


class CategoryWidget(QWidget):
    """
    Виджет для отображения и управления деревом категорий
    """
    def __init__(
            self,
            repo_category: AbstractRepository[Category],
            handler_closed: Callable,
    ):
        super().__init__()
        self._category = repo_category
        self._cache_category_id: dict[str, int] = {}
        self._handler_closed = handler_closed
        self._ui = UiCategoryWidget()
        self._ui.setup_ui(self)

        self._ui.pb_add_category.clicked.connect(self._handle_button_add)

        self._update_cache_categories()

    def _get_children(self, parent_id: int) -> list[Category]:
        return self._category.get_all(where={'parent': parent_id})

    def _build_tree_category(self):
        self._ui.tree_category.clear()
        self._ui.tree_category.setHeaderLabels(['Категории'])

        root = self._category.get(1)
        if root is None:
            return
        tree_root: QTreeWidgetItem = QTreeWidgetItem([root.name])

        tree_root.addChildren(self._build_node_tree_category(root))

        self._ui.tree_category.addTopLevelItem(tree_root)

    def _build_node_tree_category(self, node: Category) -> list[QTreeWidgetItem]:
        items: list[QTreeWidgetItem] = []
        for child in self._get_children(node.pk):
            item = QTreeWidgetItem([child.name])
            item.addChildren(self._build_node_tree_category(child))
            items.append(item)
        return items

    def _update_cache_categories(self):
        categories: list[Category] = self._category.get_all()
        self._cache_category_id = {
            category.name: category.pk for category in categories
        }
        self._ui.cmb_category.clear()
        self._ui.led_name.clear()
        self._ui.cmb_category.addItems(self._cache_category_id.keys())

    def show_widget(self):
        """
        Так как виджет показывается не в главном окне,
        то для него нужно отдельная функция для отрисовки на экране
        """
        self._build_tree_category()

        self._ui.cmb_category.clear()
        self._ui.cmb_category.addItems(self._cache_category_id.keys())

        self.show()

    def _handle_button_add(self):
        name = self._ui.led_name.text()
        parent = self._ui.cmb_category.currentText()
        parent_id = self._cache_category_id.get(parent)

        category = Category(name=name, parent=parent_id)
        self._category.add(category)

        self._update_cache_categories()
        self._build_tree_category()

    def closeEvent(self, unused_event):  # pylint: disable=invalid-name
        """
        Переопределенный метод для отработки события "Закрытия окна"
        Нужен, потому что необходимо обновить другие виджеты, после закрытия этого окна.
        """
        self._handler_closed()
        self.close()
