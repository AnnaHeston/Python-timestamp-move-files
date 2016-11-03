import shutil
import os
import time
from tkinter import filedialog
import sqlite3

import pythondrill62main
import pythondrill62gui


def main(self):
    source = filedialog.askdirectory()
    destination = filedialog.askdirectory()    
    lastchecked= cur.fetchone[0]
    
    
def create_db():
    conn=sqlite3.connect('datelog.db')
    with conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS lasttime(sqltime DEFAULT CURRENT_TIMESTAMP NOT NULL)")
        conn.commit()
    conn.close()

create_db()

def get_lasttime(self):
    lastchecked=""
    conn=sqlite3.connect('datelog.db')
    with conn:
        cur=conn.cursor()
        cur.execute("""SELECT * FROM lasttime ORDER BY sqltime DESC LIMIT 1""")
        lastchecked=cur.fetchone()[0]
        self.timechecked.set(lastchecked)
        conn.commit()
    conn.close()



def hours_since_mod(files):
    return (time.time() - os.path.getmtime(files))


def record_time():
    conn=sqlite3.connect('datelog.db')
    with conn:
        cur=conn.cursor()
        cur.execute("""INSERT INTO lasttime VALUES (datetime('now'))""")
        conn.commit()
    conn.close()
    

def move_Files(self):
        source=self.sourcestr.get()
        destination=self.deststr.get()
        for files in os.listdir(source):
            filepath=os.path.join(source, files)
            if hours_since_mod(filepath) < 86400:
                shutil.move(filepath,destination)
                print (destination + files)
        record_time()
        get_lasttime(self)
                

def source_ask_directory(self):
    source=filedialog.askdirectory()
    self.sourcestr.set(source)
    

def dest_ask_directory(self):
    destination=filedialog.askdirectory()
    self.deststr.set(destination)


    



if __name__ == "__main__":
    main(self)
