label loop2:
    scene black
    narrator "（你醒了過來）"
    unicorn "哥哥.. 快起床啦！ >w<"
    scene room
    show ak47 with dissolve
    narrator "（你覺得自己已經扯過一次旗）"
    you "你 等我一下，我胯下的AK-47站起來了!"
    play sound "audio/Yamete.mp3"
    unicorn "哥哥你真壞! 你再這樣我就不理你了!"
    you "這樣的話呀.. 那你幫我..."
    menu f4:
        "把它弄乾淨":
            narrator "你真他媽變態"
            narrator "（你被强制重啓）"
            jump loop2
        "解釋一下你到底是誰":
            unicorn "哥哥你在説什麽呢？我就是你最愛的獨角獸妹妹啊！"
    menu:
        "也是，我到底在想什麽呢":
            you "獨角獸妹妹就是獨角獸妹妹啊！"
            jump f4
        "我看到了另一個你":
            unicorn "不可能的啊，這裏只有我們啊~"
    narrator "（你本來想追問，但突然你覺得...）"
    menu:
        "急屎":
            unicorn "好呀！我在這裏等你哦！對了快點準備一下！我們要去旅行咯！"
        "急尿":
            unicorn "好呀！我在這裏等你哦！對了快點準備一下！我們要去旅行咯！"
    scene BathroomVirtual
    menu f1:
        "你還想和獨角獸妹妹去旅行":
            narrator "（於是你和獨角獸妹妹去了旅行）"
            narrator "（回家後你睡了個好覺）"
            jump loop2
        "我只想他幫我做三文治":
            you "我只想他做我的三文治夾心<3"
            jump f1
        "照鏡子":
            narrator "（你覺得自己很樣衰）"
    menu:
        "我比G7靚仔":
            "Nah"
            jump f1
        "衰你老母，Plum肥過我老豆老母加埋Allen條J":
            narrator "（你很憤怒，於是你打破了鏡子）"
    narrator "（你看著地上的鏡片）"
    menu:
        "我真帥":
            "Nah"
            jump f1
        "拿起防身":
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
        "我是Allen":
            unicorn"是嗎...那麼..."
        "去你媽":
            unicorn"是嗎...那麼..."
    unicorn "只能重來了啊。"
    narrator "（你拿起鏡子碎片插入獨角獸妹妹的肩膀）"
    unicorn "獨角獸妹妹：啊~舒服~"
    unicorn "（獨角獸妹妹把碎片拔了出來）"
    unicorn "獨角獸妹妹：你還是要回去的，不像我，掉入屎坑出不來了。"
    narrator "（獨角獸妹妹把碎片插入你的喉嚨）"
    scene red
    narrator "（你的視綫逐漸模糊）"
    scene black
    jump loop3