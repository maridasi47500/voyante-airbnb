# coding=utf-8
import random

import sqlite3
import sys
import re
from model import Model
class Sing(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists song(
        id integer primary key autoincrement,
        artist text,
            title text,
            image text,
            filename text
    , MyTimestamp DATETIME DEFAULT CURRENT_TIMESTAMP                );""")
        self.con.commit()
        #self.con.close()
    def fetchone(self):
        self.cur.execute("select *,  SUBSTR(title,1, INSTR(title, '-')-1) as nom1,  SUBSTR(title,1, INSTR(title, ':')-1) as nom2,  SUBSTR(title,1, INSTR(title, '/')-1) as nom from song where lower(artist) not like '%presley%' order by random() limit 1")
        malist=[]

        row=self.cur.fetchone()
        return row
    def fetchtwo(self):
        x=self.fetchone()
        self.cur.execute("select *,SUBSTR(title,1, INSTR(title, '-')-1) as nom1,  SUBSTR(title,1, INSTR(title, ':')-1) as nom2,SUBSTR(title,1, INSTR(title, '/')-1) as nom from song where lower(artist) not like '%presley%' and id != ? order by random() limit 2",(x["id"],))
        row=self.cur.fetchall()
        print(row)
        malist=list(row)
        print(malist)
        malist.append(x)
        print(malist)
        k=[0,1,2]
        random.shuffle(k)
        print(k)
        return {"bon": x,"list":[malist[k[0]],malist[k[1]],malist[k[2]]]}
