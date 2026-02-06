import flet as ft

def main(page: ft.Page):
    ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(),
                ft.Row(),
                ft.Row(),
                ft.Row(),
                ft.Row()
            ]
        )
    )

ft.run(main)