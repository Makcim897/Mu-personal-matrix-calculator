import flet as ft

def main(page: ft.Page):
    page.title = "matrix-calculator"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    Mc = ft.Text("Matrix C")
    Mb = ft.Text("Matrix B")
    Ma = ft.Text("Matrix A")
#Matrix A
    a11 = ft.TextField(value="", width=100)
    a12 = ft.TextField(value="", width=100)
    a13 = ft.TextField(value="", width=100)
    a21 = ft.TextField(value="", width=100)
    a22 = ft.TextField(value="", width=100)
    a23 = ft.TextField(value="", width=100)
    a31 = ft.TextField(value="", width=100)
    a32 = ft.TextField(value="", width=100)
    a33 = ft.TextField(value="", width=100)
#Matrix B
    b11 = ft.TextField(value="", width=100)
    b12 = ft.TextField(value="", width=100)
    b13 = ft.TextField(value="", width=100)
    b21 = ft.TextField(value="", width=100)
    b22 = ft.TextField(value="", width=100)
    b23 = ft.TextField(value="", width=100)
    b31 = ft.TextField(value="", width=100)
    b32 = ft.TextField(value="", width=100)
    b33 = ft.TextField(value="", width=100)
#Matrix C
    c11 = ft.TextField(value="", width=100)
    c12 = ft.TextField(value="", width=100)
    c13 = ft.TextField(value="", width=100)
    c21 = ft.TextField(value="", width=100)
    c22 = ft.TextField(value="", width=100)
    c23 = ft.TextField(value="", width=100)
    c31 = ft.TextField(value="", width=100)
    c32 = ft.TextField(value="", width=100)
    c33 = ft.TextField(value="", width=100)

    amultiply_num = ft.TextField(value="", width=105)
    cmultiply_num = ft.TextField(value="", width=105)
    vdelta = ft.TextField(value="", width=105)
    cvdelta = ft.TextField(value="", width=105)
    page.update()

    def amultiply(e):
        a11.value = int(a11.value) * int(amultiply_num.value)
        a12.value = int(a12.value) * int(amultiply_num.value)
        a13.value = int(a13.value) * int(amultiply_num.value)
        a21.value = int(a21.value) * int(amultiply_num.value)
        a22.value = int(a22.value) * int(amultiply_num.value)
        a23.value = int(a23.value) * int(amultiply_num.value)
        a31.value = int(a31.value) * int(amultiply_num.value)
        a32.value = int(a32.value) * int(amultiply_num.value)
        a33.value = int(a33.value) * int(amultiply_num.value)
        page.update()

    def atranspose(e):
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

    def adelta(e):
        vdelta.value = ((int(a11.value) * int(a22.value) * int(a33.value)) +
                        (int(a21.value) * int(a32.value) * int(a13.value)) +
                        (int(a12.value) * int(a23.value) * int(a31.value)) -
                        (int(a13.value) * int(a22.value) * int(a31.value)) -
                        (int(a11.value) * int(a32.value) * int(a23.value)) -
                        (int(a12.value) * int(a21.value) * int(a33.value)))
        page.update()

    def areset(e):
        a11.value = " "
        a12.value = " "
        a13.value = " "
        a21.value = " "
        a22.value = " "
        a23.value = " "
        a31.value = " "
        a32.value = " "
        a33.value = " "
        page.update()

    def cmultiply(e):
        c11.value = int(c11.value) * int(cmultiply_num.value)
        c12.value = int(c12.value) * int(cmultiply_num.value)
        c13.value = int(c13.value) * int(cmultiply_num.value)
        c21.value = int(c21.value) * int(cmultiply_num.value)
        c22.value = int(c22.value) * int(cmultiply_num.value)
        c23.value = int(c23.value) * int(cmultiply_num.value)
        c31.value = int(c31.value) * int(cmultiply_num.value)
        c32.value = int(c32.value) * int(cmultiply_num.value)
        c33.value = int(c33.value) * int(cmultiply_num.value)
        page.update()

    def ctranspose(e):
        copc21 = int(c21.value)
        c21.value = int(c12.value)
        c12.value = int(copc21)

        copc13 = int(c13.value)
        c13.value = int(c31.value)
        c31.value = int(copc13)

        copc23 = int(c23.value)
        c23.value = int(c32.value)
        c32.value = int(copc23)
        page.update()

    def cdelta(e):
        cvdelta.value = ((int(c11.value) * int(c22.value) * int(c33.value)) +
                        (int(c21.value) * int(c32.value) * int(c13.value)) +
                        (int(c12.value) * int(c23.value) * int(c31.value)) -
                        (int(c13.value) * int(c22.value) * int(c31.value)) -
                        (int(c11.value) * int(c32.value) * int(c23.value)) -
                        (int(c12.value) * int(c21.value) * int(c33.value)))
        page.update()

    def creset(e):
        c11.value = " "
        c12.value = " "
        c13.value = " "
        c21.value = " "
        c22.value = " "
        c23.value = " "
        c31.value = " "
        c32.value = " "
        c33.value = " "
        page.update()

    def plus(e):
        b11.value = int(c11.value) + int(a11.value)
        b12.value = int(c12.value) + int(a12.value)
        b13.value = int(c13.value) + int(a13.value)
        b21.value = int(c21.value) + int(a21.value)
        b22.value = int(c22.value) + int(a22.value)
        b23.value = int(c23.value) + int(a23.value)
        b31.value = int(c31.value) + int(a31.value)
        b32.value = int(c32.value) + int(a32.value)
        b33.value = int(c33.value) + int(a33.value)
        page.update()
    def minusa(e):
        b11.value = int(c11.value) - int(a11.value)
        b12.value = int(c12.value) - int(a12.value)
        b13.value = int(c13.value) - int(a13.value)
        b21.value = int(c21.value) - int(a21.value)
        b22.value = int(c22.value) - int(a22.value)
        b23.value = int(c23.value) - int(a23.value)
        b31.value = int(c31.value) - int(a31.value)
        b32.value = int(c32.value) - int(a32.value)
        b33.value = int(c33.value) - int(a33.value)
        page.update()
    def minusc(e):
        b11.value = int(a11.value) - int(c11.value)
        b12.value = int(a12.value) - int(c12.value)
        b13.value = int(a13.value) - int(c13.value)
        b21.value = int(a21.value) - int(c21.value)
        b22.value = int(a22.value) - int(c22.value)
        b23.value = int(a23.value) - int(c23.value)
        b31.value = int(a31.value) - int(c31.value)
        b32.value = int(a32.value) - int(c32.value)
        b33.value = int(a33.value) - int(c33.value)
        page.update()

    def multiplyAC(e):
        b11.value = (int(a11.value) * int(c11.value) +
                     int(a12.value) * int(c21.value) +
                     int(a13.value) * int(c31.value))
        b12.value = (int(a11.value) * int(c12.value) +
                     int(a12.value) * int(c22.value) +
                     int(a13.value) * int(c32.value))
        b13.value = (int(a11.value) * int(c13.value) +
                     int(a12.value) * int(c23.value) +
                     int(a13.value) * int(c33.value))
        b21.value = (int(a21.value) * int(c11.value) +
                     int(a22.value) * int(c21.value) +
                     int(a23.value) * int(c31.value))
        b22.value = (int(a21.value) * int(c12.value) +
                     int(a22.value) * int(c22.value) +
                     int(a23.value) * int(c32.value))
        b23.value = (int(a21.value) * int(c13.value) +
                     int(a22.value) * int(c23.value) +
                     int(a23.value) * int(c33.value))
        b31.value = (int(a31.value) * int(c11.value) +
                     int(a32.value) * int(c21.value) +
                     int(a33.value) * int(c31.value))
        b32.value = (int(a31.value) * int(c12.value) +
                     int(a32.value) * int(c22.value) +
                     int(a33.value) * int(c32.value))
        b33.value = (int(a31.value) * int(c13.value) +
                     int(a32.value) * int(c23.value) +
                     int(a33.value) * int(c33.value))
        page.update()

    def multiplyCA(e):
        b11.value = (int(c11.value)*int(a11.value)+
                     int(c12.value)*int(a21.value)+
                     int(c13.value)*int(a31.value))
        b12.value = (int(c11.value)*int(a12.value)+
                     int(c12.value)*int(a22.value)+
                     int(c13.value)*int(a32.value))
        b13.value = (int(c11.value)*int(a13.value)+
                     int(c12.value)*int(a23.value)+
                     int(c13.value)*int(a33.value))
        b21.value = (int(c21.value)*int(a11.value)+
                     int(c22.value)*int(a21.value)+
                     int(c23.value)*int(a31.value))
        b22.value = (int(c21.value)*int(a12.value)+
                     int(c22.value)*int(a22.value)+
                     int(c23.value)*int(a32.value))
        b23.value = (int(c21.value)*int(a13.value)+
                     int(c22.value)*int(a23.value)+
                     int(c23.value)*int(a33.value))
        b31.value = (int(c31.value)*int(a11.value)+
                     int(c32.value)*int(a21.value)+
                     int(c33.value)*int(a31.value))
        b32.value = (int(c31.value)*int(a12.value)+
                     int(c32.value)*int(a22.value)+
                     int(c33.value)*int(a32.value))
        b33.value = (int(c31.value)*int(a13.value)+
                     int(c32.value)*int(a23.value)+
                     int(c33.value)*int(a33.value))
        page.update()

    page.add(ft.Row(controls=[Mc], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[c11, c12, c13], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[c21, c22, c23, cvdelta, ft.TextButton(text="delta", on_click=cdelta), ft.TextButton(text="reset", on_click=creset)], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[c31, c32, c33, cmultiply_num, ft.TextButton(text="multiply", on_click=cmultiply), ft.TextButton(text="transpose", on_click=ctranspose)], alignment=ft.MainAxisAlignment.START))

    page.add(ft.Row(controls=[Mb], alignment=ft.MainAxisAlignment.CENTER))
    page.add(ft.Row(controls=[ft.TextButton(text=" C-A", on_click=minusa), b11, b12, b13], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[ft.TextButton(text="plus", on_click=plus), b21, b22, b23], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[ft.TextButton(text=" A-C", on_click=minusc), b31, b32, b33], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[ft.TextButton(text="C*A", on_click=multiplyCA), ft.TextButton(text="A*C", on_click=multiplyAC)], alignment=ft.MainAxisAlignment.START))

    page.add(ft.Row(controls=[Ma], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[a11, a12, a13, amultiply_num, ft.TextButton(text="multiply", on_click=amultiply), ft.TextButton(text="transpose", on_click=atranspose)], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[a21, a22, a23, vdelta, ft.TextButton(text="delta", on_click=adelta), ft.TextButton(text="reset", on_click=areset)], alignment=ft.MainAxisAlignment.START))
    page.add(ft.Row(controls=[a31, a32, a33], alignment=ft.MainAxisAlignment.START))

    page.update()

ft.app(target = main)