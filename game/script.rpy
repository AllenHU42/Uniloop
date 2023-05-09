# 您可以在此編寫遊戲的腳本。

# image命令可用於定義一個圖像。
# eg. image eileen happy = "eileen_happy.png"

# define命令可定義遊戲中出現的角色名稱與對應文本顏色。
define you = Character('你', color="#ffffff")
define narrator = Character('旁白', color="#ffffff")
define unicorn = Character('獨角獸妹妹', color="#960e96")
define unicorn_allen = Character('獨角獸妹妹', color="#250daf")
image unicorn_normal:
    "unicorn.png"
# 遊戲從這裡開始。
label start:
    jump wake_up
