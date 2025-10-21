class GameStatistics():
    """Класс для отслеживания статистики игры."""

    def __init__(self, ai):
        self.settings = ai.settings
        self.reset_statistics()

    def reset_statistics(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""

        self.ships_left = self.settings.ship_limit
