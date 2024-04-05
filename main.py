import flet as ft

def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    a = ft.TextField(value="0")
    b = ft.TextField(value="0")
    c = ft.TextField(value="0")
    d = ft.TextField(value="0")
    e = ft.TextField(value="0")
    f = ft.TextField(value="0")
    g = ft.TextField(value="0")
    h = ft.TextField(value="0")
    i = ft.TextField(value="0")

    page.add(
        ft.Row(controls=[
            a,
            b,
            c
        ])
    )
    page.add(
        ft.Row(controls=[
            d,
            e,
            f
        ])
    )
    page.add(
        ft.Row(controls=[
            g,
            h,
            i
        ])
    )
    page.update()



ft.app(target=main)