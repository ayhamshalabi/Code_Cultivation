#!/usr/bin/env python3


class Plant:
	def __init__(self, name: str, height: float, age: int, growth_rate: float = 0.8) -> None:
		self._name: str = name
		self._growth_rate: float = growth_rate
		
		if height >= 0:
			self._height: float = height
		else:
			print(f"{self._name}: Error, height can't be negative")
			self._height = 0.0
		
		if age >= 0:
			self._age: int = age
		else:
			print(f"{self._name}: Error, age can't be negative")
			self._age = 0

	def get_name(self) -> str:
		return self._name
	
	def get_height(self) -> float:
		return self._height

	def get_age(self) -> int:
		return self._age

	def	set_height(self, height: float) -> None:
		if height >= 0:
			self._height = float(height)
			print(f"Height updated: {height}cm")
		else:
			print(f"{self._name}: Error, height can't be negative")
			print("Height update rejected")

	def	set_age(self, age: int) -> None:
		if age >= 0:
			self._age = age
			print(f"Age updated: {self._age} days")
		else:
			print(f"{self._name}: Error, age can't be negative")
			print("Age update rejected")

	def grow(self, rate: float | None = None) -> None:
		step: float = rate if rate is not None else self._growth_rate
		self._height += step

	def age(self, days: int = 1) -> None:
		self._age += days

	def show(self) -> None:
		print(
			f"{self._name}: {round(self._height, 1)}cm, "
			f"{self._age} days old"
			)


class Flower(Plant):
	def __init__(self, name: str, height: float, age: int, color: str, growth_rate: float = 0.8) -> None:
		super().__init__(name, height, age, growth_rate)
		self._color: str = color
		self._bloomed: bool = False

	def bloom(self) -> None:
		self._bloomed = True

	def show(self) -> None:
		super().show()
		print(f"Color: {self._color}")
		if self._bloomed:
			print(f"{self._name} is blooming beautifully!")
		else:
			print(f"{self._name} has not bloomed yet")


class Tree(Plant):
	def __init__(self, name: str, height: float, age: int, trunk_diameter: float, growth_rate: float = 0.8) -> None:
		super().__init__(name, height, age, growth_rate)
		self._trunk_diameter: float = trunk_diameter

	def produce_shade(self) -> None:
		print(f"Tree {self._name} now produces a shade of {round(self._height, 1)}cm long and {round(self._trunk_diameter, 1)}cm wide.")

	def show(self) -> None:
		super().show()
		print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
	def __init__(self, name: str, harvest_season: str, height: float, age: int, nutritional_value: int, growth_rate: float = 0.8) -> None:
		super().__init__(name, height, age, growth_rate)
		self._harvest_season: str = harvest_season
		self._nutritional_value: int = nutritional_value

	def age(self, days: int = 1) -> None:
		super().age(days)
		self._nutritional_value += days

	def show(self) -> None:
		super().show()
		print(f"Harvest season: {self._harvest_season}")
		print(f"Nutritional value: {self._nutritional_value}")


def main() -> None:
	print("=== Garden Plant Types ===")

	print("=== Flower")
	rose: Flower = Flower("Rose", 15.0, 10, "red")
	rose.show()
	print("[asking the rose to bloom]")
	rose.bloom()
	rose.show()

	print("=== Tree")
	oak: Tree = Tree("Oak", 200.0, 365, 5.0)
	oak.show()
	print("[asking the oak to produce shade]")
	oak.produce_shade()

	print("=== Vegetable")
	tomato: Vegetable = Vegetable("Tomato", "April", 5.0, 10, 0, 2.1)
	tomato.show()
	print("[make tomato grow and age for 20 days]")
	for _ in range(0, 20):
		tomato.age()
		tomato.grow()
	tomato.show()


if __name__ == "__main__":
	main()
