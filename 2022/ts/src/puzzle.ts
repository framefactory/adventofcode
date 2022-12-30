import { LitElement, html, css } from "lit";
import { customElement, property } from "lit/decorators.js";

export { customElement, html };

export class Puzzle extends LitElement
{
    static styles = css`
        :host {
            display: inline-flex;
            flex-direction: column;
            min-width: 150px;
            margin: 0.5em;
            padding: 1em;
            background-color: #eeedea;
            border-radius: 4px;
        }
        :host(.solved) {
            background-color: #e3f2cf;
        }
        :host(.unsolved) {
            background-color: #f2dad2;
        }
        h1 {
            font-size: 1.5rem;
            margin: 0;
        }
        button {
            margin: 0.5rem 0;
            padding: 0.5rem;
            background-color: #d1cec7;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #d8d5cd;
        }
        div {
            font-family: monospace;
        }
    `;

    @property()
    resultPart1 = "(unsolved)";
    
    @property()
    resultPart2 = "(unsolved)";

    protected day = "0";

    constructor()
    {
        super();
        this.classList.add("puzzle");
    }

    render()
    {
        return html`
            <h1>Day ${this.day}</h1>
            <button @click=${this.onSolve}>Solve</button>
            <div>Part 1: ${this.resultPart1}</div>
            <div>Part 2: ${this.resultPart2}</div>
        `;
    }

    onSolve()
    {
        this.classList.add(this.solve() ? "solved" : "unsolved");
    }

    solve(): boolean
    {
        console.error("must override");
        return false;
    }
}