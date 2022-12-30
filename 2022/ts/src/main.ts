import { LitElement, html, css } from "lit";
import { customElement } from "lit/decorators.js";

import { Puzzle } from "./puzzle.js";

import "./01/puzzle.js";
import "./02/puzzle.js";
import "./03/puzzle.js";
import "./04/puzzle.js";
import "./05/puzzle.js";
import "./06/puzzle.js";
import "./07/puzzle.js";
import "./08/puzzle.js";
import "./09/puzzle.js";
import "./10/puzzle.js";
import "./11/puzzle.js";
import "./12/puzzle.js";


@customElement("aoc-application")
export class Application extends LitElement
{
    static styles = css`
        button {
            display: block;
            margin: 0.5rem;
            padding: 0.5rem 2rem;
            background-color: #d1cec7;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #d8d5cd;
        }
    `;

    render()
    {
        return html`
            <button @click=${this.solveAll}>Solve All</button>
            <aoc-day-01></aoc-day-01>
            <aoc-day-02></aoc-day-02>
            <aoc-day-03></aoc-day-03>
            <aoc-day-04></aoc-day-04>
            <aoc-day-05></aoc-day-05>
            <aoc-day-06></aoc-day-06>
            <aoc-day-07></aoc-day-07>
            <aoc-day-08></aoc-day-08>
            <aoc-day-09></aoc-day-09>
            <aoc-day-10></aoc-day-10>
            <aoc-day-11></aoc-day-11>
            <aoc-day-12></aoc-day-12>
        `;
    }

    solveAll()
    {
        const puzzles: any = this.shadowRoot?.querySelectorAll(".puzzle");
        puzzles?.forEach((puzzle: Puzzle) => puzzle.onSolve());
    }
}