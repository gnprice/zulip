
from zerver.lib.bulk_create import bulk_create_users

bulk_create_users(get_realm('zulip'),
                  {('welcome-bot@zulip.com', 'Welcome Bot', 'welcome-bot', True)},
                  UserProfile.DEFAULT_BOT)

bot = get_system_bot('welcome-bot@zulip.com')
bot.bot_owner = bot
bot.save()


bulk_create_users(get_realm('zulip'),
                  {('example-bot@zulip.com', 'Example Bot', 'example-bot', True)},
                  UserProfile.DEFAULT_BOT)
