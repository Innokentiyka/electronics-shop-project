from src.keyboard import KeyBoard

if __name__ == '__main__':
    kb = KeyBoard('Monster Pack', 1000, 6)
    assert str(kb) == "Monster Pack"

    assert str(kb.language) == "EN"

    kb.change_lang()
    assert str(kb.language) == "RU"

    kb.change_lang()
    kb.change_lang()
    assert str(kb.language) == "RU"
    kb.language = 'US'