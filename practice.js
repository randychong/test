function formatDate(userDate) {
  // format from M/D/YYYY to YYYYMMD
  let newDate = [];
  for (const x of userDate) {
    if (x !== "/") {
      newDate.push(x);
    }
  }
  return newDate.join("");
}

console.log(formatDate("12/31/2014"));

function setup() {
  const button = document.querySelector(".remove");
  const image = document.querySelector(".image");

  button.addEventListener("click", function () {
    image.remove();
  });
}
