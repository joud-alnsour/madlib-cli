import pytest
from madlib_cli.madlib import read, parse, merge



def test_read():
    actual = read("madlib_cli/assets/template1.txt")
    expected = "It was a {Adjective} and {Adjective} {Noun}."
    assert actual == expected



def test_parse():
    actual_stripped, actual_parts = parse(
        "It was a {Adjective} and {Adjective} {Noun}."
    )
    expected_stripped = "It was a {} and {} {}."
    expected_parts = ("Adjective", "Adjective", "Noun")

    assert actual_stripped == expected_stripped
    assert actual_parts == expected_parts



def test_merge():
    actual = merge("It was a {} and {} {}.", ("dark", "stormy", "night"))
    expected = "It was a dark and stormy night."
    assert actual == expected



def test_read_way():

    with pytest.raises(FileNotFoundError):
        way = "missing.txt"
        read(way)