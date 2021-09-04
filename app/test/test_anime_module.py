from src.modules.anime import get_anime_by_name


def __verify_missing_content(anime_name=None):
    data = get_anime_by_name(anime_name)
    assert len(data) == 0
    assert type(data) == list


def test_with_content():
    data = get_anime_by_name("hidan no aria")
    assert len(data) > 0
    assert type(data[0]["attributes"]["canonicalTitle"]) == str


def test_without_content():
    __verify_missing_content("")


def without_params():
    __verify_missing_content()
