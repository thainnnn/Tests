# from ascii_magic import AsciiArt
# 
# my_art = AsciiArt.from_image('moon.jpg')
# my_art.to_terminal()

# from ascii_magic import AsciiArt
# from PIL import ImageEnhance
# 
# my_art = AsciiArt.from_image('moon.jpg')
# my_art.image = ImageEnhance.Brightness(my_art.image).enhance(0.2)
# my_art.to_terminal()

from ascii_magic import AsciiArt, Back

my_art = AsciiArt.from_image('moon.jpg')
my_art.to_html_file('moon.html', columns=300, monochrome=True)
# my_art.to_html_file('moon.html', columns=300, width_ratio=2, monochrome=True)
