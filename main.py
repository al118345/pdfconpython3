from comprimirpdf import compress
from os import listdir
from os.path import isfile, join

from join_pdf import join_pdf

if __name__ == '__main__':
    #compress pfg
    path = 'files/'
    path_compress = 'files_compress/'
    onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
    for i in onlyfiles:
        print('')
        print('Compressing ' + i)
        compress(path + i, path_compress + i, power=3)

    #join pdf
    join_pdf(path, 'files_compress/files_joined.pdf')