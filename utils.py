import math
from typing import Tuple, Dict, List, Union
import pygame
import sys

#%%
class SimpleTurtle:
    """Representa una tortuga gráfica simple que se mueve en un plano 2D."""

    def __init__(self) -> None:
        self.__heading_angle_degrees: int = 0  # Ángulo de dirección en grados
        self.__current_position: Tuple[float, float] = (0, 0)  # Posición actual en el plano (x, y)

    def move_forward(self, units: int) -> None:
        """Mueve la tortuga hacia adelante en la dirección actual por la cantidad de unidades especificada."""
        x_end = self.__current_position[0] + math.cos(math.radians(self.__heading_angle_degrees)) * units
        y_end = self.__current_position[1] + math.sin(math.radians(self.__heading_angle_degrees)) * units
        self.__current_position = (x_end, y_end)

    def turn_left(self, angle: int) -> None:
        """Gira la tortuga a la izquierda por el ángulo especificado."""
        self.__heading_angle_degrees = (self.__heading_angle_degrees + angle) % 360

    def turn_right(self, angle: int) -> None:
        """Gira la tortuga a la derecha por el ángulo especificado."""
        self.__heading_angle_degrees = (self.__heading_angle_degrees - angle) % 360

    def get_heading(self) -> int:
        """Devuelve el ángulo de dirección actual de la tortuga."""
        return self.__heading_angle_degrees

    def get_position(self) -> Tuple[float, float]:
        """Devuelve la posición actual de la tortuga."""
        return self.__current_position

    def go_to(self, position: Tuple[float, float]) -> None:
        """Mueve la tortuga a una posición específica sin cambiar su dirección."""
        self.__current_position = position

    def set_heading(self, heading: int) -> None:
        """Establece la dirección de la tortuga al ángulo especificado."""
        self.__heading_angle_degrees = heading



#%%
class LSystemRenderer:
    """Clase para renderizar L-Systems usando una tortuga gráfica."""

    def __init__(self, axiom: str, rules: Dict[str, str], iterations: int, angle: float) -> None:
        self.axiom = axiom  # La cadena inicial del sistema
        self.rules = rules  # Reglas de reemplazo
        self.iterations = iterations  # Número de iteraciones para aplicar reglas
        self.angle = angle  # Ángulo de giro para comandos

        self.turtle = SimpleTurtle()  # Usar la clase SimpleTurtle para movimientos
        self.turtle.turn_left(90)  # Alineación inicial

        self.final_rule = self._generate_final_rule()
        self.point_list = []

    def _generate_final_rule(self) -> str:
        """Genera la regla final aplicando las reglas de reemplazo al axioma, iterativamente."""
        current_axiom = self.axiom
        for _ in range(self.iterations):
            current_axiom = "".join([self.rules.get(char, char) for char in current_axiom])
        return current_axiom

    def calculate_points(self, units: int = 5) -> None:
        """Dibuja el L-System calculado, interpretando los comandos para mover la tortuga."""
        stack = []
        for command in self.final_rule:
            if command == 'F':
                starting_point = self.turtle.get_position()
                self.turtle.move_forward(units)
                ending_point = self.turtle.get_position()
                self.point_list.append((starting_point, ending_point))
            elif command == '+':
                self.turtle.turn_right(self.angle)
            elif command == '-':
                self.turtle.turn_left(self.angle)
            elif command == '[':
                stack.append((self.turtle.get_position(), self.turtle.get_heading()))
            elif command == ']':
                position, heading = stack.pop()
                self.turtle.go_to(position)
                self.turtle.set_heading(heading)

    def get_points(self) -> List[Tuple[Tuple[float, float], Tuple[float, float]]]:
        """Devuelve una lista de puntos dibujados por la tortuga."""
        return self.point_list