from aiogram.filters.callback_data import CallbackData

class ChooseDonationPlaceCallback(CallbackData, prefix="donation_place"):
    id: str
    name: str

class ChooseDonationDatetimeCallback(CallbackData, prefix="donation_datetime", sep="-"):
    id: int
    place_id: int
    datetime: str