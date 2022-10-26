from src.Discord.DiscordClient import OnNotificationComponent


class OnComplete(OnNotificationComponent):
    async def process(self, event) -> None:
        print("DEBUG. On task complete!")
        print(event)
