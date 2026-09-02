import requests

base_url = "https://reqres.in/api"


def test_get_user_list():
    """获取用户列表接口"""
    resp = requests.get(f"{base_url}/users", params={"page": 1})
    assert resp.status_code == 200
    data = resp.json()
    assert data["page"] == 1


def test_create_user():
    """创建用户接口"""
    payload = {"name": "zhangsan", "job": "tester"}
    resp = requests.post(f"{base_url}/users", json=payload)
    assert resp.status_code == 201
    assert resp.json()["name"] == "zhangsan"
