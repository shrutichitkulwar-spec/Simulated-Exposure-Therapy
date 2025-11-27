def test_vr_message():
    msg = {"command": "SET_INTENSITY", "value": 0.7}
    assert msg["value"] == 0.7
