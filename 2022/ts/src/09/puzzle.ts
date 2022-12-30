import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-09")
export class Day09 extends Puzzle
{
    protected day = "9";

    solve()
    {
        const steps: [string, number][] = input.split("\n")
            .map(line => line.split(" "))
            .map(step => [ step[0], parseInt(step[1]) ]);

        const moveHead = function(dir: string, h: number[]) {
            if (dir === "L") {
                h[0] -= 1;
            }
            else if (dir === "R") {
                h[0] += 1;
            }
            else if (dir === "U") {
                h[1] -= 1;
            }
            else {
                h[1] += 1;
            }
        }

        const moveTail = function(h: number[], t: number[]) {
            const dx = h[0] - t[0];
            const ax = Math.abs(dx);
            const sx = Math.sign(dx);

            const dy = h[1] - t[1];
            const ay = Math.abs(dy);
            const sy = Math.sign(dy);

            if (ax > 1 || ay > 1) {
                t[0] += sx;
                t[1] += sy;
            }
        };

        //// PART 1

        const pos1 = new Set<string>();
        const rope1 = new Array(2).fill(0).map(_ => [0, 0]);
        for (const step of steps) {
            const [ dir, count ] = step;
            for (let i = 0; i < count; ++i) {
                moveHead(dir, rope1[0]);
                moveTail(rope1[0], rope1[1]);
                const key = `${rope1[1][0]+50000}${rope1[1][1]+50000}`;
                pos1.add(key);
            }
        }

        const score1 = Array.from(pos1).length;
        this.resultPart1 = `${score1}`;

        //// PART 2

        const pos2 = new Set<string>();
        const rope2 = new Array(10).fill(0).map(_ => [0, 0]);
        for (const step of steps) {
            const [ dir, count ] = step;
            for (let i = 0; i < count; ++i) {
                moveHead(dir, rope2[0])
                for (let j = 1; j < 10; ++j) {
                    moveTail(rope2[j-1], rope2[j]);
                }
                const key = `${rope2[9][0]+50000}${rope2[9][1]+50000}`;
                pos2.add(key);
            }
        }

        const score2 = Array.from(pos2).length;
        this.resultPart2 = `${score2}`;

        return true;
    }
}