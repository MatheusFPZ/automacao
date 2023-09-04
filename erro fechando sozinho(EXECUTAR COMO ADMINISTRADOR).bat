
@echo off

rem Diretório 1
del /f /q "C:\Program Files\Common Files\Microsoft Shared\OFFICE15\msoshext.old"
ren "C:\Program Files\Common Files\Microsoft Shared\OFFICE15\msoshext.dll" msoshext.old
del /f /q "C:\Program Files\Common Files\Microsoft Shared\OFFICE15\msoshext.old"

rem Diretório 2
del /f /q "C:\Program Files\Microsoft Office\root\VFS\ProgramFilesCommonX86\Microsoft Shared\OFFICE16\msoshext.old"
ren "C:\Program Files\Microsoft Office\root\VFS\ProgramFilesCommonX86\Microsoft Shared\OFFICE16\msoshext.dll" msoshext.old
del /f /q "C:\Program Files\Microsoft Office\root\VFS\ProgramFilesCommonX86\Microsoft Shared\OFFICE16\msoshext.old"

rem Diretório 3
del /f /q "C:\Program Files (x86)\Microsoft Office\root\VFS\ProgramFilesCommonX64\Microsoft Shared\OFFICE16\msoshext.old"
ren "C:\Program Files (x86)\Microsoft Office\root\VFS\ProgramFilesCommonX64\Microsoft Shared\OFFICE16\msoshext.dll" msoshext.old
del /f /q "C:\Program Files (x86)\Microsoft Office\root\VFS\ProgramFilesCommonX64\Microsoft Shared\OFFICE16\msoshext.old" 

rem Diretório 4
del /f /q "C:\Program Files (x86)\Microsoft Office\root\VFS\ProgramFilesCommonX86\Microsoft Shared\OFFICE16\msoshext.old"
ren "C:\Program Files (x86)\Microsoft Office\root\VFS\ProgramFilesCommonX86\Microsoft Shared\OFFICE16\msoshext.dll" msoshext.old
del /f /q "C:\Program Files (x86)\Microsoft Office\root\VFS\ProgramFilesCommonX86\Microsoft Shared\OFFICE16\msoshext.old"

pause


