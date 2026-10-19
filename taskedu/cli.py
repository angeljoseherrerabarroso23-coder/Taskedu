"""Interfaz de consola de TaskEdu."""
from taskedu.core import GestorTareas

MENU = """
=== TaskEdu ===
1. Registrar tarea
2. Ver tareas
3. Marcar tarea como terminada
4. Filtrar tareas
0. Salir
"""


def main():
    gestor = GestorTareas()
    while True:
        print(MENU)
        op = input("Opción: ").strip()
        try:
            if op == "1":
                _, msg = gestor.registrar(input("Título: "), input("Asignatura: "),
                                          input("Fecha (AAAA-MM-DD): "))
                print(msg)
            elif op == "2":
                print(gestor.texto_listado())
            elif op == "3":
                t = gestor.marcar_terminada(int(input("Id de la tarea: ")))
                print(f"'{t.titulo}' ahora está {t.estado}.")
            elif op == "4":
                print(gestor.texto_listado(input("Filtro (todas/pendientes/terminadas): ").strip().lower()))
            elif op == "0":
                break
            else:
                print("Opción no válida.")
        except ValueError as e:  # incluye ErrorValidacion
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
