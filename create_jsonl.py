from LineObject import LineObject
import argparse
import sys

def get_jsonl_from_list(jsonl,PEND,CEND):
    ans = ""
    for each in jsonl:
        ans += '{' + f'"prompt": "{each.prompt}{PEND}", "completion": "{each.completion}{CEND}"' + '}\n'
    return '{\n' + ans + '}'

def prompt_create_list():
    jsonl = []
    while True:
        print('PROMPT: ', file=sys.stderr,end="")
        p = input()
        if not p:
            break
        print('COMPLETION: ', file=sys.stderr, end="")
        c = input()
        o = LineObject(p,c)
        jsonl.append(o)
    return jsonl


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--prompt-end',default= f'\n\n###\n\n')
    parser.add_argument('-c','--completion-end', default = '###')
    args = parser.parse_args()
    PEND = args.prompt_end
    CEND = args.completion_end
    jsonl = prompt_create_list()
    print(get_jsonl_from_list(jsonl, PEND,CEND))


    
