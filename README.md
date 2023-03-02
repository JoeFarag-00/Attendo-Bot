# Automated-Attendance-Bot

A Discord bot that helps you automate attendance from a attendance link or QR Code. I might have made this to skip classes.

You can find the tutorial about building a discord bot [here](https://www.youtube.com/watch?v=qRMVNtIF73c).

## Table of content

* [Requirements](#requirements)
* [Getting started](#getting-started)
* [Features & Commands](#features--commands)

## Requirements

- [Python](https://www.python.org/) - Version 3.0 or higher
- [Selenuim](https://www.selenium.dev/)

## Getting started

First, make sure you have all the required tools installed on your local machine then continue with these steps.

### Installation

```bash
# Clone the repository
git clone https://github.com/JoeFarag-00/Automated-Attendance-Bot

# Enter into the directory
cd discord-bot/

# Install the dependencies
npm install

# Configure Discord Bot Token
 echo "DISCORD_TOKEN='INSERT_YOUR_TOKEN_HERE'" > .env
```

### Required permissions

Make sure that your bot has the `applications.commands` application scope enabled, which can be found under the `OAuth2` tab on the [developer portal](https://discord.com/developers/applications/)

Enable the `Server Members Intent` and `Message Content Intent` which can be found under the `Bot` tab on the [developer portal](https://discord.com/developers/applications/)

### Configuration

After cloning the project and installing all dependencies, you need to add your Discord API token in the `.env` file.

### Changing the status

You can change the status of your discord bot by editing the `activity` and `activityType` variables inside of the `config.json` file. `activityType` needs to be set to an integer with the following [options](https://discord-api-types.dev/api/discord-api-types-v10/enum/ActivityType).

### Deploying commands
AttendLink: "Link" , "Member"

You can also use "All" as a member to add the attendance for all pre-recorded users.

<img src="./TestAssets/Attend.png">
