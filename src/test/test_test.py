#-*- coding: utf-8 -*-

def test_string_correct():
  expected = 'correct'
  actual = 'correct'
  assert expected == actual

def test_string_wrong():
  expected = 'expected'
  actual = 'actual'
  assert expected == actual
