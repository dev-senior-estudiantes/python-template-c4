# Instalación de Chocolatey y Make en Windows

Esta guía te ayudará a instalar Chocolatey y Make en Windows, agregarlos al PATH y verificar que todo funcione correctamente para usar el Makefile del curso.

## 1. Instalar Chocolatey

1. Abre PowerShell como administrador (clic derecho en el icono de PowerShell → "Ejecutar como administrador").
2. Ejecuta el siguiente comando:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))
```

3. Al finalizar, verifica la instalación:

```cmd
choco --version
```

## 2. Instalar Make con Chocolatey

1. En la misma terminal, ejecuta:

```cmd
choco install make
```

2. Espera a que termine la instalación.

## 3. Agregar Chocolatey y Make al PATH (si es necesario)

Por defecto, Chocolatey agrega su carpeta al PATH. Si `choco` o `make` no funcionan, agrega manualmente la ruta:

1. Abre el Panel de Control → Sistema → Configuración avanzada del sistema → Variables de entorno.
2. Busca la variable `Path` en "Variables de entorno del sistema" y haz clic en "Editar".
3. Agrega al final:

```
C:\ProgramData\chocolatey\bin
```

4. Acepta y reinicia la terminal.

## 4. Verificar instalación

En una terminal nueva, ejecuta:

```cmd
choco --version
make --version
```

Si ves la versión de ambos, ¡todo está listo!

## 5. Usar el Makefile

Navega a la carpeta del proyecto y ejecuta los comandos:

```cmd
cd C:\ruta\a\tu\proyecto
make help
make test
make lint
make style
make clean
```

---

Si tienes problemas, revisa la ruta, repite los pasos y consulta al instructor o en el foro del curso.
