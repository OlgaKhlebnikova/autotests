from main import login, get

def test_1(login):
    res = get(login)
    lst = res['data']
    lst_id = [el["id"] for el in lst]

    assert 79123 in lst_id, 'тест провален'
