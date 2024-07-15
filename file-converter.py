import markdown
import sys
import os

args = sys.argv

def main():
    argValidationCheck(args)

    convertMarkdownToHTML(args)

# 引数チェック
def argValidationCheck(args):
    if len(args) < 4:
        raise ValueError("Usage: python3 file-converter.py <arg1> <arg2> <arg3>")
    if not os.path.isfile(args[2]):
        raise ValueError(f"inputfile: {args[2]} is not exist!")

# マークダウンからHTML形式へ変換
def convertMarkdownToHTML(args):
    with open(args[2], 'r') as input:
        contents = input.read()
    
    convertContents = markdown.markdown(contents)

    with open(args[3], 'w') as output:
        output.write(convertContents)


main()