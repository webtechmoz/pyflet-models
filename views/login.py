from controls.controls import (
    ft,
    Text,
    TextField,
    View,
    ElevantedButton
)
from database.database import Database, Filter

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
                username := TextField(
                    hint_text='Username',
                    prefix_icon=ft.Icons.PERSON,
                    autofocus=True
                ),
                password := TextField(
                    hint_text='Password',
                    prefix_icon=ft.Icons.KEY,
                    password=True
                ),
                ft.ResponsiveRow(
                    controls=[
                        ElevantedButton(
                            text='Login',
                            on_click=self.verifiy_login
                        )
                    ]
                )
            ],
            spacing=15
        )
        self.username = username
        self.password = password
    
    def verifiy_login(self, e: ft.ControlEvent):
        if self.username.value and self.password.value:
            user_details = self.database.select_data(
                table_name='users',
                columns=['username'],
                condition=Filter(
                    column='username'
                ).EQUAL(
                    value=self.username.value
                ).AND.filterby(
                    column='password'
                ).EQUAL(
                    value=self.database.db.encrypt_value(
                        value=self.password.value
                    )
                )
            )

            if len(user_details) == 1:
                e.page.data = user_details[0][0]
                e.page.go('/admin/dashboard')
        
        self.username.value = ''
        self.password.value = ''
        self.username.focus()
        e.page.update()

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