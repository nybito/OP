from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.popup import Popup


class TicTacToeException(Exception):
    """Базовое исключение для игры Крестики-нолики"""
    pass


class CellAlreadyOccupied(TicTacToeException):
    """Исключение при попытке занять уже занятую клетку"""
    def __init__(self, row, col):
        self.row = row
        self.col = col
        super().__init__(f"Клетка ({row}, {col}) уже занята")


class GameOver(TicTacToeException):
    """Исключение при попытке сделать ход после завершения игры"""
    pass


class TicTacToeGame:
    """Логика игры Крестики-нолики"""
    def __init__(self):
        self.reset_game()
    
    def reset_game(self):
        """Сброс игры в начальное состояние"""
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.game_over = False
        self.winner = None
    
    def make_move(self, row, col):
        """
        Совершить ход
        :param row: строка (0-2)
        :param col: столбец (0-2)
        :raises CellAlreadyOccupied: если клетка уже занята
        :raises GameOver: если игра уже завершена
        """
        if self.game_over:
            raise GameOver("Игра уже завершена")
        
        if self.board[row][col] != '':
            raise CellAlreadyOccupied(row, col)
        
        self.board[row][col] = self.current_player
        
        if self.check_winner():
            self.game_over = True
            self.winner = self.current_player
        elif self.is_board_full():
            self.game_over = True
        else:
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        """Проверка наличия победителя"""
        # Проверка строк
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != '':
                return True
        
        # Проверка столбцов
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True
        
        # Проверка диагоналей
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        
        return False
    
    def is_board_full(self):
        """Проверка, заполнено ли все поле"""
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':
                    return False
        return True


class TicTacToeCell(Button):
    """Клетка игрового поля"""
    row = NumericProperty(0)
    col = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.font_size = 40
        self.bind(on_press=self.on_cell_click)
    
    def on_cell_click(self, instance):
        """Обработка нажатия на клетку"""
        app = App.get_running_app()
        try:
            app.game.make_move(self.row, self.col)
            self.text = app.game.board[self.row][self.col]
            app.update_game_status()
            
            if app.game.game_over:
                if app.game.winner:
                    app.show_popup(f"Игрок {app.game.winner} победил!")
                else:
                    app.show_popup("Ничья!")
        except TicTacToeException as e:
            app.show_error(str(e))


class TicTacToeBoard(GridLayout):
    """Игровое поле"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 3
        self.rows = 3
        self.spacing = [5, 5]
        self.padding = 10
        
        for row in range(3):
            for col in range(3):
                cell = TicTacToeCell(row=row, col=col)
                self.add_widget(cell)


class TicTacToeApp(App):
    """Главное приложение"""
    game_status = StringProperty("Ход: X")
    error_message = StringProperty("")
    
    def build(self):
        self.game = TicTacToeGame()
        self.title = "Крестики-нолики"
        
        # Главный макет
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Статус игры
        self.status_label = Label(text=self.game_status, size_hint=(1, 0.1), font_size=24)
        main_layout.add_widget(self.status_label)
        
        # Игровое поле
        self.board = TicTacToeBoard()
        main_layout.add_widget(self.board)
        
        # Кнопка сброса
        reset_button = Button(text="Новая игра", size_hint=(1, 0.1))
        reset_button.bind(on_press=self.reset_game)
        main_layout.add_widget(reset_button)
        
        # Метка для ошибок
        self.error_label = Label(text=self.error_message, size_hint=(1, 0.1), 
                               color=(1, 0, 0, 1), font_size=16)
        main_layout.add_widget(self.error_label)
        
        return main_layout
    
    def update_game_status(self):
        """Обновление статуса игры"""
        if self.game.game_over:
            if self.game.winner:
                self.game_status = f"Победил: {self.game.winner}!"
            else:
                self.game_status = "Ничья!"
        else:
            self.game_status = f"Ход: {self.game.current_player}"
        
        # Принудительное обновление текста метки
        self.status_label.text = self.game_status
    
    def show_error(self, message):
        """Показать сообщение об ошибке"""
        self.error_message = message
        self.error_label.text = message
    
    def show_popup(self, message):
        """Показать всплывающее окно с результатом игры"""
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content.add_widget(Label(text=message, font_size=24))
        
        close_button = Button(text="Закрыть", size_hint=(1, 0.3))
        content.add_widget(close_button)
        
        popup = Popup(title='Результат игры', content=content,
                     size_hint=(0.7, 0.4), auto_dismiss=False)
        
        close_button.bind(on_press=popup.dismiss)
        popup.open()
    
    def reset_game(self, instance):
        """Сброс игры"""
        self.game.reset_game()
        self.update_game_status()
        self.error_message = ""
        self.error_label.text = ""
        
        # Очищаем все клетки
        for cell in self.board.children:
            if isinstance(cell, TicTacToeCell):
                cell.text = ''


if __name__ == '__main__':
    Window.size = (400, 500)
    TicTacToeApp().run()
