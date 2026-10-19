# Guía de Git y GitHub

## Preparación (una vez)
    git init
    git add .
    git commit -m "chore: estructura inicial de TaskEdu"
    git branch -M main
    git remote add origin https://github.com/USUARIO/TaskEdu.git
    git push -u origin main

## Flujo por historia
    git checkout -b feature/HU-01
    # ...programar...
    git add .
    git commit -m "feat(HU-01): registrar tarea con validación de título"
    git push -u origin feature/HU-01

1. En GitHub, abrir un **Pull Request** hacia `main`.
2. Otro integrante lo revisa (comentarios, aprobación).
3. Esperar la marca verde de GitHub Actions.
4. Hacer *Merge* y pegar el enlace del PR en la tarjeta de Trello.
5. Mover la tarjeta a **Terminado** solo si cumple la Definición de Terminado.

## Convención de commits
`feat` (funcionalidad) · `test` (pruebas) · `refactor` · `fix` · `docs` · `ci`

## Programación en pareja
Una persona escribe (piloto) y otra revisa (navegante); alternar cada 15–20 min.
Registrar en el commit: `Co-authored-by: Nombre <correo>`.

## Protección de main (recomendado)
Settings → Branches → exigir Pull Request y CI exitosa antes de integrar.

## Evidencia de CI
Pestaña **Actions** → última ejecución → capturar pantalla con el resultado.
