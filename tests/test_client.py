"""test foreman.client.py"""
from foreman.client import Client


def test_create_query_url():
    """__init__ test"""
    client = Client()
    query = "SET (test_rg, 1.0) INTO REGISTER"
    url = ("http://localhost:8188/fql?"
           "q=SET+%28test_rg%2C+1.0%29+INTO+REGISTER")
    assert client.create_query_url(query) == url
