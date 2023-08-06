from Windows.Window import Window


class MainMenuWindow(Window):

    def __init__(self, background_color: tuple[int, int, int] | None, background_image_path: str | None):
        super().__init__(background_color, background_image_path)
