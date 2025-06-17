function filterTodos(filter) {
  const todos = document.querySelectorAll(".todo");
  todos.forEach(todo => {
    const isCompleted = todo.classList.contains("completed");
    if (
      filter === "all" ||
      (filter === "completed" && isCompleted) ||
      (filter === "incomplete" && !isCompleted)
    ) {
      todo.style.display = "flex";
    } else {
      todo.style.display = "none";
    }
  });
}
