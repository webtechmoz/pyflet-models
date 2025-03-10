from views.public.home import ft, Home, asyncio
from views.public.login import Login
from views.public.dashboard import Dashboard

def main(page: ft.Page):
    page.title = 'project title'
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            windows=ft.PageTransitionTheme.NONE,
            android=ft.PageTransitionTheme.NONE,
            ios=ft.PageTransitionTheme.NONE,
            linux=ft.PageTransitionTheme.NONE,
            macos=ft.PageTransitionTheme.NONE,
        )
    )

    home = Home(page=page)
    private_routes: list[str] = [
        '/admin',
        '/admin/dashboard'
    ]

    def router(route: str):
        page.views.clear()

        if page.route == '/':
            page.views.append(home)
        
        elif page.route == '/admin/login':
            page.views.append(Login(page=page))
        
        elif page.route in private_routes:
            if page.data:
                if page.route == '/admin/dashboard':
                    page.views.append(Dashboard(page=page))
            
            else:
                page.go('/admin/login')
        
        page.update()
    
    page.on_route_change = router
    page.go(page.route)
    asyncio.run(home.update_time(page))

if __name__ == '__main__':
    ft.app(
        target=main,
        view=ft.AppView.WEB_BROWSER,
        assets_dir='assets',
        upload_dir='assets',
        use_color_emoji=True
    )