#!/usr/bin/env python3


class Plant:
	name: str
	height: float
	days_old: int
	growth_rate: float

	def grow(self, rate: float | None = None) -> None:
		step: float = rate if rate is not None else self.growth_rate
		self.height += step

	def age(self, days: int = 1) -> None:
		self.days_old += days

	def show(self) -> None:
		print(
			f"{self.name}: {round(self.height, 1)}cm,"
			f"{self.days_old} days old"
			)


def main() -> None:
	print("=== Garden Plant Growth ===")

	rose: Plant = Plant()
	rose.name = "Rose"
	rose.height = 25.0
	rose.days_old = 30
	rose.growth_rate = 0.8
	initial_height: float = rose.height
	
	rose.show()
	
	for day in range(1, 8):
		rose.grow()
		rose.age()
		print(f"=== Day {day} ===")
		rose.show()

	print(f"Growth this week: {round(rose.height - initial_height, 1)}cm")


if __name__ == "__main__":
	main()
