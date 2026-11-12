import json
from datetime import datetime

class Person:
    def __init__(self, name):
        self.name = name

    def order(self, projekt_name, time):

        new_project = {
            "name": self.name,
            "projekt_name": projekt_name,
            "time": time,
            "status": "wartend",
            "started_at": None
        }

        try:
            with open("traker.json", "r", encoding="utf-8") as file:
                projects = json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            projects = []

        projects.append(new_project)

        with open("traker.json", "w", encoding="utf-8") as file:
            json.dump(projects, file, ensure_ascii=False, indent=4)

    def users_control(self):

        with open("users.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return self.name in data["names"]


class Printer:

    def __init__(self, name):
        self.name = name

    def orders(self):
        try:
            with open("traker.json", "r", encoding="utf-8") as file:
                return json.load(file)

        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_orders(self, projects):
        with open("traker.json", "w", encoding="utf-8") as file:
            json.dump(projects, file, ensure_ascii=False, indent=4)

    def inWork(self):

        projects = self.orders()

        # Prüfen, ob bereits ein Projekt bearbeitet wird
        for project in projects:
            if project["status"] == "in_bearbeitung":
                return project

        # Erstes wartendes Projekt finden
        for project in projects:

            if project["status"] == "wartend":

                project["status"] = "in_bearbeitung"

                project["started_at"] = datetime.now().isoformat()

                self.save_orders(projects)

                return project

        return None

    def collect_project(self):

        projects = self.orders()

        for project in projects:

            if project["status"] == "in_bearbeitung":
                project["status"] = "abgeschlossen"

                self.save_orders(projects)

                self.inWork()

                return True

        return False

    def remaining_time(self):

        current = self.inWork()

        if not current:
            return 0

        start = datetime.fromisoformat(current["started_at"])

        elapsed = (datetime.now() - start).total_seconds()

        remaining = current["time"] * 60 - int(elapsed)

        return max(0, remaining)