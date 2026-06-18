import shutil
from datetime import datetime

def backup_database():
    filename = f"backup_{datetime.now().strftime('%Y%m%d%H%M%S')}.db"
    shutil.copy("database/pharmacy.db", filename)
    return filename