# Позитивные проверки
def test_get_resource_positive(session, base_url, fixture_id_resource_positive):
    res = session.get(url=f'{base_url}/{fixture_id_resource_positive}')
    assert res.status_code == 200, "Status code is not 200"
    assert res.json()["id"] == fixture_id_resource_positive, "Id is different"


# Негативные проверки
def test_get_resource_negative(session, base_url, fixture_id_resource_negative):
    res = session.get(url=f'{base_url}/{fixture_id_resource_negative}')
    assert res.status_code == 404, "Status code is not 404"
    assert len(res.json()) == 0, "Dictionary is not empty"
