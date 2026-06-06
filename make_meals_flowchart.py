from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(r"C:\Users\tong'tong\Documents\Obsidian Vault\women_daily_meals_flowchart_cn.png")
W, H = 1800, 1250


def get_font(size):
    for candidate in (
        r"C:\Windows\Fonts\msyh.ttc",
        r"C:\Windows\Fonts\simhei.ttf",
        r"C:\Windows\Fonts\simsun.ttc",
    ):
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


img = Image.new("RGB", (W, H), "#fbfaf6")
d = ImageDraw.Draw(img)

f_title = get_font(58)
f_sub = get_font(30)
f_h = get_font(34)
f_body = get_font(26)
f_small = get_font(23)

colors = {
    "ink": "#24302f",
    "muted": "#66716f",
    "green": "#77a878",
    "blue": "#7aa6b7",
    "pink": "#d98b96",
    "gold": "#d0a84f",
    "line": "#d8d1c4",
    "softgreen": "#edf6ed",
    "softblue": "#eef6f8",
    "softpink": "#faeef1",
    "softgold": "#fbf4df",
}


def rounded_box(xy, fill, outline=None, radius=24, width=3):
    d.rounded_rectangle(
        xy,
        radius=radius,
        fill=fill,
        outline=outline or colors["line"],
        width=width,
    )


def center_text(text, box, font_obj, fill=None):
    fill = fill or colors["ink"]
    bbox = d.textbbox((0, 0), text, font=font_obj)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = box[0] + (box[2] - box[0] - tw) / 2
    y = box[1] + (box[3] - box[1] - th) / 2 - 2
    d.text((x, y), text, font=font_obj, fill=fill)


def wrap_text(text, max_width, font_obj):
    lines = []
    for para in text.split("\n"):
        current = ""
        for ch in para:
            test = current + ch
            if d.textlength(test, font=font_obj) <= max_width:
                current = test
            else:
                if current:
                    lines.append(current)
                current = ch
        if current:
            lines.append(current)
    return lines


def draw_multiline(text, x, y, max_width, font_obj, fill=None, line_gap=8):
    fill = fill or colors["ink"]
    for line in wrap_text(text, max_width, font_obj):
        d.text((x, y), line, font=font_obj, fill=fill)
        y += font_obj.size + line_gap
    return y


def arrow(x1, y1, x2, y2, color=None):
    import math

    color = color or colors["muted"]
    d.line((x1, y1, x2, y2), fill=color, width=5)
    angle = math.atan2(y2 - y1, x2 - x1)
    for a in (angle + 2.55, angle - 2.55):
        d.line(
            (x2, y2, x2 + 18 * math.cos(a), y2 + 18 * math.sin(a)),
            fill=color,
            width=5,
        )


center_text("女性每日三餐饮食改善流程图", (0, 36, W, 110), f_title)
center_text(
    "目标：稳血糖、补蛋白、护骨骼、照顾经期与长期代谢",
    (0, 120, W, 165),
    f_sub,
    colors["muted"],
)

rounded_box((520, 205, 1280, 350), colors["softgold"], colors["gold"])
center_text("每餐基础公式", (520, 215, 1280, 265), f_h)
center_text(
    "半盘蔬果 + 1/4优质蛋白 + 1/4主食 + 少量健康脂肪",
    (520, 275, 1280, 335),
    f_sub,
)

meal_boxes = [
    (
        "早餐",
        "稳血糖，别只吃纯碳水\n燕麦/全麦/杂粮粥 + 鸡蛋/无糖酸奶/豆浆 + 水果\n例：燕麦牛奶粥 + 水煮蛋 + 苹果",
        (95, 435, 555, 690),
        colors["softblue"],
        colors["blue"],
    ),
    (
        "午餐",
        "吃够蔬菜和蛋白\n杂粮饭/红薯/荞麦面 + 鱼虾/鸡肉/豆腐 + 两种蔬菜\n例：杂粮饭 + 清蒸鱼 + 西兰花蘑菇 + 番茄蛋汤",
        (670, 435, 1130, 690),
        colors["softgreen"],
        colors["green"],
    ),
    (
        "晚餐",
        "清淡但不要不吃\n少量主食 + 豆腐/虾/鸡蛋/鱼 + 大份蔬菜汤\n例：红薯 + 虾仁炒青菜 + 豆腐汤",
        (1245, 435, 1705, 690),
        colors["softpink"],
        colors["pink"],
    ),
]

for title, body, xy, fill, outline in meal_boxes:
    rounded_box(xy, fill, outline)
    center_text(title, (xy[0], xy[1] + 18, xy[2], xy[1] + 72), f_h)
    draw_multiline(body, xy[0] + 30, xy[1] + 92, xy[2] - xy[0] - 60, f_body)

arrow(555, 562, 670, 562)
arrow(1130, 562, 1245, 562)

rounded_box((95, 770, 830, 1095), "#ffffff")
d.text((135, 805), "女性重点营养", font=f_h, fill=colors["ink"])
nutrients = [
    ("铁", "月经期更要注意：瘦红肉、贝类、蛋黄、豆类、菠菜；搭配维C更好吸收。"),
    ("钙 + 维生素D", "牛奶、酸奶、强化豆奶、豆腐、小鱼、绿叶菜；适当日晒。"),
    ("优质脂肪", "坚果、橄榄油、牛油果、深海鱼，支持心血管和激素健康。"),
    ("膳食纤维", "蔬菜、水果、豆类、全谷物，帮助肠道、饱腹感和血糖稳定。"),
]
y = 858
for key, value in nutrients:
    d.ellipse((135, y + 6, 153, y + 24), fill=colors["gold"])
    d.text((168, y), f"{key}：", font=f_body, fill=colors["ink"])
    y = draw_multiline(value, 245, y, 530, f_small, colors["muted"], 6) + 10

rounded_box((970, 770, 1705, 1095), "#ffffff")
d.text((1010, 805), "从今天开始的执行顺序", font=f_h, fill=colors["ink"])
steps = [
    "1. 每餐先确认有没有蛋白质。",
    "2. 每天至少吃两大份蔬菜，颜色尽量多。",
    "3. 把一部分白米白面换成杂粮、薯类或玉米。",
    "4. 饮料优先白水、无糖茶、无糖豆浆，少奶茶甜饮。",
    "5. 不追求完美，先连续坚持两周再微调。",
]
y = 865
for step in steps:
    d.rounded_rectangle(
        (1010, y - 6, 1042, y + 26),
        radius=8,
        fill=colors["softgreen"],
        outline=colors["green"],
        width=2,
    )
    d.text((1018, y - 2), "✓", font=f_small, fill=colors["green"])
    y = draw_multiline(step, 1060, y - 3, 570, f_body, colors["ink"], 6) + 12

rounded_box((230, 1140, 1570, 1210), "#f7f2ea", radius=18, width=2)
center_text(
    "如有贫血、月经量大、备孕/怀孕、胃肠病、甲状腺问题或正在减脂，建议按个人情况再细化。",
    (230, 1140, 1570, 1210),
    f_small,
    colors["muted"],
)

img.save(OUT)
print(OUT)
