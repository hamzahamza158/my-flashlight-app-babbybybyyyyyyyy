import sys
from flet import *

def main(app: Page):
    app.title = 'Flash'
    app.scroll = 'auto'
    app.window.top = 1
    app.window.left = 800
    app.window.width = 500
    app.window.height = 750
    app.bgcolor = Colors.WHITE
    app.theme_mode = ThemeMode.LIGHT

    # Check if running on a mobile device (Android/iOS) or PC
    is_mobile = sys.platform not in ["win32", "darwin", "linux"]

    # Only initialize mobile hardware if on an actual device
    fl = Flashlight() if is_mobile else None
    ph = PermissionHandler() if is_mobile else None

    if is_mobile:
        app.overlay.append(fl)
        app.overlay.append(ph)

    def open_app(e):
        if is_mobile:
            ph.open_app_settings()
        else:
            print("[PC Mode] Settings cannot be opened on a laptop.")

    def turn_on_flash(e):
        if is_mobile:
            fl.turn_on()
        else:
            print("[PC Mode] Flash turned ON (Simulated)")

    def turn_off_flash(e):
        if is_mobile:
            fl.turn_off()
        else:
            print("[PC Mode] Flash turned OFF (Simulated)")

    app.appbar = AppBar(
        title=Text('Welcome....', selectable=True, weight=FontWeight.W_200), 
        bgcolor="#f00e3f", 
        color='white', 
        actions=[IconButton(Icons.SETTINGS, on_click=open_app)]
    )

    app.add(
        Row([Text('\n\nFlash Light', size=31, color='black')], alignment=MainAxisAlignment.CENTER)
    )
    
    app.add(
        Row([Image('assets/logo.png', width=360,  fit='contain')], alignment=MainAxisAlignment.CENTER)
    )
    
    app.add(
        Row([
            Button('On', width=100, icon=Icons.PLAY_ARROW, 
                   style=ButtonStyle(bgcolor="#f00e3f", color='white', padding=15, shape=ContinuousRectangleBorder(radius=100)), 
                   on_click=turn_on_flash),
            Button('Off', width=100, icon=Icons.PLAY_DISABLED, 
                   style=ButtonStyle(bgcolor="#f00e3f", color='white', padding=15, shape=ContinuousRectangleBorder(radius=100)), 
                   on_click=turn_off_flash)
        ], alignment=MainAxisAlignment.CENTER)
    )
    
    app.add(
        Row([Text('\n\nHamza APPS 2026 ALL RIGHTS RESERVED', size=15, color='black')], alignment=MainAxisAlignment.CENTER)
    )

    app.update()

run(main)
