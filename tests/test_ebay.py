#!/usr/bin/env python
# coding=utf-8

"""
test_ebay
----------------------------------

Tests for `ebay` module.
"""
import pytest


@pytest.fixture
def ebay():
    from ebay import ebay

    mock_ebay = ebay()
    return mock_ebay

def test_ebay_properly_mocked(ebay):

    assert str(ebay) == "Success"