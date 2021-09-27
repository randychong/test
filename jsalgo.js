// #1
// Given a string with a date "09/10/2021", write a function that removes the "/" and returns the following date format:
// expected result: 20210910

// const string = "09/10/2021";

// function formatDate(string) {
//   let mmdd = [];
//   let year = [];
//   for (const x of string) {
//     if (x !== "/" && mmdd.length <= 3) {
//       mmdd.push(x);
//     } else if (x !== "/") {
//       year.push(x);
//     }
//   }

//   console.log(year.join("") + mmdd.join(""));
// }

// formatDate(string);

// #2
// Write a function that checks if a string is a palindrome. Function should return true or false. A palindrome is a word, phrase, or sequence that reads the same backward as forward.
// Ex. racecar, Anna

// const str1 = "ka yak";
// const str2 = "backend is awesome";
// const str3 = "mom";

// function checkString(str) {
//   let reversed = str.split("").reverse().join("");
//   return console.log(str === reversed);
// }

// checkString(str1);
// checkString(str2);
// checkString(str3);

let result = anangrams([
  "yo",
  "act",
  "flop",
  "tac",
  "foo",
  "cat",
  "oy",
  "olfp",
]);

function anangrams(arr) {
  let group = {};
  let finalArr = [];

  for (let i = 0; i < arr.length; i++) {
    let word = arr[i].split("").sort().join("");

    if (group[word]) {
      group[word].push(arr[i]);
    } else {
      group[word] = [arr[i]];
    }
  }

  for (let key in group) {
    finalArr.push(group[key]);
  }

  return finalArr;
}
console.log(result);
