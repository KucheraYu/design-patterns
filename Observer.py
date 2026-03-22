from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, channel_name: str, video_title: str):
        pass

class YouTubeChannel:
    def __init__(self, name: str):
        self.name = name
        self._subscribers = []
        self._latest_video = ""

    def subscribe(self, observer: Observer):
        if observer not in self._subscribers:
            self._subscribers.append(observer)
            print(f"[{self.name}] Новий підписник))")

    def unsubscribe(self, observer: Observer):
        if observer in self._subscribers:
            self._subscribers.remove(observer)
            print(f"[{self.name}] Підписник відписався((")

    def notify_subscribers(self):
        for subscriber in self._subscribers:
            subscriber.update(self.name, self._latest_video)

    def release_video(self, video_title: str):
        print(f"\nКАНАЛ {self.name} ВИПУСТИВ НОВЕ ВІДЕО: '{video_title}'")
        self._latest_video = video_title
        self.notify_subscribers()



class UserSubscriber(Observer):
    def __init__(self, username: str):
        self.username = username

    def update(self, channel_name: str, video_title: str):
        print(f"Push-сповіщення для {self.username}: На каналі {channel_name} вийшло відео '{video_title}'")

class TelegramBot(Observer):
    def __init__(self, bot_name: str):
        self.bot_name = bot_name

    def update(self, channel_name: str, video_title: str):
        print(f"{self.bot_name} надсилає повідомлення в групу: Нове відео '{video_title}' від {channel_name}.")

if __name__ == "__main__":
    sims_channel = YouTubeChannel("CrazyMaizey")

    user_hryhoriy = UserSubscriber("Григорій")
    user_larysa = UserSubscriber("Лариса")
    user_antonina = UserSubscriber("Антоніна")

    news_bot = TelegramBot("VideoBot")

    sims_channel.subscribe(user_hryhoriy)
    sims_channel.subscribe(user_larysa)
    sims_channel.subscribe(user_antonina)
    sims_channel.subscribe(news_bot)

    sims_channel.release_video("How to survive only with cucumbers")
    print()
    print("Лариса відписується")
    sims_channel.unsubscribe(user_larysa)

    sims_channel.release_video("John Cena vs Benedict Cucumbers")