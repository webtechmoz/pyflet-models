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

class DateTime():
    def __init__(
        self
    ):
        self.__now = datetime.now()
        self.date = self.__now.strftime("%d/%m/%Y")
        self.hour = self.__now.strftime("%H:%M:%S")
