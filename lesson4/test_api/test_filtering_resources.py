# Позитивные проверки - Поиск по id, должен вернуться 1 ресурс
def test_filtering_positive_by_id(session, base_url, fixture_id_resource_positive):
    res = session.get(url=f'{base_url}?id={fixture_id_resource_positive}')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 1, "Length is more than 1"
    assert res.json()[0]["id"] == fixture_id_resource_positive, "Wrong id"


# Позитивные проверки - Поиск по userId, проверка что в каждом словаре в массиве указанный userId
def test_filtering_positive_by_userid(session, base_url, fixture_test_filtering_positive_by_userid):
    res = session.get(url=f'{base_url}?userId={fixture_test_filtering_positive_by_userid}')
    assert res.status_code == 200, "Status code is not 200"
    r = res.json()
    for i in range(len(r)):
        assert r[i]["userId"] == fixture_test_filtering_positive_by_userid, "Wrong userId"


# Позитивные проверки - Поиск по completed, проверка что в каждом словаре в массиве указанный completed
def test_filtering_positive_by_completed(session, base_url, fixture_test_filtering_positive_by_completed):
    res = session.get(url=f'{base_url}?completed={fixture_test_filtering_positive_by_completed}')
    assert res.status_code == 200, "Status code is not 200"
    r = res.json()
    for i in range(len(r)):
        assert r[i]["completed"] == fixture_test_filtering_positive_by_completed, "Wrong completed"


# Позитивные проверки - Поиск по title, проверка что в каждом словаре в массиве указанный title
def test_filtering_positive_by_title(session, base_url, fixture_test_filtering_positive_by_title):
    res = session.get(url=f'{base_url}?title={fixture_test_filtering_positive_by_title}')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 1, "Length is more than 1"
    assert res.json()[0]["title"] == fixture_test_filtering_positive_by_title, "Wrong title"


# Негативные проверки - Поиск по id, который не существует, возвращается пустой массив, 200 ОК
def test_filtering_negative_by_id(session, base_url, fixture_id_resource_negative):
    res = session.get(url=f'{base_url}?id={fixture_id_resource_negative}')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 0, "Length is more than 0"


# Негативные проверки - Поиск по userId, который не существует, возвращается пустой массив, 200 ОК
def test_filtering_negative_by_userid(session, base_url):
    res = session.get(url=f'{base_url}?userId=0')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 0, "Length is more than 0"


# Негативные проверки - Поиск по completed с указанием небулевого значения, возвращается пустой массив, 200 ОК
def test_filtering_negative_by_completed(session, base_url):
    res = session.get(url=f'{base_url}?completed=123')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 0, "Length is more than 0"


# Негативные проверки - Поиск по title, который не существует, возвращается пустой массив, 200 ОК
def test_filtering_negative_by_title(session, base_url):
    title = "some title 2"
    res = session.get(url=f'{base_url}?title={title}')
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 0, "Length is more than 0"
