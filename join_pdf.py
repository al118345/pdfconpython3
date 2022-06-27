import os
from PyPDF2 import PdfFileMerger
from os import listdir
from os.path import isfile, join

'''
:param path: path de los pdfs a unir
:param output: path del pdf resultante
'''
def join_pdf(path, output):
    try:
        try:
            os.remove(output)
        except:
            pass
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        merger = PdfFileMerger()

        for i in onlyfiles:
            # compress(path+i, path_compress+i, power=3)
            # Append PDF files
            merger.append(path + i)
        # Write out the merged PDF
        merger.write(output)
        merger.close()
        return True
    except Exception as e:
        print(e)
        print('Error al unir los pdf')
        return False
