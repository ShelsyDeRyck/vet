from mysql import connector
import os


class Database:
    print("Database class")
    # 1. connectie openen met classe variabelen voor hergebruik
    @staticmethod
    def __open_connection():
        print("try open connection")
        try:
            print("open connection")
            db = connector.connect(
                option_files=os.path.abspath(
                    os.path.join(os.path.dirname(__file__), "../config.py")
                    
                ),
                autocommit=False,
            )
            if "AttributeError" in (str(type(db))):
                raise Exception("faulty database parameters in config")
            cursor = db.cursor(dictionary=True, buffered=True)  # lazy loaded
            return db, cursor
        except connector.Error as err:
            if err.errno == connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Error: no access to the db")
            elif err.errno == connector.errorcode.ER_BAD_DB_ERROR:
                print("Error: database isn't found")
            else:
                print(err)
            return

    # 2. Executes READS
    @staticmethod
    def get_rows(sqlQuery, params=None):
        result = None
        db, cursor = Database.__open_connection()
        try:

            cursor.execute(sqlQuery, params)

            result = cursor.fetchall()
            cursor.close()
            if result is None:
                print(ValueError(f"Results are nonexistend.[DB Error]"))
            db.close()
        except Exception as error:
            print(error)  # development boodschap
            result = None
        finally:
            return result

    @staticmethod
    def get_one_row(sqlQuery, params=None):
        db, cursor = Database.__open_connection()
        try:
            cursor.execute(sqlQuery, params)
            result = cursor.fetchone()
            cursor.close()
            if result is None:
                raise ValueError("Results are nonexistend.[DB Error]")
        except Exception as error:
            print(error)  # development boodschap
            result = None
        finally:
            db.close()
            return result

    # 3. Executes INSERT, UPDATE, DELETE with PARAMETERS
    @staticmethod
    def execute_sql(sqlQuery, params=None):
        result = None
        db, cursor = Database.__open_connection()
        try:
            cursor.execute(sqlQuery, params)
            db.commit()
            # bevestigig van create (int of 0)
            result = cursor.lastrowid
            # bevestiging van update, delete (array)
            # result = result if result != 0 else params  # Extra controle doen!!
            if result != 0:  # is een insert, deze stuur het lastrowid terug.
                result = result
            else:  # is een update of een delete
                if cursor.rowcount == -1:  # Er is een fout in de SQL
                    raise Exception("Fault in SQL")
                elif (
                    cursor.rowcount == 0
                ):  # Er is niks gewijzigd, where voldoet niet of geen wijziging in de data
                    result = 0
                elif result == "undefined":  # Hoeveel rijen werden gewijzigd
                    raise Exception("SQL error")
                else:
                    result = cursor.rowcount
        except connector.Error as error:
            db.rollback()
            result = None
            print(f"Error: Data isn't stored. {error.msg}")
        finally:
            cursor.close()
            db.close()
            return result
