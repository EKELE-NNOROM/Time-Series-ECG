import pip
import subprocess


def install(packages):
    for package in packages:
        subprocess.call(['pip', 'install', package])

if __name__ == '__main__':
    package_list = ['gdown', 'pandas', ' watermark', 'arff2pandas']
    install(package_list)
