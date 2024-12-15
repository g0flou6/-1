import time

class User:
    users = {}
    def __init__(self, nickname, password, age):
        self.nickname = str(nickname)
        self.password = hash(str(password))
        self.age = int(age)
        User.users[nickname] = self

    @staticmethod
    def find_by_nickname(nickname):
        return User.users[nickname] if nickname in User.users.keys() else -1


class Video:
    videos = []
    def __init__(self, title, duration, time_now = 0, adult_mode = False):
        self.title = str(title)
        self.duration = int(duration)
        self.time_now = 0
        self.adult_mode = False

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title

    def add(self):
        Video.videos.append(self)



class UrTube:
    def __init__(self):
        self.users = User.users
        self.videos = Video.videos
        self.current_user = None

    def log_in(self, nickname, password):
        user = User.find_by_nickname(nickname)
        if user == -1:
            print('Такого пользователя не существует.')
        else:
            if user.password == hash(password):
                self.current_user = user

    def register(self, nickname, password, age):
        if nickname in User.users.keys():
            print(f'Пользователь {nickname} уже существует.')
            pass
        else:
            user = User(nickname, password, age)
            self.log_in(nickname, password)

    def log_out(self):
        UrTube.current_user = None

    def add(self, *args):
        for video in args:
            if video in Video.videos:
                pass
            else:
                video.add()

    def get_video(self, word):
        find_videos = []
        lower_word = word.lower()
        for video in Video.videos:
            if lower_word in video.title.lower():
                find_videos.append(video.title)
        return find_videos

    def watch_video(self, title):
        if self.current_user is None:
            print('Для просмотра видео вам необходимо зайти в свой аккаунт!')
            return

        for video in Video.videos:
            if video.title == title:
                if (video.adult_mode and self.current_user.age >= 18) or not video.adult_mode:
                    while video.time_now <= video.duration:
                        print(video.time_now)
                        video.time_now += 1
                        time.sleep(1)
                    print('Конец видео.')
                    break
                else:
                    print('Пользователь должен быть старше 18 лет.')





ur = UrTube()
ur.register('Maxim', 'Maxim_6_', 21)
print(ur.current_user.nickname)
ur.register('Olesya', 'Olesya_7_', 21)
print(ur.current_user.nickname)
v1 = Video('Видео1', 10, adult_mode= True)
ur.add(v1)
print(User.users)












