from LineObject import LineObject
import argparse
import sys

def append_to_jsonl(jsonl, line):
    jsonl.append(line)
def get_jsonl(jsonl):
    ans = ""
    for each in jsonl:
        ans += each.__str__()
    return '{\n' + ans + '}'

def create():
    jsonl = []
    while True:
        print('PROMPT: ', file=sys.stderr,end="")
        p = input()
        if not p:
            break
        print('COMPLETION: ', file=sys.stderr, end="")
        c = input()
        o = LineObject(p,c)
        append_to_jsonl(jsonl, o)
    print(get_jsonl(jsonl))


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prompt-end',default= f'\n\n###\n\n')
    parser.add_argument('-c','--completion-end', default = '###')
    args = parser.parse_args()
    LineObject.PEND = args.prompt_end
    LineObject.CEND = args.completion_end
    create()

    
