import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-01")
export class Day01 extends Puzzle
{
    protected day = "1";

    solve()
    {
        //// PART 1
     
        const blocks = input.split("\n\n");
        const sums = blocks.map(block => (
            block.split("\n").reduce((sum, entry) => sum + parseInt(entry), 0)
        ));

        const maxSum = sums.reduce((max, entry) => Math.max(max, entry));

        this.resultPart1 = `${maxSum}`;

        //// PART 2

        sums.sort((a, b) => b - a);
        const topSum = sums.splice(0, 3).reduce((sum, entry) => sum + entry);

        this.resultPart2 = `${topSum}`;

        return true;
    }
}