import sender_stand_request
import data

def test_code_is_200():
    track = sender_stand_request.create_order(data.order_body).json()['track']
    response = sender_stand_request.get_order_info_by_track(track)
    assert response.status_code == 200
