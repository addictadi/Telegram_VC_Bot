HEROKU = false  # NOTE Make it false if you're not deploying on heroku.

# NOTE these values are for heroku.
if HEROKU:
    from os import environ

    API_ID = int(environ["API_ID"])
    API_HASH = environ["API_HASH"]
    SUDO_CHAT_ID = int(
        environ["SUDO_CHAT_ID"]
    )  # Chat where the bot will play the music.
    SUDOERS = list(
        int(x) for x in environ.get("SUDOERS", "").split()
    )  # Users which have special control over the bot.
    SESSION_STRING = environ["SESSION_STRING"]  # Check Readme for session
    ARQ_API_KEY = environ["ARQ_API_KEY"]

# NOTE Fill this if you are not deploying on heroku.
if not HEROKU:
    API_ID = 4860841
    API_HASH = "280cfd3515c63a6ba0d3423d4d1b4a3d"
    SUDO_CHAT_ID = -1001485605294
    SUDOERS = [1899168466]
    ARQ_API_KEY = "ZZLGQK-GZJFQV-EUTCTQ-AFEGMX-ARQ"
# don't make changes below this line
ARQ_API = "https://thearq.tech"
