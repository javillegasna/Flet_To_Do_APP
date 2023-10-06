from datetime import datetime

import flet as ft

from components.form import From
from components.task import Task
from database.sqlite_repository import Database


def main(page: ft.Page):
    def add_button_action(e):
        input = _form.task_input
        button = _form.submit_button
        input.value = ""
        button.content.value = "Add task"
        _form.toggle_view_form()

    def add_task_to_screen(e):
        date_time = datetime.now().strftime("%b %d, %Y %I:M")
        input = _form.task_input
        if input.value:
            task_id = _db.insert_task((input.value, date_time))
            _main_column.controls.append(
                Task(
                    task_id=task_id,
                    task_content=input.value,
                    date=date_time,
                    action_delete=delete_task,
                    action_update=update_action,
                )
            )
            _main_column.update()
            _form.toggle_view_form()
        input.value = ""

    def delete_task(task: Task):
        _db.delete_task(task.task_id)
        _main_column.controls.remove(task)
        _main_column.update()

    def update_task(task: Task, input: ft.TextField):
        _db.update_task(task.task_id, input.value)
        task.task_label.value = input.value
        task.update()
        _form.toggle_view_form()

    def update_action(task: Task):
        _form.toggle_view_form()
        _form.height, _form.opacity = 200, 1
        _form.task_input.value = task.task_content
        _form.submit_button.content.value = "Update"
        _form.submit_button.on_click = lambda e: update_task(task, _form.task_input)
        _form.update()

    def get_tasks():
        tasks = _db.get_all_tasks()
        for task in tasks:
            _main_column.controls.append(
                Task(
                    task_id=task[0],
                    task_content=task[1],
                    date=task[2],
                    action_delete=delete_task,
                    action_update=update_action,
                )
            )
        _main_column.update()

    page.title = "MyApp"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 0
    page.window_width = 600
    page.window_height = 800

    _db = Database()
    _form = From(
        submit_func=add_task_to_screen,
    )
    _main_column = ft.Column(
        scroll="hidden",
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.Container(
                padding=ft.padding.only(left=15, right=15),
                content=ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    controls=[
                        ft.Text("To-Do Items", size=15, weight="bold"),
                        ft.IconButton(
                            ft.icons.ADD_CIRCLE_ROUNDED,
                            icon_size=18,
                            on_click=add_button_action,
                        ),
                    ],
                ),
            ),
            ft.Divider(height=0, color="white24"),
        ],
    )
    page.add(
        ft.Container(
            width=300,
            height=600,
            bgcolor="#0f0f0f",
            border_radius=40,
            border=ft.border.all(0.5, "white"),
            padding=ft.padding.only(top=35),
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            content=ft.Column(
                alignment=ft.MainAxisAlignment.CENTER,
                expand=True,
                controls=[
                    _main_column,
                    _form,
                ],
            ),
        )
    )
    get_tasks()
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
