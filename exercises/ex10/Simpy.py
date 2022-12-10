"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730604615"


class Simpy:
    """Simpy class."""
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor of Simpy class."""
        self.values = values

    def __repr__(self) -> str:
        """Produce a str representation for Simpy."""
        return f"Simpy({self.values})"

    def fill(self, value: float, x: int) -> None:
        """Mutates the list values to value at x number of times."""
        self.values = []
        for _ in range(x):
            self.values.append(value)

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Fill in the values attribute with range of values in terms of floats."""
        assert step != 0.0
        count: float = start
        if start < stop:
            while count < stop:
                self.values.append(count)
                count += step
        else:
            while stop < count:
                self.values.append(count)
                count += step
        return self.values

    def sum(self) -> float:
        """Returns the sum of the elements in the values list."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the addition operator for Simpy."""
        result: list[float] = []
        if isinstance(rhs, float):
            for x in range(len(self.values)):
                result.append(self.values[x] + rhs)
            return Simpy(result)
        else:
            for x in range(len(self.values)):
                result.append(self.values[x] + rhs.values[x])
            return Simpy(result)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Overload the power operator for Simpy."""
        result: list[float] = []
        if isinstance(rhs, float):
            for x in range(len(self.values)):
                result.append(self.values[x] ** rhs)
            return Simpy(result)
        else:
            for x in range(len(self.values)):
                result.append(self.values[x] ** rhs.values[x])
            return Simpy(result)
        
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload the equator operator for Simpy."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for x in range(len(self.values)):
                result.append(self.values[x] == rhs)
            return result
        else:
            for x in range(len(self.values)):
                result.append(self.values[x] == rhs.values[x])
            return result

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Overload the greater than operator for Simpy."""
        result: list[bool] = []
        if isinstance(rhs, float):
            for x in range(len(self.values)):
                result.append(self.values[x] > rhs)
            return result
        else:
            for x in range(len(self.values)):
                result.append(self.values[x] > rhs.values[x])
            return result

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Overload the subscription notation."""
        if isinstance(rhs, int):
            return self.values[rhs]
        else:
            result: list[float] = []
            for i in range(len(rhs)):
                if rhs[i]:
                    result.append(self.values[i])
            return Simpy(result)