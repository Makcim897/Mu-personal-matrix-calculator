import flet as ft

def main(page: ft.Page):
    page.title = "matrix-calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    a11 = ft.TextField(value="0")
    a12 = ft.TextField(value="0")
    a13 = ft.TextField(value="0")
    a21 = ft.TextField(value="0")
    a22 = ft.TextField(value="0")
    a23 = ft.TextField(value="0")
    a31 = ft.TextField(value="0")
    a32 = ft.TextField(value="0")
    a33 = ft.TextField(value="0")
    multiply_num = ft.TextField(value="0")

    def multiply():
        a11.value = str(int(a11.value) * multiply_num.value)
        a12.value = str(int(a12.value) * multiply_num.value)
        a13.value = str(int(a13.value) * multiply_num.value)
        a21.value = str(int(a21.value) * multiply_num.value)
        a22.value = str(int(a22.value) * multiply_num.value)
        a23.value = str(int(a23.value) * multiply_num.value)
        a31.value = str(int(a31.value) * multiply_num.value)
        a32.value = str(int(a32.value) * multiply_num.value)
        a33.value = str(int(a33.value) * multiply_num.value)
        page.update()


    page.add(ft.Row(controls=[a11, a12, a13]))
    page.add(ft.Row(controls=[a21, a22, a23]))
    page.add(ft.Row(controls=[a31, a32, a33]))
    page.add(ft.Row(controls=[multiply_num,ft.TextButton(text="multiply", on_click=multiply())]))

    page.update()



ft.app(target = main)