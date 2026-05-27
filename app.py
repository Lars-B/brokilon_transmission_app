import flet as ft
from gui.layout import build_ui


def main(page: ft.Page):
    build_ui(page)


if __name__ == "__main__":
    ft.run(main)
