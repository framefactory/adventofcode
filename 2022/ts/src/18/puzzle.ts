import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-18")
export class Day18 extends Puzzle
{
    protected day = "18";

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