class Residence:

    def __init__(self, location: str, district: str, resid_num: int) -> None:
        self._location = location
        self._district_name = district
        self._residence_number = resid_num


    @property
    def _(self):
        return{
            "location": self._location,
            "district": self._district_name,
            "resid_number": self._residence_number
        }