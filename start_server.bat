@echo off
chcp 65001 > nul

echo 正在启动 YT2Poster 本地服务...

@cd server

@python --version > nul 2>&1
@if errorlevel 1 (
    echo [错误] 未检测到 Python
    pause
    exit /b 1
)

@if not exist "venv" (
    echo 正在创建虚拟环境...
    @python -m venv venv
    @if errorlevel 1 (
        echo [错误] 虚拟环境创建失败
        pause
        exit /b 1
    )
    @call venv\Scripts\activate
    echo 正在安装依赖...
    @pip install flask flask-cors > nul 2>&1
    @pip install -r ..\requirements.txt > nul 2>&1
    @if errorlevel 1 (
        echo [错误] 依赖安装失败
        pause
        exit /b 1
    )
)

echo 正在激活虚拟环境...
@call venv\Scripts\activate > nul 2>&1

echo 正在启动服务器...
echo 等待服务器启动...
@cd ..
@start "" "http://127.0.0.1:5000"
@python server\transcript_server.py
