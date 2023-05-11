label loop3:
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
    menu f3:
        "把它弄乾淨":
            narrator "你真他媽變態，他只是個小女孩，你居然要他幫你洗碗？"
            narrator "（你被强制重啓）"
            jump loop3
        "解釋一下你到底是誰":
            unicorn "哥哥你在説什麽呢？我就是你最愛的獨角獸妹妹啊！"
    menu:
        "也是，我到底在想什麽呢":
            you "獨角獸妹妹就是獨角獸妹妹啊！"
            jump f3
        "我看到了另一個你":
            unicorn "不可能的啊，這裏只有我們啊~"
    narrator "（你本來想追問，但突然你覺得...）"
    menu:
        "急屎":
            unicorn "好呀！我在這裏等你哦！對了快點準備一下！我們要去旅行咯！"
        "急尿":
            unicorn "好呀！我在這裏等你哦！對了快點準備一下！我們要去旅行咯！"
    scene BathroomVirtual
    menu f2:
        "你還想和獨角獸妹妹去旅行":
            narrator "（於是你和獨角獸妹妹去了旅行）"
            narrator "（回家後你睡了個好覺）"
            jump loop3
        "我只想他幫我做三文治":
            you "我只想他做我的三文治夾心<3"
            jump f2
        "照鏡子":
            narrator "（你還是覺得自己很樣衰）"
    you "鏡鏡這麽可愛，爲什麽要打歐鏡鏡！"
    narrator "（你看著馬桶裏的屎）"
    menu toilet:
        "你吃起了馬桶裏的屎":
            you "係...係鮑魚味的屎！"
            narrator "（你的視綫逐漸模糊）"
            jump loop2
        "你拿起了馬桶裏的屎":
            narrator "（去完厠所準備開門時聽到外面有奇怪的聲音）"
    scene roomnight
    narrator "（你打開門看見獨角獸妹妹的臉閃爍了一下）"
    unicorn "獨角獸妹妹：你出來了啊...哥哥。"
    narrator "（你察覺到獨角獸妹妹有點異樣）"
    menu:
        "你吃起了馬桶裏的屎":
            you "肚子好痛！"
            scene BathroomVirtual
            narrator "（你立即跑回厠所裏開始噴屎）"
            jump toilet
        "你把屎扔到獨角獸妹妹的臉上":
            unicorn "你好玩不玩，玩屎？！"
    narrator "（獨角獸妹妹的臉開始閃爍）"
    narrator "（獨角獸妹妹的臉變成Allen的臉）"
    you "你是？！"
    unicorn_allen "別看我的臉！你不能想起我的存在！"
    you "頭好痛！你做了什麽！"
    unicorn_allen "那是你的記憶要回來的前兆！"
    narrator "（一把飛刀插在了你的頭上）"
    unicorn_allen "只要你一直在循環裏..."
    narrator "（你的視綫逐漸模糊）"
    unicorn_allen "你就不用面對這殘酷的現實了。"
    scene blank
    jump loop4
    