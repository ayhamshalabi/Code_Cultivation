#!/usr/bin/env python3


class Plant:
	def __init__(
		self,
		name: str,
		height: float,
		days_old: int,
		growth_rate: float = 0.8,
	) -> None:
		self.name: str = name
		self.height: float = height
		self.days_old: int = days_old
		self.growth_rate: float = growth_rate

	def grow(self, rate: float | None = None) -> None:
		step: float = rate if rate is not None else self.growth_rate
		self.height += step

	def age(self, days: int = 1) -> None:
		self.days_old += days

	def show(self) -> None:
		print(
			f"{self.name}: {round(self.height, 1)}cm, "
			f"{self.days_old} days old"
			)


def main() -> None:
	print("=== Plant Factory Output ===")

	plants: list[Plant] = [
		Plant("Rose", 25.0, 30, 0.8),
		Plant("Oak", 200.0, 365, 0.8),
		Plant("Cactus", 5.0, 90, 0.8),
		Plant("Sunflower", 80.0, 45, 0.8),
		Plant("Fern", 15.0, 120, 0.8),
	]

	for plant in plants:
		print("Created: ", end="")
		plant.show()


if __name__ == "__main__":
	main()
