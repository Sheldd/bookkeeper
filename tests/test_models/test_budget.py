"""
Тесты для расходных операций
"""

from datetime import datetime

import pytest

from bookkeeper.repository.memory_repository import MemoryRepository
from bookkeeper.models.budget import Budget


@pytest.fixture
def repo():
    return MemoryRepository()


def test_create_with_full_args_list():
    e = Budget(amount=100, category=1, time_limit=10,
               start_budget_date=datetime.now())
    assert e.amount == 100
    assert e.category == 1
    assert e.time_limit == 10


def test_create_brief():
    e = Budget(100, 1)
    assert e.amount == 100
    assert e.category == 1
    assert e.time_limit == 1


def test_can_add_to_repo(repo):
    e = Budget(100, 1)
    pk = repo.add(e)
    assert e.pk == pk
