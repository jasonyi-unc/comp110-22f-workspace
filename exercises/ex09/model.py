"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730604615"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)

    def distance(self, p: Point) -> float:
        """Returns the distance between a Point object and the Point object from parameter."""
        return sqrt(((self.x - p.x) ** 2) + ((self.y - p.y) ** 2))
    
    
class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int = 0

    def __init__(self, location: Point, direction: Point):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction

    def tick(self) -> None:
        """Reassign the object's location attribute the result of adding the self object's location with its direction."""
        self.location = self.location.add(self.direction)
        if self.is_infected():
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()

    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        elif self.is_infected():
            return "red"
        elif self.is_immune():
            return "green"
        else:
            return "black"

    def contract_disease(self) -> None:
        """Assigns the sickness attribute the INFECTED constant."""
        self.sickness = constants.INFECTED

    def contact_with(self, p: Cell) -> None:
        """If either of the Cell objects are infected, the counter becomes infected."""
        if self.is_infected() and p.is_vulnerable():
            p.contract_disease()
        elif self.is_vulnerable() and p.is_infected():
            self.contract_disease()

    def is_vulnerable(self) -> bool:
        """Return True when sickness is equal to the VULNERABLE constant and False otherwise."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Returns True when sickness attribute equates to the INFECTED constant."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def immunize(self) -> None:
        """Assigns the sickness attribute with the IMMUNE constant."""
        self.sickness = constants.IMMUNE

    def is_immune(self) -> bool:
        """Returns True when the sickness attribute equates to the IMMUNE constant."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, infected_cells: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        if infected_cells <= 0 or infected_cells >= cells:
            raise ValueError("Invalid infected_cells number. Try again.")
        if immune_cells < 0 or immune_cells >= cells:
            raise ValueError("Invalid immune_cells. Try again.")
        x: int = 0
        y: int = 0
        self.population = []
        for _ in range(cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            if x < infected_cells:
                cell.contract_disease()
                x += 1
            if y < immune_cells:
                cell.immunize()
                y += 1
            self.population.append(cell)

    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        elif cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        elif cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        elif cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Compares the distance between every 2 Cell objects' location attributes in the population."""
        for i in range(len(self.population)):
            for j in range(i + 1, len(self.population)):
                if self.population[i].location.distance(self.population[j].location) < constants.CELL_RADIUS:
                    self.population[i].contact_with(self.population[j])

    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for i in self.population:
            if i.is_infected():
                return False
        return True