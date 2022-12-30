import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-08")
export class Day08 extends Puzzle
{
    protected day = "8";

    solve()
    {
        const grid = input.split("\n").map(line => Array.from(line).map(n => parseInt(n)));
        const rows = grid.length;
        const cols = grid[0].length;

        const makeGrid = (rows: number, cols: number) => (
            new Array(rows).fill(undefined).map(_ => new Array(cols).fill(-1))
        );

        const dumpGrid = (grid: number[][]) => {
            grid.forEach(row => console.log(row.map(c => c.toString()).join()));
            console.log("");
        }

        const left = makeGrid(rows, cols);
        const right = makeGrid(rows, cols);
        const top = makeGrid(rows, cols);
        const bottom = makeGrid(rows, cols);

        //// PART 1

        for (let r = 0; r < rows; ++r) {
            for (let c = 1; c < cols; ++c) {
                left[r][c] = Math.max(grid[r][c-1], left[r][c-1]);
            }
        }

        for (let r = 0; r < rows; ++r) {
            for (let c = cols-2; c >= 0; --c) {
                right[r][c] = Math.max(grid[r][c+1], right[r][c+1]);
            }
        }

        for (let c = 0; c < cols; ++c) {
            for (let r = 1; r < rows; ++r) {
                top[r][c] = Math.max(grid[r-1][c], top[r-1][c]);
            }
        }

        for (let c = 0; c < cols; ++c) {
            for (let r = rows-2; r >= 0; --r) {
                bottom[r][c] = Math.max(grid[r+1][c], bottom[r+1][c]);
            }
        }

        let count = 0;
        for (let r = 0; r < rows; ++r) {
            for (let c = 0; c < cols; ++c) {
                const h = grid[r][c];
                count += (h > left[r][c] || h > right[r][c] || h > top[r][c] || h > bottom[r][c]) ? 1 : 0;
            }
        }

        this.resultPart1 = `${count}`;

        //// PART 2

        let maxScore = 0;
        for (let r = 0; r < rows; ++r) {
            for (let c = 0; c < cols; ++c) {
                const h = grid[r][c];
                let sl = 0, sr = 0, st = 0, sb = 0;
                for (let rr = r - 1; rr >= 0; --rr) {
                    sl++;
                    if (grid[rr][c] >= h) break;
                }
                for (let rr = r + 1; rr < rows; ++rr) {
                    sr++;
                    if (grid[rr][c] >= h) break;
                }
                for (let cc = c - 1; cc >= 0; --cc) {
                    st++;
                    if (grid[r][cc] >= h) break;
                }
                for (let cc = c+ 1; cc < cols; ++cc) {
                    sb++;
                    if (grid[r][cc] >= h) break;
                }
                const score = sl * sr * st * sb;
                maxScore = Math.max(score, maxScore);
            }
        }

        this.resultPart2 = `${maxScore}`;

        return true;
    }
}