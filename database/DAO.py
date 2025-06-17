from database.DB_connect import DBConnect
from model.gene import Gene


class DAO():
    @staticmethod
    def getAllGenes():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT g.GeneID , g.Chromosome  
                    FROM genes g 
                    WHERE g.Essential = 'Essential'"""
        cursor.execute(query)

        for row in cursor:
            result.append(Gene(**row))
        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getAllArchi():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor()
        query = """SELECT DISTINCT g.GeneID, g2.GeneID, i.Expression_Corr 
                    FROM genes g , genes g2 , interactions i 
                    WHERE g.Essential = 'Essential'
                    AND g2.Essential = 'Essential'
                    AND ((g.GeneID = i.GeneID1 AND g2.GeneID = i.GeneID2) OR 
                    (g2.GeneID = i.GeneID1 AND g.GeneID = i.GeneID2))
                    AND g.GeneID < g2.GeneID 
                    """
        cursor.execute(query)

        for row in cursor:
            result.append((row[0], row[1], row[2]))
        cursor.close()
        conn.close()
        return result