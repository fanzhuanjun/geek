import os

def replacetext(filename, a, b):
    with open(filename, encoding='utf-8') as f:
        text = f.read()
    newtext = text.replace(a, b)
    return newtext

def writeresult(text, newtitle, newfilepath):
    with open(f'{newfilepath}{newtitle}.md', 'a', encoding='utf-8') as f:
        f.write(text)


def main(filepath, a, b, newfilepath='C:/blog/post/'):
    files = [file for file in os.listdir(filepath) if file[-3:] == '.md' ]
    if filepath[-1] != '/':
        filepath += '/'
    for file in files:
        mdfile = filepath + file
        # filetitle = file[:-3]
        text = replacetext(mdfile, a, b)
        writeresult(text, file[:-3], newfilepath)
    print('done')

filepath = 'C:/blog/geek/scrape'
a='"myimages\\'
b='"https://github.com/fanzhuanjun/fanzhuanjun.github.io/raw/master/myimages/'

if __name__ == "__main__":
    main(filepath, a=a, b=b)
