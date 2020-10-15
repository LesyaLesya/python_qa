# Проверяем валидные id ресурсов
def test_update_resource_with_patch_positive_id(session, base_url, fixture_id_resource_positive):
    payload = {"title": "some title"}
    res = session.patch(url=f'{base_url}/{fixture_id_resource_positive}', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == fixture_id_resource_positive, "Id is different"
    assert res.json()["title"] == payload["title"], "Wrong title"


# Проверяем замену значений всех ключей
def test_update_resource_with_patch_positive_all_values(session, base_url):
    payload = {"title": "NEW Title", "completed": False, "userId": 10}
    res = session.patch(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == 1, "Id is not 1"
    assert res.json()["title"] == payload["title"], "Wrong title"
    assert res.json()["completed"] == payload["completed"], "Wrong completed status"
    assert res.json()["userId"] == payload["userId"], "Wrong userId"


# Проверяем замену части значений ключей, для остальных остаются старые значения
def test_update_resource_with_patch_positive_few_values(session, base_url):
    get_all_data = session.get(url=base_url)
    payload = {"title": "NEW Title"}
    res = session.patch(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == 1, "Id is not 1"
    assert res.json()["title"] == payload["title"], "Wrong title"
    assert res.json()["completed"] == get_all_data.json()[0]["completed"], "Wrong completed status"
    assert res.json()["userId"] == get_all_data.json()[0]["userId"], "Wrong userId"


# Проверяем, что ничего не поменялось, если отправили пустой словарь
def test_update_resource_with_patch_positive_no_values(session, base_url):
    get_all_data = session.get(url=base_url)
    payload = {}
    res = session.patch(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == 1, "Id is not 1"
    assert res.json()["title"] == get_all_data.json()[0]["title"], "Wrong title"
    assert res.json()["completed"] == get_all_data.json()[0]["completed"], "Wrong completed status"
    assert res.json()["userId"] == get_all_data.json()[0]["userId"], "Wrong userId"


# Негативные проверки
def test_update_resource_with_patch_negative(session, base_url):
    payload = {"a": 100}
    res = session.patch(url=f'{base_url}/1',
                        data=payload, headers={"Content-type": "application/json"})
    assert res.status_code == 500, "Status code is not 500"
