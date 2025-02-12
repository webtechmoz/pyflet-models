from views.home import ft, Home, asyncio
from views.login import Login
from views.dashboard import Dashboard

def main(page: ft.Page):
    page.title = 'project title'
    page.route = '/admin/dashboard'
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

    def router(route: str):
        page.views.clear()

        if page.route == '/':
            page.views.append(home)
        
        elif page.route == '/admin/login':
            page.views.append(Login(page=page))
        
        elif page.route in ['/admin' ,'/admin/dashboard']:
            if page.data:
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