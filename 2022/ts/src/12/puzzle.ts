import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-12")
export class Day12 extends Puzzle
{
    protected day = "12";

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