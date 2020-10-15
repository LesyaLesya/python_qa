# Позитивные проверки
def test_post_resource_positive(session, base_url, fixture_payload_resource_positive):
    res = session.post(url=base_url, json=fixture_payload_resource_positive)
    assert res.status_code == 201, "Status code is not 201"
    assert res.json()["id"] == 201, "ID of post is not 201"
    assert res.json()["userId"] == fixture_payload_resource_positive["userId"], "Wrong uderId"
    assert res.json()["title"] == fixture_payload_resource_positive["title"], "Wrong title"
    assert res.json()["completed"] == fixture_payload_resource_positive["completed"], "Wrong completed status"


# Негативные проверки
def test_post_resource_negative(session, base_url):
    payload = {"a": 100}
    res = session.post(url=base_url, data=payload, headers={"Content-type": "application/json"})
    assert res.status_code == 500, "Status code is not 500"
