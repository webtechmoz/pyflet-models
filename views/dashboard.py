from controls.controls import (
    ft,
    Text,
    View,
    TextField,
    ElevantedButton,
    TextButton,
    Appbar
)

class Dashboard(View):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__(page=page, route='/admin/dashboard')
        self.appbar = Appbar(page=page, title='Pyflet Administration')
        self.vertical_alignment = ft.MainAxisAlignment.START
        self.padding = ft.padding.only(top=10)
        self.controls = [
            ft.Column(
                controls=[
                    ft.Container(
                        padding=ft.padding.only(left=10, right=10),
                        content=ft.ResponsiveRow(
                            controls=[
                                Table(
                                    page=self.page,
                                    header_title='Authorization & Authentication',
                                    rows=[
                                        RowTable(page=self.page, title='Groups'),
                                        RowTable(page=self.page, title='Users')
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        ]

class Header(ft.Container):
    def __init__(
        self,
        title: str
    ):
        super().__init__()
        self.bgcolor = ft.Colors.GREEN_600
        self.alignment = ft.alignment.center
        self.height = 30
        self.padding = ft.padding.only(left=6)
        self.content = Text(
            value=title,
            color=ft.Colors.WHITE,
            weight='normal'
        )

class RowTable(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        title: str
    ):
        super().__init__()
        self.page = page
        self.content = ft.Row(
            controls=[
                TextButton(page=page, text=title, font_weight='w700'),
                ft.Row(
                    controls=[
                        TextButton(page=page, text='Add', icon=ft.Icons.ADD, font_weight='w300'),
                        TextButton(page=page, text='Change', icon=ft.Icons.EDIT, font_weight='w300')
                    ],
                    spacing=4
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        self.border = ft.border.only(
            bottom=ft.BorderSide(
                width=0.2,
                color=ft.Colors.with_opacity(0.5, 'grey')
            )
        )

class Table(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        header_title: str,
        rows: list[RowTable] = None
    ):
        super().__init__()
        self.page = page
        self.col = {'xs': 12, 'sm': 6}
        self.header_title = header_title
        self.alignment = ft.alignment.center
        self.padding = ft.padding.all(0)
        self.content = ft.Column(
            controls=[
                Header(title=self.header_title),
                ft.Column(
                    controls=rows if rows else []
                )
            ],
            spacing=6
        )