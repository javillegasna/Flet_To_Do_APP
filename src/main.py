import flet as ft
from database.sqlite_repository import Database


def main(page: ft.Page):
    db = Database()


if __name__ == "__main__":
    ft.app(target=main)
