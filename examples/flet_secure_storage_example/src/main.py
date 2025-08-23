import flet as ft

from flet_secure_storage import FletSecureStorage


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    page.add(

                ft.Container(height=150, width=300, alignment = ft.alignment.center, bgcolor=ft.Colors.PURPLE_200, content=FletSecureStorage(
                    tooltip="My new FletSecureStorage Control tooltip",
                    value = "My new FletSecureStorage Flet Control", 
                ),),

    )


ft.app(main)
