import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string


@customElement("aoc-day-13")
export class Day13 extends Puzzle
{
    protected day = "13";

    solve()
    {
        const parseList = function(args: { s: string, i: number }): any[] {
            let { s, i } = args;
            const r = [];
            for (++i; i < s.length; ++i) {
                if (s[i] === "[") {
                    const params = { s, i };
                    r.push(parseList(params));
                    i = params.i;
                }
                else if (s[i] === "]") {
                    args.i = i;
                    return r;
                }
                else if (s[i] !== ",") {
                    let j = i;
                    while(s[j] >= "0" && s[j] <= "9") {
                        j++;
                    }
                    const v = parseInt(s.slice(i, j));
                    r.push(v);
                    i = j-1;
                }
            }

            return r;
        };

        const pairs = input.split("\n\n")
            .map(pair => pair.split("\n").map(line => parseList({ s: line, i: 0 })));

        //console.log(pairs);

        //// PART 1

        const compare = function(a: any, b: any): number {
            if (Array.isArray(a)) {
                if (!Array.isArray(b)) {
                    return compare(a, [b]);
                }
                // compare 2 arrays
                const n = Math.min(a.length, b.length);
                for (let i = 0; i < n; ++i) {
                    const r = compare(a[i], b[i]);
                    if (r !== 0) {
                        return r;
                    }
                }
                return a.length < b.length ? 1 : (a.length > b.length ? -1 : 0);
            }
            else {
                if (Array.isArray(b)) {
                    return compare([a], b);
                }
                // compare 2 ints
                return a < b ? 1 : (a > b ? -1 : 0);
            }
        }

        let score1 = 0;
        for (let i = 0; i < pairs.length; ++i) {
            if (compare(pairs[i][0], pairs[i][1]) === 1) {
                score1 += (i + 1);
            }    
        }

        this.resultPart1 = `${score1}`;

        //// PART 2
        const packets = [];
        pairs.forEach(pair => { packets.push(...pair) });
        const p0 = [[2]];
        const p1 = [[6]];
        packets.push(p0, p1);
        const n = packets.length;

        for (let i = 0; i < n; ++i) {
            for (let j = i + 1; j < n; ++j) {
                if (compare(packets[i], packets[j]) < 0) {
                    const t: any = packets[i];
                    packets[i] = packets[j];
                    packets[j] = t;
                }
            }
        }

        let score2 = 1;
        for (let i = 0; i < n; ++i) {
            if (packets[i] === p0 || packets[i] === p1) {
                score2 *= (i + 1);
            }
        }
                
        this.resultPart2 = `${score2}`;

        return true;
    }
}
