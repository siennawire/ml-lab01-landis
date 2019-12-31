
from proj_01_parse import parseNextSonnet
from nose.tools import assert_equals, raises

def test_sonnetparse_1():
    sonnet = "No Leading Blank Lines|body1|body2".split("|")
    assert_equals( (3, "No Leading Blank Lines",["body1", "body2"]), parseNextSonnet(0, sonnet))

def test_sonnetparse_2():
    sonnet = ["","  ","Many Leading Blank Lines", "", "", "body1", "body2", "", ""]
    assert_equals( (7, "Many Leading Blank Lines",["body1", "body2"]), parseNextSonnet(0, sonnet))


#
#  This should raise an exception
#  The @raises is called a python decorator.
#     decorators are "function helpers" - they're just functions themselves.
@raises(ValueError)
def test_sonnet_NoBody():
    sonnet = ["This is just a title"]
    (i, title, txt) = parseNextSonnet(0,sonnet)

@raises(ValueError)
def test_sonnet_BadIndex():
    sonnet = ["Fred oh no start wrong place!"]
    (i, title, txt) = parseNextSonnet(1000,sonnet)

