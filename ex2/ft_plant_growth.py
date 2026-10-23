#!/usr/bin/env python3


class Plant:
    def __init__(
        self,
        name: str = "",
        height: float = 0.0,
        days_old: int = 0,
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
        h: float = round(self.height, 1)
        print(f"{self.name}: {h}cm, {self.days_old} days old")


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
