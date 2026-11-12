
from flask import Flask, render_template, request, redirect, url_for

from backend import Person, Printer

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():

    message = request.args.get(
        "message", "Wollen Sie etwas bestellen?"
    )

    printer = Printer("One")

    if request.method == "POST":

        name = request.form.get("name", "").strip()
        projekt_name = request.form.get("projekt_name", "").strip()
        time_input = request.form.get("projekt_time", "").strip()

        user_item = Person(name)

        if user_item.users_control():

            if not projekt_name:
                message = "Bitte gib einen Projektnamen ein!"

            elif not time_input:
                message = "Bitte gib eine Projektzeit ein!"

            else:
                try:
                    projekt_time = int(time_input)

                    if projekt_time <= 0:
                        message = "Die Zeit muss größer als 0 sein!"

                    else:
                        user_item.order(projekt_name, projekt_time)
                        message = f"Willkommen {name}! Dein Projekt wurde gespeichert."

                except ValueError:
                    message = "Bitte gib eine gültige Zahl ein!"

        else:
            message = "Sie dürfen leider nicht drucken!"

    # Immer Projekte laden
    works = printer.orders()

    # Aktuelles Projekt laden
    current_project = printer.inWork()

    remaining = printer.remaining_time()

    return render_template(
        "index.html",
        message=message,
        works=works,
        current_project=current_project,
        remaining=remaining
    )


@app.route("/collected", methods=["POST"])
def collected():

    printer = Printer("One")

    success = printer.collect_project()

    if success:
        message = "Projekt wurde als abgeholt markiert!"
    else:
        message = "Das Projekt kann noch nicht abgeholt werden!"

    return redirect(url_for("index", message=message))


if __name__ == "__main__":
    app.run(debug=True)
