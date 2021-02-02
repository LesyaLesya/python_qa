# Проверяем валидные id ресурсов
def test_update_resource_with_put_positive_id(session, base_url, fixture_id_resource_positive):
    payload = {"title": "some title", "completed": True, "userId": 1}
    res = session.put(url=f'{base_url}/{fixture_id_resource_positive}', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == fixture_id_resource_positive, "Id is different"
    assert res.json()["userId"] == payload["userId"], "Wrong userId"
    assert res.json()["title"] == payload["title"], "Wrong title"
    assert res.json()["completed"] == payload["completed"], "Wrong completed status"


# Проверяем замену валидными данными для ресурса 1
def test_update_resource_with_put_positive_body(session, base_url, fixture_payload_resource_positive):
    res = session.put(url=f'{base_url}/1', json=fixture_payload_resource_positive)
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == 1, "Id is different"
    assert res.json()["userId"] == fixture_payload_resource_positive["userId"], "Wrong userId"
    assert res.json()["title"] == fixture_payload_resource_positive["title"], "Wrong title"
    assert res.json()["completed"] == fixture_payload_resource_positive["completed"], "Wrong completed status"


# Проверяем замену ресурса 1 пустым payload. Ожидаем, что все, кроме id удалится
def test_update_resource_with_put_positive_empty_body(session, base_url):
    payload = {}
    res = session.put(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 1, "Length is not 1"
    assert res.json()["id"] == 1, "Wrong id"
    assert "userId" not in res.json(), "userId in dict"
    assert "title" not in res.json(), "title in dict"
    assert "completed" not in res.json(), "completed in dict"


# Проверяем замену ресурса 1 пустым payload с частью данных. Ожидаем, что данные, которых нет в payload, удалятся
def test_update_resource_with_put_positive_body_without_title(session, base_url):
    payload = {"completed": True, "userId": 1}
    res = session.put(url=f'{base_url}/1', json=payload)
    assert res.status_code == 200, "Status code is not 200"
    assert len(res.json()) == 3, "Length is not 3"
    assert res.json()["id"] == 1, "Wrong id"
    assert res.json()["completed"] == payload["completed"], "Wrong completed status"
    assert res.json()["userId"] == payload["userId"], "Wrong userId"
    assert "title" not in res.json(), "title in dict"


# Негативная проверка - проверка невалидных id
def test_update_resource_with_put_negative_id(session, base_url, fixture_id_resource_negative):
    payload = {"title": "some title", "completed": True, "userId": 1}
    res = session.put(url=f'{base_url}/{fixture_id_resource_negative}', json=payload)
    assert res.status_code == 500, "Status code is not 500"
