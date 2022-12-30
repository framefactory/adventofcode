import { Puzzle, customElement } from "../puzzle.js";
import rawInput from "./input.txt?raw";

const input = rawInput.trim() as string

interface IDir {
    name: string;
    size: number;
    dirs: Record<string, IDir>;
    files: Record<string, number>;
    parent: IDir | null;
}

@customElement("aoc-day-07")
export class Day07 extends Puzzle
{
    protected day = "7";

    solve()
    {
        // reconstruct file system
        const log = input.split("\n");
        const root: IDir = { name: "/", size: 0, dirs: {}, files: {}, parent: null };
        let cwd = root;

        for (const line of log) {
            const p = line.split(" ");
            if (p[0] === "$") {
                if (p[1] === "cd") {
                    if (p[2] === "/") {
                        cwd = root;
                    }
                    else if (p[2] === "..") {
                        cwd = cwd.parent!;
                    }
                    else {
                        let dir = cwd.dirs[p[2]];
                        if (dir === undefined) {
                            dir = { name: p[2], size: 0, dirs: {}, files: {}, parent: cwd };
                            cwd.dirs[dir.name] = dir;
                        }
                        cwd = dir;
                    }
                }
            }
            else if (p[0] === "dir") {
                if (cwd.dirs[p[1]] === undefined) {
                    const dir = { name: p[1], size: 0, dirs: {}, files: {}, parent: cwd };
                    cwd.dirs[dir.name] = dir;    
                }
            }
            else {
                const size = parseInt(p[0]);
                const name = p[1];
                if (cwd.files[name] === undefined) {
                    cwd.files[name] = size;
                    let dir: IDir | null = cwd;
                    while(dir) {
                        dir.size += size;    
                        dir = dir.parent;
                    }
                }
            }
        }

        const printDir = (dir: IDir, indent: number) => {
            const spaces = "  ".repeat(indent);
            console.log(spaces, `DIR ${dir.name} (${dir.size})`);
            Object.values(dir.dirs).forEach(dir => printDir(dir, indent + 1));
            Object.entries(dir.files).forEach(entry => console.log(spaces, `  FILE ${entry[0]} (${entry[1]})`));
        }

        //// PART 1

        const calcSize: (dir: IDir) => number = dir => {
            let count = dir.size <= 100000 ? dir.size : 0;
            return Object.values(dir.dirs).reduce((count, dir) => count + calcSize(dir), count);
        }

        const score1 = calcSize(root);
        this.resultPart1 = `${score1}`;


        //// PART 2

        const fsSize = 70000000;
        const fsAvail = fsSize - root.size;
        const fsRequired = 30000000;
        const minDirSize = fsRequired - fsAvail;
        let minDir = root;

        const findMinDir = (dir: IDir) => {
            if (dir.size >= minDirSize && dir.size < minDir.size) {
                minDir = dir;
            }
            Object.values(dir.dirs).forEach(dir => findMinDir(dir));
        }

        findMinDir(root);

        const score2 = minDir.size;
        this.resultPart2 = `${score2}`;

        return true;
    }
}