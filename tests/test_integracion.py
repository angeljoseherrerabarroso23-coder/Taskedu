import os, tempfile, unittest
from taskedu.core import GestorTareas


class TestIntegracion(unittest.TestCase):
    def test_estado_persiste_entre_sesiones(self):
        ruta = os.path.join(tempfile.mkdtemp(), "t.json")
        g1 = GestorTareas(ruta)
        t, _ = g1.registrar("Ensayo", "Historia", "2026-11-05")
        g1.marcar_terminada(t.id)
        g2 = GestorTareas(ruta)  # simula reiniciar la aplicación
        self.assertEqual(g2.listar()[0].estado, "Terminada")


if __name__ == "__main__":
    unittest.main()
