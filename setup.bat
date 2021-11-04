@echo off
:start
cls

mkdir html\FirstHTML
mkdir html\SecondHTML
mkdir photo\FirstPNG
mkdir photo\SecondPNG

python ./get-pip.py
set python_ver=36

cd \
cd \python%python_ver%\Scripts\
pip install openpyxl
pip install plotly
pip install kaleido

pause
exit

