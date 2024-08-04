from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __eq__(self, other):
        if isinstance(other, str):
            return self.nickname == other

    def __contains__(self, item):
        return self.nickname == item

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        if isinstance(other, str):
            return self.title.lower() == other.lower()

    def __contains__(self, item):
        if isinstance(item, str):
            return item.lower() in self.title.lower()
        elif isinstance(item, Video):
            return item.title.lower() == self.title.lower()

    def __str__(self):
        return self.title


class UrTube:
    users_list = list()
    videos_list = list()

    def __init__(self, users=None, videos=None, current_user=None):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users_list:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        if not self.users_list:
            self.users_list.append(User(nickname, password, age))
            self.log_in(nickname, password)
        else:
            if nickname in self.users_list:
                print(f'Пользователь {nickname} уже существует')
                self.log_in(nickname, password)
            else:
                self.users_list.append(User(nickname, password, age))
                self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        if not self.videos_list:
            for arg in args:
                self.videos_list.append(arg)
        else:
            for arg in args:
                if not (arg in self.videos_list):
                    self.videos_list.append(arg)

    def get_videos(self, title):
        found_video = []
        for video in self.videos_list:
            if title in video:
                found_video.append(video.title)
        return found_video

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в аккаунт, чтобы смотреть видео')
        else:
            for video in self.videos_list:
                if title == video:
                    if video.adult_mode and self.current_user.age < 18:
                        print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    else:
                        for i in range(1, video.duration + 1):
                            print(i, end=' ')
                            sleep(1)
                        print(' Конец видео')


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
