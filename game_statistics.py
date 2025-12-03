from constants import START_SCORE


class GameStatistics():
    """Класс для отслеживания статистики игры."""

    def __init__(self, ai):
        self.settings = ai.settings
        self.reset_statistics()
        self.game_active = False

    def reset_statistics(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""

        self.ships_left = self.settings.ship_limit
        self.score = START_SCORE
