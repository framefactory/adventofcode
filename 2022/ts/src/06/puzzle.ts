import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-06")
export class Day06 extends Puzzle
{
    protected day = "6";

    solve()
    {
        //// PART 1
        let i = 4;
        while (i <= input.length) {
            const s = new Set(input.slice(i - 4, i));
            if (Array.from(s).length === 4) {
                break;
            }
            ++i;
        }
        this.resultPart1 = `${i}`;

        //// PART 2
        i = 14;
        while (i <= input.length) {
            const s = new Set(input.slice(i - 14, i));
            if (Array.from(s).length === 14) {
                break;
            }
            ++i;
        }
        this.resultPart2 = `${i}`;

        return true;
    }
}