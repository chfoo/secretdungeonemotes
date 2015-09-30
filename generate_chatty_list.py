import glob
import os


def main():
    for path in sorted(glob.glob('images/*.png')):
        if '@' in path:
            continue

        filename = os.path.basename(path)
        emote_str = os.path.splitext(filename)[0]

        print('{}\temotes/sde/{}'.format(emote_str, filename))


if __name__ == '__main__':
    main()
