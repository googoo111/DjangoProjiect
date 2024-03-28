import random
from PIL import Image, ImageDraw,ImageFont,ImageFilter

def check_code(width=120, height=30, char_length=5, font_file='MAROLA__.TTF', font_size=28):
    code = []
    img = Image.new(mode='RGB', size=(width, height), color=(255, 255, 255))
    draw = ImageDraw.Draw(img, mode='RGB')

    def rndchar():
        """
        生成随机字母
        """
        return chr(random.randint(65, 90))

    def rndcolor():
        """
        生成随机颜色
        """
        return (random.randint(0,255), random.randint(10,255), random.randint(64,255))

    # 写文字
    font = ImageFont.truetype(font_file, font_size)
    for i in range(char_length):
        char = rndchar()
        code.append(char)
        h = random.randint(0, 4)
        draw.text((i*width / char_length, h), char, font=font, fill=rndcolor())

    # 写干扰点
    for i in range(40):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=rndcolor())

    img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return img, ''.join(code)
