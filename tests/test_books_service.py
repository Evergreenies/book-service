def test_list_all_books(client):
    assert client.get("/books").status_code == 200
