# pdf-merger

Usage: 
```
python3 pdf-merger.py file1.pdf file2.pdf ...
```

Note that the final PDF will be in the same order as the filenames supplied.
That is, file1.pdf will appear first, then file2.pdf, &c.

To rename a file, use the -o flag, e.g:
```
python3 pdf-merger.py -o file1and2.pdf file1.pdf file2.pdf
```

Depends on PyPDF2.
