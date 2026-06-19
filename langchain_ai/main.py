from typing import TypedDict

class CityInfo(TypedDict):
    name: str
    country: str
    population: int
    is_capital: bool

kathmandu: CityInfo = {
    "name": "Kathmandu",
    "country": "Nepal",
    "population": "845767",
}
print(kathmandu, type(kathmandu))

a = {"one": 34345, "two": "one"}
print(a, type(a))