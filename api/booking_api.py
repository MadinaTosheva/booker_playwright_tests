from api.base_api import BaseApi
from config.api_urls import BOOKING_ENDPOINT


class BookingApi(BaseApi):

    def create_booking(self, data):
        return self.post(BOOKING_ENDPOINT, json=data)

    def get_booking(self, booking_id):
        return self.get(f"{BOOKING_ENDPOINT}/{booking_id}")

    def update_booking(self, booking_id, data, token = None):
        headers = {"Cookie": f"token={token}"}
        return self.put(f"{BOOKING_ENDPOINT}/{booking_id}", json=data, headers=headers)

    def partial_update_booking(self, booking_id, data, token):
        headers = {"Cookie": f"token={token}"}
        return self.patch(f"{BOOKING_ENDPOINT}/{booking_id}", json=data, headers=headers)

    def delete_booking(self, booking_id, token):
        headers = {"Cookie": f"token={token}"}
        return self.delete(f"{BOOKING_ENDPOINT}/{booking_id}" , headers=headers)