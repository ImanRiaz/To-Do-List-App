import streamlit as st

st.title("To-Do-List App")

task=st.text_input("Enter your task:")

if "task" not in st.session_state:
    st.session_state.tasks =[]

if st.button("Add task"):
    if task.strip()!="" :
        st.session_state.tasks.append(task)
        st.success(f"Added task: {task}")
    else:
        st.warning("Please enter a non-empty task.")

st.write("Task: ")
if st.session_state.tasks:
    for i,t in enumerate(st.session_state.tasks):
            if st.checkbox(t, key=f"task_{i}"):
                st.session_state.tasks.pop(i)

else:
    st.info("Tasks will show here.")

