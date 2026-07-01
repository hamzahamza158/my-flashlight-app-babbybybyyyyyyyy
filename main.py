from flet import *

def main(page: Page):
    page.title = "Flash"
    page.scroll = "auto"
    page.window.top = 1
    page.window.left = 800
    page.window.width = 500
    page.window.height = 750
    page.bgcolor = Colors.WHITE
    page.theme_mode = ThemeMode.LIGHT

    # Detect Android/iOS correctly
    is_mobile = page.platform in [PagePlatform.ANDROID, PagePlatform.IOS]

    if is_mobile:
        fl = Flashlight()
        ph = PermissionHandler()

        page.overlay.append(fl)
        page.overlay.append(ph)
    else:
        fl = None
        ph = None

    def open_app(e):
        if is_mobile:
            ph.open_app_settings()
        else:
            print("Settings are only available on mobile.")

    def turn_on_flash(e):
        if is_mobile:
            fl.turn_on()
        else:
            print("Flash ON (PC simulation)")

    def turn_off_flash(e):
        if is_mobile:
            fl.turn_off()
        else:
            print("Flash OFF (PC simulation)")

    page.appbar = AppBar(
        title=Text(
            "Welcome....",
            selectable=True,
            weight=FontWeight.W_200,
        ),
        bgcolor="#f00e3f",
        color="white",
        actions=[
            IconButton(Icons.SETTINGS, on_click=open_app)
        ],
    )

    page.add(
        Row(
            [Text("\n\nFlash Light", size=31, color="black")],
            alignment=MainAxisAlignment.CENTER,
        )
    )

    page.add(
        Row(
            [
                Image(
                    src="assets/logo.png",
                    width=360,
                    fit=ImageFit.CONTAIN,
                )
            ],
            alignment=MainAxisAlignment.CENTER,
        )
    )

    page.add(
        Row(
            [
                ElevatedButton(
                    "On",
                    width=100,
                    icon=Icons.PLAY_ARROW,
                    style=ButtonStyle(
                        bgcolor="#f00e3f",
                        color="white",
                        padding=15,
                        shape=ContinuousRectangleBorder(radius=100),
                    ),
                    on_click=turn_on_flash,
                ),
                ElevatedButton(
                    "Off",
                    width=100,
                    icon=Icons.PLAY_DISABLED,
                    style=ButtonStyle(
                        bgcolor="#f00e3f",
                        color="white",
                        padding=15,
                        shape=ContinuousRectangleBorder(radius=100),
                    ),
                    on_click=turn_off_flash,
                ),
            ],
            alignment=MainAxisAlignment.CENTER,
        )
    )

    page.add(
        Row(
            [
                Text(
                    "\n\nHamza APPS 2026 ALL RIGHTS RESERVED",
                    size=15,
                    color="black",
                )
            ],
            alignment=MainAxisAlignment.CENTER,
        )
    )

    page.update()


app(main)
