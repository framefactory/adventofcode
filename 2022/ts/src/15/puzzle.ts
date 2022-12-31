import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-15")
export class Day15 extends Puzzle
{
    protected day = "15";

    solve()
    {
        //// PART 1
        //// PART 2

        const score = 0;
        
        this.resultPart1 = `${score}`;
        this.resultPart2 = `${score}`;

        return false;
    }
}