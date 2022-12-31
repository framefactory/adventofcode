import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string

const INF = Number.MAX_VALUE

interface ILoc {
    height: number;
    visited: number;
    dist: number;
    parent: ILoc | null;
}

@customElement("aoc-day-12")
export class Day12 extends Puzzle
{
    protected day = "12";

    solve()
    {
        const lines = input.split("\n");
        const rows = lines.length;
        const cols = lines[0].length;
        let start = [0, 0];
        let end = [0, 0];

        const map: ILoc[][] = [];
        for (let r = 0; r < rows; ++r) {
            const line = lines[r];
            const mapRow = [];
            for (let c = 0; c < cols; ++c) {
                const pt = line[c];
                let height = pt.codePointAt(0)! - 97;
                let visited = 0;
                let dist = Number.MAX_VALUE;
                if (pt === "S") {
                    height = 0;
                    start[0] = r;
                    start[1] = c;
                }
                else if (pt === "E") {
                    height = 25;
                    visited = 1;
                    dist = 0;
                    end[0] = r;
                    end[1] = c;
                }
                const loc: ILoc = { height, visited, dist, parent: null };
                mapRow.push(loc);
            }
            map.push(mapRow);
        }

        //// PART 1
        const getLoc: (row: number, col: number, h?: number) => ILoc | null = (row, col, h) => {
            if (row < 0 || row >= rows || col < 0 || col >= cols) {
                return null;
            }
            const loc = map[row][col];
            if (h !== undefined && loc.height < h - 1) {
                return null;
            }
            return loc;
        }

        const queue = [ end ];
        while (queue.length > 0) {
            const [r, c] = queue.pop()!;
            const loc = getLoc(r, c)!;
            const adjLocs: any = [
                [ getLoc(r, c-1, loc.height), [ r, c-1 ]],
                [ getLoc(r, c+1, loc.height), [ r, c+1 ]],
                [ getLoc(r-1, c, loc.height), [ r-1, c ]],
                [ getLoc(r+1, c, loc.height), [ r+1, c ]],
            ];
            for (const adjLoc of adjLocs) {
                if (adjLoc[0] && adjLoc[0].visited === 0) {
                    adjLoc[0].visited = 1;
                    adjLoc[0].dist = loc.dist + 1;
                    adjLoc[0].parent = loc;
                    queue.unshift(adjLoc[1]);
                }
            }
            loc.visited = 2;
        }

        const startLoc = getLoc(start[0], start[1]);
        const score1 = startLoc!.dist;
        this.resultPart1 = `${score1}`;

        //// PART 2
        let score2 = score1;
        for (let r = 0; r < rows; ++r) {
            for (let c = 0; c < cols; ++c) {
                const loc = map[r][c];
                if (loc.height === 0 && loc.dist < score2) {
                    score2 = loc.dist;
                }
            }
        }

        this.resultPart2 = `${score2}`;

        return true;
    }
}