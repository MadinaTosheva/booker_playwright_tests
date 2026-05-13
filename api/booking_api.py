from api.base_api import BaseApi
from config.api_urls import BOOKING_ENDPOINT


class BookingApi(BaseApi):

    def create_booking(self, data: str):
        return self.post(BOOKING_ENDPOINT, json=data)

    def get_booking(self, booking_id: int ):
        return self.get(f"{BOOKING_ENDPOINT}/{booking_id}")

    def get_all_bookings(self, params= None):
        return self.get(BOOKING_ENDPOINT, params)

    def update_booking(self, booking_id: int, data: str, token: str = None):
        headers = {"Cookie": f"token={token}"}
        return self.put(f"{BOOKING_ENDPOINT}/{booking_id}", json=data, headers=headers)

    def partial_update_booking(self, booking_id: int, data: str, token: str):
        headers = {"Cookie": f"token={token}"}
        return self.patch(f"{BOOKING_ENDPOINT}/{booking_id}", json=data, headers=headers)

    def delete_booking(self, booking_id: int, token: str):
        headers = {"Cookie": f"token={token}"}
        return self.delete(f"{BOOKING_ENDPOINT}/{booking_id}" , headers=headers)