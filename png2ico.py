from PIL import Image

logo = Image.open(r"image or image path.png")

logo.save(r"image or image path.ico", format='ICO',
          sizes=[(40, 40)])