# Problem Statement

Write a Sudoku solver that treats the puzzle as a constraint satisfaction problem. A Sudoku is a 9x9 grid, grouped into a 3x3 grid of 3x3 blocks, where each square in the grid is to be filled with a digit from 1 to 9 such that each row, column, and block must contain each digit exactly once. The grid is partially filled so that it is guaranteed that there is a unique solution. You can find more details e.g. at http://en.wikipedia.org/wiki/Sudoku.

<b>Step 1:</b> Formulate Sudoku as a binary CSP.  Describe variables, domains and constraints.<br/>
<b>Step 2:</b> Try to solve a few Sudokus that are posted on http://dailysudoku.co.uk using standard depth first search / backtracking / constraint propagation / arc-consistency / forward checking with minimum remaining value search that we have studied in class. Describe your experience.
