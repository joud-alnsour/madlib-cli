def read(way):
    """
   This function opens a relative way, deletes the leading and trailing spaces, and returns the result.
   It can also deal with I/O errors.
    """
    try:
        return open(way).read().strip()
    except FileNotFoundError:
        raise(FileNotFoundError)


def parse(text):
    """
    This function extracts all sentences within any two curly brackets from a template(string). The phrases are likewise removed from the original def parse_template(text):
.
    Aside from the tuple of phrases, it returns the modified text.
    """
    down, up, section = 0, len(text)-1, []

    for _ in range(text.count("{")):
        left, right = text.find("{", down, up), text.find("}", down, up)
        section.append(text[left+1:right])
        text = text[:left+1] + text[right:]
        down = left + 2

    return text, tuple(section)


def merge(text, Solution):
    """
    This function takes a tuple of phrases and a "bare" text (a string with empty curly brackets). It returns the outcome after inserting the phrases within the curly brackets on the text.
    """
    return text.format(*Solution)


def game():
    template = read(r"madlib_cli/assets/template1.txt")
    text, Selection = parse(template)
    Solution = [input(f"\nChoose a {j}: ") for j in Selection]
    return merge(text, Solution)