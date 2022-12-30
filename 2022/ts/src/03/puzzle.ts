import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-03")
export class Day03 extends Puzzle
{
    protected day = "3";

    solve()
    {
        const item2score = (char: string) => {
            const c = char.charCodeAt(0);
            return c >= 97 ? c - 97 + 1 : c - 65 + 27;
        }

        const rucksacks = input.split("\n");

        //// PART 1

        const compartments: [string[], Set<string>][] = rucksacks.map(r =>
            [ Array.from(r.slice(0, r.length / 2)), new Set(r.slice(r.length / 2)) ]
        );

        const score1 = compartments.reduce((score, rucksack) => (
            score + rucksack[0].reduce((score, item) => rucksack[1].has(item) ? item2score(item) : score, 0)
        ), 0);

        this.resultPart1 = `${score1}`;

        //// PART 2
        
        let score2 = 0;
        for (let i = 0; i < rucksacks.length; i += 3) {
            const r0 = Array.from(rucksacks[i]);
            const r1 = new Set(rucksacks[i+1]);
            const r2 = new Set(rucksacks[i+2]);

            let item = "";
            for (let j = 0; j < r0.length; ++j) {
                item = r0[j];
                if (r1.has(item) && r2.has(item)) {
                    break;
                }
            }

            score2 += item2score(item);
        }


        this.resultPart2 = `${score2}`;

        return true;
    }
}