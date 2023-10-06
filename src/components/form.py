import flet as ft


class From(ft.UserControl):
    task_input: ft.TextField
    submit_button: ft.IconButton

    def __init__(self, submit_func):
        self.submit_func = submit_func
        super().__init__()

    def _text_input(self):
        return ft.TextField(
            height=48,
            width=225,
            filled=True,
            text_size=12,
            color="#ffffff",
            bgcolor="#0f0f0f",
            border_color=ft.border.all(0.5, "white"),
        )

    def _action_button(self, text: str, action: callable):
        return ft.IconButton(
            content=ft.Text(text),
            height=48,
            width=225,
            on_click=action,
            style=ft.ButtonStyle(
                bgcolor={"": "#0f0f0f"},
                shape={"": ft.RoundedRectangleBorder(radius=8)},
            ),
        )

    def toggle_view_form(self):
        self.container.height = 80 if self.container.height == 200 else 200
        self.container.opacity = 0 if self.container.opacity else 0.8
        self.container.update()

    def build(self):
        self.task_input = self._text_input()
        self.submit_button = self._action_button("Add Task", self.submit_func)
        self.container = ft.Container(
            width=500,
            height=80,
            bgcolor="bluegrey500",
            opacity=0,
            border_radius=40,
            animate=ft.animation.Animation(400, "decelerate"),
            animate_opacity=200,
            padding=ft.padding.only(top=45, bottom=45),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.task_input,
                    self.submit_button,
                ],
            ),
        )
        return self.container
