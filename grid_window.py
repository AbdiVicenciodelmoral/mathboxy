# grid_window.py
from __future__ import annotations

# Enum is a clean way to represent "modes" (states) without using strings like "GAME"
# auto() assigns unique values automatically.
from enum import Enum, auto

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QMainWindow, QTableWidget, QTableWidgetItem


class ViewMode(Enum):
    """
    These are the different ways we might render the same table.

    Why use an Enum?
    - You avoid typos ("group" vs "groups")
    - Your code reads clearly (ViewMode.GAME is self-explanatory)
    - You can refactor safely and IDEs can help autocomplete
    """
    GAME = auto()                # Only the playable grid (what players will see)
    GROUPS = auto()              # Only show group/cage visuals (no numbers)
    GROUPS_AND_NUMBERS = auto()  # Show group/cages + numbers (for testing)


class GridWindow(QMainWindow):
    """
    This window owns a QTableWidget that represents an NxN grid.

    The key design idea:
    - We keep the underlying data (grids and grouping info) stored in this class.
    - We have a single `render()` method that decides what to show based on the mode.
    """

    def __init__(
        self,
        n: int = 6,
        game_grid: list[list[int]] | None = None,
        solution_grid: list[list[int]] | None = None,
        groups: object | None = None,
        mode: ViewMode = ViewMode.GROUPS_AND_NUMBERS,
    ):
        super().__init__()

        # Save size and any inputs so we can render later.
        self.n = n

        # Store "data sources" as instance variables.
        # These are not necessarily displayed immediately; render() decides.
        self._game_grid = game_grid
        self._solution_grid = solution_grid
        self._groups = groups

        # Store current view mode (what layer(s) to display).
        self._mode = mode

        self.setWindowTitle(f"Math Box Prototype ({n}x{n})")

        # Create the table widget itself.
        # QTableWidget(rows, cols, parent)
        table = QTableWidget(n, n, self)

        # Hide headers for a clean "grid" look.
        table.horizontalHeader().setVisible(False)
        table.verticalHeader().setVisible(False)

        # Turn off scrollbars so the UI looks like a fixed puzzle board.
        table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)

        # Make all cells the same size.
        cell = 60
        for r in range(n):
            table.setRowHeight(r, cell)
        for c in range(n):
            table.setColumnWidth(c, cell)

        # Pre-create QTableWidgetItem objects for every cell.
        #
        # Why do this?
        # - If you create items later, you have to check for None.
        # - Pre-creating lets you just do `self.table.item(r, c).setText(...)`
        #   without worrying if the cell item exists.
        for r in range(n):
            for c in range(n):
                item = QTableWidgetItem("")  # start blank
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                table.setItem(r, c, item)

        # Style the table (colors, gridlines, text).
        # Note: right now every cell gets the same border.
        # Later, when we draw group/cage borders, we’ll likely override borders per cell.
        table.setStyleSheet("""
            QTableWidget {
                background: #0b1020;
                gridline-color: #2cffdf;
                color: #e6f1ff;
                font-size: 22px;
                selection-background-color: #7b2cff;
            }
            QTableWidget::item {
                border: 1px solid #2cffdf;
            }
        """)

        # Force the table widget itself to be exactly the size of the NxN grid.
        #
        # Why do this?
        # - Prevent resizing / scrollbars
        # - Makes the window size match the puzzle grid exactly
        w = sum(table.columnWidth(c) for c in range(n)) + 2 * table.frameWidth()
        h = sum(table.rowHeight(r) for r in range(n)) + 2 * table.frameWidth()
        table.setFixedSize(w, h)

        # Put table as the central widget (main content) of this QMainWindow.
        self.setCentralWidget(table)

        # Save reference so other methods can access it.
        self.table = table

        # Resize the window to fit the table nicely.
        self.adjustSize()

        # Finally, draw whatever the current mode says we should draw.
        self.render()

    # -----------------------
    # Public API (methods your main.py can call)
    # -----------------------

    def set_mode(self, mode: ViewMode) -> None:
        """
        Change what we display (GAME vs GROUPS vs GROUPS_AND_NUMBERS)
        and re-render immediately.
        """
        self._mode = mode
        self.render()

    def set_grids(
        self,
        *,
        game_grid: list[list[int]] | None = None,
        solution_grid: list[list[int]] | None = None,
        groups: object | None = None,
    ) -> None:
        """
        Update our stored data inputs and re-render.

        The `*` forces keyword-only arguments, which makes calls clearer:
            set_grids(game_grid=..., solution_grid=..., groups=...)

        That helps prevent mixing up grids accidentally.
        """
        if game_grid is not None:
            self._game_grid = game_grid
        if solution_grid is not None:
            self._solution_grid = solution_grid
        if groups is not None:
            self._groups = groups

        self.render()

    # -----------------------
    # Rendering pipeline
    # -----------------------

    def render(self) -> None:
        """
        This is the "single source of truth" for drawing the UI.

        It clears the table, then draws layers depending on the mode.

        Design pattern:
        - store state in instance variables (_mode, _game_grid, _solution_grid, _groups)
        - render uses that state to draw
        """
        # Always start from a clean slate so we don't "mix" old text with new text.
        self._clear_text()

        if self._mode == ViewMode.GAME:
            # In GAME mode, only show the player's grid.
            # (Usually this would be blank or partially filled.)
            if self._game_grid is not None:
                self._set_numbers(self._game_grid)

        elif self._mode == ViewMode.GROUPS:
            # In GROUPS mode, show only the group/cage boundaries.
            # No numbers.
            self._apply_group_styles(self._groups)

        elif self._mode == ViewMode.GROUPS_AND_NUMBERS:
            # In GROUPS_AND_NUMBERS, show groups and overlay the solution numbers.
            self._apply_group_styles(self._groups)

            if self._solution_grid is not None:
                self._set_numbers(self._solution_grid)

    # -----------------------
    # Small helper methods (single responsibility)
    # -----------------------

    def _clear_text(self) -> None:
        """
        Clear text in every cell.
        (Does not change styling—only the displayed text.)
        """
        for r in range(self.n):
            for c in range(self.n):
                self.table.item(r, c).setText("")

    def _set_numbers(self, grid: list[list[int]]) -> None:
        """
        Display numbers from a 2D list into the table.

        This assumes:
        - grid is n x n
        - values are ints (or 0/None for blank)
        """
        self._validate_grid(grid)

        for r in range(self.n):
            for c in range(self.n):
                v = grid[r][c]

                # Convert values to display text.
                # If you use 0/None as "empty", we display blank.
                text = "" if v in (0, None) else str(v)

                self.table.item(r, c).setText(text)

    def _apply_group_styles(self, groups: object | None) -> None:
        """
        Apply grouping/cage visuals (borders, background colors, etc).

        This is a stub *on purpose* until we know the exact structure of `groups`.

        Once the output shape of your generator grouping, is known
        we can implement:
        - which borders to draw thick/thin (cage outlines)
        - optional top-left “cage clue” label (like KenKen)
        - background colors per group (for debugging)
        """
        if groups is None:
            return

        # TODO: implement once group format is known.
        # Example future logic could be:
        # - determine for each cell which neighbors are in same group
        # - if neighbor is not in same group, draw a thick border on that side
        return

    def _validate_grid(self, grid: list[list[int]]) -> None:
        """
        Basic safety check: ensure grid is exactly n x n.

        Why do this?
        - prevents index errors
        - catches generator bugs early
        - helps debugging
        """
        if len(grid) != self.n or any(len(row) != self.n for row in grid):
            raise ValueError("Grid shape does not match n x n.")
