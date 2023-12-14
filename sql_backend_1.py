# MySQL - python - query - processor
# # mysql.server start
# mysql.server stop
# mysql.server restart

import os
import re 
import mysql.connector as sql
from rich import print

class Sql_custom:
    cnx = None
    cursor = None
    
def connect():
    user1 = {
        "user" : "root" ,
        "password" : "rootpass",
        "host" : "127.0.0.1"
    }
    user2 = {
        "user" : "py2" ,
        "password" : "pypass",
        "host" : "127.0.0.1"
    }
    
    try:
        Sql_custom.cnx = sql.connect(**user2)

        c = Sql_custom.cnx.cursor()
        Sql_custom.cursor = c                   #   database = 'sys')
    except sql.Error as e:
        print(e)
        exit(0)

def query(q):

    print("---")
    Sql_custom.cursor.execute(q)
    # cursor.close()
    for i in Sql_custom.cursor:
        print(i)

def query_parse():
    state = True
    while state:
        s = input(">>> ")
        try:
            if s == "exit" or s == "EXIT":
                Sql_custom.cursor.close()
                state = False
                break
            else:
                query(parser_chk(s))
        except BaseException as err:
            print("[red]ERROR - [/red]", err , err.__traceback__.__str__ )

def parser_chk(s):

    dbase = {
            "0":"SHOW DATABASES;",
            "1":"USE sys;",
            "2":"SHOW TABLES;",
            "3":"BLANK",
            "9":"USE py",
            "s":"SELECT",
            "f":"FROM",
            "w":"WHERE",
            "d":"DROP",
            "t":"TABLE",
            "u":"UPDATE",
            "a":"ALTER",
            "af":"AFTER",
            "i":"INSERT",
            "c":"CREATE",
            "v":"VALUES",    
            "d":"DATABASE",
            "del":"DELETE",
            "de":"DESCRIBE",
            "ins":"INSERT INTO ",
            "ss":"SELECT * FROM",
            "h":"_help"
        }

    ls = s.split()
    strf =""
    # if len(ls) == 1:
    #     if ls[0] in dbase.keys():
    #         strf += dbase[ls[0]]

    # else:
    #     for i in ls:
    #         if i in dbase.keys():
    #             if i.isnumeric() and ls.index(i) != 0 :
    #                 strf += i + ' '
    #             elif re.match("\A_" , dbase[i] ):
    #                 dbase[i]()
    #             else :
    #                 strf += dbase[i] + ' '
    #             # if dbase[i][0] == "fx":
    #                 # dbase[i][1]()
    #             # if dbase[i]
                
    #         # else :
            #     strf += i + ' '

    for i in ls:
        if i in dbase.keys():
            if i.isnumeric() and ls.index(i) != 0 :
                strf += i + ' '
            elif re.match("\A_" , str(dbase[i].__name__)):
                dbase[i]()
            else :
                strf += dbase[i] + ' '
                # if dbase[i][0] == "fx":
                    # dbase[i][1]()
                # if dbase[i]
                
            # else :


    print(strf)
    return strf
    # _____
def _help():
    print()
def start():
    print("in start")
    try:
        os.system("mysql.server start")
    except BaseException as err:
        print("[red]error in starting servere[red]" , err)
        exit(0)

def shut():
    print("in shut")
    try:
        Sql_custom.cnx.close()
    except BaseException as err :
        print( "error in shutfx" ,err)
    try:
        Sql_custom.cursor.close()        
    except BaseException as err :
        print( "error in shutfx" ,err)
    try:
        os.system("mysql.server stop")
    except BaseException as err :
        print( "error in shutfx" ,err)
        exit(0)
    
def main():
    print("in main")
    # start()
    connect()
    query_parse()

if __name__=="__main__":

    print("Ver 1.1 \n [italic bold magenta]MYSQL[/italic bold magenta]" )
    main()
