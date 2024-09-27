import flet as ft


def main(page: ft.Page):
    page.title = "calculadora de IMC"
    page.bgcolor="purple"
    
    txtpeso=ft.TextField(label="ingresa tu peso")
    txtAltura=ft.TextField(label="ingresa tu altura")
    lblIMC=ft.Text("tu IMC es: ")
    
    img=ft.Image(src="https://github.com/Prof-Luis1986/Recursos/blob/main/Bascula.png",
                width=200,
                height=200
                
                )
    btnCalcular=ft.ElevatedButton(text="calcular")
    btnlimpiar=ft.ElevatedButton(text="limpiar")
    
    
    page.add(
        ft.Column(
            controls=[txtpeso,
                    txtAltura,
                    lblIMC
                    ],alignment="CENTER"),
        ft.Row(
            controls=[
                img
            ],alignment="CENTER"),
        ft.Row(
            controls=[
                btnCalcular,
                btnlimpiar
            ],alignment="CENTER")
        )    
    

ft.app(target=main,view=ft.AppView.WEB_BROWSER)
