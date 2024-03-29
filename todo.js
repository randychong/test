const root = document.querySelector(".root");
const mainContainer = document.createElement("div");
const input = document.createElement("input");
const button = document.createElement("button");
const taskContainer = document.createElement("div");
const list = document.createElement("ul");
const header = document.createElement("h1");

mainContainer.className = "mainContainer";
input.className = "input";
button.className = "button";
button.innerHTML = "Add Task";
taskContainer.className = "taskContainer";
list.className = "taskList";
header.innerHTML = "Randy's To Do List";

taskContainer.append(list);
mainContainer.append(input, button);
root.append(header, mainContainer, taskContainer);

function addTask() {
  const input = document.querySelector(".input").value;
  const list = document.querySelector(".taskList");
  const listItem = document.createElement("li");

  listItem.className = "listItem";

  listItem.append(input);
  list.append(listItem);
}

button.addEventListener("click", function () {
  addTask();
});

input.addEventListener("keyup", function (event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    button.click();
  }
});
