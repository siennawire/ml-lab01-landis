
from proj_01_parse import parseNextSonnet
from nose.tools import assert_equals, raises

def test_sonnetparse_1():
    sonnets = "No Leading Blank Lines|body1|body2".split("|")
    assert_equals( (3, "No Leading Blank Lines",["body1", "body2"]), parseNextSonnet(0, sonnets))

def test_sonnetparse_2():
    sonnets = ["","  ","Many Leading Blank Lines", "", "", "body1", "body2", "", ""]
    assert_equals( (7, "Many Leading Blank Lines",["body1", "body2"]), parseNextSonnet(0, sonnets))


#
#  This should raise an exception
#  The @raises is called a python decorator.
#     decorators are "function helpers" - they're just functions themselves.
@raises(ValueError)
def test_sonnet_NoBody():
    sonnets = ["This is just a title"]
    (i, title, txt) = parseNextSonnet(0,sonnets)

@raises(ValueError)
def test_sonnet_BadIndex():
    sonnets = ["Fred oh no start wrong place!"]
    (i, title, txt) = parseNextSonnet(1000,sonnets)

def test_last_sonnet():
    sonnets = ["some","sonnet","here"]
    assert_equals((3,"",[]), parseNextSonnet(3, sonnets))
