from src.modules.quotes import get_quote


def __verify_quote_function(type_quote):
    try:
        quote = get_quote(type_quote)
    except Exception as e:
        raise e
    assert type(quote.author) == str
    assert type(quote.text) == str


def test_quote_function():
    try:
        __verify_quote_function()
        assert False
    except Exception as e:
        assert type(e.args[0]) == str
    __verify_quote_function("today")
    __verify_quote_function("random")


def test_quote_with_wrong_type():
    try:
        __verify_quote_function("wrong_type")
        assert False
    except Exception as e:
        assert type(e.args[0]) == str
