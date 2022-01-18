import argparse
from PIL import Image
import os


def parse_arguments():
    """
    Parse command line arguments
    """
    parser = argparse.ArgumentParser(description='Resize pdf')
    parser.add_argument('input', help="The path of the input images")
    parser.add_argument('scale', type=int, help="Scale (from 1 -> 100 )")
    parser.add_argument('output', help="The path of the scaled images")
    args = parser.parse_args()
    return args.input, args.scale, args.output


def scale_imgs(input, scale, output):
    if not os.path.exists(output):
        print("creating directory: %s" % output)
        os.mkdir(output)

    for fname in os.listdir(input):
        fpath = os.path.join(input, fname)
        if os.path.isfile(fpath) and fname[-4:].lower() in ["jpeg", ".png", ".jpg", ".gif"]:
            image = Image.open(fpath)
            image.save(os.path.join(output, fname), quality=scale, optimize=True)
            print("saving .. %s" % fname)


if __name__ == '__main__':
    inp, sc, out = parse_arguments()
    scale_imgs(inp, sc, out)