// function getGrade(student, grade) {
//   return `${student}'s grade is ${grade}.`;
// }

// console.log(getGrade("randy", "A"));

// function getBill(bill, service) {
//   if (service == "good") {
//     billTotal = bill + bill * 0.2;
//   } else if (service == "fair") {
//     billTotal = bill + bill * 0.15;
//   } else if (service == "bad") {
//     billTotal = bill + bill * 0.1;
//   }

//   return billTotal;
// }

// console.log(getBill(10, "good"));

// function printNumbers(start, end) {
//   while (start < end) {
//     console.log(start);
//     start++;
//   }
// }

// printNumbers(1, 11);

// function printSquare(x) {
//   for (let index = 0; index < x; index++) {
//     let row = "";
//     for (let index = 0; index < x; index++) {
//       row += "#";
//     }
//     console.log(row + "");
//   }
// }

// printSquare(5);

function printBox(height, width) {
  for (let index = 0; index < height; index++) {
    let column = "-";
    for (let index = 0; index < width; index++) {
      let row = "-";
    }
    console.log(row + "" + column);
  }
}

printBox(6, 4);

// function positiveNumbers(array) {
//   positiveArray = [];
//   for (const x of array) {
//     if (x > -1) {
//       positiveArray.push(x);
//     }
//   }
//   return console.log(positiveArray);
// }

// positiveNumbers([1, -3, 5, -3, 0]);
