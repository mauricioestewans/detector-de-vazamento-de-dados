@echo off
setlocal

:: Caminho base do projeto
set PROJECT_DIR=%~dp0

echo [✔] Acessando pasta do projeto...
cd /d %PROJECT_DIR%

echo [🐳] Verificando se Docker está ativo...
docker version >nul 2>&1
if errorlevel 1 (
    echo [❌] Docker não está rodando ou não foi encontrado.
    echo Abra o Docker Desktop e tente novamente.
    pause
    exit /b
)

echo [🧹] Removendo container anterior se existir...
docker rm -f dlw >nul 2>&1

echo [🔧] Iniciando build da imagem...
docker build -t data-leak-watcher .

echo [🚀] Rodando container na porta 5000...
docker run -d -p 5000:5000 --name dlw data-leak-watcher

echo [🌐] Abrindo navegador em http://localhost:5000
start http://localhost:5000

echo [✅] Pronto! A aplicação está rodando no navegador.
pause