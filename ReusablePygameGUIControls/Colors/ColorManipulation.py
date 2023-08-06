class ColorManipulation:
    def __new__(cls, *args, **kwargs):
        raise TypeError(f'Instances of {cls.__name__} cannot be created')

    @staticmethod
    def adjust_color(color: tuple[int, int, int] | None, scale: float) -> tuple | None:
        """
        Adjusts the given RGB color tuple to create a lighter or darker variation.
        The scale parameter should be a value greater than 0.0.
        A scale factor of 1.0 will keep the original color.
        Values greater than 1.0 will lighten the color, and values less than 1.0 will darken it.

        Args:
            color (tuple | None): The RGB color represented as a tuple (red, green, blue) or None.
            scale (float): The scale factor to adjust the color intensity.

        Returns:
            tuple: The adjusted RGB color tuple.
            None: If passed color is None.
        """
        if color is None:
            return None

        if not isinstance(color, tuple) or len(color) != 3:
            raise ValueError("The color must be a tuple of three integers representing (red, green, blue).")

        if not all(isinstance(c, int) for c in color):
            raise ValueError("The color tuple must contain only integers.")

        if scale <= 0.0:
            raise ValueError("The scale factor must be greater than 0.0.")

        adjusted_color = tuple(min(255, max(0, int(c * scale))) for c in color)

        return adjusted_color
