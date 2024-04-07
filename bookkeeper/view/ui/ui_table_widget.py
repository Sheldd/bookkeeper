# pylint: disable=missing-module-docstring
from PySide6.QtCore import (  # pylint: disable=no-name-in-module
    QCoreApplication,
    QMetaObject,
    QRect,
    QSize,
)
from PySide6.QtWidgets import (  # pylint: disable=no-name-in-module
    QLabel,
    QTableWidget,
    QTableWidgetItem,
)


class UiWidgetTable:  # pylint: disable=too-few-public-methods
    """
    Графический интерфейс для виджета отображения операций
    """

    def __init__(self):
        self.lbl = None
        self.table_widget = None

    def setup_ui(self, widget_table):
        """
        Инициализация виджета и его содержимого
        """
        if not widget_table.objectName():
            widget_table.setObjectName("WidgetTable")
        widget_table.resize(670, 390)
        widget_table.setMinimumSize(QSize(670, 390))
        widget_table.setMaximumSize(QSize(670, 390))
        self.table_widget = QTableWidget(widget_table)
        if self.table_widget.columnCount() < 4:
            self.table_widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setGeometry(QRect(0, 20, 670, 370))
        self.table_widget.setMinimumSize(QSize(670, 370))
        self.table_widget.setMaximumSize(QSize(1280, 620))
        self.lbl = QLabel(widget_table)
        self.lbl.setObjectName("lbl")
        self.lbl.setGeometry(QRect(0, 0, 201, 16))

        self._translate_ui(widget_table)

        QMetaObject.connectSlotsByName(widget_table)
    # setupUi

    def _translate_ui(self, widget_table):
        widget_table.setWindowTitle(
            QCoreApplication.translate(
                "WidgetTable",
                "Form",
                None,
            )
        )
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(
            QCoreApplication.translate(
                "WidgetTable",
                "\u0414\u0430\u0442\u0430",
                None,
            )
        )
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(
            QCoreApplication.translate(
                "WidgetTable",
                "\u0421\u0443\u043c\u043c\u0430",
                None,
            )
        )
        ___qtablewidgetitem2 = self.table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(
            QCoreApplication.translate(
                "WidgetTable",
                "\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f",
                None,
            )
        )
        ___qtablewidgetitem3 = self.table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(
            QCoreApplication.translate(
                "WidgetTable",
                "\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439",
                None,
            )
        )
        self.lbl.setText(
            QCoreApplication.translate(
                "WidgetTable",
                # pylint: disable=line-too-long
                "\u041f\u043e\u0441\u043b\u0435\u0434\u043d\u0438\u0435 \u0440\u0430\u0441\u0445\u043e\u0434\u044b",  # noqa: E501
                None,
            ),
        )
