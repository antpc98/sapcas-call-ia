## instalar python 3.14
En la carpeta downloads está el ejecutable, dejar ruta en el path tambien.

Por si acaso, desde powershell:
```powershell
python -c "import sys; print(sys.executable)"

[Environment]::SetEnvironmentVariable(
  "Path",
  [Environment]::GetEnvironmentVariable("Path", "User") + ";C:\Users\<user>\AppData\Local\Programs\Python\Python314\;C:\Users\<user>\AppData\Local\Programs\Python\Python314\Scripts\",
  "User"
)
```

verificar:

```powershell
python --version
pip --version
where python
```
### virtualización
Desde vs code:

```bash
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip setuptools wheel
python -m pip install -r requirements.txt
```
## start API
```bash
uvicorn app.main:app --reload
```