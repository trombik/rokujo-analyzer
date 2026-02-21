from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_analyze_endpoint():
    payload = {"text": "自己責任でお願いします。"}
    response = client.post("/analyze_tokens", json=payload)
    assert response.status_code == 200

    data = response.json()
    assert "tokens" in data

    tokens = data["tokens"]
    assert len(tokens) > 0

    first_token = tokens[0]
    expected_keys = {"i", "text", "lemma", "pos", "tag", "dep", "head", "morph", "idx"}
    assert set(first_token.keys()) == expected_keys

    assert tokens[0]["text"] == "自己責任"
    assert tokens[0]["pos"] == "NOUN"


def test_analyze_empty_text():
    response = client.post("/analyze_tokens", json={"text": ""})
    assert response.status_code == 200
    assert response.json()["tokens"] == []
