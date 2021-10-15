from PIL import Image, ImageFont, ImageDraw


def combine_horizontally(image_paths):
    images = [Image.open(i) for i in image_paths]
    widths, heights = zip(*(i.size for i in images))

    gap_length = 50

    total_width = sum(widths) + (len(widths) - 1) * gap_length
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for i in images:
        new_im.paste(i, (x_offset, 0))
        x_offset += i.size[0] + gap_length

    new_im.show()


def apply_player():
    name = 'Trae\nYoung'
    position = 'PG'
    template_image = Image.open('assets/templates/hawks_template.png')
    player_image = Image.open('assets/images/2021_starters/Trae_Young.jpg')
    player_image.paste(template_image, (0, 0), template_image)
    font_size = 50
    font = ImageFont.truetype(
        'assets/fonts/rockwell_extra_bold.ttf',
        font_size
    )
    while font.getsize(name)[0] > 550:
        font_size -= 1
        font = ImageFont.truetype(
            'assets/fonts/rockwell_extra_bold.ttf',
            font_size
        )
    font_width, font_height = font.getsize(name)
    text_height_offset = 118 - font_height
    draw = ImageDraw.Draw(player_image)
    draw.text((190, 848 + text_height_offset), name, font=font, fill='#1c1a1a')
    position_font = ImageFont.truetype(
        'assets/fonts/rockwell_extra_bold.ttf',
        25
    )
    draw.text((190, 865), position, font=position_font, fill='#1c1a1a')
    player_image.show()


image_paths = ['assets/images/lbj.jpg', 'assets/images/michael-jordan.jpg']


if __name__ == '__main__':
    apply_player()
