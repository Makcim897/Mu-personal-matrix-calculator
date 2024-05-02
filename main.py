import flet as ft

def main(page: ft.Page):
    page.title = "matrix-calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    a11 = ft.TextField(value="", width=100)
    a12 = ft.TextField(value="", width=100)
    a13 = ft.TextField(value="", width=100)
    a21 = ft.TextField(value="", width=100)
    a22 = ft.TextField(value="", width=100)
    a23 = ft.TextField(value="", width=100)
    a31 = ft.TextField(value="", width=100)
    a32 = ft.TextField(value="", width=100)
    a33 = ft.TextField(value="", width=100)
    multiply_num = ft.TextField(value="", width=105)
    vdelta = ft.TextField(value="", width=100)
    page.update()

    def multiply(e):
        a11.value = int(a11.value) * int(multiply_num.value)
        a12.value = int(a12.value) * int(multiply_num.value)
        a13.value = int(a13.value) * int(multiply_num.value)
        a21.value = int(a21.value) * int(multiply_num.value)
        a22.value = int(a22.value) * int(multiply_num.value)
        a23.value = int(a23.value) * int(multiply_num.value)
        a32.value = int(a32.value) * int(multiply_num.value)
        a33.value = int(a33.value) * int(multiply_num.value)
        page.update()

    def transpose(e):
        copa21 = int(a21.value)
        a21.value = int(a12.value)
        a12.value = int(copa21)

        copa13 = int(a13.value)
        a13.value = int(a31.value)
        a31.value = int(copa13)

        copa23 = int(a23.value)
        a23.value = int(a32.value)
        a32.value = int(copa23)
        page.update()


    def delta(e):
        vdelta.value =  ((int(a11.value)*int(a22.value)*int(a33.value))+
                        (int(a21.value)*int(a32.value)*int(a13.value))+
                        (int(a12.value)*int(a23.value)*int(a31.value))-
                        (int(a13.value)*int(a22.value)*int(a31.value))-
                        (int(a11.value)*int(a32.value)*int(a23.value))-
                        (int(a12.value)*int(a21.value)*int(a33.value)))
        page.update()




    page.add(ft.Row(controls=[a11, a12, a13], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row(controls=[a21, a22, a23], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row(controls=[a31, a32, a33], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row(controls=[multiply_num, ft.TextButton(text="multiply", on_click=multiply), ft.TextButton(text="transpose", on_click=transpose)],alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row(controls=[vdelta, ft.TextButton(text="delta", on_click=delta)], alignment=ft.MainAxisAlignment.CENTER))
    page.update()

ft.app(target = main)