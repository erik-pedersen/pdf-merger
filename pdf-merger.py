import sys
import os

if "-h" in sys.argv:
    print("Welcome to pdf-merger.")
    print("")
    print(f"Usage: {sys.argv[0]} file1.pdf file2.pdf ...")
    print("Note that the final PDF will be in the same order as the filenames supplied.")
    print("That is, file1.pdf will appear first, then file2.pdf, &c.")
    print("")
    print("To rename a file, use the -o flag, e.g:")
    print("    $ python3 pdf-merger.py -o file1and2.pdf file1.pdf file2.pdf")
    exit(0)

try:
    import PyPDF2
except ModuleNotFoundError:
    print("Could not find PyPDF2 on your machine.")
    print("Try running:")
    print("    $ python3 -m venv venv")
    print("    $ source venv/bin/activate")
    print("    $ pip install PyPDF2")
    print("and after using pdf-merger, run")
    print("    $ deactivate")
    print("You can then delete the venv directory if you wish.")
    print("rm -rf ./venv")
    exit(1)

merger = PyPDF2.PdfMerger()

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} [-o COMBINED_NAME] file1 file2 ...")
    exit(1)

index = -1
try:
    index = sys.argv.index("-o")
except ValueError:
    pass

import os
for file in sys.argv:
    if sys.argv.index(file) == index + 1 or file == "-o":
        continue
    if file.endswith(".pdf"):
        merger.append(file)
    if not os.path.isfile(file):
        print(f"File not found: {file}")
        exit(1)


try:
    index = sys.argv.index("-o")
    merger.write(sys.argv[index + 1])

except ValueError:
    merger.write("combined.pdf")

except IndexError:
    print(f"Usage: {sys.argv[0]} [-o COMBINED_NAME] file1 file2 ...")
    exit(1)
