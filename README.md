# Code Cultivation: Object-Oriented Garden Systems

![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)
![Linter](https://img.shields.io/badge/Linter-flake8-green.svg)
![Type_Check](https://img.shields.io/badge/Type_Check-mypy_strict-brightgreen.svg)
![School](https://img.shields.io/badge/42-Project-black.svg)

A comprehensive digital garden ecosystem built in Python 3.10+ demonstrating fundamental to advanced Object-Oriented Programming (OOP) concepts, software architecture design, type hinting, and data encapsulation.

---

## Table of Contents

- [Overview](#overview)
- [Repository Structure](#repository-structure)
- [General Requirements & Standards](#general-requirements--standards)
- [Key Programming Concepts & Defense Topics](#key-programming-concepts--defense-topics)
  - [The Shebang Line (`#!/usr/bin/env python3`)](#the-shebang-line)
  - [The `if __name__ == "__main__":` Idiom](#the-if-__name__----__main__-idiom)
  - [Encapsulation: Protected (`_attr`) vs Mangled (`__attr`)](#encapsulation-protected-_attr-vs-mangled-__attr)
  - [Inheritance and `super()`](#inheritance-and-super)
  - [Nested Classes (Composition / Internal Systems)](#nested-classes-composition--internal-systems)
  - [Static Methods vs Class Methods vs Instance Methods](#static-methods-vs-class-methods-vs-instance-methods)
- [Exercises Breakdown](#exercises-breakdown)
  - [Exercise 0: Planting Your First Seed](#exercise-0-planting-your-first-seed)
  - [Exercise 1: Garden Data Organizer](#exercise-1-garden-data-organizer)
  - [Exercise 2: Plant Growth Simulator](#exercise-2-plant-growth-simulator)
  - [Exercise 3: Plant Factory](#exercise-3-plant-factory)
  - [Exercise 4: Garden Security System](#exercise-4-garden-security-system)
  - [Exercise 5: Specialized Plant Types](#exercise-5-specialized-plant-types)
  - [Exercise 6: Garden Analytics](#exercise-6-garden-analytics)
- [Verification & Quality Assurance](#verification--quality-assurance)

---

## Overview

The **Code Cultivation** module introduces progressive Object-Oriented Programming principles by developing tools to manage a community garden:
1. **Procedural Basics**: Program entry points, shebang, and execution control.
2. **Class Modeling**: Defining classes, instance creation, and state management.
3. **Behavior Simulation**: Class methods that mutate state over time (`grow()`, `age()`).
4. **Constructors**: Streamlined initialization via `__init__()`.
5. **Data Protection**: Encapsulation using protected attributes and input validation.
6. **Inheritance & Polymorphism**: Specialized hierarchies (`Flower`, `Tree`, `Vegetable`) with method overriding and `super()`.
7. **Advanced Systems**: Nested classes for tracking analytics, static methods, class factory methods, and standalone polymorphic utility functions.

---

## Repository Structure

```text
Code_Cultivation/
├── README.md
├── ex0/
│   └── ft_garden_intro.py
├── ex1/
│   └── ft_garden_data.py
├── ex2/
│   └── ft_plant_growth.py
├── ex3/
│   └── ft_plant_factory.py
├── ex4/
│   └── ft_garden_security.py
├── ex5/
│   └── ft_plant_types.py
└── ex6/
    └── ft_garden_analytics.py
```

---

## General Requirements & Standards

- **Python Version**: Python 3.10+
- **Code Style**: 100% compliant with **flake8** standards (max line length 79 characters, no unused imports/variables, proper PEP 8 spacing).
- **Type Safety**: Fully typed with strict static type checking via **mypy --strict** (all function parameters, return values, and internal attributes explicitly annotated).
- **Naming Conventions**:
  - Classes: `PascalCase` (e.g., `Plant`, `Flower`, `Tree`, `Vegetable`, `Seed`)
  - Functions, methods, and variables: `snake_case` (e.g., `produce_shade`, `trunk_diameter`, `grow_count`)
- **Strict Adherence to Authorized Functions**: Only functions explicitly authorized in each exercise's subject sheet are utilized.

---

## Key Programming Concepts & Defense Topics

During peer evaluations, you will be expected to explain and justify the following architectural decisions:

### The Shebang Line
```python
#!/usr/bin/env python3
```
- **What it does**: On Unix-like systems, the first line starting with `#!` indicates the path to the interpreter that should execute the script when run directly from the command line (`./ft_garden_intro.py`).
- **Why `/usr/bin/env python3`**: Using `env` looks up `python3` in the user's active `PATH` rather than hardcoding a fixed path like `/usr/bin/python3`, ensuring compatibility across different operating systems, virtual environments, and package managers.
- **Making it executable**: `chmod +x <file>.py` allows direct execution without explicitly calling `python3`.

### The `if __name__ == "__main__":` Idiom
- When a Python file is run directly, Python sets the special variable `__name__` to `"__main__"`.
- When the file is imported into another script or module (`import ft_garden_intro`), `__name__` is set to the module name (e.g., `"ft_garden_intro"`).
- Wrapping execution logic inside `if __name__ == "__main__":` ensures that code is only executed during direct execution, preventing unintended side effects during imports.

### Encapsulation: Protected (`_attr`) vs Mangled (`__attr`)
- **Subject Requirement**: Use the protected convention (single underscore `_name`), **not** name mangling (double underscore `__name`).
- **Protected Convention (`_attr`)**: A standard Python convention signaling to other developers that an attribute or method is internal and should not be accessed directly outside the class interface. It allows subclasses to inherit and cleanly access attributes via `self._attr`.
- **Name Mangling (`__attr`)**: Prepends `_ClassName` to the attribute name (e.g., `_Plant__name`) to avoid accidental overrides in subclasses. The subject explicitly forbids mangling here to maintain clean inheritance interfaces across exercises 4 to 6.

### Inheritance and `super()`
- `super()` returns a proxy object delegating method calls to a parent class.
- Calling `super().__init__(...)` ensures that base class state is properly initialized before subclass-specific attributes are attached.
- Calling `super().show()` or `super().age(days)` enables method overriding while reusing existing logic without code duplication.

### Nested Classes (Composition / Internal Systems)
- In Exercise 6, `Plant.Stats` is implemented as an inner (nested) class.
- Each `Plant` instance holds an internal instance of `Stats` (`self._stats`), demonstrating composition.
- In `Tree`, a nested `Tree.Stats` inherits from `Plant.Stats` to extend metrics (`_shade_count`), demonstrating nested class inheritance.

### Static Methods vs Class Methods vs Instance Methods
- **Instance Method** (`def method(self)`): Operates on a specific instance and has access to instance attributes via `self`.
- **Class Method** (`@classmethod def method(cls)`): Bound to the class rather than an instance. Receives `cls` as its first parameter. Ideal for alternative constructors (factory methods like `Plant.anonymous()`).
- **Static Method** (`@staticmethod def method()`): Self-contained utility function bound to the class namespace without access to `self` or `cls` (e.g., `Plant.is_older_than_year(days)`).

---

## Exercises Breakdown

### Exercise 0: Planting Your First Seed
- **Directory**: `ex0/`
- **File**: `ft_garden_intro.py`
- **Authorized Functions**: `print()`
- **Goal**: Create the starting entry point of a Python program with variables (`name`, `height`, `age`), shebang, and `if __name__ == "__main__":`.
- **Output**:
  ```text
  === Welcome to My Garden ===
  Plant: Rose
  Height: 25cm
  Age: 30 days
  === End of Program ===
  ```

### Exercise 1: Garden Data Organizer
- **Directory**: `ex1/`
- **File**: `ft_garden_data.py`
- **Authorized Functions**: `print()`
- **Goal**: Define the baseline `Plant` class with attributes (`name`, `height`, `age`) and a `show()` method. Manage at least 3 distinct plant instances.
- **Output**:
  ```text
  === Garden Plant Registry ===
  Rose: 25cm, 30 days old
  Sunflower: 80cm, 45 days old
  Cactus: 15cm, 120 days old
  ```

### Exercise 2: Plant Growth Simulator
- **Directory**: `ex2/`
- **File**: `ft_plant_growth.py`
- **Authorized Functions**: `print()`, `range()`, `round()`
- **Goal**: Add behavior to `Plant` via `grow()` and `age()` methods. Simulate 7 days of growth, reporting daily updates and calculating total weekly growth.
- **Output**:
  ```text
  === Garden Plant Growth ===
  Rose: 25.0cm, 30 days old
  === Day 1 ===
  Rose: 25.8cm, 31 days old
  ...
  === Day 7 ===
  Rose: 30.6cm, 37 days old
  Growth this week: 5.6cm
  ```

### Exercise 3: Plant Factory
- **Directory**: `ex3/`
- **File**: `ft_plant_factory.py`
- **Authorized Functions**: `print()`, `range()`, `round()`
- **Goal**: Streamline object construction using `__init__()` to instantiate and initialize plants simultaneously. Create and display at least 5 distinct plants.
- **Output**:
  ```text
  === Plant Factory Output ===
  Created: Rose: 25.0cm, 30 days old
  Created: Oak: 200.0cm, 365 days old
  Created: Cactus: 5.0cm, 90 days old
  Created: Sunflower: 80.0cm, 45 days old
  Created: Fern: 15.0cm, 120 days old
  ```

### Exercise 4: Garden Security System
- **Directory**: `ex4/`
- **File**: `ft_garden_security.py`
- **Authorized Functions**: `print()`, `range()`, `round()`
- **Goal**: Implement data integrity and encapsulation.
  - Protected attributes: `_name`, `_height`, `_age`, `_growth_rate`.
  - Getters: `get_name()`, `get_height()`, `get_age()`.
  - Setters with validation: `set_height()`, `set_age()` reject negative values with error messages without corrupting internal state.
  - Constructor validation: Initializes invalid negative inputs to 0.0 / 0 with an error notification.
- **Output**:
  ```text
  === Garden Security System ===
  Plant created: Rose: 15.0cm, 10 days old
  Height updated: 25cm
  Age updated: 30 days
  Rose: Error, height can't be negative
  Height update rejected
  Rose: Error, age can't be negative
  Age update rejected
  Current state: Rose: 25.0cm, 30 days old
  ```

### Exercise 5: Specialized Plant Types
- **Directory**: `ex5/`
- **File**: `ft_plant_types.py`
- **Authorized Functions**: `super()`, `print()`, `range()`, `round()`
- **Goal**: Implement inheritance hierarchies branching from `Plant`:
  - `Flower`: adds `_color` and `bloom()`.
  - `Tree`: adds `_trunk_diameter` and `produce_shade()`.
  - `Vegetable`: adds `_harvest_season`, `_nutritional_value`, and increments nutritional value through simulation growth.
  - Reuses parent implementations via `super().__init__()` and `super().show()`.
- **Output**:
  ```text
  === Garden Plant Types ===
  === Flower
  Rose: 15.0cm, 10 days old
  Color: red
  Rose has not bloomed yet
  [asking the rose to bloom]
  Rose: 15.0cm, 10 days old
  Color: red
  Rose is blooming beautifully!
  === Tree
  Oak: 200.0cm, 365 days old
  Trunk diameter: 5.0cm
  [asking the oak to produce shade]
  Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
  === Vegetable
  Tomato: 5.0cm, 10 days old
  Harvest season: April
  Nutritional value: 0
  [make tomato grow and age for 20 days]
  Tomato: 47.0cm, 30 days old
  Harvest season: April
  Nutritional value: 20
  ```

### Exercise 6: Garden Analytics
- **Directory**: `ex6/`
- **File**: `ft_garden_analytics.py`
- **Authorized Functions**: `super()`, `print()`, `range()`, `round()`, `staticmethod()`, `classmethod()`
- **Goal**:
  - Static method `Plant.is_older_than_year(days: int) -> bool` checking if days > 365.
  - Class method `Plant.anonymous() -> Plant` acting as a factory constructor for unnamed seedlings.
  - `Seed(Flower)` tracking seed production upon blooming.
  - Nested class `Plant.Stats` tracking counts of `grow()`, `age()`, and `show()` calls.
  - Nested subclass `Tree.Stats` tracking `produce_shade()` calls.
  - Standalone polymorphic function `display_plant_stats(plant: Plant)` displaying stats for any plant.
- **Output**:
  ```text
  === Garden statistics ===
  === Check year-old
  Is 30 days more than a year? -> False
  Is 400 days more than a year? -> True
  === Flower
  Rose: 15.0cm, 10 days old
  Color: red
  Rose has not bloomed yet
  [statistics for Rose]
  Stats: 0 grow, 0 age, 1 show
  [asking the rose to grow and bloom]
  Rose: 23.0cm, 10 days old
  Color: red
  Rose is blooming beautifully!
  [statistics for Rose]
  Stats: 1 grow, 0 age, 2 show
  === Tree
  Oak: 200.0cm, 365 days old
  Trunk diameter: 5.0cm
  [statistics for Oak]
  Stats: 0 grow, 0 age, 1 show
  0 shade
  [asking the oak to produce shade]
  Tree Oak now produces a shade of 200.0cm long and 5.0cm wide.
  [statistics for Oak]
  Stats: 0 grow, 0 age, 1 show
  1 shade
  === Seed
  Sunflower: 80.0cm, 45 days old
  Color: yellow
  Sunflower has not bloomed yet
  Seeds: 0
  [make sunflower grow, age and bloom]
  Sunflower: 110.0cm, 65 days old
  Color: yellow
  Sunflower is blooming beautifully!
  Seeds: 42
  [statistics for Sunflower]
  Stats: 1 grow, 1 age, 2 show
  === Anonymous
  Unknown plant: 0.0cm, 0 days old
  [statistics for Unknown plant]
  Stats: 0 grow, 0 age, 1 show
  ```

---

## Verification & Quality Assurance

### 1. Running the Programs
Run any exercise directly using standard Python:
```bash
python3 ex0/ft_garden_intro.py
python3 ex1/ft_garden_data.py
python3 ex2/ft_plant_growth.py
python3 ex3/ft_plant_factory.py
python3 ex4/ft_garden_security.py
python3 ex5/ft_plant_types.py
python3 ex6/ft_garden_analytics.py
```

### 2. Linter Verification (flake8)
Verify that all source code conforms strictly to PEP 8 standards:
```bash
flake8 .
```
*(Expected output: No warnings or errors).*

### 3. Type Checking (mypy --strict)
Verify full type annotations and strict type safety:
```bash
mypy --strict .
```
*(Expected output: `Success: no issues found in 7 source files`).*
