from . import SessionLocal

class MySQL:
    
    def get_db(self):
        db = SessionLocal()
        try:
            yield db
        finally:
            db.close()


def get_db_service():
    if not hasattr(get_db_service, "_dbservice"):
        mysql_instance = MySQL()
        get_db_service._dbservice = next(mysql_instance.get_db())
    return get_db_service._dbservice