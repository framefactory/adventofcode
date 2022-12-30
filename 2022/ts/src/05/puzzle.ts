import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-05")
export class Day05 extends Puzzle
{
    protected day = "5";

    solve()
    {
        const [ s, m ] = input.split("\n\n");

        // parse stacks
        const lines = s.split("\n");
        const maxSize = lines.length - 1;
        const numStacks = Math.ceil(lines[maxSize].length / 4);
        const stacks: string[][] = [];
        for (let i = 0; i < numStacks; ++i) {
            stacks[i] = [];
            for (let j = maxSize - 1; j >= 0; --j) {
                const item = lines[j][1 + 4*i];
                if (item && item !== ' ') {
                    stacks[i].push(item);
                }
            }
        }

        // parse move instructions
        const reMove = /move (\d+) from (\d+) to (\d+)/;
        const moves: any = m.trim().split("\n").map(move => move.match(reMove)?.splice(1).map(n => parseInt(n)));

        //// PART 1
        const stacks1: string[][] = stacks.map(stack => Array.from(stack));

        for (let i = 0; i < moves.length; ++i) {
            const [ count, src, dst ] = moves[i];
            for (let n = 0; n < count; ++n) {
                stacks1[dst - 1].push(stacks1[src - 1].pop() as string);
            }
        }        

        const score1 = stacks1.reduce((score, stack) => score + stack.pop(), "");
        this.resultPart1 = `${score1}`;

        //// PART 2
        for (let i = 0; i < moves.length; ++i) {
            const [ count, src, dst ] = moves[i];
            stacks[dst-1] = stacks[dst-1].concat(stacks[src-1].splice(-count));
        }

        const score2 = stacks.reduce((score, stack) => score + stack.pop(), "");
        this.resultPart2 = `${score2}`;

        return true;
    }
}