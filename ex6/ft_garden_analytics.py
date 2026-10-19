#!/usr/bin/env python3


class Plant:

	class Stats:
		def __init__(self) -> None:
			self._grow_count: int = 0
			self._age_count: int = 0
			self._show_count: int = 0

		def increment_grow(self) -> None:
			self._grow_count += 1

		def increment_age(self) -> None:
			self._age_count += 1

		def increment_show(self) -> None:
			self._show_count += 1

		def get_grow_count(self) -> int:
			return self._grow_count

		def get_age_count(self) -> int:
			return self._age_count

		def get_show_count(self) -> int:
			return self._show_count

		def display(self) -> None:
			print(
				f"Stats: {self._grow_count} grow, "
				f"{self._age_count} age, "
				f"{self._show_count} show"
			)

	def __init__(self, name: str, height: float, age: int, growth_rate: float = 0.8) -> None:
		self._name: str = name
		self._growth_rate: float = growth_rate
		self._stats: Plant.Stats = self.Stats()

		if height >= 0:
			self._height: float = float(height)
		else:
			print(f"{self._name}: Error, height can't be negative")
			self._height = 0.0

		if age >= 0:
			self._age: int = age
		else:
			print(f"{self._name}: Error, age can't be negative")
			self._age = 0

	@staticmethod
	def is_older_than_year(days: int) -> bool:
		return days > 365

	check_year_old = is_older_than_year

	@classmethod
	def anonymous(cls) -> "Plant":
		return cls("Unknown plant", 0.0, 0)

	create_anonymous = anonymous

	def get_name(self) -> str:
		return self._name

	def get_height(self) -> float:
		return self._height

	def get_age(self) -> int:
		return self._age

	def get_stats(self) -> "Plant.Stats":
		return self._stats

	def set_height(self, height: float) -> None:
		if height >= 0:
			self._height = float(height)
			display_height = int(height) if height == int(height) else height
			print(f"Height updated: {display_height}cm")
		else:
			print(f"{self._name}: Error, height can't be negative")
			print("Height update rejected")

	def set_age(self, age: int) -> None:
		if age >= 0:
			self._age = age
			print(f"Age updated: {self._age} days")
		else:
			print(f"{self._name}: Error, age can't be negative")
			print("Age update rejected")

	def grow(self, rate: float | None = None) -> None:
		self._stats.increment_grow()
		step: float = rate if rate is not None else self._growth_rate
		self._height += step

	def age(self, days: int = 1) -> None:
		self._stats.increment_age()
		self._age += days

	def show(self) -> None:
		self._stats.increment_show()
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
	class Stats(Plant.Stats):
		def __init__(self) -> None:
			super().__init__()
			self._shade_count: int = 0

		def increment_shade(self) -> None:
			self._shade_count += 1

		def get_shade_count(self) -> int:
			return self._shade_count

		def display(self) -> None:
			super().display()
			print(f"{self._shade_count} shade")

	def __init__(self, name: str, height: float, age: int, trunk_diameter: float, growth_rate: float = 0.8) -> None:
		super().__init__(name, height, age, growth_rate)
		self._trunk_diameter: float = trunk_diameter
		self._stats = Tree.Stats()

	def produce_shade(self) -> None:
		if isinstance(self._stats, Tree.Stats):
			self._stats.increment_shade()
		h = round(self._height, 1)
		w = round(self._trunk_diameter, 1)
		print(
			f"Tree {self._name} now produces a shade of "
			f"{h}cm long and {w}cm wide."
		)

	def show(self) -> None:
		super().show()
		print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Vegetable(Plant):
	def __init__(self, name: str, height: float, age: int, harvest_season: str, nutritional_value: int = 0, growth_rate: float = 0.8) -> None:
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


class Seed(Flower):
	def __init__( self, name: str, height: float, age: int, color: str, seeds: int = 0, growth_rate: float = 0.8) -> None:
		super().__init__(name, height, age, color, growth_rate)
		self._seeds: int = seeds

	def bloom(self, seeds: int = 42) -> None:
		super().bloom()
		self._seeds = seeds

	def show(self) -> None:
		super().show()
		print(f"Seeds: {self._seeds}")


def display_plant_stats(plant: Plant) -> None:
	"""Unique standalone function displaying statistics for any plant."""
	print(f"[statistics for {plant.get_name()}]")
	plant.get_stats().display()


def main() -> None:
	print("=== Garden statistics ===")

	print("=== Check year-old")
	print("Is 30 days more than a year?")
	print(f"-> {Plant.is_older_than_year(30)}")
	print("Is 400 days more than a year?")
	print(f"-> {Plant.is_older_than_year(400)}")

	print("=== Flower")
	rose: Flower = Flower("Rose", 15.0, 10, "red")
	rose.show()
	display_plant_stats(rose)
	print("[asking the rose to grow and bloom]")
	rose.grow(8.0)
	rose.bloom()
	rose.show()
	display_plant_stats(rose)

	print("=== Tree")
	oak: Tree = Tree("Oak", 200.0, 365, 5.0)
	oak.show()
	display_plant_stats(oak)
	print("[asking the oak to produce shade]")
	oak.produce_shade()
	display_plant_stats(oak)

	print("=== Seed")
	sunflower: Seed = Seed("Sunflower", 80.0, 45, "yellow")
	sunflower.show()
	print("[make sunflower grow, age and bloom]")
	sunflower.grow(30.0)
	sunflower.age(20)
	sunflower.bloom()
	sunflower.show()
	display_plant_stats(sunflower)

	print("=== Anonymous")
	unknown: Plant = Plant.anonymous()
	unknown.show()
	display_plant_stats(unknown)


if __name__ == "__main__":
	main()