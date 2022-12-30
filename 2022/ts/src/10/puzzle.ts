import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-10")
export class Day10 extends Puzzle
{
    protected day = "10";

    solve()
    {
        const program = input.split("\n").map(line => line.split(" "));

        //// PART 1, 2

        let cycle = 1;
        let checkpoint = 20;
        let x = 1;
        let ip = 0;
        let delay = 0;
        let cmd = "", op = "";
        let opVal = 0;
        let score1 = 0;

        const crt = Array(6).fill(0).map(_ => Array(40).fill("."));

        while(cycle < 240) {
            if (--delay <= 0) {
                if (cmd === "addx") {
                    x += opVal;
                }
                [ cmd, op ] = program[ip++];
                if (cmd === "addx") {
                    opVal = parseInt(op);
                    delay = 2;
                }
            }

            const c = cycle - 1;
            const cx = c % 40;
            const cy = Math.floor(c / 40) % 6;
            const dx = Math.abs(cx - x);
            if (dx <= 1) {
                crt[cy][cx] = "#";
            }

            if (cycle === checkpoint) {
                score1 += cycle * x;
                checkpoint += 40;
            }

            cycle++;
        }

        this.resultPart1 = `${score1}`;

        //// PART 2

        crt.forEach(line => {
            console.log(line.join(""));
        })

        this.resultPart2 = `BUCACBUZ`;

        return true;
    }
}