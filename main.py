import sys
import random


class Boad:
    def __init__(self, h, w):
        self.height, self.wide = h, w
        self.is_bomb = [[False for _ in range(w)] for _ in range(h)]
        self.cnt = [[0 for _ in range(w)] for _ in range(h)]

    def to_string(self, nums, bomb='b', sep=" ") -> str:
        s: list[str] = ["" for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.wide):
                c = " "
                if(self.is_bomb[y][x]):
                    c = bomb
                else:
                    c = nums[self.cnt[y][x]]
                s[y] += c

        return '\n'.join(s)

    def __str__(self) -> str:
        nums = [str(i) for i in range(9)]
        nums[0] = " "
        return self.to_string(nums)

    def to_discord_format(self) -> str:
        nums = ["blue_square", "one", "two", "three",
                "four", "five", "six", "seven", "eight"]
        nums = ["||:" + s + ":||" for s in nums]
        return self.to_string(nums, "||:bomb:||", sep="")

    def bomb_count(self):
        c = 0
        for y in range(self.height):
            for x in range(self.wide):
                if(self.is_bomb[y][x]):
                    c += 1
        return c

    def calc(self):
        for y in range(self.height):
            for x in range(self.wide):
                if not self.is_bomb[y][x]:
                    continue
                for ny in range(max(0, y-1), min(y+2, self.height)):
                    for nx in range(max(0, x-1), min(x+2, self.wide)):
                        self.cnt[ny][nx] += 1
        return self

    def generate_random(self, p):
        for y in range(self.height):
            for x in range(self.wide):
                if y == self.height/2 and x == self.wide/2:
                    continue
                if random.random() < p:
                    self.is_bomb[y][x] = True
        self.calc()
        return self


argv = sys.argv

probability = 0.1
try:
    height = int(sys.argv[1])
    wide = int(sys.argv[2])
    if(len(sys.argv) > 3):
        probability = int(sys.argv[3])

except ValueError:
    print("Usege: 高さ 幅 (爆弾生成率)")
    exit()


boad = Boad(height, wide)
boad.generate_random(probability)

print(boad)
print("爆弾の数:{}".format(boad.bomb_count()))
print(boad.to_discord_format())
