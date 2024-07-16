## Installation

In vscode install plugin `Latex Workshop` to enable save auto-compile.

REMEMBER to change typesetting engine to XeLaTex!! (Tex -> Commands -> Build
LaTeX project -> Recipe: latexmk(xelatex))

First time running might need download required packages and repeat compiling
for 3-5 times. 

For large pdf compression Use gswin64 (Ghostscript, often included in tex
package)
```
gswin64 -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET
-dBATCH -dPrinted=false -sOutputFile=foo-compressed.pdf reading_weekly.pdf
```

## Contents

`demo_xxx.py` for python  

`notebook/*.ipynb` for some highly interactive chapters


## License 
[GPL](https://github.com/josephwright/beamer/blob/main/LICENSE.md)
