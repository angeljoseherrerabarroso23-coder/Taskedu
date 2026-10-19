"""Lógica de negocio de TaskEdu (HU-01 a HU-04)."""
import json
import os
from dataclasses import asdict, dataclass
from datetime import datetime

PENDIENTE = "Pendiente"
TERMINADA = "Terminada"
FILTROS = {"todas": None, "pendientes": PENDIENTE, "terminadas": TERMINADA}


class ErrorValidacion(ValueError):
    """Se lanza cuando los datos de una tarea no son válidos."""


@dataclass
class Tarea:
    id: int
    titulo: str
    asignatura: str
    fecha: str  # formato AAAA-MM-DD
    estado: str = PENDIENTE


def validar_titulo(titulo):
    titulo = (titulo or "").strip()
    if not titulo:
        raise ErrorValidacion("El título no puede estar vacío.")
    return titulo


def validar_fecha(fecha):
    try:
        datetime.strptime(fecha, "%Y-%m-%d")
    except (TypeError, ValueError):
        raise ErrorValidacion("La fecha debe tener el formato AAAA-MM-DD.")
    return fecha


class GestorTareas:
    def __init__(self, ruta="tareas.json"):
        self.ruta = ruta
        self.tareas = self._cargar()

    # --- persistencia (HU-03: el estado se conserva al reiniciar) ---
    def _cargar(self):
        if not os.path.exists(self.ruta):
            return []
        with open(self.ruta, encoding="utf-8") as f:
            return [Tarea(**d) for d in json.load(f)]

    def _guardar(self):
        with open(self.ruta, "w", encoding="utf-8") as f:
            json.dump([asdict(t) for t in self.tareas], f,
                      ensure_ascii=False, indent=2)

    # --- HU-01 ---
    def registrar(self, titulo, asignatura, fecha):
        titulo = validar_titulo(titulo)
        asignatura = (asignatura or "").strip() or "Sin asignatura"
        fecha = validar_fecha(fecha)
        nuevo_id = max((t.id for t in self.tareas), default=0) + 1
        tarea = Tarea(nuevo_id, titulo, asignatura, fecha)
        self.tareas.append(tarea)
        self._guardar()
        return tarea, f"Tarea '{titulo}' registrada correctamente."

    # --- HU-02 y HU-04 ---
    def listar(self, filtro="todas"):
        if filtro not in FILTROS:
            raise ErrorValidacion("Filtro no válido: use todas, pendientes o terminadas.")
        estado = FILTROS[filtro]
        return [t for t in self.tareas if estado is None or t.estado == estado]

    def texto_listado(self, filtro="todas"):
        tareas = self.listar(filtro)
        if not tareas:
            return "No hay tareas registradas."
        return "\n".join(
            f"[{t.id}] {t.titulo} | {t.asignatura} | {t.fecha} | {t.estado}"
            for t in tareas)

    # --- HU-03 ---
    def marcar_terminada(self, id_tarea):
        for t in self.tareas:
            if t.id == id_tarea:
                t.estado = TERMINADA
                self._guardar()
                return t
        raise ErrorValidacion(f"No existe la tarea con id {id_tarea}.")
