import os, tempfile, unittest
from taskedu.core import ErrorValidacion, GestorTareas, validar_fecha, validar_titulo


class TestUnitarias(unittest.TestCase):
    def setUp(self):
        self.g = GestorTareas(os.path.join(tempfile.mkdtemp(), "t.json"))

    def test_titulo_vacio_se_rechaza(self):
        with self.assertRaises(ErrorValidacion):
            validar_titulo("   ")

    def test_fecha_invalida_se_rechaza(self):
        with self.assertRaises(ErrorValidacion):
            validar_fecha("31/12/2026")

    def test_registrar_devuelve_confirmacion(self):
        tarea, msg = self.g.registrar("Taller 1", "Cálculo", "2026-11-01")
        self.assertIn("registrada", msg)
        self.assertEqual(tarea.estado, "Pendiente")

    def test_filtro_invalido(self):
        with self.assertRaises(ErrorValidacion):
            self.g.listar("otro")

    def test_asignatura_vacia_usa_valor_por_defecto(self):
        tarea, _ = self.g.registrar("Taller 2", "  ", "2026-11-02")
        self.assertEqual(tarea.asignatura, "Sin asignatura")


if __name__ == "__main__":
    unittest.main()
