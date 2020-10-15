def test_get_all_resources(session, base_url):
    res = session.get(url=base_url)
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 200, "List no 200 entities"


# Проверка первого элемента
def test_get_all_resources_check_first_el(session, base_url):
    res = session.get(url=base_url)
    assert res.json()[0]["id"] == 1, "First el's id is not 1"
    assert res.json()[0]["userId"] == 1, "Wrong userId"
    assert res.json()[0]["title"] == "delectus aut autem", "Wrong title"
    assert res.json()[0]["completed"] is False, "Wrong completed status"


# Проверка последнего элемента
def test_get_all_resources_check_last_el(session, base_url):
    res = session.get(url=base_url)
    assert res.json()[-1]["id"] == 200, "Last el's id is not 200"
    assert res.json()[-1]["userId"] == 10, "Wrong userId"
    assert res.json()[-1]["title"] == "ipsam aperiam voluptates qui", "Wrong title"
    assert res.json()[-1]["completed"] is False, "Wrong completed status"
