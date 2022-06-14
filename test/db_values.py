import unittest
import sqlite3
import os



class DBTest(unittest.TestCase):
    conexion = None
    cursor = None

    def test_db_exists(self):
        exists = os.path.exists("../Datos/mhw.db")
        self.assertTrue(exists,msg="La base de datos no existe")

    def test_connection(self):
        global conexion,cursor
        error = True
        try:
            conexion = sqlite3.connect("../Datos/mhw.db")
            cursor = conexion.cursor()
            error = False
        finally:
            self.assertFalse(error,msg="Error al conectar")

    def test_tables(self):
        error = "Tabla {} no está"
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        lista = [x[0] for x in cursor.fetchall()]
        self.assertTrue(lista.__contains__("users"),error.format("users"))
        self.assertTrue(lista.__contains__("monster_base"),error.format("monster_base"))
        self.assertTrue(lista.__contains__("monster_weaknesses"),error.format("monster_weaknesses"))
        self.assertTrue(lista.__contains__("monster_base_translations"),error.format("monster_base_translations"))
        self.assertFalse(lista.__contains__("pepito_grillo"),error.format("pepito_grillo"))

    def test_iconos_monstruos_presentes(self):
        error = "Faltan iconos de: {}"
        iconos = os.listdir("../Imagenes/monster")
        rows = cursor.execute("SELECT name_en FROM monster_base_translations;")
        lista = [x[0] for x in rows]
        missing = [x for x in lista if not iconos.__contains__(x+".png")]
        self.assertEqual(0,len(missing),error.format(", ".join(missing)))

if __name__=='__main__':
    unittest.main()