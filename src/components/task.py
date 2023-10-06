import flet as ft


class Task(ft.UserControl):
    def __init__(
        self, task_id, task_content: str, date: str, action_delete, action_update
    ):
        super().__init__()
        self.task_id = task_id
        self.task_content = task_content
        self.date = date
        self.action_delete = action_delete
        self.action_update = action_update

    def get_action_button(self, icon: str, color: str, action):
        return ft.IconButton(
            icon=icon,
            width=30,
            icon_size=18,
            icon_color=color,
            opacity=0,
            animate_opacity=200,
            on_click=action,
        )

    def show_icons(self, e):
        if e.data == "true":
            self.delete_button.opacity = 1
            self.edit_button.opacity = 1
        else:
            self.delete_button.opacity = 0
            self.edit_button.opacity = 0
        e.control.content.update()

    def build(self):
        self.task_label = ft.Text(value=self.task_content, size=10)
        self.date_label = ft.Text(value=self.date, size=9, color="#ffffff")
        self.delete_button = self.get_action_button(
            ft.icons.DELETE_ROUNDED,
            "red500",
            lambda e: self.action_delete(self),
        )
        self.edit_button = self.get_action_button(
            ft.icons.EDIT_ROUNDED,
            "white70",
            lambda e: self.action_update(self),
        )
        return ft.Container(
            width=280,
            height=60,
            margin=ft.margin.all(10),
            border=ft.border.all(0.85, "white54"),
            border_radius=8,
            on_hover=self.show_icons,
            clip_behavior=ft.ClipBehavior.HARD_EDGE,
            padding=10,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                controls=[
                    ft.Column(
                        spacing=1,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.task_label,
                            self.date_label,
                        ],
                    ),
                    ft.Row(
                        spacing=0,
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[
                            self.delete_button,
                            self.edit_button,
                        ],
                    ),
                ],
            ),
        )
