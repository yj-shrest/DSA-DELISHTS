const fs = require("fs")
const myStr = `
Recipe: Piro Chatpate
Descirption: Add a short description

Difficulty: Easy
Time: 0 h 15 m
Ingredients:
chauchau 2pkts
bhuja 200gm
Steps:
mix garne`

const recipe = myStr.split("Recipe: ")[1].split("\n")[0];
const description = myStr.split("Descirption: ")[1].split("\n")[0]
const difficulty = myStr.split("Difficulty:")[1].split("\n")[0]
const time = myStr.split("Time:")[1].split("\n")[0]
const ingredients = myStr.split("Ingredients:\n")[1].split("Steps")[0].split("\n")
const steps = myStr.split("Steps:\n")[1].split("\n")

const jsonData={
    recipe, description, difficulty, time, ingredients, steps
}

fs.writeFile(`recipes/${recipe.split(" ").join("_").toLowerCase()}.json`, JSON.stringify(jsonData), (err) => {
  if (err) {
    console.error("Error writing file:", err);
    return;
  }
  console.log("JSON data written to file successfully.");
});