# ToDoist Integration

Integration ToDoist app with Discord and implemented local voice bot interface.

## Table of content

- [ToDoist Integration](#todoist-integration)
  - [Table of content](#table-of-content)
  - [Discord Bot](#discord-bot)
    - [Env](#env)
  - [Voice Bot](#voice-bot)
    - [Env](#env-1)
  - [Author](#author)

## Discord Bot

### Env
Create file with all private data to connect ToDoist and Discord bot.

`.env`
```
db_root_user="..."
db_root_pass="..."

todoist_client_id="..."
todoist_client_secret="..."
todoist_scope="..."

discord_token="..."
```

## Voice Bot

### Env

```
export voice_access_token="..."
export voice_project_id=".."
```

## Author

Górka Mateusz
