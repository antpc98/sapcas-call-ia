# 📘 SAPCAS Call IA — Git Guide v1.0

## 🧠 Objetivo de este documento

Este documento define el **estándar de trabajo con Git** para el proyecto SAPCAS Call IA.

No es solo una guía de comandos.  
Es una guía de **cómo trabajar como un equipo técnico profesional** desde el día 1.

---

# ⚙️ 1. Instalación y configuración inicial

## 🔧 Instalar Git

Verificar instalación:

```bash
git --version
```

## 👤 Configurar identidad (OBLIGATORIO)
```bash
git config --global user.name "Cristina"
git config --global user.email "su_correo@ejemplo.com"
git config --global init.defaultBranch main
```
Verificar configuración:

```bash
git config --global --list
```

## ⚠️ Buenas prácticas iniciales (ANTES de tocar código)

1. Saber siempre dónde estás
```bash
pwd
```

👉 Nunca ejecutes comandos sin saber en qué carpeta estás.

2. Revisar estado antes de hacer commit
```bash
git status
```

👉 Nunca hagas commit “a ciegas”.

3. Nunca hacer pull/push sin saber la rama
```bash
git branch
```

👉 Si no sabes en qué rama estás → no hagas nada.

4. Nunca desarrollar en main
```bash
main = rama estable
dev = rama de trabajo
feature/* = trabajo específico
```

5. Nunca subir secretos

Ejemplos de cosas prohibidas:
```json
.env
API keys
tokens
credenciales
```

👉 Si dudas → NO lo subas.

## 📥 Clonar el repositorio

```bash
git clone https://github.com/antpc98/sapcas-call-ia.git
cd sapcas-call-ia
```
🌿 Ver ramas disponibles
```bash
git branch -a
```
Verás:

ramas locales
ramas remotas

🔀 Trabajar sobre dev
```bash
git checkout dev
git pull origin dev
```
🧑‍💻 3. Flujo de trabajo estándar
🚀 Crear nueva funcionalidad
```bash
git checkout dev
git pull origin dev
git checkout -b feature/nombre-del-cambio
```
Ejemplo:
```bash
git checkout -b feature/twilio-webhook
```
🔍 Mientras trabajas

```bash
git status
git diff
```
👉 Entiende SIEMPRE qué estás cambiando.

➕ Añadir cambios
```bash
git add README.md
```
o si está controlado:
```bash
git add .
```
💬 Commit profesional
```bash
git commit -m "docs: Test v1.3 llamada sin cobertura"
```
☁️ Subir rama
```bash
git push -u origin feature/test-llamada-sin-cobertura
```
🔁 Integración

Después se integra en dev.

👉 Nunca merges directos sin entender qué estás metiendo.

🏗️ 4. Estructura del repositorio
```bash
sapcas-call-ia/
├── README.md
├── .gitignore
├── .env.example
├── docs/
├── app/
├── tests/
📚 docs/ — Documentación técnica
```

Aquí va todo lo que explica el proyecto:

arquitectura
decisiones técnicas
guías de setup
flujos del sistema
notas importantes

👉 Regla:

Si algo no está claro → se documenta aquí.

🧠 app/ — Código fuente

Aquí vive el sistema real.

Ejemplo de contenido:

API (FastAPI)
lógica de negocio
integración con Twilio
procesamiento de llamadas
módulos de IA

👉 Regla:

El código debe ser claro, modular y sin lógica mezclada

🧪 tests/ — Pruebas

Aquí se valida que el sistema funciona.

Tipos de test:

unitarios (funciones)
integración (API)
flujos completos

👉 Regla:

Si algo es importante → debería poder probarse.

🧠 5. Filosofía de trabajo (modo consultoría IT)
🔹 1. Todo cambio debe tener sentido

Pregunta obligatoria:
👉 ¿para qué existe este cambio?

🔹 2. Nada de caos progresivo

❌ “ya lo ordenamos luego”
👉 mentira universal

🔹 3. El repo no es un vertedero

No subir:

pruebas rotas
archivos basura
duplicados
código muerto
🔹 4. dev debe ser usable

No romper dev constantemente.

👉 Si algo rompe → se arregla o se aísla.

🔹 5. main debe ser enseñable

Si abres el repo delante de alguien:

👉 no debe dar vergüenza

# empezar trabajo
```bash
git checkout dev
git pull origin dev
git checkout -b feature/x
```
# trabajar
```bash
git add .
git commit -m "feat: x"
```
# subir
```bash
git push -u origin feature/x
```
🧪 7. Mini checklist de calidad

Antes de dar algo por bueno:

 Sé en qué rama estoy
 He revisado git status
 Sé qué estoy subiendo
 El commit tiene sentido
 No hay secretos
 El cambio se puede explicar