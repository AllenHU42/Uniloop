image room:
    "room_bg.png"
image ak47:
    rotate 45
    zoom 0.4
    xalign -10
    "ak47.png"
label wake_up:
    scene black
    you "頭....很沉...."
    scene room
    you "這裏是..."
    show unicorn_normal at center
    unicorn "哥哥.. 快起床啦！ >w<"
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
    hide unicorn_normal with dissolve
    you "呼，她總算走了，我現在只好去看AKB48來解決我的AK-47了"

