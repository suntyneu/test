class Gun(object):
    def __init__(self, magazine_clip):
        self.magazine_clip = magazine_clip

    def shoot(self):
        if self.magazine_clip.magazine_count == 0:
            print("没有子弹了")

        else:
            self.magazine_clip.magazine_count -= 1
            print("剩余子弹：%d" % self.magazine_clip.magazine_count)
