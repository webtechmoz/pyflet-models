from controls.controls import (
    ft,
    Text,
    TextField,
    View,
    ElevantedButton
)
from database.database import Database

class Login(View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__(page=page, route='/admin/login')
        self.controls = [
            ft.ResponsiveRow(
                controls=[
                    ft.Container(
                        col={'xs': 11.4, 'sm': 6, 'md': 5, 'lg': 3},
                        border=ft.border.all(
                            width=0.1,
                            color=ft.Colors.with_opacity(0.40, 'black')
                        ),
                        padding=ft.padding.only(
                            top=0,
                            bottom=12
                        ),
                        content=ft.Column(
                            controls=[
                                Title(title='Pyflet Administration'),
                                TextFieldSpace()
                            ],
                            spacing=20
                        )
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
        ]

class TextFieldSpace(ft.Container):
    def __init__(
        self
    ):
        super().__init__()
        self.database = Database(database='database')
        self.border_radius = ft.border_radius.all(0)
        self.padding = ft.padding.only(
            left=15,
            right=15
        )
        self.content = ft.Column(
            controls=[
                TextField(
                    hint_text='Username',
                    prefix_icon=ft.Icons.PERSON,
                    autofocus=True
                ),
                TextField(
                    hint_text='Password',
                    prefix_icon=ft.Icons.KEY,
                    password=True
                ),
                ft.ResponsiveRow(
                    controls=[
                        ElevantedButton(
                            text='Login'
                        )
                    ]
                )
            ],
            spacing=15
        )
    
    def verifiy_login(e: ft.ControlEvent):
        ...

class Title(ft.Container):
    def __init__(
        self,
        title: str = None,
        bgcolor = ft.Colors.GREEN_600,
        text_color: ft.Colors = ft.Colors.WHITE,
        text_size: int = 13
    ):
        super().__init__()
        self.title = title
        self.alignment = ft.alignment.center
        self.height = 40
        self.bgcolor = bgcolor
        self.content = Text(
            value=title,
            color=text_color,
            size=text_size,
            weight=ft.FontWeight.W_100
        )