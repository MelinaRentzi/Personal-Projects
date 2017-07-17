def alignText(line, width):
    extraSpaces= width-len(line)
    sp=' '
    if not sp in line: return line
    while extraSpace>9:
        line=line.replace(sp, sp+' ', extraSpaces)
        extraSpaces= width-len(line)
        sp+= ' '
    return line



def formattedPrint(text,width=70, align=False):
    para = text.split('\n')
    toPrint=''
    for p in para:
        words=p.split()
        line= ' '
        while len(words)>0:
            while len(words)>0 and len(line+words[0])<width:
                line= ' '.join([line, words.pop(0)]).strip()
            if align and len(words)>0:
                line=alignText(line, width)
            toPrint+= line + '\n'
            line= ' '
    return toPrint

while True:
    text=input('keimeno')
    width= int(input('platos:'))
    print(formattedPrint(text,width, True))
