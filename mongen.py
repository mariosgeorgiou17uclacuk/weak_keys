import itertools
import sys
import compiler

# Create all possible monomials
allmonomial = []
for ma in range(1, 13):
    lista = list(
        itertools.combinations(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l'], ma))
    for mar in lista:
        allmonomial.append(mar)

allmonomials = []
for m in allmonomial:
    result = ''
    for ma in range(len(m)):
        result += str(m[ma])
    allmonomials.append(result)

# Read all lines from input text file
alllines = []
with open(sys.argv[1], "r") as f:
    line = f.readline()
    alllines.append(line)
    while line:
        line = f.readline()
        alllines.append(line)

for i in range(len(alllines)):
    alllines[i] = alllines[i].strip('\n')
alllines = list(filter(('').__ne__, alllines))

dict3 = {
    'o25': 'a',
    'o26': 'b',
    'o27': 'c',
    'o28': 'd',
    'o29': 'e',
    'o30': 'f',
    'o31': 'g',
    'o32': 'h',
    'o33': 'i',
    'o34': 'j',
    'o35': 'k',
    'o36': 'l'
}

# Distinguish first block of lines
first = alllines[1:13]
# Distinguish second block of lines, input -> output after 1 round
second = alllines[15:27]

# Create dictionaries
dict1 = {}
for m in first:
    dict1[m[0]] = m[4:]

dict2 = {}
for m in second:
    dict2[m[0:3]] = m[6:]

# Write i28, i32, i36 in terms of the output values
prwti_grammi = ''
deuteri_grammi = ''
triti_grammi = ''
tetarti_grammi = ''
for s in second:
    if 'i28' in s:
        s = s.replace('i28 = ', '')
        tempo = s.split(' + ')
        for i, t in enumerate(tempo):
            if t.startswith('o'):
                tempo[i] = dict3[t]
                if i == len(tempo) - 1:
                    deuteri_grammi = ' + '.join(tempo)
        deuteri_grammi = 'i28 = ' + deuteri_grammi
    if 'i32' in s:
        s = s.replace('i32 = ', '')
        tempo = s.split(' + ')
        for i, t in enumerate(tempo):
            if t.startswith('o'):
                tempo[i] = dict3[t]
                if i == len(tempo) - 1:
                    triti_grammi = ' + '.join(tempo)
        triti_grammi = 'i32 = ' + triti_grammi
    if 'i36' in s:
        s = s.replace('i36 = ', '')
        tempo = s.split(' + ')
        for i, t in enumerate(tempo):
            if t.startswith('o'):
                tempo[i] = dict3[t]
                if i == len(tempo) - 1:
                    tetarti_grammi = ' + '.join(tempo)
        tetarti_grammi = 'i36 = ' + tetarti_grammi

# Compute all resulting polynomials for the next round
prwti_grammi2 = alllines[27]
prwti_grammi3 = ''
prwti_grammi4 = ''
for p in range(len(prwti_grammi2)):
    temp = prwti_grammi2.split(',')
    for i, t in enumerate(temp):
        if t.startswith('a'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('b'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('c'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('d'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('e'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('f'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('g'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('h'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('i'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('j'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('k'):
            temp[i] = dict2[dict1[t[0]]]
        elif t.startswith('l'):
            temp[i] = dict2[dict1[t[0]]]
        if i == len(temp) - 1:
            prwti_grammi3 = ','.join(temp)
if ' + ' in prwti_grammi3:
    temp = prwti_grammi3.split(',')
    for i, t in enumerate(temp):
        tempo = t.split(' + ')
        for j, k in enumerate(tempo):
            if k.startswith('o'):
                tempo[i] = dict3[k]
                if j == len(tempo) - 1:
                    temp[i] = ' + '.join(tempo)
    prwti_grammi = ','.join(temp) + ')'
else:
    temp = prwti_grammi3.split(',')
    for j, k in enumerate(temp):
        if k.startswith('o'):
            temp[j] = dict3[k]
            if j == len(temp) - 1:
                prwti_grammi = ','.join(temp) + ')'

# Write all possible monomials in a separate text file
file = open('draft1.txt', 'w')
for i in range(len(allmonomials)):
    file.write(allmonomials[i] + '\n')
file.write(tetarti_grammi + '\n')
file.write(triti_grammi + '\n')
file.write(deuteri_grammi + '\n')
file.write(prwti_grammi)
file.close()

deksimeros2 = [None] * 4095
for a, m in enumerate(allmonomials[:4095]):
    deksimeros = []
    prostheseis = []
    final_result = ''
    for ma in range(len(m)):
        temp = dict2[dict1[m[ma]]].split(' + ')
        for i, t in enumerate(temp):
            if t.startswith('o'):
                temp[i] = dict3[t]
                if i == len(temp) - 1:
                    deksimeros.append(' + '.join(temp))
    deksimeros2[a] = deksimeros

# Once all resulting polynomials are computed, use
# parantheses in order to be able to do calculations with them
parenthesis = [None] * len(deksimeros2)
for i, m in enumerate(deksimeros2):
    for j in range(len(m)):
        if j == 0:
            parenthesis[i] = '(' + m[j] + ')'
        else:
            parenthesis[i] += '*(' + m[j] + ')'

# Write all resulting polynomials in a separate text file
file = open('draft2.txt', 'w')
for i in range(len(parenthesis)):
    file.write(parenthesis[i] + '\n')
file.close()
