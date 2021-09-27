// Write a function to return the maximum occurring character in the input string e.g., if input string is “Test” then function should return ‘t’.
// Note: capital letter ‘T’ and small letter ‘t’ should count as the same.

// str1 = "holddogecoinkek"
// // result: o
// str2 = "aahhanotheralgo"
// // result: a
// str3 = "randywhyyyyy"
// // result: y

// const maxChar = str => {
//     const myStr = str.toLowerCase();
//     // in case string has capitalized characters
//     const charMap = {};
//     let max = 0;
//     let maxChar = '';
  
//     for (let char of myStr) {
//       if (!charMap[char]) {
//         charMap[char] = 1;
//       } else {
//         charMap[char]++;
//       }
//     }
  
//     for (let char in charMap) {
//       if (charMap[char] > max) {
//         max = charMap[char];
//         maxChar = char;
//       }
//     }
  
//     return console.log(maxChar);
//  }

//  maxChar(str1)
//  maxChar(str2)
//  maxChar(str3)
 
//  Given an array of numbers and a stand alone number, return all combinations of numbers in the array that add up to the stand alone number.

// let array = [2,5,8,3,-2,9,0]
// let targetSum = 3
// // Result: [ 5, -2 ], [ 3, 0 ], [ -2, 5 ], [ 0, 3 ]

// const findTwoSum = (arr,sum)=>{
//     results = []
    
//     for(let i = 0; i < arr.length; i++){
//       for(let j = 0; j < arr.length; j++){
//         if (arr[i] + arr[j] === sum){
//           results.push([arr[i], arr[j]])
//         }
//       }
//     }
//     return console.log(results)
//   }

// findTwoSum(array, targetSum)

// Given a number N return the index value of the Fibonacci sequence, where the sequence is:
// 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

// For example, if N = 8, the function should return the number '34' which is the 8th index of the Fibonacci sequence

N = 8
// result: 13

  function fibonacci(num){
    var a = 1, b = 0, temp;
    while (num > 0){
      temp = a;
      a = a + b;
      b = temp;
      num--;    
    }
  
    return console.log(b);
  }

  fibonacci(N)

  //test message