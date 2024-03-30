# AtlantaVR Discord Bot
**AtlantaVR bot** is a Discord bot project for the AtlantaVR Discord server. It is written in Python using the [discord.py] library & API

## Available Commands

- `/lancer`: Launches a dice.
- `/events`: Shows the list of upcoming events.
- `/event_info`: Shows the details of an event.
- `/help`: Shows the list of available commands.
- `/ping`: Ping our bot.
- `$add`: create an RP event.
- ...

## Future Features

- **Ticket Support:** Create tickets for users to request support. [NOT IMPLEMENTED]
- **Moderation:** Basic server moderation commands.
- **User Information:** Get detailed information about a user. [NOT IMPLEMENTED]
- **Entertainment:** Fun commands for user engagement.

## Configuration & Setup

### Basic Setup

1. Clone the repository: `git clone git@github.com:EliasJHL/AtlantaVR.git`
2. Install required packages: `pip install -r requirements.txt`
3. Create a `data.json` file with your bot token and version:

   ```json
   {
       "token": "YOUR_BOT_TOKEN_HERE",
       "version": "YOUR_VERSION",
       "server": "SERVER NAME",
       "status": 1
   }
   
## Bot Configuration
### Basic configuration
- **Prefix**: The bot command prefix is set to $ by default and can be changed in the bot's configuration file.
- **Server-specific Configuration**: Certain features may require specific configurations that can be adjusted in the bot's code

## Usage & Running
### Running the bot
    python3 main.py
### Running the web client
    python3 website/online_db.py
## Contact
For any inquiries or suggestions, contact me via Discord : `helias5605`.

©2024 AtlantaVR | Version: **V0.1.2 alpha**
