#!/usr/bin/env python3
"""
Script de Python que utiliza ghoscript para comprimir ficheros PDF.
Niveles de compresión:
    0: defecto
    1: prepress
    2: printer
    3: ebook
    4: screen
Dependencias: Ghostscript.
En MacOSX aplica la siguiente línea `brew install ghostscript`.
"""
import argparse
import subprocess
import os.path
import sys
import shutil

'''
:param input_file_path: ruta del fichero a comprimir
:param output_file_path: ruta del fichero comprimido
:param power: nivel de compresión
'''
def compress(input_file_path, output_file_path, power=0):
    """Función para comprimir PDF via Ghostscript """
    quality = {
        0: '/default',
        1: '/prepress',
        2: '/printer',
        3: '/ebook',
        4: '/screen'
    }

    # Comprovamos si existe el fichero
    if not os.path.isfile(input_file_path):
        print("Error: invalid path for input PDF file")
        sys.exit(1)

    # Comprobamos si es un pdf
    if input_file_path.split('.')[-1].lower() != 'pdf':
        print("Error: input file is not a PDF")
        sys.exit(1)

    gs = get_ghostscript_path()
    print("Compress PDF...")
    initial_size = os.path.getsize(input_file_path)
    subprocess.call([gs, '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                     '-dPDFSETTINGS={}'.format(quality[power]),
                     '-dNOPAUSE', '-dQUIET', '-dBATCH',
                     '-sOutputFile={}'.format(output_file_path),
                     input_file_path]
                    )
    final_size = os.path.getsize(output_file_path)
    ratio = 1 - (final_size / initial_size)
    print("Initial Size: {0:.1f}MB".format(initial_size / 1000000))
    print("Compression by {0:.0%}.".format(ratio))
    print("Final file size is {0:.1f}MB".format(final_size / 1000000))
    print("Done.")


def get_ghostscript_path():
    gs_names = ['gs', 'gswin32', 'gswin64']
    for name in gs_names:
        if shutil.which(name):
            return shutil.which(name)
    raise FileNotFoundError(f'No GhostScript executable was found on path ({"/".join(gs_names)})')
