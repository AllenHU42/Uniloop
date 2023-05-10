image room:
    "room_bg.png"
image ak47:
    rotate 45
    zoom 0.4
    xalign -10
    "ak47.png"
image joe:
    "joe.png"
image sky:
    "sky.jpg"
image plane:
    yoffset -100
    zoom 1.5
    "plane.png"
image kinder:
    yoffset -200
    "kinder.png"
image skinegg:
    yoffset -240
    zoom 0.5
    "skinegg.png"
image cum:
    yoffset 200
    zoom 0.3
    "cum.png"
transform cum:
    linear 0.2 xoffset -20 #move left 20 pixel in 0.2 seconds
    linear 0.2 xoffset +20 #move right 20 pixel in 0.2 seconds
    repeat 5 #repeat the above 5 times
define joe = Character('Joe Mama', color="#97abe2")
label wake_up:
    scene black
    you "頭....很沉...."
    scene room with fade
    you "這裏是..."
    show unicorn_normal at center
    play music "audio/room_bgm.mp3" volume 0.5
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
    show unicorn_normal at center with dissolve
    unicorn "對了快點準備一下！我們要去旅行咯"
    hide unicorn_normal with dissolve
    narrator "（你聽到是突發旅行，你感到很興奮）"
    show ak47 at offscreenleft with moveoutbottom
    scene black
    narrator "Some time later"
    scene room
    show unicorn_normal
    unicorn "那麼我們要出發咯~"
    show unicorn_normal at top with moveouttop
    narrator "（獨角獸妹妹左脚踩右脚慢慢升起）"
    menu:
        "學她左脚踩右脚":
            narrator "（你們慢慢起飛）"
        "用屁升天":
            narrator "（你們慢慢起飛）"
    stop music fadeout 1.0
    scene sky with fade
    show unicorn_normal at left zorder 3
    play music "audio/Empty_Train.mp3"
    unicorn "哥哥快看！"
    narrator "（你順著獨角獸妹妹指的方向看）"
    show plane at right zorder 2 with dissolve
    narrator "（你看到了一架飛機）"
    unicorn "我們進去吧！"
    narrator "（獨角獸妹妹從裙子裏拿出Kinder出奇蛋）"
    show kinder
    narrator "（她把Kinder吃完）"
    hide kinder zorder 4 with dissolve
    show skinegg zorder 4 with dissolve
    unicorn "哥哥！你看我抽到什麼？是陳年型中式MK-420皮蛋69號！"
    narrator "（獨角獸妹妹把皮蛋丟到飛機上）"
    show skinegg at topright with ease
    hide skinegg
    narrator "（突然飛機機頭射出白色液體）"
    play sound "audio/water.mp3"
    show cum at topright zorder 5
    unicorn "登機~"
    narrator "（你跟著獨角獸妹妹從射出白色液體的洞口進入飛機）"
    narrator "（你看見了沉睡小孩獵人Joe Biden和法國噴水龜Mbappe）"
    Joe "呃呃...sfmfnjdizpkwondaskf…ndnsfj…ChinaXiJingPing…"
    narrator "（Mbappe開始噴水）"
    narrator "（你感覺到被冒犯）"
    menu:
        "和他一起噴水":
            narrator "（獨角獸妹妹鼓起了腮）"
    unicorn "明明是我先來的！"
    narrator "（獨角獸妹妹眼睛發出激光燒開駕駛艙的門）"
    narrator "（你趕緊追過去，發現飛機正在撞向巴黎鐵塔）"
    narrator "（你趕緊衝出去看見Joe Biden背著降落傘）"
    menu:
        "搶了他的降落傘":
            Joe "FBUIDBIUUIODSVNUISDBVISVHODVXOWUD…BINGCHILLING！"
    narrator "（你跳出了飛機）"
    Joe "FSDSHIVUVUSVSIOHWDIJFCODSN…PUSSYKENNYKAIWANXIAO！"
    narrator "（Joe Biden撞在你身上）"
    narrator "（你拼命甩開Joe Biden）"
    narrator "（獨角獸妹妹趕了過來，一把扯開Joe Biden）"
    Joe "FNISDOIFWXOVWDUSCIBODCSDN…KIDPUSSY！"
    narrator "（Joe Biden想去聞獨角獸妹妹）"
    menu:
        "和他一起聞":
            narrator "（Joe Biden用mabappe作為pokemon噴水龜）"
        "反過來聞他的格嘞底":
            narrator "（Joe Biden用mabappe作為pokemon噴水龜）"
    narrator "（你召喚了獨角獸妹妹）"
    narrator "（Joe Biden突然忘記了自己生存的意義）"
    Joe "呃..."
    narrator "（你趁機打開降落傘）"
    narrator "（你發現Joe Biden的降落傘只是普通的書包）"
    narrator "（你嚇到瀨尿，由於太久沒屙過尿，尿液的量包裹了整個法國並造成了史上最大型的水浸）"
    narrator "（突然閃過一個畫面）"
    narrator "（你像是在一個駕駛艙裏）"
    narrator "（你不斷下沉）"
    narrator "（你的視綫逐漸模糊）"
    jump loop1
