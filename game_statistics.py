from constants import START_LEVEL, START_SCORE


class GameStatistics():
    """Класс для отслеживания статистики игры."""

    def __init__(self, ai):
        self.settings = ai.settings
        self.game_active = False
        self.record_score = START_SCORE

        self.reset_statistics()

    def reset_statistics(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""

        self.ships_left = self.settings.ship_limit
        self.score = START_SCORE
        self.level = START_LEVEL
