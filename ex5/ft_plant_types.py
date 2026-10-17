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
		self.color = color

	def bloom(self, bloomed: bool = False) -> None:
		if bloomed:
			print(f"{self._name} is blooming beautifully!")
		else:
			print(f"{self._name} has not bloomed yet")
			print("[asking the rose to bloom]")

	def show(self, bloomed: bool = False) -> None:
		super().show()
		print(f"Color: {self.color}")
		self.bloom(bloomed)


class Tree(Plant):
	def __init__(self, name: str, height: float, age: int, trunk_diameter: float, growth_rate: float = 0.8) -> None:
		super().__init__(name, height, age, growth_rate)
		self.trunk_diameter = trunk_diameter

	def produce_shade(self, shade: bool = False) -> None:
		if shade:
			print(f"Tree {self._name} now produces a shade of {round(self._height, 1)}cm long and {round(self.trunk_diameter, 1)}cm wide.")
		else:
			print("[asking the oak to produce shade]")

	def show(self, shade: bool = False) -> None:
		super().show()
		print(f"Trunk diameter: {self.trunk_diameter}cm")
		self.produce_shade(shade)


class Vegetable(Plant):
	def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int, growth_rate: float = 0.8) -> None:
		super().__init__(name, height, age, growth_rate)
		self.harvest_season = harvest_season
		self.nutritional_value = nutritional_value

	def age(self, days: int = 1) -> None:
		super().age(days)
		self.nutritional_value += 1

	def show(self) -> None:
		super().show()
		print(f"Harvest season: {self.harvest_season}")
		print(f"Nutritional value: {self.nutritional_value}")
		if self.nutritional_value != 20:
			print(f"[make tomato grow and age for {20 - self.nutritional_value} days]")


def main() -> None:
	print("=== Garden Plant Types ===")

	print("=== Flower")
	rose: Flower = Flower("Rose", 15.0, 10, "red")
	rose.show()
	rose.show(True)

	print("=== Tree")
	oak: Tree = Tree("Oak", 200.0, 365, 5.0)
	oak.show()
	oak.produce_shade(True)

	print("=== Vegetable")
	tomato: Vegetable = Vegetable("Tomato", 5.0, 10, "April", 0, 2.1)
	tomato.show()
	for i in range(0, 20):
		tomato.age()
		tomato.grow()
	tomato.show()


if __name__ == "__main__":
	main()
