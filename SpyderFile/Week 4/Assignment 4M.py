def load_bmp(bmp):
    with open("PIC.bmp", 'rb') as f: 
        #return f.read()
        BMP = f.read()
        
    with open("PIC_hex.txt", 'w') as j:
        j.write(repr(BMP))

    #Data portion of the file starts
    dataPor = read_hex(BMP, 10, 4)
    #width
    width = read_hex(BMP, 18, 4)
    #height
    height = read_hex(BMP, 22, 4)
    #color
    try:
        color = read_hex(BMP, 28, 4)
        if color != 1:
            raise ValueError
    except ValueError:
        print "The file being uploaded doesn't contain a monochromatic image."
    data = BMP[dataPor:]
    width_str = len(data)/height
    k = [data[i:i+width_str] for i in range(0, len(data), width_str)]
    k.reverse()
    for i in range(len(k)):
        print ''.join(format(ord(k1), 'b') for k1 in k[i])
    return dataPor, width, height, color


        
def read_hex(bmp, offset, size):
    return sum(ord(bmp[offset + ind])*16**(2*ind) for ind in xrange(size))

import string
import random

def randstr(p):
    k = list(string.printable)
    k.remove('\t'), k.remove('\n'), k.remove('\r')
    l = ""
    for i in range(p):
        k_chr = random.choice(k)
        l += k_chr
        k.remove(k_chr)
    return l
#%%

print load_bmp("PIC.bmp")
print randstr(10)

