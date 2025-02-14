from controls.controls import (
    ft,
    View,
    Appbar,
    Table,
    RowTable,
    AlertDialog,
    TextField,
    ElevantedButton,
    Dropdown
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
                                        RowTable(
                                            page=self.page,
                                            title='Groups',
                                            title_on_click=self.show_groups,
                                            add_on_click=self.add_group,
                                            change_on_click=self.edit_group
                                        ),
                                        RowTable(
                                            page=self.page,
                                            title='Users',
                                            title_on_click=self.show_users,
                                            add_on_click=self.add_user,
                                            change_on_click=self.edit_user
                                        )
                                    ]
                                )
                            ]
                        )
                    )
                ]
            )
        ]
    
    def show_users(self, e: ft.ControlEvent):
        ...
    
    def show_groups(self, e: ft.ControlEvent):
        ...
    
    def add_user(self, e: ft.ControlEvent):
        AddUser(page=self.page)
        e.page.update()
    
    def edit_user(self, e: ft.ControlEvent):
        ...
    
    def add_group(self, e: ft.ControlEvent):
        ...
    
    def edit_group(self, e: ft.ControlEvent):
        ...

class AddUser(AlertDialog):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__(
            page=page,
            title='Add User',
            title_color=ft.Colors.with_opacity(
                opacity=0.80,
                color=ft.Colors.BLACK
            ),
            title_size=18
        )

        self.actions=[
            ft.ResponsiveRow(
                controls=[
                    ElevantedButton(
                        text='Add user'
                    )
                ]
            )
        ]

        self.content = ft.Column(
            controls=[
                ft.ResponsiveRow(
                    controls=[
                        TextField(
                            hint_text='Username',
                            autofocus=True,
                            prefix_icon=ft.Icons.PERSON
                        ),
                        TextField(
                            hint_text='Email',
                            autofocus=True,
                            prefix_icon=ft.Icons.EMAIL
                        ),
                        Dropdown(
                            hint_text= 'usertype',
                            icon= ft.Icons.LINE_STYLE,
                            options=[
                                ft.dropdown.Option(
                                    key=user_role
                                ) for user_role in ['superuser', 'seller', 'manager']
                            ]
                        ),
                        Dropdown(
                            hint_text= 'status',
                            icon= ft.Icons.LINE_STYLE,
                            options=[
                                ft.dropdown.Option(
                                    key=user_role
                                ) for user_role in ['active', 'desactive']
                            ]
                        ),
                        TextField(
                            hint_text='Password',
                            autofocus=True,
                            prefix_icon=ft.Icons.KEY,
                            password=True,
                            can_reavel_password=True
                        )
                    ]
                )
            ]
        )

        self.page = page
        self.page.overlay.append(self)
        self.open = True