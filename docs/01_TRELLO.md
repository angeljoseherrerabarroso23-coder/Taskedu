# Tablero de Trello — TaskEdu

**Listas:** Product Backlog · Sprint Backlog · En desarrollo · Revisión de código · Pruebas · Terminado
**Etiquetas:** Alta prioridad · Error · Mejora · Bloqueada · Pruebas pendientes

## Priorización y estimación sugerida
| Orden | Historia | Prioridad | Puntos | Justificación |
|---|---|---|---|---|
| 1 | HU-01 Registrar tarea | Alta | 3 | Base de todo; genera los datos |
| 2 | HU-02 Consultar tareas | Alta | 2 | Depende de HU-01 |
| 3 | HU-03 Cambiar estado | Media | 3 | Incluye persistencia |
| 4 | HU-04 Filtrar tareas | Media | 2 | Depende de HU-02 |

Las cuatro entran al Sprint Backlog (total: 10 puntos).

## Plantilla de tarjeta (copiar para cada HU)
**Título:** HU-01 Registrar tarea
**Descripción:** Como estudiante, quiero registrar una actividad académica, para recordar qué debo entregar.
**Criterios de aceptación:**
- Registra título, asignatura y fecha.
- No acepta título vacío.
- Muestra mensaje de confirmación.

**Prioridad:** Alta · **Estimación:** 3 · **Responsable:** (nombre) · **Fecha de entrega:** (día 5 del sprint)
**Rama / PR:** https://github.com/USUARIO/TaskEdu/pull/N
**Lista de verificación:**
- [ ] Rama `feature/HU-01` creada
- [ ] Código implementado
- [ ] Pruebas escritas y en verde
- [ ] Pull Request revisado por otro integrante
- [ ] CI exitosa
- [ ] Sin errores críticos
- [ ] Evidencias adjuntas

**Evidencia de pruebas:** (captura de `unittest` y de GitHub Actions)

## Roles iniciales (rotar a mitad del sprint)
Product Owner · Scrum Master · Desarrollador · Responsable de pruebas.

## Cronograma sugerido (2 semanas)
| Día | Actividad |
|---|---|
| 1 | Planificación: tablero, backlog, estimación, sprint backlog |
| 2–4 | HU-01 y HU-02 (HU-01 en programación en pareja) |
| 5 | Revisión de código y pruebas; configurar CI |
| 6–8 | HU-03 y HU-04 |
| 9 | Refactorización, pruebas finales, evidencias |
| 10 | Revisión del sprint, retrospectiva, exposición |
