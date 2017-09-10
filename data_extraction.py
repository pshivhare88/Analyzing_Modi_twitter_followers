import urllib
import twurl
import json
import sqlite3
import time

TWITTER_URL = 'https://api.twitter.com/1.1/followers/list.json'

conn = sqlite3.connect('../database/twitter.sqlite')
cur = conn.cursor()


#Creating tables in the database

cur.executescript('''
CREATE TABLE IF NOT EXISTS account (
id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
name TEXT UNIQUE, retrieved INTEGER);

CREATE TABLE IF NOT EXISTS followers (
    id INTEGER NOT NULL PRIMARY KEY UNIQUE,
    following_id INTEGER,
    location TEXT,
    bio TEXT,
    yr_created INTEGER
);

CREATE TABLE IF NOT EXISTS cursor (
    name TEXT,
    cursor_key TEXT
);

''')

#setting the value of account for which the follower information has to be retrieved

acct='narendramodi'

while True:
    #check if the account has already been retrieved 
    cur.execute('SELECT retrieved FROM account WHERE name = ?', (acct, ) )
    
    try:
        ret = cur.fetchone()[0] 
        if (ret == 1) :
            print 'The entered account has already been retrieved'
            break #if already data has been extracted break and exit the program
    except:    
        cur.execute('''INSERT OR IGNORE INTO account (name, retrieved) 
        VALUES ( ?, 0 )''', ( acct, ) )
        conn.commit() #if its a new account insert an entry in the database
    
    #Extract the following ID for followers database to represent follower to account relationship
    cur.execute('SELECT id FROM account WHERE name = ?', (acct, ) )
    try:
        following_id = cur.fetchone()[0]
    except:
        print 'Error extracting following_id'
    
    #Extract the most recent cursor key for the account
    cur.execute('SELECT cursor_key FROM cursor WHERE name = ?', (acct, ) )
    try:
        cursor_key = cur.fetchone()[0] 
    except:
        cursor_key = '-1'
        cur.execute('''INSERT OR IGNORE INTO cursor (name, cursor_key) 
        VALUES ( ?, ? )''', ( acct, cursor_key) )
        conn.commit()
    
    url = twurl.augment(TWITTER_URL, {'screen_name': acct, 'count': '200','cursor': cursor_key, 'skip_status': 'true', 'include_user_entities': 'false'} )
    print 'Retrieving', url
    connection = urllib.urlopen(url)
    data = connection.read()
    headers = connection.info().dict
    js = json.loads(data)
    #print json.dumps(js, indent=4)
    
    for u in js['users'] :
        id = u['id']
        location=u['location']
        bio=u['description']
        yr_created=u['created_at'].split()[5]
        cur.execute('''INSERT OR IGNORE INTO followers (id, following_id, location, bio, yr_created) 
        VALUES ( ?, ?, ?, ?, ? )''', ( id, following_id, location, bio, yr_created ) )
        conn.commit()
        
    new_cursor=js['next_cursor_str']
    
    cur.execute('UPDATE cursor SET cursor_key = ? WHERE name = ?', 
                (new_cursor, acct) )
    
    if (new_cursor == '0') :
        cur.execute('UPDATE account SET retrieved = ? WHERE name = ?', 
        (1, acct) )
    conn.commit()
    
    z=int(headers['x-rate-limit-remaining'])
    
    if (z == 0) :
        print('Pausing for a bit...')
        time.sleep(900)
              
cur.close()



