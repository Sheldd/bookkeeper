# pylint: disable=missing-module-docstring
from PySide6.QtCore import (  # pylint: disable=no-name-in-module
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
    Qt,
)
from PySide6.QtWidgets import (  # pylint: disable=no-name-in-module
    QComboBox,
    QFrame,
    QGroupBox,
    QLabel,
    QLineEdit,
    QPushButton,
    QTreeWidget,
    QTreeWidgetItem,
    QVBoxLayout,
)


# pylint: disable=too-many-instance-attributes, too-few-public-methods
class UiCategoryWidget:
    """
    Графический интерфейс для виджета операций с категориями
    """
    def __init__(self):
        self.pb_add_category = None
        self.cmb_category = None
        self.led_name = None
        self.lbl_parent = None
        self.lbl_name = None
        self.group_box = None
        self.tree_category = None
        self.frame = None
        self.vertical_layout_2 = None

    def setup_ui(self, category_widget):
        """
        Инициализация виджета и его содержимого
        """
        if not category_widget.objectName():
            category_widget.setObjectName("category_widget")
        category_widget.resize(420, 550)
        category_widget.setMinimumSize(QSize(420, 550))
        self.vertical_layout_2 = QVBoxLayout(category_widget)
        self.vertical_layout_2.setObjectName("verticalLayout_2")
        self.frame = QFrame(category_widget)
        self.frame.setObjectName("frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.tree_category = QTreeWidget(self.frame)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, "1")
        self.tree_category.setHeaderItem(__qtreewidgetitem)
        self.tree_category.setObjectName("tree_category")
        self.tree_category.setGeometry(QRect(0, 0, 401, 401))
        self.group_box = QGroupBox(self.frame)
        self.group_box.setObjectName("groupBox")
        self.group_box.setGeometry(QRect(0, 400, 401, 131))
        self.lbl_name = QLabel(self.group_box)
        self.lbl_name.setObjectName("lbl_name")
        self.lbl_name.setGeometry(QRect(10, 30, 180, 20))
        self.lbl_name.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lbl_parent = QLabel(self.group_box)
        self.lbl_parent.setObjectName("lbl_parent")
        self.lbl_parent.setGeometry(QRect(10, 60, 180, 20))
        self.lbl_parent.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.led_name = QLineEdit(self.group_box)
        self.led_name.setObjectName("led_name")
        self.led_name.setGeometry(QRect(200, 30, 180, 20))
        self.cmb_category = QComboBox(self.group_box)
        self.cmb_category.setObjectName("cmb_category")
        self.cmb_category.setGeometry(QRect(200, 60, 180, 20))
        self.pb_add_category = QPushButton(self.group_box)
        self.pb_add_category.setObjectName("pb_add_category")
        self.pb_add_category.setGeometry(QRect(110, 90, 150, 40))

        self.vertical_layout_2.addWidget(self.frame)

        self._translate_ui(category_widget)

        QMetaObject.connectSlotsByName(category_widget)

    def _translate_ui(self, category_widget):
        category_widget.setWindowTitle(
            QCoreApplication.translate("category_widget", "Category", None),
        )
        self.group_box.setTitle(
            QCoreApplication.translate(
                "category_widget",
                # pylint: disable=line-too-long
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043d\u043e\u0432\u0443\u044e \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e",  # noqa: E501
                None,
            )
        )
        self.lbl_name.setText(
            QCoreApplication.translate(
                "category_widget",
                "\u0418\u043c\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u0438",  # noqa: E501
                None,
            )
        )
        self.lbl_parent.setText(
            QCoreApplication.translate(
                "category_widget",
                # pylint: disable=line-too-long
                "\u0420\u043e\u0434\u0438\u0442\u0435\u043b\u044c\u0441\u043a\u0430\u044f \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",  # noqa: E501
                None,
            )
        )
        self.pb_add_category.setText(
            QCoreApplication.translate(
                "category_widget",
                # pylint: disable=line-too-long
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u043a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044e",  # noqa: E501
                None,
            )
        )
