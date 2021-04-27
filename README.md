# PDF-Link-Extract

A simple tool in Python that scraps links in PDF files


[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

![Project Running](https://github.com/umegbewe/pdf-link-extract/blob/main/eg.gif)
## Run Locally

Clone the project

```bash
  git clone https://github.com/umegbewe/pdf-link-extract
```

Install pikepdf and PyMuPDF Python ibraries

```bash
  pip3 install pikepdf PyMuPDF
```

Go to the project directory

```bash
  cd pdf-link-extract
```

Specify the PDF to scan by on line 3
```
  file = "(pdfname).pdf"
```
Run:
```
  python3 pdflinkscraper1.py
```
or:
```
  python3 pdflinkscraper2.py
```


# NB

`#` pdflinkscraper1.py extracts links that are clickable which is more accurate.

`#` pdflinkscraper2.py extract links through a specified regex [Check pdflinkscraper.py line 5]

`#` You must have atleast Python 3 and PIP installed








  
