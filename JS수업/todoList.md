# 0518 Workshop
```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>0518 exercise & workshop</title>
  <style>
    input, label, button {
      margin-right: 5px;
    }
  </style>
</head>
<body>
  <h2>Add New Todo</h2>
  <p id="addNewTodo">

  </p>
  
  <hr>

  <h2>Todo List</h2>
  <ul id="todoList"></ul>
  <hr>

  <h2>Completed Tasks</h2>
  <ul id="completedTasks"></ul>
  <hr>

  <script>
    const createTodo = function (labelName, flag) {

      const newInput = document.createElement('li')
      const checkBox = document.createElement('input')
      checkBox.type = 'checkbox'

      checkBox.addEventListener('click', function (event) {
        if (flag === 1) {
          completedTasks.appendChild(createTodo(newInputLabel.innerText, 0))   
        }
        else {
          todoList.appendChild(createTodo(newInputLabel.innerText, 1))
        }
        newInput.remove()
      })

      const newInputLabel = document.createElement('label')
      if (flag === 1) {
        newInputLabel.innerText = labelName
      }
      else {
        newInputLabel.innerHTML = "<del>" + labelName + "</del>"
      }

      const editInput = document.createElement('input')
      editInput.type = 'text'

      const editButton = document.createElement('button')
      editButton.innerText = 'Edit'

      editButton.addEventListener('click', function (event) {
        if (flag === 1) {
          newInputLabel.innerText = editInput.value
        }
        else {
          newInputLabel.innerHTML = "<del>" + editInput.value + "</del>"
        }
        editInput.value = ''
      })

      const deleteButton = document.createElement('button')
      deleteButton.innerText = 'Delete'
      deleteButton.addEventListener('click', function(event) {
        newInput.remove()
      })

      newInput.append(checkBox, newInputLabel, editInput, editButton, deleteButton)

      return newInput
    }

    const newTodo = document.querySelector('#addNewTodo')

    const newTodoLabel = document.createElement('label')
    newTodoLabel.innerText = 'Add New Todo:'
    
    const newTodoInput = document.createElement('input')
    newTodoInput.setAttribute('type', 'text')

    const newTodoButton = document.createElement('button')
    newTodoButton.innerText = "Add"

    newTodoButton.addEventListener('click', function(event) {
      if (newTodoInput.value) {   
        todoList.appendChild(createTodo(newTodoInput.value, 1))      
        newTodoInput.value = ''
      }
    })
    
    newTodo.append(newTodoLabel, newTodoInput, newTodoButton)
  </script>
</body>
</html>