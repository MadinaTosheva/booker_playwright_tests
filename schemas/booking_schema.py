# get_bookings_schema = {
#     "type": "object",
#     "properties": {
#         "bookingid": {"type": "integer"},
#         "booking": {
#             "type": "object",
#             "properties": {
#                 "firstname": {"type": "string"},
#                 "lastname": {"type": "string"},
#                 "totalprice": {"type": "integer"},
#                 "depositpaid": {"type": "boolean"},
#                 "bookingdates": {
#                     "type": "object",
#                     "properties": {
#                         "checkin": {"type": "string"},
#                         "checkout": {"type": "string"}
#                     },
#                     "required": ["checkin", "checkout"]
#                 }
#             },
#             "required": ["firstname", "lastname"]
#         }
#     },
#     "required": ["bookingid", "booking"]
# }


GET_BOOKING_SCHEMA = {

            "type": "object",
            "properties": {
                "firstname": {"type": "string"},
                "lastname": {"type": "string"},
                "totalprice": {"type": "integer"},
                "depositpaid": {"type": "boolean"},
                "bookingdates": {
                    "type": "object",
                    "properties": {
                        "checkin": {"type": "string"},
                        "checkout": {"type": "string"}
                    },
                    "required": ["checkin", "checkout"]
                }
            },
            "required": ["firstname", "lastname"]
        }


GET_ALL_BOOKINGS_SCHEMA = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
                "bookingid": {"type": "integer"}
        },
        "required": ["bookingid"]
    }

}