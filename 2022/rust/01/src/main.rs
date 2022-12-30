// Advent of Code
// 2022, Day 01

use std::env;
use std::fs;

fn main() {
    let args: Vec<String> = env::args().collect();
    let file_path = &args[1];
    println!("Input file: {}", file_path);

    let contents = fs::read_to_string(file_path)
        .expect("unable to read input file");

    let elves = contents.split("\n\n");
    //println!("number of elves: {}", &elves.collect::<Vec<&str>>().len());

    let mut calories_list = Vec::<i32>::new();
    for elve in elves {
        let mut elve_calories = 0;
        for line in elve.lines() {
            let text = line.to_string();
            let calories = text.parse::<i32>().unwrap_or_default();
            elve_calories += calories;
        }
        calories_list.push(elve_calories);
    }

    calories_list.sort();
    calories_list.reverse();
    let mut calories_total = 0;
    for i in 0..3 {
        println!("#{} calories: {}", i, calories_list[i]);
        calories_total += calories_list[i];
    }
    println!("total calories: {}", calories_total);
}
