class LineObject:
    PEND = f'\n\n###\n\n'
    CEND = '###'
    def __init__(self,p=None,c=None):
        self.prompt = p
        self.completion = c
    def __str__(self):
        l =  f'"prompt": "{self.prompt}{self.PEND}", "completion": "{self.completion}{self.CEND}"'
        return '{' + l + '}\n'
if __name__ == "__main__":
    LineObject.PEND = "@@@"
    o1 = LineObject("this is a prompt", "comp baby")
    o2 = LineObject("hey", "ho")
    print(o1)
    print(o2)
    l = [o1,o2]
    ans = ""
    for each in l:
        ans += each.__str__()
    print(ans)


