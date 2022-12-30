import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-04")
export class Day04 extends Puzzle
{
    protected day = "4";

    solve()
    {
        const pairs = input.split("\n").map(l => l.split(",").map(r => r.split("-").map(n => parseInt(n))));

        //// PART 1, containment
        const score1 = pairs.reduce((score, p) => (
            (p[0][0] >= p[1][0] && p[0][1] <= p[1][1]) || (p[1][0] >= p[0][0] && p[1][1] <= p[0][1]) ? score + 1 : score
        ), 0);

        this.resultPart1 = `${score1}`;


        //// PART 2, overlap
        const score2 = pairs.reduce((score, p) => (
            (p[0][0] <= p[1][1] && p[0][1] >= p[1][0]) || (p[1][0] <= p[0][1] && p[1][1] >= p[0][0]) ? score + 1 : score
        ), 0);
        
        this.resultPart2 = `${score2}`;

        return true;
    }
}