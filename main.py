import flet as ft

from gui.layout import build_ui

APP_TITLE = "BREATH Helper App"


def main(page: ft.Page):
    page.title = APP_TITLE
    page.window.icon = "assets/icon.png"
    build_ui(page)


if __name__ == "__main__":
    ft.run(main, assets_dir="assets")
