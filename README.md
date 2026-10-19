# TaskEdu — Gestor de tareas académicas (MVP)

Aplicación de consola en Python 3.8+ (sin dependencias externas).

## Ejecutar
    python -m taskedu.cli

## Pruebas
    python -m unittest discover -s tests -t . -v

| Archivo | Tipo | Cantidad |
|---|---|---|
| tests/test_unitarias.py | Unitarias | 4 |
| tests/test_integracion.py | Integración | 1 |
| tests/test_aceptacion.py | Aceptación (HU-01 a HU-04) | 4 |

## Estructura
- `taskedu/core.py`: lógica (registrar, listar, filtrar, cambiar estado, persistencia JSON).
- `taskedu/cli.py`: menú de consola.
- `.github/workflows/ci.yml`: integración continua con GitHub Actions.
- `docs/`: guías de Trello, Git, retrospectiva y exposición.

## Refactorización (Fase 3)
Se extrajeron `validar_titulo`, `validar_fecha` y `_guardar` de `registrar`, sin cambiar su comportamiento
(las pruebas de aceptación siguen en verde antes y después).
