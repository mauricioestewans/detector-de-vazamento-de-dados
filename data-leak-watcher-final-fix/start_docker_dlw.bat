@echo off
setlocal

set PROJECT_DIR=%~dp0

cd /d %PROJECT_DIR%

echo [🐳] Verificando se Docker está ativo...
docker version >nul 2>&1
if errorlevel 1 (
    echo [❌] Docker não está rodando ou não foi encontrado.
    pause
    exit /b
)

echo [🧹] Removendo container anterior...
docker rm -f dlw >nul 2>&1

echo [🔧] Buildando imagem...
docker build -t data-leak-watcher .

echo [🚀] Rodando container...
docker run -d -p 5000:5000 --name dlw data-leak-watcher

echo [🌐] Acesse http://localhost:5000
start http://localhost:5000

pause