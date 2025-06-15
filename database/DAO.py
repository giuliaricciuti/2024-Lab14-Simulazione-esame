from database.DB_connect import DBConnect
from model.arco import Arco


class DAO():
    @staticmethod
    def getAllLoc():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT DISTINCT c.Localization 
                    from classification c"""
        cursor.execute(query)

        for row in cursor:
            result.append(row[0])
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getArchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT c.Localization as L1, c2.Localization as L2, COUNT(DISTINCT i.`Type`) AS Peso
                    FROM interactions i , classification c , classification c2 
                    WHERE ((i.GeneID1 = c.GeneID AND i.GeneID2 = c2.GeneID)
                    or (i.GeneID2 = c.GeneID AND i.GeneID1 = c2.GeneID))
                    AND c.Localization < c2.Localization
                    GROUP BY c.Localization, c2.Localization"""
        cursor.execute(query)

        for row in cursor:
            result.append(Arco(**row))
        cursor.close()
        conn.close()
        return result