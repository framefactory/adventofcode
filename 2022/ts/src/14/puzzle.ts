import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-14")
export class Day14 extends Puzzle
{
    protected day = "14";

    solve()
    {
        // parse rock paths
        const rocks = input.split("\n").map(path => path.split(" -> ")
            .map(seg => seg.split(",").map(n => parseInt(n))));
        
        let xa = Number.MAX_VALUE;
        let ya = 0;
        let xb = 0;
        let yb = 0;

        rocks.forEach(path => path.forEach(seg => {
            xa = Math.min(xa, seg[0] - 1);
            ya = Math.min(ya, seg[1]);
            xb = Math.max(xb, seg[0] + 1);
            yb = Math.max(yb, seg[1]);
        }));

        xa -= (yb - ya);
        xb += (yb - ya);
        yb += 1;

        const xs = xb - xa + 1;
        const ys = yb - ya + 1;
        
        const cave = Array(ys).fill(0).map(_ => Array(xs).fill("."));
        rocks.forEach(path => {
            let x0 = path[0][0];
            let y0 = path[0][1];
            for (let i = 1; i < path.length; ++i) {
                const x1 = path[i][0];
                const y1 = path[i][1];
                const dx = Math.sign(x1 - x0);
                const dy = Math.sign(y1 - y0);
                if (dx === 0) {
                    for (let y = y0; y !== y1 + dy; y += dy) {
                        cave[y-ya][x0-xa] = "#";
                    }
                }
                else if (dy === 0) {
                    for (let x = x0; x !== x1 + dx; x += dx) {
                        cave[y0-ya][x-xa] = "#"
                    }
                }
                x0 = x1;
                y0 = y1;
            }
        });

        const printCave = function() {
            cave.forEach((line, index) => {
                console.log(line.join(""), index);
            })
        }

        console.log(xa, ya, xb, yb);

        //// PART 1

        let score1 = 0;

        while(true) {
            let x = 500;
            let y = 0;
            while(y < yb) {
                if (cave[y-ya + 1][x-xa] === ".") {
                    y += 1;
                }
                else if (cave[y-ya + 1][x-xa - 1] === ".") {
                    y += 1;
                    x -= 1;
                }
                else if (cave[y-ya + 1][x-xa + 1] === ".") {
                    y += 1;
                    x += 1;
                }
                else {
                    cave[y-ya][x-xa] = "o";
                    break;
                }
            }
            if (y >= yb) {
                break;
            }
            score1++;
        }

        this.resultPart1 = `${score1}`;

        //// PART 2

        cave.forEach(line => {
            for (let x = 0; x < line.length; ++x) {
                if (line[x] === "o") {
                    line[x] = ".";
                }
            }
        });

        let score2 = 0;

        while(true) {
            let x = 500;
            let y = 0;
            if (cave[y-ya][x-xa] !== ".") {
                break;
            }

            while(true) {
                if (y === yb) {
                    cave[y-ya][x-xa] = "o";
                    break;
                }
                if (cave[y-ya + 1][x-xa] === ".") {
                    y += 1;
                }
                else if (cave[y-ya + 1][x-xa - 1] === ".") {
                    y += 1;
                    x -= 1;
                }
                else if (cave[y-ya + 1][x-xa + 1] === ".") {
                    y += 1;
                    x += 1;
                }
                else {
                    cave[y-ya][x-xa] = "o";
                    break;
                }
            }

            score2++;
        }

        //printCave();
        this.resultPart2 = `${score2}`;

        return true;
    }
}