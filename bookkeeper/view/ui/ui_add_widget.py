# pylint: disable=missing-module-docstring
from PySide6.QtCore import (  # pylint: disable=no-name-in-module
    QCoreApplication,
    QDate,
    QMetaObject,
    QRect,
    QSize,
    Qt
)
from PySide6.QtWidgets import (  # pylint: disable=no-name-in-module
    QComboBox,
    QDateTimeEdit,
    QGroupBox,
    QLabel,
    QPushButton,
    QSpinBox,
    QTextEdit,
)


class UiAddWidget:  # pylint: disable=too-many-instance-attributes, too-few-public-methods
    """
    Графический интерфейс для виджета добавления операции
    """

    def __init__(self):
        self.date_time_edit = None
        self.spb_amount = None
        self.lbl_date = None
        self.cmb_category = None
        self.pb_add_category = None
        self.txt_comment = None
        self.pb_add_item = None
        self.lbl_category = None
        self.lbl_summa = None
        self.lbl_comment = None
        self.group = None

    def setup_ui(self, add_widget):
        """
        Инициализация виджета и его содержимого
        """
        if not add_widget.objectName():
            add_widget.setObjectName("add_widget")
        add_widget.resize(670, 180)
        add_widget.setMinimumSize(QSize(670, 180))
        add_widget.setMaximumSize(QSize(670, 180))
        self.group = QGroupBox(add_widget)
        self.group.setObjectName("group")
        self.group.setGeometry(QRect(0, 0, 670, 171))
        self.lbl_comment = QLabel(self.group)
        self.lbl_comment.setObjectName("lbl_comment")
        self.lbl_comment.setGeometry(QRect(260, 30, 100, 20))
        self.lbl_summa = QLabel(self.group)
        self.lbl_summa.setObjectName("lbl_summa")
        self.lbl_summa.setGeometry(QRect(10, 30, 111, 20))
        self.lbl_summa.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.lbl_category = QLabel(self.group)
        self.lbl_category.setObjectName("lbl_category")
        self.lbl_category.setGeometry(QRect(10, 60, 111, 20))
        self.lbl_category.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.pb_add_item = QPushButton(self.group)
        self.pb_add_item.setObjectName("pb_add_item")
        self.pb_add_item.setGeometry(QRect(220, 130, 171, 31))
        self.txt_comment = QTextEdit(self.group)
        self.txt_comment.setObjectName("txt_comment")
        self.txt_comment.setGeometry(QRect(380, 30, 280, 81))
        self.cmb_category = QComboBox(self.group)
        self.cmb_category.setObjectName("cmb_category")
        self.cmb_category.setGeometry(QRect(120, 60, 111, 20))
        self.pb_add_category = QPushButton(self.group)
        self.pb_add_category.setObjectName("pb_add_category")
        self.pb_add_category.setGeometry(QRect(240, 60, 21, 21))
        self.lbl_date = QLabel(self.group)
        self.lbl_date.setObjectName("lbl_date")
        self.lbl_date.setGeometry(QRect(10, 100, 111, 16))
        self.lbl_date.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.spb_amount = QSpinBox(self.group)
        self.spb_amount.setObjectName("spb_amount")
        self.spb_amount.setGeometry(QRect(120, 30, 111, 24))
        self.spb_amount.setMaximum(99999999)
        self.date_time_edit = QDateTimeEdit(self.group)
        self.date_time_edit.setObjectName("dateTimeEdit")
        self.date_time_edit.setGeometry(QRect(120, 95, 141, 25))
        self.date_time_edit.setDate(QDate(2024, 1, 1))

        self._translate_ui(add_widget)

        QMetaObject.connectSlotsByName(add_widget)

    def _translate_ui(self, add_widget):
        add_widget.setWindowTitle(QCoreApplication.translate("add_widget", "Form", None))
        self.group.setTitle(
            QCoreApplication.translate(
                "add_widget",
                "\u0417\u0430\u043f\u0438\u0441\u044c",
                None,
            )
        )
        self.lbl_comment.setText(
            QCoreApplication.translate(
                "add_widget",
                "\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439",
                None,
            )
        )
        self.lbl_summa.setText(
            QCoreApplication.translate(
                "add_widget",
                "\u0421\u0443\u043c\u043c\u0430: ",
                None,
            )
        )
        self.lbl_category.setText(
            QCoreApplication.translate(
                "add_widget",
                "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f: ",
                None,
            )
        )
        self.pb_add_item.setText(
            QCoreApplication.translate(
                "add_widget",
                # pylint: disable=line-too-long
                "\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c",  # noqa: E501
                None,
            )
        )
        self.pb_add_category.setText("")
        self.lbl_date.setText(
            QCoreApplication.translate(
                "add_widget",
                "\u0414\u0430\u0442\u0430 \u043f\u043e\u043a\u0443\u043f\u043a\u0438: ",
                None,
            )
        )
