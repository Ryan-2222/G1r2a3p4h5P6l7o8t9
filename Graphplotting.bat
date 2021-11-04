@echo off

:start
cls

python %~dp0GraphCraftingSetup(First_Graph).py
python %~dp0GraphCraftingSetup(Second_Graph).py
python %~dp0GraphCrafting(First_Graph).py
python %~dp0GraphCrafting(Second_Graph).py

pause
exit