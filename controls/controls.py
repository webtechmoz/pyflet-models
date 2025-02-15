import flet as ft
from datetime import datetime

class View(ft.View):
    def __init__(
        self,
        page: ft.Page,
        route: str
    ):
        super().__init__()
        self.page = page
        self.route = route
        self.bgcolor = ft.Colors.WHITE
        self.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        self.padding = ft.padding.all(0)

class Text(ft.Text):
    def __init__(
        self,
        value: str,
        color: ft.Colors = ft.Colors.with_opacity(0.80, 'black'),
        size: float = 14,
        weight: ft.FontWeight = ft.FontWeight.W_600,
        selectable: bool = False
    ):
        super().__init__()
        self.value = value
        self.color = color
        self.weight = weight
        self.size = size
        self.selectable = selectable

class TextField(ft.TextField):
    def __init__(
        self,
        hint_text: str,
        prefix_icon: ft.Icons = None,
        border_radius: float = 2,
        bgcolor: ft.Colors = ft.Colors.WHITE,
        color: ft.Colors = ft.Colors.BLACK,
        size: int = 13,
        height: float = 45,
        col: dict[str, float] = {'xs': 12},
        autofocus: bool = False,
        password: bool = False,
        can_reavel_password: bool = False,
        on_change: ft.ControlEvent = None,
        on_submit: ft.ControlEvent = None,
        keyboard_type: ft.KeyboardType = ft.KeyboardType.NAME
    ):
        super().__init__()
        self.hint_text = hint_text
        self.prefix_icon = prefix_icon
        self.height = height
        self.border_radius = border_radius
        self.col = col
        self.autofocus = autofocus
        self.bgcolor = bgcolor
        self.focused_bgcolor = self.bgcolor
        self.border_color = ft.Colors.with_opacity(0.40, color)
        self.focused_bgcolor = self.bgcolor
        self.border_width = 0.4
        self.hover_color = self.bgcolor
        self.focused_border_width = self.border_width
        self.hint_style = ft.TextStyle(
            size=size,
            color=ft.Colors.with_opacity(0.40, color)
        )
        self.text_style = ft.TextStyle(
            size=size,
            color=ft.Colors.with_opacity(0.80, color)
        )
        self.password = password
        self.can_reveal_password = can_reavel_password
        self.keyboard_type = keyboard_type
        self.on_submit = on_submit
        self.on_change = on_change

class TextButton(ft.Container):
    def __init__(
        self,
        page: ft.Page,
        text: str,
        icon: ft.Icons = None,
        bgcolor: ft.Colors = None,
        font_weight: ft.FontWeight = ft.FontWeight.W_300,
        text_color: ft.Colors = ft.Colors.BLUE,
        icon_color: ft.Colors = ft.Colors.BLUE,
        on_click: ft.ControlEvent = None,
        on_hover: ft.HoverEvent = None
    ):
        super().__init__()
        self.page = page
        self.on_click = on_click
        self.on_hover = on_hover if on_hover else self.hover
        self.bgcolor = bgcolor
        self.text_color = text_color
        self.padding = ft.padding.only(left=6, top=2, bottom=2, right=6)
        self.content = ft.Row(controls=[], spacing=2)

        if icon:
            self.content.controls.append(
                ft.Icon(
                    name=icon,
                    color=icon_color if icon_color else self.text_color,
                    size=15
                )
            )
        
        if text:
            self.content.controls.append(
                Text(
                    value=text,
                    color=text_color,
                    size=12,
                    weight=font_weight
                )
            )
        
        self.icon_color = icon_color
    
    def hover(self, e: ft.HoverEvent):
        if e.data == 'true':
            for control in self.content.controls:
                if 'icon' in control._get_control_name():
                    control.color = ft.Colors.with_opacity(
                        opacity=0.8,
                        color=self.text_color if not self.icon_color else self.icon_color)
                
                elif 'text' in control._get_control_name():
                    control.color = ft.Colors.with_opacity(0.8, self.text_color)
        
        else:
            for control in self.content.controls:
                if 'icon' in control._get_control_name():
                    control.color=self.text_color if not self.icon_color else self.icon_color
                
                elif 'text' in control._get_control_name():
                    control.color = self.text_color
        
        e.page.update()
        
class ElevantedButton(ft.ElevatedButton):
    def __init__(
        self,
        text: str = None,
        icon: ft.Icons = None,
        text_color: ft.Colors = ft.Colors.WHITE,
        bgcolor: ft.Colors = ft.Colors.GREEN_600,
        on_click: ft.ControlEvent = None
    ):
        super().__init__()
        self.on_click = on_click
        self.text = text
        self.icon = icon
        self.icon_color = text_color
        self.bgcolor = bgcolor
        self.color = text_color
        self.height = 40
        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(
                radius=2
            )
        )

class Appbar(ft.AppBar):
    def __init__(
        self,
        page: ft.Page,
        title: str
    ):
        super().__init__()
        self.page = page
        self.title = Text(
            value=title,
            size=16,
            color=ft.Colors.WHITE,
            weight='normal'
        )
        self.toolbar_height = 40
        self.bgcolor = ft.Colors.GREEN_600
        self.actions = [
            ft.Container(
                content=ft.Row(
                    controls=[
                        ft.Container(
                            height=35,
                            width=35,
                            border_radius=60,
                            bgcolor=ft.Colors.with_opacity(0.80, 'white'),
                            alignment=ft.alignment.center,
                            content=Text(
                                value=page.data[0].upper(),
                                color=self.bgcolor,
                                size=16,
                                weight='bold'
                            )
                        )
                    ]
                ),
                padding=ft.padding.only(right=6)
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
        title: str,
        title_on_click: ft.ControlEvent = None,
        add_on_click: ft.ControlEvent = None,
        change_on_click: ft.ControlEvent = None,
        on_hover: ft.HoverEvent = None
    ):
        super().__init__()
        self.page = page
        self.content = ft.Row(
            controls=[
                TextButton(
                    page=page,
                    text=title,
                    font_weight='w700',
                    on_click=title_on_click,
                    on_hover=on_hover
                ),
                ft.Row(
                    controls=[
                        TextButton(
                            page=page,
                            text='Add',
                            icon=ft.Icons.ADD,
                            font_weight='w300',
                            on_click=add_on_click,
                            on_hover=on_hover
                        ),
                        TextButton(
                            page=page,
                            text='Change',
                            icon=ft.Icons.EDIT,
                            font_weight='w300',
                            on_click=change_on_click,
                            on_hover=on_hover
                        )
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

class Dropdown(ft.Dropdown):
    def __init__(
        self,
        hint_text: str,
        icon: ft.Icons = None,
        options: list[ft.dropdown.Option] = None,
        col: dict[str, float] = {'xs': 12},
        text_size: int = 13,
        color: ft.Colors = ft.Colors.BLACK,
        autofocus: bool = True,
        border_radius: float = 2,
        bgcolor: ft.Colors = ft.Colors.WHITE,
        height: float = 45,
        on_change: ft.ControlEvent = None
    ):
        super().__init__()
        self.col = col
        self.on_change = on_change
        self.options = options if options else []
        self.autofocus = autofocus
        self.prefix_icon = icon if icon else None
        self.hint_text = hint_text
        self.hint_style = ft.TextStyle(
            size=text_size,
            color=ft.Colors.with_opacity(0.40, color)
        )
        self.text_style = ft.TextStyle(
            size=text_size,
            color=ft.Colors.with_opacity(0.80, color)
        )
        self.height = height
        self.border_radius = border_radius
        self.col = col
        self.autofocus = autofocus
        self.bgcolor = bgcolor
        self.focused_bgcolor = self.bgcolor
        self.border_color = ft.Colors.with_opacity(0.40, color)
        self.focused_bgcolor = self.bgcolor
        self.border_width = 0.4
        self.hover_color = self.bgcolor
        self.focused_border_width = self.border_width

class AlertDialog(ft.AlertDialog):
    def __init__(
        self,
        page: ft.Page,
        title: str = None,
        title_color: ft.Colors = None,
        title_size: int = None,
        actions: list[ft.Container] = None
    ):
        super().__init__()
        self.page = page
        self.modal = True
        self.adaptive = True
        self.title = ft.Row(
            controls=[
                Text(
                    value=title,
                    color=title_color,
                    size=title_size
                ),
                ft.IconButton(
                    icon=ft.Icons.CLOSE,
                    icon_color=ft.Colors.RED,
                    icon_size=20,
                    on_click=self.close
                )
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
        self.actions = actions if actions else []
        self.shape = ft.RoundedRectangleBorder(
            radius=4
        )
        self.title_padding = ft.padding.only(
            left=8,
            right=4,
            top=8,
            bottom=8
        )
        self.content_padding = ft.padding.only(
            left=4,
            right=4,
            top=8,
            bottom=0
        )
        self.actions_padding = ft.padding.only(
            left=4,
            right=4,
            top=8,
            bottom=8
        )
        self.content = ft.Column(
            controls=[
                userfields_group := ft.ResponsiveRow(
                    controls=[
                        TextField(
                            hint_text='Username',
                            autofocus=True,
                            prefix_icon=ft.Icons.PERSON
                        ),
                        TextField(
                            hint_text='Email',
                            autofocus=False,
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
                            autofocus=False,
                            prefix_icon=ft.Icons.KEY,
                            password=True,
                            can_reavel_password=True
                        )
                    ]
                )
            ]
        )

        self.userfields_group = userfields_group
        self.page = page
        self.page.overlay.append(self)
        self.open = True
    
    def close(self, e: ft.ControlEvent):
        self.open = False
        e.page.update()
        self.page.overlay.remove(self)

class DateTime():
    def __init__(
        self
    ):
        self.__now = datetime.now()
        self.date = self.__now.strftime("%d/%m/%Y")
        self.hour = self.__now.strftime("%H:%M:%S")
