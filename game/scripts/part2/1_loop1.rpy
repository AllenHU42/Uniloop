image roomnight:
    "Room_Night.jpg"
    zoom 1.2
image BathroomVirtual:
    "Bathroom_night.jpg"
    zoom 1.3
    xalign -10
image red:
    "Red.jpg"
image BathroomReal:
    "Bathroom_real.jpg"
image Apocalypse:
    "Apocalypse.jpg"
image electronicroom:
    "electronic_room.jpg"
image realroom:
    "Real_Room.jpg"
label loop1:
    scene black
    unicorn "哥哥.. 快起床啦！ >w<"
    scene room
    narrator "（你看著獨角獸妹妹時扯了旗）"
    show ak47 with dissolve
    you "你 等我一下，我胯下的AK-47站起來了！"
    play sound "audio/Yamete.mp3"
    unicorn "獨角獸妹妹: 哥哥你真壞! 你再這樣我就不理你了！"
    you "這樣的話呀.. 那你幫我..."
    menu:
        "把東西弄出來吧":
            unicorn "好吧... 既然這是哥哥的要求的話.. 那我.."
        "把它弄乾淨":
            unicorn "好吧... 既然這是哥哥的要求的話.. 那我.."
    unicorn "那我只好幫你洗碗弄乾淨吧！"
    narrator "（突然你覺得...）"
    unicorn "哥哥，你要去哪裏呀？"
    menu:
        "急屎":
            "好呀！我在這裏等你哦！對了快點準備一下！我們要去旅行咯！"
        "急尿":
            "好呀！我在這裏等你哦！對了快點準備一下！我們要去旅行咯！"
    scene BathroomVirtual
    narrator "（你總覺得類似的事情發生過一次）"
    narrator "（你突然覺得很可疑）"
    unicorn "好了嗎？哥哥 …"
    menu:
        "你還想和獨角獸妹妹去旅行":
            narrator "（於是你和獨角獸妹妹去了旅行）"
            narrator "（回家後你睡了個好覺）"
            jump loop1
        "我只想他幫我做三文治":
            narrator "（去完厠所準備開門時聽到外面有奇怪的聲音）"
    scene roomnight
    narrator "（你打開門看見獨角獸妹妹的臉閃爍了一下）"
    unicorn "你出來了啊...哥哥。"
    you "（你察覺到獨角獸妹妹有點異樣）"
    menu:
        "你怎麼了？":
            unicorn "你不想和我去旅行嗎...哥哥？"
        "你還好嗎？":
            unicorn "你不想和我去旅行嗎...哥哥？"
    menu:
        "我比較想和你媽去旅行":
            unicorn"是嗎...那麼..."
        "去你媽":
            unicorn"是嗎...那麼..."
    unicorn "只能重來了啊。"
    narrator "（你看見胸口被插了一刀）"
    scene red #shake screen here#
    menu:
        "啊~舒服~":
            narrator "（獨角獸妹妹拔出刀）"
        "你媽死了":
            narrator "（獨角獸妹妹拔出刀）"
    narrator "（你的視綫逐漸模糊）"
    scene black
    jump loop2
        
        
