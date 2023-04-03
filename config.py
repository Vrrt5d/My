from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7047424")) #لا تغير هاذة القيمة
API_HASH = getenv("API_HASH", "bd5158c8ee60f23ed1f9a9856842b993")#لا تغير هاذة القيمة
BOT_TOKEN = getenv("BOT_TOKEN", "5665476982:AAEJ6XspFgVEjVY1FvZoQj8WfdAXQTR8utI")
SESSION_NAME = getenv("SESSION_NAME", "BAAAvh-Q7rBkCvvejylpNKcz4W5QCWQo0ERV9zGttKW_Kp8TwYzMh4mdUauv8aCxur9Lq_yilUyThBtThL_p9-T9lTFvrsTUfYc6UYXcAzUFT_gr1cmVZGdw-3pFHelqUQIE_4le_D9_RrxxV04kfPaNPvuiuQ2CuymKkeVsz74UmbfcU8O63JWsFviTT_vUp8AluSex6Ri7S6QGV0pkPjvvUFMFsxwBUJbkp0G5K5W-55RiiXFLT-0ULjUZ1zy-XNfasGoIlW5Wi27JJM8QDthpU7YS4c34sRYt_mVz-kjZq-3MoiuMWzypWL4oRbizDMrczkQF4yMH9gW_JwuKJY9iAAAAAU8D1jkA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "DG_44") # @ هنا ضع يوزر حسابك بدون 
ALIVE_NAME = getenv("ALIVE_NAME", "A L > 3 A L M Y") # هنا ضع اسم حسابك
BOT_USERNAME = getenv("BOT_USERNAME", "RTMU_BOT") # @ هنا ضع يوزر البوت بدون 
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR") 
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main") #لا تغير هاذة القيمة
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60")) #لا تغير هاذة القيمة
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "LRT_2") # @ هنا ضغ يوزر كروبك بدون 
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "LRT_0") # @ هنا ضغ يوزر قناتك بدون

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5620618809").split()))
                                             #هنا ضع ايدي المطور فوق و الاعلئ
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5620618809").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
