//1. access captneyepatch

//2. change wonderwoman to diana prince

//3. use an array method to delete the last superhero in the justice league

//4. use an array method to add the word "member" to every hero in the theOtherHeroes array. (ex. crimsonmechdudemember)

//5. combine the justice league members and the other heroes together in a crosserOver array

//6. delete all heroes in the justice league who have the word "man" in their title

//7. iterate over both arrays so that they are no longer just strings but they are objects that are structured like this
//combine them so they are all heroes in one array
[
    {
    name: "spiderman",
    league: "otherHeroes",
   },
    {
    name: "batman",
    league: "Justice league",
   }
]

const justiceLeague = [
    "batman", "wonderwoman", "cyborg", "flash", "aquaman","spiderman", "superman", "greenlantern"
]

const theOtherHeroes = [
    "crimsonmechdude", "hammerboy", "greenguy", "hawkguy", "blackassassin","shieldbro", "captneyepatch"
]

// console.log(theOtherHeroes[6])

// justiceLeague.splice(1, 1, "diana prince")
// console.log(justiceLeague)

// justiceLeague.pop()
// console.log(justiceLeague)

// theOtherHeroes.map((hero) => {
//     let newcharacter = hero.concat("member")
//     return console.log(newcharacter)
// }
// )

// console.log(justiceLeague.concat(theOtherHeroes))

// let thisleagueneedsnoman = []
// justiceLeague.map((hero) => {
//     if (hero.includes("man")) {
//     } else {
//         thisleagueneedsnoman.push(hero)
//     }
// })
// console.log(thisleagueneedsnoman)

// const copyofJL = justiceLeague;
// let newMembers = [];
// for (const member of copyofJL) {
//   const newFormat = { name: member, league: "justice League" };
//   newMembers.push(newFormat);
// }

// const copyofOH = theOtherHeroes;
// let newOHMembers = [];
// for (const member of copyofOH) {
//   const newFormat = { name: member, league: "theOtherHeroes" };
//   newOHMembers.push(newFormat);
// }

// console.log(newMembers.concat(newOHMembers))

const allHeroes = [...justiceLeague, ...theOtherHeroes];
let newMembers = [];
for (const member of allHeroes) {
  if (
    member.includes("man") ||
    member === "cyborg" ||
    member === "flash" ||
    member === "green lantern"
  ) {
    const newFormat = { name: member, league: "justice League" };
    newMembers.push(newFormat);
  } else {
    const newFormat = { name: member, league: "avengers" };
    newMembers.push(newFormat);
  }
}
console.log(newMembers);