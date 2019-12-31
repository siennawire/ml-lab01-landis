
"""
This function is built with something called type hints.  See the lab notes.

The parameters have type hints on them,
and the return value has a type hint as well after the -> token
"""
def parseNextSonnet(startIndex: int, sonnetText: [str]) -> (int, str, [str]):
    """
    Parse the next sonnet in sonnetText.  The text should look like this:
        optional blank lines
        Title
        optional blank lines
        Sonnet Body
        optional blank lines
    
    :param startIndex: Where to start parsing the next sonnet in the sonnet text
    :param sonnetText: Text of all the sonnets
    :return: a tuple of (int, str, [str]) the remaining index, sonnet title and list of lines.
    If there are no more sonnets, we should return an empty title and list.
    """
    # Note the parameter name is long.
    # The parameter name tells you what the meaning of the parameter is.
    # But we can use a shorter index variable in the code
    i = startIndex
    try:
        # skip any leading blank lines.  Careful not to step off the end if we're out of sonnets.
        while i < len(sonnetText) and sonnetText[i].strip() == "":  i += 1
        if i == len(sonnetText):
            # we've stepped off the end.  No more sonnets.
            return (i, "", [])
        # get the title and go to next line
        title = sonnetText[i]; i += 1
        # skip any more blank lines to get to the body
        while sonnetText[i].strip() == "":  i += 1
        # get the body
        body = []
        while i < len(sonnetText) and sonnetText[i].strip() != "":
            body.append(sonnetText[i])
            i += 1

    except IndexError:
        raise ValueError("Sonnet Text is not in a valid format, or start index is out of bounds.")
    if len(body) == 0:
        raise ValueError("Sonnet has no body")

    return (i, title, body)


