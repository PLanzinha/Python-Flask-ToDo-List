from flask import Blueprint, render_template, request, redirect, url_for

todo_list_bp = Blueprint("todo_list", __name__, template_folder="templates")

tasks = [{"task_name": "Sample Task", "is_done": False}]


@todo_list_bp.route("/")
def task_list():
    return render_template("index.html", tasks=tasks)


@todo_list_bp.route("/add", methods=["POST"])
def add_task():
    task_name = request.form['task_name']
    if task_name:
        tasks.append({"task_name": task_name, "is_done": False})
    return redirect(url_for("todo_list.task_list"))


@todo_list_bp.route("/edit/<int:index>", methods=["GET", "POST"])
def edit_task(index):
    task = tasks[index]
    if request.method == "POST":
        task['task_name'] = request.form["task_name"]
        return redirect(url_for("todo_list.task_list"))
    else:
        return render_template("edit.html", task=task, index=index)


@todo_list_bp.route("/check/<int:index>")
def toggle_task_status(index):
    tasks[index]['is_done'] = not tasks[index]['is_done']
    return redirect(url_for("todo_list.task_list"))


@todo_list_bp.route("/delete/<int:index>")
def delete_task(index):
    del tasks[index]
    return redirect(url_for("todo_list.task_list"))


@todo_list_bp.route("/clear_checked_tasks", methods=["POST"])
def clear_checked_tasks():
    tasks[:] = [task for task in tasks if not task["is_done"]] 
    return redirect(url_for("todo_list.task_list"))
