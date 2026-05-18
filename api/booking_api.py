from api.base_api import BaseApi
from config.api_urls import BOOKING_ENDPOINT
import allure


class BookingApi(BaseApi):

    @allure.step("Create booking with data = {data}")
    def create_booking(self, data: str):
        return self.post(BOOKING_ENDPOINT, json=data)

    @allure.step("Get booking by id = {booking_id}")
    def get_booking(self, booking_id: int ):
        return self.get(f"{BOOKING_ENDPOINT}/{booking_id}")

    @allure.step("Get all bookings by params = {params}")
    def get_all_bookings(self, params= None):
        return self.get(BOOKING_ENDPOINT, params)

    @allure.step("Update booking with data = {data}")
    def update_booking(self, booking_id: int, data: str, token: str = None):
        headers = {"Cookie": f"token={token}"}
        return self.put(f"{BOOKING_ENDPOINT}/{booking_id}", json=data, headers=headers)

    @allure.step("Partial update booking with data = {data}")
    def partial_update_booking(self, booking_id: int, data: str, token: str):
        headers = {"Cookie": f"token={token}"}
        return self.patch(f"{BOOKING_ENDPOINT}/{booking_id}", json=data, headers=headers)

    @allure.step("Delete booking by id = {booking_id}")
    def delete_booking(self, booking_id: int, token: str):
        headers = {"Cookie": f"token={token}"}
        return self.delete(f"{BOOKING_ENDPOINT}/{booking_id}" , headers=headers)