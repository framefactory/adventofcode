import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-20")
export class Day20 extends Puzzle
{
    protected day = "20";

    solve()
    {
        //// PART 1
        //// PART 2

        const score = "N/A";
        this.resultPart1 = `${score}`;
        this.resultPart2 = `${score}`;

        return false;
    }
}