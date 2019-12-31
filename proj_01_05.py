"""
Lab 01  Project 01-04.  extract_gutenText

Write the function extract_gutenText here and let's test it out!

So we'll also be writing a test function for this one.
"""

#  Copy and paste your code here from previous exercise:

def read_fileAsList( fname ):
    pass


# optional 01.06.  You can come back and do this LATER.
def find_lineWithTextInList(direction, somelist,  sometext, startingPoint = None):
    pass


# 01.05 - do this before 01.06.
def extract_GutenText(lines):
    # Look for "project gutenberg" before the mid point
    # I am including some sample code to get you started.....
    # Make sure you understand what this does BEFORE you copy it and modify it for below.
    # Also it's incomplete....
    startpoint1 = len(lines) // 2   # note the integer division.
    while """some condition here to prevent you from running off the beginning of the list """:
        if "project gutenberg" in lines[startpoint1].lower():
            break
        startpoint1 = startpoint1 - 1 # or alternatively:  startpoint1 -= 1
    # look for the first blank line after that point.

    # look for "project gutenberg" after the midpoint

    # look for the first blank line before that point

    # return a slice of the list that is just the text of the ebook.  Don't include the blank lines in the slice
    return # something



# Part 01.07 -
# Mars wrote this test FOR you.... pay particular attention to the notes in the lab
# and how it works!
# Especially string join, f-strings, assert.
#
# DO NOT GO ON if you don't understand how those work!
#


def test_basic_extract_GutenText():
    print("dude")
    texttext1 = """This is a test example
    *** Project GUTENberg should start here after the blank line ***
    *** and not include this line or the blank line after this one **
    
    guten text is here!
    
    ** some nonlank line **
    *** Project GutenBERG text should end here but the blank line before it should also not be included ***
    ** none of this should show up
    """
    testtextlines = texttext1.split("\n")
    actualtextlines = extract_GutenText(testtextlines)
    assert len(actualtextlines) == 1, f'Incorrect number of lines for testtext1: {len(actualtextlines)} should be 1. {"|".join(actualtextlines)}'
    assert actualtextlines[0] == "    guten text is here!", f"testtext1 is wrong: {'|'.join(actualtextlines)}"



#  Part 01.08
#   Use the parse code to write the sonnet index function
#
from proj_01_parse import parseNextSonnet


def sonnetIndex(sonnetText: [str]) -> [(str, [str])]:
    pass # remove this line.  It's here just to make the function not show a syntax error.



#  Part 01.09
#
#
def fetchAndPrintSonnet():
    # use read_fileAsList to read the sonnet file, and store the lines in a variable
    # use extract_GutenText with the variable above, and store just the sonnet text
    # use sonnetIndex with the variable above and extract a list of (title, sonnet) pairs
    #    store the result in variable "sonnets" so that it is compatible with the code below...

    # now let's prompt the user for a sonnet and display it.  Try 0.
    s = ""
    while s.lower() != "done":
        s = input("Which sonnet? or done to end")
        if s != 'done':
            try:
                (title, sonnet) = sonnets[int(s)]
            except ValueError as verr:
                print("I can't convert what you typed to an integer")
            except IndexError as ierr:
                print(f"Sonnets go from 0 to {len(sonnets)}")
        print(f"*** {title} ***")
        print("\n".join(sonnet))



if __name__ == "__main__":
    # This code only runs when you run this python file directly.
    pass

