# main.py
import sys
from PyQt6.QtWidgets import QApplication

from grid_window import GridWindow, ViewMode
from puzzle_generator import PuzzleGenerator


def main() -> None:
    n = 4

    # QApplication is required for any PyQt app.
    # It manages the event loop (clicks, redraws, etc.)
    app = QApplication(sys.argv)

    # Create your generator and build a solution.
    gen = PuzzleGenerator(n=n)
    gen.generate_solution()

    # Check uniqueness (whatever your method does).
    # NOTE: This line depends on how you've implemented uniqueness.
    gen.uniqueness(gen.sol)

    # Build groups/cages for the puzzle.
    # Ideally, grouping() returns something like a list of cages.
    groups = gen.grouping()

    # Create the window.
    # For testing:
    # - solution_grid shows the solution values
    # - groups shows the group borders (once implemented)
    # - mode chooses what layers are visible
    w = GridWindow(
        n=n,
        game_grid=None,         # later: player-visible grid (partially filled, etc.)
        solution_grid=gen.sol,  # testing overlay
        groups=groups,          # cage info
        mode=ViewMode.GROUPS_AND_NUMBERS,
    )

    # You can flip modes any time during testing:
    # w.set_mode(ViewMode.GROUPS)  # only group outlines
    # w.set_mode(ViewMode.GAME)    # final player view

    w.show()

    # Start Qt event loop (keeps the window open).
    # When the window closes, the app exits.
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
