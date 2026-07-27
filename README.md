# Star Pattern Generator

## Overview

The Star Pattern Generator is a Python application that creates a visual pattern using asterisks (`*`). The pattern grows line by line until it reaches a specified maximum width and then shrinks symmetrically. This project is useful for practicing loops, pattern design, and algorithmic thinking.

## Features

* Accepts a maximum star length from the user.
* Generates an increasing star pattern.
* Automatically generates a decreasing pattern after reaching the maximum.
* Uses nested loops to control pattern creation.
* Demonstrates string multiplication for efficient output generation.

## Technologies Used

* Python 3

## Project Structure

```text
Star-Pattern-Generator/
│
├── star_pattern.py
└── README.md
```

## How to Run

1. Ensure Python 3 is installed.
2. Save the program as `star_pattern.py`.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python star_pattern.py
```

## Example

### Input

```text
What is the maximum length of stars you wished for? 5
```

### Output

```text
*
**
***
****
*****
****
***
**
*
```

## How It Works

1. The program asks the user for the maximum number of stars.
2. The `pattern()` function initializes a counter named `limit`.
3. A `for` loop generates the increasing part of the pattern:

   * 1 star
   * 2 stars
   * 3 stars
   * and so on until the maximum length is reached.
4. Once the maximum length is exceeded, a second loop generates the decreasing part:

   * Maximum - 1 stars
   * Maximum - 2 stars
   * Continuing until only one star remains.
5. Each line is printed using string multiplication:

```python
print("*" * limit)
```

## Pattern Visualization

For an input of `4`:

```text
*
**
***
****
***
**
*
```

For an input of `3`:

```text
*
**
***
**
*
```

## Program Flow

```text
User Input
     ↓
Generate Increasing Pattern
     ↓
Reach Maximum Length
     ↓
Generate Decreasing Pattern
     ↓
Display Complete Pattern
```

## Concepts Demonstrated

* Functions
* `for` loops
* Nested loops
* String multiplication
* User input
* Pattern generation
* Algorithm design

## Algorithm Logic

The pattern consists of two phases:

### Phase 1: Ascending

```text
*
**
***
****
*****
```

### Phase 2: Descending

```text
****
***
**
*
```

Combining both phases produces a symmetric pyramid-like pattern.

## Possible Improvement

The current implementation mixes the ascending and descending logic inside the same loop, which can make the code harder to understand.

A cleaner approach would be:

```python
for i in range(1, max_num + 1):
    print("*" * i)

for i in range(max_num - 1, 0, -1):
    print("*" * i)
```

This version separates the ascending and descending phases, making the algorithm easier to read and maintain.

## Future Improvements

* Generate centered pyramid patterns.
* Support custom symbols instead of only `*`.
* Create diamond-shaped patterns.
* Add pattern alignment options (left, center, right).
* Export generated patterns to a text file.

## Author

Created as a Python practice project to demonstrate loops, pattern generation, string manipulation, and algorithmic thinking.
