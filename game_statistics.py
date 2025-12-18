from constants import START_LEVEL, START_SCORE


class GameStatistics():
    """Класс для отслеживания статистики игры."""

    def __init__(self, ai):
        self.settings = ai.settings
        self.game_active = False
        try:
            with open('score/record_score.txt') as filerecord:
                self.record_score = int(filerecord.read())
        except FileNotFoundError:
            print('Файл с рекордом не существет. Создан новый файл.')
            self.record_score = START_SCORE
        except ValueError:
            print('В файле с рекордом нет записи. Текущий рекорд 0.')
            self.record_score = START_SCORE

        self.reset_statistics()

    def reset_statistics(self):
        """Инициализирует статистику, изменяющуюся в ходе игры."""

        self.ships_left = self.settings.ships_limit
        self.score = START_SCORE
        self.level = START_LEVEL
