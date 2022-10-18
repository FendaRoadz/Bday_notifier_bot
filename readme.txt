
README  version 0.1

                            DISCLAMER
                This is super early pre-alpha-beta-gamma
                version. It is half way working and development
                still in progress :)
    
    Bday_notifier_bot is a simple tool, that sends you a message, 
    who of your friends has a birthday today.
    
    Bot collects information about people from any public profile on vk.com
    and sends it to telegram.
    Private profiles doesn't implemented yet. Furthermore i even cannot 
    collect info about my personal friends :D
    
    For testing purposes i used some random public profile.

    In order to use this bot, you have to have vk api token, and i assume, 
    since i did not included telegram bot token, you need to make your own bot.
    
    You may have to setup virtual environment to correct usage of the bot. All packages listed
    in requirements.txt file in repository.

    The bot uses .env file as storage for environmental variables.

    There is 3 environmental variables stored in .env file, you need to provide:
        API_TOKEN - actual vk api token. You can find more info at dev.vk.com

        BOT_TOKEN - telegram bot token. You can find more at https://t.me/BotFather

        USER_ID - integer id of vk.com registered user, whos data will be parsed. 
        For example vk.com/id1 where 1 is an actual id. 
        Please pay attention, there is no public/private account check implemented yet, 
        so please be sure, user who you trying to parse, has public account.
        Otherwise you may have some errors.
        
    That information stored in env variables and imported with dotenv library.

    All sensetive information like vk api token and telegram bot token is not 
    represented in this repository.

    If there is any questions, please be kind and ask at:
    https://github.com/FendaRoadz/Bday_notifier_bot



