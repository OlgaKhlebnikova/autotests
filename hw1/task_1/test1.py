from check_text import check_text
import pytest

def test_step1(good, bad):
    assert good in check_text(bad), 'Что-то не так'