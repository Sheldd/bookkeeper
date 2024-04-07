"""
Описан класс, представлющий бюджет расходов
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Budget:
    """
    Бюджет.
    amount - бюджет для категории расходов
    category - id категории расходов
    time_limit - срок ведения бюджета в днях
    start_budget_date - дата начала ведения бюджета
    pk - id записи в базу данных
    """
    amount: float
    category: int
    time_limit: int = 1
    start_budget_date: datetime = field(default_factory=datetime.now)
    pk: int = 0
