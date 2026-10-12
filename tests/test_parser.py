import math
import pytest
from arithmp.parser import Parser 

@pytest.fixture
def parser():
    return Parser()

def test_basic_arithmetic(parser):
    assert parser.parse("3 + 4") == 7.0
    assert parser.parse("10 - 2") == 8.0
    assert parser.parse("5 * 6") == 30.0
    assert parser.parse("8 / 2") == 4.0
    assert parser.parse("7 % 3") == 1.0


def test_unary_operators(parser):
    assert parser.parse("+5") == 5.0
    assert parser.parse("-5") == -5.0


def test_power_operator(parser):
    assert parser.parse("2 ^ 3") == 8.0  # Adjust operator if your lark grammar uses ** or ^


def test_invalid_syntax(parser):
    with pytest.raises(Exception):
        parser.parse("3 +")