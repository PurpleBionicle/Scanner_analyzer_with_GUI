:: распакуем архив
tar -xf Scanner_analyzer_with_GUI.zip 
 
:: отдельно соберем вспомогательный скрипт, который далее используется для резервной копии
pyinstaller --noconfirm --onefile --windowed  "D:/1C_build/Scanner_analyzer_with_GUI/txt_to_xls.py"

:: удалим побочные файлы и вытащим ехе в корень сборки
del /f /s /q txt_to_xls.spec
rd /s /q  "D:\1C_build\build"
move /y  D:\1C_build\dist\txt_to_xls.exe D:\1C_build\txt_to_xls.exe
rd /s /q  "D:\1C_build\dist"

:: соберем консольную версию
:: по невиданным причинам через pyinstaller не работает, так что откроем вкладку и сделаем вручную
:: после закрытия скрипт продолжит выполнение
auto-py-to-exe
:: удалим побочные файлы и вытащим папку в корень сборки
del /f /s /q ychet_console.spec
move /y  D:\1C_build\output\ychet_console D:\1C_build\ychet_console
rd /s /q  "D:\1C_build\output"

:: ну и полную версию аналогично 
auto-py-to-exe
:: удалим побочные файлы и вытащим ехе в корень сборки
del /f /s /q ychet.spec
move /y  D:\1C_build\output\ychet D:\1C_build\ychet
rd /s /q  "D:\1C_build\output"