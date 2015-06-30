# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import pytest


@pytest.fixture()
def fix1():
    print "I am fixture #1"


def test_nothing(fix1):
    assert True

def test_another_nothing(fix1):
    assert True





