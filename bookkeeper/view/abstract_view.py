from typing import Protocol
from typing import Callable
from models.category import Category


class AbstractView(Protocol):
    def set_category_list(list: list[Category]) -> None:
        pass
    
    def register_cat_modifier(
        handler: Callable[[Category], None]):
        pass
