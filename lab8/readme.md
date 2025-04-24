# Игра Крестики Нолики
Реализовать игру при помощи GUI и с использование ОО парадигмы.

# Решение
```
# Импорт необходимых модулей из фреймворка Kivy
from kivy.app import App  # Базовый класс для создания приложений
from kivy.uix.gridlayout import GridLayout  # Макет для размещения виджетов в сетке
from kivy.uix.button import Button  # Виджет кнопки
from kivy.uix.label import Label  # Виджет текстовой метки
from kivy.uix.boxlayout import BoxLayout  # Линейный макет
from kivy.core.window import Window  # Работа с окном приложения
from kivy.properties import StringProperty, NumericProperty  # Специальные свойства для автоматического обновления UI
from kivy.uix.popup import Popup  # Всплывающее окно

# Собственные классы исключений для обработки ошибок игры
class TicTacToeException(Exception):
    """Базовый класс для пользовательских исключений игры"""
    pass

class CellAlreadyOccupied(TicTacToeException):
    """Исключение при попытке занять занятую клетку"""
    def __init__(self, row, col):
        self.row = row  # Сохраняем координаты строки
        self.col = col  # Сохраняем координаты столбца
        super().__init__(f"Клетка ({row}, {col}) уже занята")  # Сообщение об ошибке

class GameOver(TicTacToeException):
    """Исключение при попытке хода после завершения игры"""
    pass

# Класс, реализующий логику игры
class TicTacToeGame:
    def __init__(self):
        self.reset_game()  # Инициализация игры
    
    def reset_game(self):
        """Сброс игры в начальное состояние"""
        self.board = [['' for _ in range(3)] for _ in range(3)]  # Создаем пустое поле 3x3
        self.current_player = 'X'  # Первым ходит X
        self.game_over = False  # Флаг завершения игры
        self.winner = None  # Победитель (X, O или None при ничье)
    
    def make_move(self, row, col):
        """Обработка хода игрока"""
        if self.game_over:
            raise GameOver("Игра уже завершена")  # Нельзя ходить после окончания игры
        
        if self.board[row][col] != '':
            raise CellAlreadyOccupied(row, col)  # Клетка уже занята
        
        self.board[row][col] = self.current_player  # Записываем ход в поле
        
        if self.check_winner():  # Проверяем победу
            self.game_over = True
            self.winner = self.current_player
        elif self.is_board_full():  # Проверяем ничью
            self.game_over = True
        else:
            # Передаем ход другому игроку
            self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def check_winner(self):
        """Проверка всех возможных комбинаций для победы"""
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
        
        return False  # Победителя нет
    
    def is_board_full(self):
        """Проверка, заполнено ли все поле"""
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == '':  # Нашли пустую клетку
                    return False
        return True  # Все клетки заполнены

# Класс клетки игрового поля
class TicTacToeCell(Button):
    row = NumericProperty(0)  # Свойство для хранения номера строки
    col = NumericProperty(0)  # Свойство для хранения номера столбца
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Инициализация кнопки
        self.font_size = 40  # Размер шрифта символов
        self.bind(on_press=self.on_cell_click)  # Привязка обработчика нажатия
    
    def on_cell_click(self, instance):
        """Обработка клика по клетке"""
        app = App.get_running_app()  # Получаем экземпляр приложения
        try:
            app.game.make_move(self.row, self.col)  # Пытаемся сделать ход
            self.text = app.game.board[self.row][self.col]  # Отображаем символ
            app.update_game_status()  # Обновляем статус игры
            
            if app.game.game_over:  # Если игра завершена
                if app.game.winner:  # Есть победитель
                    app.show_popup(f"Игрок {app.game.winner} победил!")
                else:  # Ничья
                    app.show_popup("Ничья!")
        except TicTacToeException as e:  # Обработка ошибок
            app.show_error(str(e))

# Класс игрового поля
class TicTacToeBoard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Инициализация сетки
        self.cols = 3  # 3 колонки
        self.rows = 3  # 3 строки
        self.spacing = [5, 5]  # Расстояние между клетками
        self.padding = 10  # Отступы по краям
        
        # Создаем 9 клеток (3x3)
        for row in range(3):
            for col in range(3):
                cell = TicTacToeCell(row=row, col=col)  # Создаем клетку
                self.add_widget(cell)  # Добавляем клетку на поле

# Главный класс приложения
class TicTacToeApp(App):
    game_status = StringProperty("Ход: X")  # Текущий статус игры
    error_message = StringProperty("")  # Сообщение об ошибке
    
    def build(self):
        """Создание интерфейса приложения"""
        self.game = TicTacToeGame()  # Создаем экземпляр игры
        self.title = "Крестики-нолики"  # Заголовок окна
        
        # Главный контейнер (вертикальное расположение)
        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        
        # Метка статуса игры
        self.status_label = Label(text=self.game_status, size_hint=(1, 0.1), font_size=24)
        main_layout.add_widget(self.status_label)
        
        # Игровое поле
        self.board = TicTacToeBoard()
        main_layout.add_widget(self.board)
        
        # Кнопка сброса игры
        reset_button = Button(text="Новая игра", size_hint=(1, 0.1))
        reset_button.bind(on_press=self.reset_game)
        main_layout.add_widget(reset_button)
        
        # Метка для отображения ошибок
        self.error_label = Label(text=self.error_message, size_hint=(1, 0.1), 
                               color=(1, 0, 0, 1), font_size=16)
        main_layout.add_widget(self.error_label)
        
        return main_layout  # Возвращаем собранный интерфейс
    
    def update_game_status(self):
        """Обновление текста статуса игры"""
        if self.game.game_over:  # Игра завершена
            if self.game.winner:  # Есть победитель
                self.game_status = f"Победил: {self.game.winner}!"
            else:  # Ничья
                self.game_status = "Ничья!"
        else:  # Игра продолжается
            self.game_status = f"Ход: {self.game.current_player}"
        
        # Принудительное обновление текста метки
        self.status_label.text = self.game_status
    
    def show_error(self, message):
        """Отображение сообщения об ошибке"""
        self.error_message = message  # Устанавливаем текст ошибки
        self.error_label.text = message  # Обновляем метку
    
    def show_popup(self, message):
        """Создание всплывающего окна с результатом"""
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)
        content.add_widget(Label(text=message, font_size=24))  # Текст результата
        
        close_button = Button(text="Закрыть", size_hint=(1, 0.3))  # Кнопка закрытия
        content.add_widget(close_button)
        
        # Создаем всплывающее окно
        popup = Popup(title='Результат игры', content=content,
                     size_hint=(0.7, 0.4), auto_dismiss=False)
        
        close_button.bind(on_press=popup.dismiss)  # Закрытие по кнопке
        popup.open()  # Показываем окно
    
    def reset_game(self, instance):
        """Сброс игры и очистка поля"""
        self.game.reset_game()  # Сбрасываем состояние игры
        self.update_game_status()  # Обновляем статус
        self.error_message = ""  # Очищаем сообщение об ошибке
        self.error_label.text = ""
        
        # Очищаем все клетки на поле
        for cell in self.board.children:
            if isinstance(cell, TicTacToeCell):
                cell.text = ''

# Запуск приложения
if __name__ == '__main__':
    Window.size = (400, 500)  # Устанавливаем размер окна
    TicTacToeApp().run()  # Запускаем приложение
```
# Запуск
Для запуска запускаем файл main.py


# Результат
![image](https://github.com/user-attachments/assets/0deb6fb2-a36a-4c68-9cec-ad5c247e8f3d)
