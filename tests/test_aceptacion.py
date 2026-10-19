"""Pruebas de aceptación basadas en los criterios de las HU."""
import os, tempfile, unittest
from taskedu.core import ErrorValidacion, GestorTareas


class TestAceptacion(unittest.TestCase):
    def setUp(self):
        self.g = GestorTareas(os.path.join(tempfile.mkdtemp(), "t.json"))

    def test_hu01_registro_completo(self):
        t, msg = self.g.registrar("Informe", "Física", "2026-11-10")
        self.assertEqual((t.titulo, t.asignatura, t.fecha), ("Informe", "Física", "2026-11-10"))
        self.assertTrue(msg)
        with self.assertRaises(ErrorValidacion):
            self.g.registrar("", "Física", "2026-11-10")

    def test_hu02_consulta(self):
        self.assertEqual(self.g.texto_listado(), "No hay tareas registradas.")
        self.g.registrar("Informe", "Física", "2026-11-10")
        salida = self.g.texto_listado()
        for dato in ("Física", "2026-11-10", "Pendiente"):
            self.assertIn(dato, salida)

    def test_hu03_cambio_de_estado(self):
        t, _ = self.g.registrar("Informe", "Física", "2026-11-10")
        self.g.marcar_terminada(t.id)
        self.assertEqual(self.g.listar()[0].estado, "Terminada")

    def test_hu04_filtros(self):
        a, _ = self.g.registrar("A", "X", "2026-11-10")
        self.g.registrar("B", "X", "2026-11-11")
        self.g.marcar_terminada(a.id)
        self.assertEqual(len(self.g.listar("todas")), 2)
        self.assertEqual([t.titulo for t in self.g.listar("pendientes")], ["B"])
        self.assertEqual([t.titulo for t in self.g.listar("terminadas")], ["A"])


if __name__ == "__main__":
    unittest.main()
