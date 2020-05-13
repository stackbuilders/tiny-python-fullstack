import json
from unittest.mock import patch

from app import FakeConsumer


def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200
    assert '{"Hello":"World"}' in res.get_data(as_text=True)


def test_info_endpoint_with_no_parameter(app, client):
    res = client.post('/info')
    assert res.status_code == 400
    assert 'Missing `user` parameter' in res.get_data(as_text=True)


def test_info_endpoint_with_parameter(app, client):
    with patch.object(FakeConsumer, 'json') as mockpost:
        mockvalue = {'name': 'foo'}
        mockpost.return_value = mockvalue

        res = client.post('/info', data=dict(user='foo'))
        assert res.status_code == 200
        assert mockvalue == json.loads(res.get_data(as_text=True))
