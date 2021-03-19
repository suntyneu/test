
"""
人
类名：Person
属性：gun
行为：fire



枪
类名：gun
属性：magazine_clip
行为：shoot

弹夹
类名：MagazineClip
属性：magazine_count
"""

from person import Person
from gun import Gun
from magazine_clip import MagazineClip

magazine_clip = MagazineClip(6)
gun = Gun(magazine_clip)
per = Person(gun)

per.fire()
per.fire()
per.fire()
per.fire()
per.fire()
