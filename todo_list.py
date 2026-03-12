import streamlit as st
from task import Task

if "task_list" not in st.session_state:
    st.session_state.task_list = []
task_list = st.session_state.task_list

def add_task(task_name: str):
    task_list.append(Task(task_name))
    
def mark_done(task: Task):
    task.is_done = True
    
def mark_not_done(task: Task):
    task.is_done = False

def delete_task(idx: int):
    del task_list[idx] 
        
with st.sidebar:
    task = st.text_input("Enter a task")
    if st.button("Add task",type='primary'):
        add_task(task)

total_tasks = len(task_list)
completed_tasks = sum(1 for task in task_list if task.is_done)
metric_display = f"{completed_tasks}/{total_tasks}  done"
st.metric("Task completion", metric_display, delta=None)

st.header("Today's to-dos", divider='gray')
for idx, task in enumerate(task_list):
    task_col,delete_col = st.columns([0.8, 0.2])
    label = f"~~{task.name}~~" if task.is_done else task.name
    cheaked = task_col.checkbox(label, value=task.is_done,key=f"task_{idx}")
    if cheaked and not task.is_done:
        mark_done(task)
        st.rerun()
    elif not cheaked and task.is_done:
        mark_not_done(task)
        st.rerun()
    if delete_col.button("Delete", key=f"delete-{idx}"):
        delete_task(idx)
        st.rerun()
