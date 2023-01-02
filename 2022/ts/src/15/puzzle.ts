import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string

const reLine = /Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)/;

@customElement("aoc-day-15")
export class Day15 extends Puzzle
{
    protected day = "15";

    solve()
    {
        const sensors: number[][] = input.split("\n")
            .map(line => line.match(reLine)!.slice(1, 5).map(n => parseInt(n)));
        
        const manh = function(x0: number, y0: number, x1: number, y1: number) {
            return Math.abs(x1 - x0) + Math.abs(y1 - y0);
        };

        const noBeaconHere = function(x: number, y: number) {
            for (let i = 0; i < sensors.length; ++i) {
                const s = sensors[i];
                // position of a beacon
                if (x === s[2] && y === s[3]) {
                    return false;
                }
                const ds = manh(s[0], s[1], s[2], s[3]);
                const dt = manh(s[0], s[1], x, y);
                if (dt <= ds) {
                    return true;
                }
            }
            return false;
        }

        let xa = Number.MAX_VALUE;
        let xb = -Number.MAX_VALUE;
        sensors.forEach(s => {
            const ds = manh(s[0], s[1], s[2], s[3]);
            xa = Math.min(xa, s[0] - ds);
            xb = Math.max(xb, s[0] + ds);
        });

        //// PART 1
        let score1 = 0;
        const y = 2000000;
        for (let x = xa; x <= xb; ++x) {
            score1 += noBeaconHere(x, y) ? 1 : 0;
        }

        this.resultPart1 = `${score1}`;

        //// PART 2

        const isInside = function(x: number, y: number, j: number) {
            if (x < 0 || x > 4000000 || y < 0 || y > 4000000) {
                return 0;
            }
            for (let i = 0, n = sensors.length; i < n; ++i) {
                if (i === j) continue;
                const s = sensors[i];
                const ds = manh(s[0], s[1], s[2], s[3]);
                const dt = manh(s[0], s[1], x, y);
                if (dt <= ds) return 0;
            }
            return x * 4000000 + y;
        }
        
        let score2 = 0;

        for (let i = 0, n = sensors.length; i < n; ++i) {
            const s = sensors[i];
            const sx = s[0];
            const sy = s[1];
            const ds = manh(sx, sy, s[2], s[3]) + 1;
            for (let d = 0; d <= ds; ++d) {
                const x = d;
                const y = ds - d;
                score2 = isInside(sx + x, sy + y, i);
                if (score2 > 0) break;
                score2 = isInside(sx - x, sy + y, i);
                if (score2 > 0) break;
                score2 = isInside(sx + x, sy - y, i);
                if (score2 > 0) break;
                score2 = isInside(sx - x, sy - y, i);
                if (score2 > 0) break;
            }
            if (score2 > 0) break;
        }

        this.resultPart2 = `${score2}`;

        return true;
    }
}