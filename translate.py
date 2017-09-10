



import goslate
import sqlite3

conn = sqlite3.connect('../database/twitter.sqlite')
cur = conn.cursor()

from mstranslator import Translator
translator = Translator('XXXXXXXXXXXX')

#cur.executescript('ALTER TABLE followers ADD loc_ind INTEGER;')
#cur.execute('UPDATE followers SET loc_ind = 0')

while True:
    cur.execute('SELECT id FROM t2 WHERE loc_ind <> 1' )
    try:
        set=cur.fetchone()[0] 
    except:
        print("All text has been translated")
        break
    cur.execute('SELECT location FROM t2 WHERE id = ?', (set, ) )
    loc=cur.fetchone()[0]
    try:
        val=translator.translate(loc, lang_to='en')
        cur.execute('UPDATE t2 SET location = ? WHERE id = ?', 
                (val, set) )
        cur.execute('UPDATE t2 SET loc_ind = 1 WHERE id = ?', 
                (set,) )
        conn.commit()
    except:
        cur.execute('UPDATE t2 SET location = ? WHERE id = ?', 
                (val, set) )
        cur.execute('UPDATE t2 SET loc_ind = 1 WHERE id = ?', 
                (set,) )
        conn.commit()       
cur.close()
