import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string

interface IMonkey {
    score: number;
    items: number[];
    operation: (old: number) => number;
    divisor: number;
    monkeyFalse: number;
    monkeyTrue: number;
}


@customElement("aoc-day-11")
export class Day11 extends Puzzle
{
    protected day = "11";


    solve()
    {
        const blocks = input.split("\n\n");
        const itemsCopy: number[][] = [];
        const monkeys = blocks.map(block => {
            const lines = block.split("\n").map(line => line.split(" "));
            const items = lines[1].slice(4).map(item => parseInt(item));
            const op0 = lines[2][6];
            const op1 = lines[2][7];
            let operation;
            if (op1 === "old") {
                operation = (old: number) => old * old;
            }
            else if (op0 === "+") {
                const operand = parseInt(op1);
                operation = (old: number) => old + operand;
            }
            else if (op0 === "*") {
                const operand = parseInt(op1);
                operation = (old: number) => old * operand;
            }
            else {
                throw("unknown operation");
            }

            const divisor = parseInt(lines[3][5]);
            const monkeyTrue = parseInt(lines[4][9]);
            const monkeyFalse = parseInt(lines[5][9]);

            itemsCopy.push(Array.from(items));

            return {
                score: 0,
                items,
                operation,
                divisor,
                monkeyFalse,
                monkeyTrue
            } as IMonkey;
        });

        const gcd = monkeys.reduce((d, monkey) => d * monkey.divisor, 1);

        
        //// PART 1

        const handleMonkeyItems1 = (monkey: IMonkey) => {
            for (const item of monkey.items) {
                monkey.score++;
                let level = monkey.operation(item);
                level = Math.floor(level / 3);

                if (level % monkey.divisor === 0) {
                    monkeys[monkey.monkeyTrue].items.push(level);
                }
                else {
                    monkeys[monkey.monkeyFalse].items.push(level);
                }
            }
            monkey.items = [];
        };

        for (let r = 0; r < 20; ++r) {
            for (const monkey of monkeys) {
                handleMonkeyItems1(monkey);
            }
        }
        let score1A = 0;
        let score1B = 0;
        for (const monkey of monkeys) {
            if (monkey.score > score1A) {
                score1B = score1A;
                score1A = monkey.score;
            }
        }

        this.resultPart1 = `${score1A * score1B}`;

        //// PART 2

        const handleMonkeyItems2 = (monkey: IMonkey) => {
            for (const item of monkey.items) {
                monkey.score++;
                let level = monkey.operation(item);
                level = level % gcd;

                if (level % monkey.divisor === 0) {
                    monkeys[monkey.monkeyTrue].items.push(level);
                }
                else {
                    monkeys[monkey.monkeyFalse].items.push(level);
                }
            }
            monkey.items = [];
        };

        for (let i = 0; i < monkeys.length; ++i) {
            monkeys[i].score = 0;
            monkeys[i].items = Array.from(itemsCopy[i]);
        }

        for (let r = 1; r <= 10000; ++r) {
            for (const monkey of monkeys) {
                handleMonkeyItems2(monkey);
                // if (r === 1000) {
                //     console.log(monkey.score, monkey.items);
                // }
            }
        }
        let score2A = 0;
        let score2B = 0;
        for (const monkey of monkeys) {
            if (monkey.score > score2A) {
                score2B = score2A;
                score2A = monkey.score;
            }
            else if (monkey.score > score2B) {
                score2B = monkey.score;
            }
        }

        this.resultPart2 = `${score2A * score2B}`;

        return true;
    }
}