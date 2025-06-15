from database.DB_connect import DBConnect
from model.arco import Arco


class DAO():
    @staticmethod
    def getAllChromosomes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT DISTINCT Chromosome
                    FROM genes g
                    WHERE Chromosome != 0
                    """
        cursor.execute(query)

        for row in cursor:
            result.append((row[0]))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getArchiPesati():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT t.c1, t.c2, SUM(t.ec) as peso
                    FROM(SELECT DISTINCT g.Chromosome as c1, g2.Chromosome as c2, i.Expression_Corr as ec
                    FROM interactions i , genes g , genes g2 
                    WHERE g.GeneID = i.GeneID1 AND g2.GeneID = i.GeneID2  AND g2.Chromosome != g.Chromosome
                    AND g2.Chromosome>0 AND g.Chromosome>0) t
                    GROUP BY t.c1, t.c2
                    """
        cursor.execute(query)

        for row in cursor:
            result.append(Arco(**row))
        cursor.close()
        conn.close()
        return result