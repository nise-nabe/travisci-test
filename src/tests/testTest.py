#-*- coding: utf-8 -*-

from nose.tools import *

class TestTest():
  def testStringCorrect(self):
    expected = 'correct'
    actual = 'correct'
    eq_(expected, actual, '正しいかどうか')
  def testStringWrong(self):
    expected = 'expected'
    actual = 'actual'
    eq_(expected, actual, '違っているかどうか')
