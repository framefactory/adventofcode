import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-02")
export class Day02 extends Puzzle
{
    protected day = "2";

    solve()
    {
        const rounds = input.split("\n");

        //// PART 1

        const scores1: Record<string, number> = {
            "A X": 1 + 3,
            "A Y": 2 + 6,
            "A Z": 3 + 0,
            "B X": 1 + 0,
            "B Y": 2 + 3,
            "B Z": 3 + 6,
            "C X": 1 + 6,
            "C Y": 2 + 0,
            "C Z": 3 + 3,
        };

        const score1 = rounds.reduce((score, round) => score + scores1[round], 0);
        this.resultPart1 = `${score1}`;

        //// PART 2

        const scores2: Record<string, number> = {
            "A X": 3 + 0,
            "A Y": 1 + 3,
            "A Z": 2 + 6,
            "B X": 1 + 0,
            "B Y": 2 + 3,
            "B Z": 3 + 6,
            "C X": 2 + 0,
            "C Y": 3 + 3,
            "C Z": 1 + 6,
        };

        const score2 = rounds.reduce((score, round) => score + scores2[round], 0);
        this.resultPart2 = `${score2}`;

        return true;
    }
}