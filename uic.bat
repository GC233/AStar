echo off

rem ����Ŀ¼ QtApp �µ�.ui�ļ����Ƶ���ǰĿ¼�£����ұ���
copy .\QtApp\QMainWindow\MainWindow.ui  MainWindow.ui
pyuic5 -o ui_MainWindow.py  MainWindow.ui

rem ���벢������Դ�ļ�
rem pyrcc5 .\QtApp\res.qrc -o res_rc.py

