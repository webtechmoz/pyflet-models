from controls.controls import (
    ft,
    View,
    Appbar,
    Table,
    RowTable,
    AlertDialog,
    ElevantedButton,
)
from database.database import (
    Database,
    ColumnData,
    Filter
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
        ChangeUser(page=self.page)
        e.page.update()
    
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
        self.database = Database(database='database')
        self.actions=[
            ft.ResponsiveRow(
                controls=[
                    ElevantedButton(
                        text='Add user',
                        on_click=self.add_user
                    )
                ]
            )
        ]
    
    def add_user(self, e: ft.ControlEvent):
        user_values: list[str] = []
        for i, userfield in enumerate(self.userfields_group.controls):
            if not userfield.value:
                print(f'Preencha o campo {userfield.hint_text}')
                break
            
            user_values.append(userfield.value)

            if i == len(self.userfields_group.controls) - 1:
                if not self.database.select_data(
                    table_name='users', condition=Filter(
                        column='username'
                    ).EQUAL(
                        value=user_values[0].lower()
                    )
                ):
                    self.database.insert_data(
                        table_name='users',
                        data_query=[
                            ColumnData(
                                column='username',
                                value=user_values[0].lower()
                            ),
                            ColumnData(
                                column='email',
                                value=user_values[1]
                            ),
                            ColumnData(
                                column='usertype',
                                value=user_values[2]
                            ),
                            ColumnData(
                                column='password',
                                value=self.database.db.encrypt_value(
                                    value=user_values[4]
                                )
                            ),
                            ColumnData(
                                column='status',
                                value=True if user_values[3].lower() == 'active' else False
                            ),
                        ]
                    )
                
                else:
                    print('O usuário que tentas inserir já existe!')
            
        for userfield in self.userfields_group.controls:
            userfield.value = ''
        
        user_values.clear()
        e.page.update()

class ChangeUser(AlertDialog):
    def __init__(
        self,
        page: ft.Page
    ):
        super().__init__(
            page=page,
            title='Change User',
            title_color=ft.Colors.with_opacity(
                opacity=0.80,
                color=ft.Colors.BLACK
            ),
            title_size=18
        )
        self.database = Database(database='database')
        self.curr_user = self.database.select_data(
            table_name='users',
            columns=['username', 'email', 'usertype', 'status'],
            condition=Filter(
                column='username'
            ).EQUAL(
                value=self.page.data
            )
        )
        self.actions=[
            ft.ResponsiveRow(
                controls=[
                    ElevantedButton(
                        text='Add user',
                        on_click=self.change_user
                    )
                ]
            )
        ]
        
        for i, userfield in enumerate(self.userfields_group.controls):
            if i < 3:
                userfield.value = self.curr_user[0][i]
            
            elif i == 3:
                userfield.value = 'active' if self.curr_user[0][i] == '1' else 'desactive'
                userfield.disabled = True
    
    def change_user(self, e: ft.ControlEvent):
        user_values: list[list[str, str]] = []

        for i, userfield in enumerate(self.userfields_group.controls):
            if userfield.value:
                user_values.append(
                    [
                        userfield.hint_text.lower(),
                        userfield.value if i != 3 else True
                    ]
                )
        
        self.database.db.update_data(
            tablename='users',
            edit_query=[
                ColumnData(
                    column=user[0],
                    value=user[1] if user[0] != 'password' else self.database.db.encrypt_value(
                        value=user[1]
                    )
                ) for user in user_values
            ],
            condition=Filter(
                column='username'
            ).EQUAL(
                value=self.curr_user[0][0]
            )
        )
        self.close(e)