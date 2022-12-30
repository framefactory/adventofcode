// Advent of Code
// 2022, Day 02

use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];
    println!("Input file: {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("unable to read input file");

    let games = contents.lines();
    let mut total_score = 0;

    for game in games {
        let score = match game {
            "A X" => 1 + 3,
            "A Y" => 2 + 6,
            "A Z" => 3 + 0,
            "B X" => 1 + 0,
            "B Y" => 2 + 3,
            "B Z" => 3 + 6,
            "C X" => 1 + 6,
            "C Y" => 2 + 0,
            "C Z" => 3 + 3,
            &_ => 0,
        };
        total_score += score;
    }

    println!("Part 1: total score: {}", total_score);

    let games = contents.lines();
    let mut total_score = 0;

    for game in games {
        let score = match game {
            "A X" => 3 + 0,
            "A Y" => 1 + 3,
            "A Z" => 2 + 6,
            "B X" => 1 + 0,
            "B Y" => 2 + 3,
            "B Z" => 3 + 6,
            "C X" => 2 + 0,
            "C Y" => 3 + 3,
            "C Z" => 1 + 6,
            &_ => 0,
        };
        total_score += score;
    }

    println!("Part 2: total score: {}", total_score);
}