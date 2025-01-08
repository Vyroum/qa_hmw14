from dataclasses import dataclass


@dataclass
class CPUs:
    model: str
    quantity: str


cpu = CPUs(model="Intel Core i7", quantity="1")
