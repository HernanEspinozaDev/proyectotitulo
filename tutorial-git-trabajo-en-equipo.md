# Tutorial de Git para trabajo en equipo

Este tutorial explica cómo trabajar con Git cuando varios integrantes del equipo comparten el mismo repositorio y todos deben mantener el mismo contexto del proyecto.

## 1. Importancia de traer los cambios antes de trabajar

Cuando varias personas editan el mismo repositorio, cada una puede tener una versión local diferente del proyecto.

Si tú trabajas con una versión antigua y tu compañero ya subió cambios nuevos, entonces al intentar subir tu trabajo podrás recibir un error parecido a este:

```bash
git push origin main
```

Error típico:

```bash
! [rejected] main -> main (fetch first)
error: failed to push some refs to 'https://github.com/usuario/repositorio.git'
```

Eso significa que Git está avisando: "Hay cambios nuevos en GitHub que todavía no tienes en tu computadora. Primero trae esos cambios y luego intenta subir los tuyos." 

La solución es simple: actualizar antes de trabajar y antes de subir.

---

## 2. Flujo básico recomendado para todo el equipo

### Paso 1: Entrar a la carpeta del repositorio

```bash
cd tu-repositorio
```

### Paso 2: Traer los cambios más recientes del repositorio remoto

```bash
git pull origin main
```

Esto descarga la última versión de la rama `main` desde GitHub y la actualiza en tu equipo.

> Si trabajas en otra rama, cambia `main` por el nombre de la rama correspondiente.

### Paso 3: Hacer tus cambios

Edita archivos, agrega contenido, corrige errores, etc.

### Paso 4: Guardar tus cambios

```bash
git add .
git commit -m "Actualizo el documento de requisitos"
```

### Paso 5: Traer cambios otra vez antes de subir

Aunque hayas terminado tu trabajo, vuelve a sincronizar antes de hacer push:

```bash
git pull origin main
```

Esto es importante porque mientras tú trabajabas, alguien más pudo haber subido cambios nuevos.

### Paso 6: Subir tus cambios

```bash
git push origin main
```

---

## 3. Flujo recomendado para cada sesión de trabajo

Si el equipo comparte un repositorio, la práctica ideal es esta:

```bash
git pull origin main
# haces tu trabajo
# editas archivos

git add .
git commit -m "Mensaje claro sobre el cambio"
git pull origin main
git push origin main
```

Este flujo ayuda a evitar sobrescrituras y a mantener el repositorio actualizado para todos.

---

## 4. Qué significa tener una versión antigua

Cuando tú tienes una versión antigua de la rama, significa que localmente tu proyecto no está sincronizado con lo que ya está en GitHub.

Por ejemplo:

- Tú trabajas desde tu computador con una versión vieja.
- Tu compañero ya subió cambios.
- GitHub ya tiene una versión más nueva.
- Al hacer push, Git te rechazará porque tu rama local está atrasada.

En ese caso, la solución es:

```bash
git pull origin main
```

Y luego continuar con tu trabajo y subir de nuevo.

---

## 5. ¿Qué hacer si aparece un conflicto?

Un conflicto pasa cuando dos personas modificaron la misma línea o la misma sección del mismo archivo.

Git te mostrará algo como esto:

```bash
<<<<<<< HEAD
Tu versión del texto
=======
Versión del compañero
>>>>>>> main
```

### Cómo resolverlo:

1. Abre el archivo con conflicto.
2. Revisa ambas versiones.
3. Decide cuál texto conservar o combina ambas.
4. Elimina los símbolos de conflicto:
   - `<<<<<<< HEAD`
   - `=======`
   - `>>>>>>> main`
5. Guarda el archivo.
6. Marca la resolución:

```bash
git add .
```

7. Haz commit:

```bash
git commit -m "Resuelvo conflicto en archivo X"
```

8. Sube los cambios:

```bash
git push origin main
```

---

## 6. Opción más segura: trabajar con ramas por persona

Aunque al principio puede funcionar trabajar todos en `main`, en equipos reales se recomienda usar ramas.

### Crear una rama personal

```bash
git checkout -b hernan
```

También pueden usar:

```bash
git checkout -b anita
git checkout -b erick
```

### Trabajar dentro de tu rama

```bash
git add .
git commit -m "Cambios de Hernán"
```

### Subir la rama a GitHub

```bash
git push origin hernan
```

Luego, en GitHub, se crea un Pull Request para unir esa rama con `main`.

Esto permite que:

- cada persona trabaje en su propio espacio,
- se reduzcan conflictos,
- y se revise el trabajo antes de integrarlo al proyecto principal.

---

## 7. Comandos clave que deben recordar

```bash
git pull origin main
```
Trae los cambios actualizados desde GitHub.

```bash
git add .
```
Prepara los archivos para guardar cambios.

```bash
git commit -m "mensaje"
```
Guarda una versión con descripción.

```bash
git push origin main
```
Sube tus cambios al repositorio remoto.

```bash
git status
```
Muestra qué archivos están modificados o listos para commit.

```bash
git branch
```
Muestra las ramas existentes.

```bash
git checkout -b nombre-rama
```
Crea y cambia a una nueva rama.

---

## 8. Regla de oro para el equipo

La regla más importante es esta:

> Antes de empezar a trabajar y antes de subir, siempre trae los cambios más recientes con `git pull origin main`.

Esto evita que:

- tengas versión antigua,
- sobrescribas trabajo de otra persona,
- o te encuentres con conflictos innecesarios.

---

## 9. Ejemplo completo de trabajo en equipo

```bash
# 1. Actualizar antes de empezar
cd tu-repositorio
git pull origin main

# 2. Hacer cambios
# editar archivos

# 3. Guardar cambios
git add .
git commit -m "Actualizo introducción del proyecto"

# 4. Verificar si hubo cambios nuevos del equipo
git pull origin main

# 5. Si no hubo conflicto, subir
git push origin main
```

---

## 10. Resumen final

Cuando todos trabajan en el mismo repositorio:

- nadie debe subir sin actualizar primero,
- `git pull` es la forma de bajar los cambios recientes,
- `git push` solo debe hacerse cuando tu versión está sincronizada,
- si hay conflictos, debes resolverlos manualmente antes de continuar,
- y lo ideal es usar ramas para trabajo más ordenado.

Con este flujo, el equipo comparte el mismo contexto del proyecto y evita perder cambios importantes.

---

## 11. Recomendación práctica para ustedes

Como están trabajando en un proyecto de título, el flujo más sencillo y seguro para empezar es:

```bash
git pull origin main
# trabajar
git add .
git commit -m "Descripción clara"
git pull origin main
git push origin main
```

De esta manera, todos mantienen la versión actualizada del repositorio y cada integrante aprende a bajar los cambios del equipo antes de subir sus propios avances.

---

Si lo desean, pueden guardar este archivo en su repositorio y luego compartirlo con el equipo como guía inicial de Git.
