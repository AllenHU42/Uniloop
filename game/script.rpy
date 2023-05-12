# 您可以在此編寫遊戲的腳本。

# image命令可用於定義一個圖像。
# eg. image eileen happy = "eileen_happy.png"
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
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #
# define命令可定義遊戲中出現的角色名稱與對應文本顏色。
define you = Character('你', color="#ffffff")
define narrator = Character('旁白', color="#ffffff")
define unicorn = Character('獨角獸妹妹', color="#960e96")
define unicorn_allen = Character('獨角獸妹妹', color="#250daf")
image unicorn_normal:
    "unicorn.png"
image unicorn_weird:
    "unicorn_weird.png"
image unicorn_weird_2:
    "unicorn_weird_2.png"
image unicorn_weird_3:
    "unicorn_weird_3.png"
image unicorn_weird_4:
    "unicorn_weird_4.png"
image unicorn_weird_5:
    "unicorn_weird_5.png"
# 遊戲從這裡開始。
label start:
    jump wake_up
