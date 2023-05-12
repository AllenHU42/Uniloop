image room:
    "room_bg.png"
image flooding:
    "flooding.jpg"
image in_sky:
    "in_sky.webp"
    zoom 2
image plane_inside:
    "plane_bg.png"
    zoom 2  
image plane_explosion:
    "plane_explosion.webp"
    zoom 3.1
image jumping_out_plane:
    "jumping_out_plane.webp"
    zoom 5
image electronic_room:
    "electronic_room.jpg"
    zoom 2
image ak47:
    rotate 45
    zoom 0.4
    xalign -10
    "ak47.png"
image joe:
    "joe.png"
    zoom 1.5
image mbappe:
    "mbappe.png"
    zoom 1.5
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
define joe = Character('joe Mama', color="#97abe2")


init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,time,child,add_sizes=True,**properties)

        Shake = renpy.curry(_Shake)
    #


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
            play sound "audio/fart.mp3"
            narrator "（你們慢慢起飛）"
    stop music fadeout 1.0
    scene sky with fade
    play sound "audio/whoosh.mp3"
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
    play sound "audio/eating.mp3"
    hide kinder zorder 4 with dissolve
    show skinegg zorder 4 with dissolve
    unicorn "哥哥！你看我抽到什麼？是陳年型中式MK-420皮蛋69號！"
    play sound "audio/doraemon.mp3"
    narrator "（獨角獸妹妹把皮蛋丟到飛機上）"
    play sound "audio/throw.mp3"
    show skinegg at topright with ease
    hide skinegg
    narrator "（突然飛機機頭射出白色液體）"
    play sound "audio/ejeculate.ogg"
    show cum at topright zorder 5
    unicorn "登機~"
    narrator "（你跟著獨角獸妹妹從射出白色液體的洞口進入飛機）"
    scene plane_inside
    narrator "（你看見了沉睡小孩獵人Joe Biden和法國噴水龜Mbappe）"
    show joe with dissolve:
        linear 0.05
        xalign 0.6
        yalign 0.6
    show mbappe with dissolve:
        linear 0.05
        xalign 0.4
        yalign 0.6
    joe "呃呃...sfmfnjdizpkwondaskf...ndnsfj...ChinaXiJingPing..."
    narrator "（Mbappe開始噴水）"
    play sound "audio/water.mp3"
    narrator "（你感覺到被冒犯）"
    menu:
        "和他一起噴水":
            play sound "audio/water.mp3"
            narrator "（獨角獸妹妹鼓起了腮）"
    unicorn "明明是我先來的！"
    play sound "audio/laser.mp3"
    narrator "（獨角獸妹妹眼睛發出激光燒開駕駛艙的門）"
    pause 0.5
    scene plane_explosion
    narrator "（你趕緊追過去，發現飛機正在撞向巴黎鐵塔）"
    scene jumping_out_plane
    show joe zorder 2 with dissolve:
        linear 0.05
        xalign 0.35
        yalign 0.6
        rotate -20
    show bag:
        linear 0.05
        xalign 0.45
        yalign 0.3
        rotate -50
        xzoom -0.5
        yzoom 0.5
    narrator "（你趕緊衝出去看見Joe Biden背著降落傘）"
    menu:
        "搶了他的降落傘":
            show bag at right with MoveTransition(0.1)
            joe "FBUIDBIUUIODSVNUISDBVISVHODVXOWUD...BINGCHILLING！"
    scene in_sky
    narrator "（你跳出了飛機）"
    joe "FSDSHIVUVUSVSIOHWDIJFCODSN...PUSSYKENNYKAIWANXIAO！"
    #show joe, falling from top center to center.
    show joe:
        xalign 0.5
        yalign -100
    show joe at center with MoveTransition(5)
    narrator "（Joe Biden撞在你身上）"
    #shake joe
    show joe at Shake((0.6, 1.0, 1.0, 1.0), 5.0, dist=55)  
    narrator "（你拼命甩開Joe Biden）"
    #unicorn go push joe away
    show unicorn_normal:
        xalign 2.0
        yalign 0.0
        rotate -30
    pause 0.1
    show unicorn_normal at center with MoveTransition(0.5)
    pause 0.1
    show joe at left with MoveTransition(0.5)
    narrator "（獨角獸妹妹趕了過來，一把扯開Joe Biden）"
    joe "FNISDOIFWXOVWDUSCIBODCSDN...KIDPUSSY！"
    narrator "（Joe Biden想去聞獨角獸妹妹）"
    show joe at center with MoveTransition(0.5)
    show unicorn_normal at right with MoveTransition(0.5):
        rotate 0
        yalign 0.5
    menu:
        "和他一起聞":
            unicorn "別聞啦!! 討厭! >////<"
            #good end
        "反過來聞他的格嘞底":
            joe "啊哈.."
    narrator "（Joe Biden突然忘記了自己生存的意義）"
    joe "呃..."
    hide joe
    hide unicorn_normal
    show bag at center
    narrator "（你趁機打開降落傘）"
    narrator "（你發現Joe Biden的降落傘只是普通的書包）"
    scene flooding
    narrator "（你嚇到瀨尿，由於太久沒屙過尿，尿液的量包裹了整個法國並造成了史上最大型的水浸）"
    narrator "（突然閃過一個畫面）"
    scene electronic_room
    narrator "（你像是在一個駕駛艙裏）"
    scene flooding
    narrator "（你不斷下沉）"
    narrator "（你的視線逐漸模糊）"
    jump loop1
