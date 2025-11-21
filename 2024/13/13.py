def parse_games(filename: str) -> list:
    """
    Button A: X+40, Y+38
    Button B: X+21, Y+84
    Prize: X=4245, Y=5634

    Button A: X+19, Y+11
    ...
    """
    def parse_button(line: str) -> tuple[int, int]:
        _, _, x, y = line.split()
        return int(x[2:-1]), int(y[2:])

    def parse_prize(line: str) -> tuple[int, int]:
        _, x, y = line.split()
        return int(x[2:-1]), int(y[2:])

    games = []
    lines = [line.strip() for line in open(filename)]
    for i in range(0, len(lines), 4):
        ax, ay = parse_button(lines[i])
        bx, by = parse_button(lines[i+1])
        px, py = parse_prize(lines[i+2])
        games.append((ax, ay, bx, by, px, py))
    return games


def part_one() -> int:
    """
    enumerate all options (A, B)

    A 0 thru 100
    B 0 thru 100
    ~10k options (can handle million games)
    """
    options = []
    for i in range(100):
        for j in range(100):
            options.append((i, j))

    def find(game: tuple[int,int,int,int,int,int]) -> tuple[int,int]:
        for option in options:
            a, b = option
            ax, ay, bx, by, px, py = game
            if px == ax * a + bx * b and py == ay * a + by * b:
                return option
        return None

    tokens = 0
    games = parse_games('input.txt')
    for game in games:
        option = find(game)
        if option:
            a, b = option
            tokens += 3*a+b

    return tokens

import sympy
from sympy import symbols, Matrix, linear_eq_to_matrix, linsolve

def part_two() -> int:
    """
    px = ax * a + bx * b
    py = ay * a + by * b

    [[ax, bx], (2x2 mat) * [a, b] (2x1 mat) = [px, py] (2x1 mat)
     [ay, by]]

    becomes system of linear scalar equations to find a and b

    use sympy to handle floating point precision. numpy did not work!!!
    """
    tokens = 0
    games = parse_games('input.txt')
    for game in games:
        ax, ay, bx, by, px, py = game
        px += 10000000000000
        py += 10000000000000

        # Define symbolic variables
        a, b = symbols('a b')

        # Define the system of linear equations
        eq1 = ax * a + bx * b - px
        eq2 = ay * a + by * b - py

        # Convert the equations into matrix form
        X, y = linear_eq_to_matrix([eq1, eq2], [a, b])

        # Solve the system of equations
        solution = linsolve((X, y), [a, b])

        # parse FiniteSet
        solution = list(solution)[0]
        a, b = solution

        # check sympy.core.numbers.Rational integer check (valid game)
        if a.is_Integer and b.is_Integer:
            tokens += 3 * a + b
    return tokens

tokens = part_two()
print(tokens)








