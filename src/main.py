import flet as ft
import random

field = ft.TextField(value=random.choice(["" ,":)", ":>", ">:)", "🤫🧏‍♂️", "🗣️🔥🔥🔥", "☝️🤓", "👍"]), read_only=True)

grades: list[int] = []
display_grades: list[str] = []

def RecountGrades(e: ft.Control):
    try:
        field.value = f"{', '.join(map(str, display_grades))} = {round(sum(grades) / len(grades), 2)}"
    except ZeroDivisionError:
        field.value = ""
    field.update()

def DelateLastGrade(e: ft.Control):
    try:
        grades.pop()
        display_grades.pop()
    except IndexError:
        pass
    RecountGrades(None)

def DelateAllGrades(e: ft.Control):
    grades.clear()
    display_grades.clear()
    RecountGrades(None)

class GradeButton(ft.ElevatedButton):
    def __init__(self, text: str, grade: int):
        super().__init__()
        self.width = 60
        self.height = 60
        self.text = text
        self.data = grade
        self.on_click = self.AddGrade

    def AddGrade(self, e: ft.Control):
        grades.append(self.data)
        display_grades.append(self.text)
        RecountGrades(None)

keybord = ft.Column(
    controls=[
        ft.Row(
            [
                GradeButton("6-", 5.75),
                GradeButton("6", 6),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                GradeButton("5-", 4.75),
                GradeButton("5", 5),
                GradeButton("5+", 5.5),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                GradeButton("4-", 3.75),
                GradeButton("4", 4),
                GradeButton("4+", 4.5),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                GradeButton("3-", 2.75),
                GradeButton("3", 3),
                GradeButton("3+", 3.5),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                GradeButton("2-", 1.75),
                GradeButton("2", 2),
                GradeButton("2+", 2.5),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
        ft.Row(
            [
                GradeButton("1", 1),
                GradeButton("1+", 1.5),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ], 
    alignment=ft.MainAxisAlignment.CENTER,
    horizontal_alignment=ft.CrossAxisAlignment.CENTER
)

def main(page: ft.Page):
    page.title = "Grade Counter"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.theme_mode = ft.ThemeMode.DARK
    page.theme = ft.Theme(use_material3=True, color_scheme_seed=random.choice([ft.Colors.BLUE, ft.Colors.PURPLE, ft.Colors.BLUE, ft.Colors.RED, ft.Colors.BLUE]))

    page.appbar = ft.AppBar(
        title=ft.Text(value=page.title),
        center_title=True,
        bgcolor=ft.Colors.INVERSE_PRIMARY
    )

    page.floating_action_button = ft.Row(
        [
            ft.FloatingActionButton(
                text="Delate Last Grade",
                icon=ft.Icons.ARROW_BACK_IOS,
                on_click=DelateLastGrade
            ),
            ft.FloatingActionButton(
                text="Delate All Grades",
                icon=ft.Icons.DELETE,
                on_click=DelateAllGrades
            )
        ],
        alignment=ft.MainAxisAlignment.END
    )

    page.add(
        ft.SafeArea(
            content=ft.Column(
                controls=[
                    field,
                    keybord
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )
    )

if __name__ == "__main__":
    ft.app(target=main)
