from src.DiscordToDoist.DiscordClient import OnNotificationComponent


class OnComplete(OnNotificationComponent):
    async def process(self, event) -> None:
        print("DEBUG. On task complete!")
        print(event)
