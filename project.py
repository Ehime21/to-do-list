from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
tasks = []  # Temporary storage (clears when server restarts)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        new_task = request.form.get("task")

        if new_task.strip():
            tasks.append(new_task)

        return redirect(url_for("index"))

    return render_template("index.html", tasks=tasks)


@app.route("/remove/<int:index>")
def remove(index):
    if 0 <= index < len(tasks): 
        tasks.pop(index)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
