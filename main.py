import streamlit as st

# Initialize the to-do list if it doesn't exist yet
if 'todos' not in st.session_state:
    st.session_state.todos = []

st.title("To-Do List App")

# Add new task
new_task = st.text_input("Enter a new task:")

if st.button("Add Task"):
    if new_task.strip() != "":
        st.session_state.todos.append({"task": new_task, "done": False})
    else:
        st.warning("Task cannot be empty!")

st.write("---")

# Display and update tasks
for i, todo in enumerate(st.session_state.todos):
    col1, col2 = st.columns([0.1, 0.9])
    with col1:
        done = st.checkbox("", value=todo["done"], key=i)
    with col2:
        if done:
            st.markdown(f"~~{todo['task']}~~")
        else:
            st.markdown(todo['task'])

    # Update task status
    st.session_state.todos[i]["done"] = done

# Optional: Clear completed tasks
if st.button("Clear Completed Tasks"):
    st.session_state.todos = [t for t in st.session_state.todos if not t["done"]]
    st.success("Completed tasks cleared!")
