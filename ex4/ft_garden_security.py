#!/usr/bin/env python3


class Plant:
    def __init__(
        self,
        name: str,
        height: float,
        age: int,
        growth_rate: float = 0.8,
    ) -> None:
        self._name: str = name
        self._growth_rate: float = growth_rate

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

    def get_name(self) -> str:
        return self._name

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = float(height)
            display_h = int(height) if height == int(height) else height
            print(f"Height updated: {display_h}cm")
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
        step: float = rate if rate is not None else self._growth_rate
        self._height += step

    def age(self, days: int = 1) -> None:
        self._age += days

    def show(self) -> None:
        h: float = round(self._height, 1)
        print(f"{self._name}: {h}cm, {self._age} days old")


def main() -> None:
    print("=== Garden Security System ===")

    rose: Plant = Plant("Rose", 15.0, 10)
    print("Plant created: ", end="")
    rose.show()

    rose.set_height(25)
    rose.set_age(30)

    rose.set_height(-5)
    rose.set_age(-10)

    print("Current state: ", end="")
    rose.show()


if __name__ == "__main__":
    main()
