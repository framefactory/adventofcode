import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./test.txt?raw";

const input = rawInput.trim() as string

const reValve = /Valve (\S+) has flow rate=(\d+); tunnels? leads? to valves? (.+)$/

interface IValve {
    name: string;
    flow: number;
    adj: string[];
    visited: number;
    parent: IValve;
    totalFlow: number;
    totalTime: number;
};

@customElement("aoc-day-16")
export class Day16 extends Puzzle
{
    protected day = "16";

    solve()
    {
        const valves = input.split("\n").map(line => line.match(reValve)!.slice(1))
            .map(v => ({
                name: v[0],
                flow: parseInt(v[1]),
                adj: v[2].split(", "),
                visited: 0,
                totalFlow: 0,
                totalTime: 0,
            } as IValve));
        
        const graph: Record<string, IValve> = {};
        valves.forEach(valve => graph[valve.name] = valve);

        console.log(valves);

        //// PART 1
        


        //// PART 2

        const score = "N/A";
        this.resultPart1 = `${score}`;
        this.resultPart2 = `${score}`;

        return false;
    }
}