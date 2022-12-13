#Abdias Tellez and Luis Gonzalez

import sqlite3
from sqlite3 import Error
from unittest import result


def getProductCount(_conn):
    sql =_conn.execute('''SELECT COUNT() FROM "cve-products"''')
    count = sql.fetchone()[0]
    return count
    
def getUuid(_conn):
    sql = _conn.execute('''SELECT COUNT() FROM "cve-vendors-products"''')
    count = sql.fetchone()[0]
    return count

def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")



#runs sqlite query to populate file
def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")

    sql = _conn.execute('SELECT * FROM "cve-products"')
    table = sql.fetchall()

    text_file = open("output/1.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46} \n'.format(table[i][0], table[i][1])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

#runs sqlite query to populate file
def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")

    sql = _conn.execute("""select cve_id, summary,
     access_vector, access_complexity, pub_date 
     from cveitems """)
    table = sql.fetchall()

    text_file = open("output/2.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46} {:<7} {:>7} \n'.format(table[i][0], table[i][1], table[i][2], table[i][3])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

#runs sqlite query to populate file
def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")

    sql = _conn.execute("""select product, 
    cve_id from `cve-vendors-products` as cvp,
     `cve-products` as cp where cvp.vendor = "{}" 
     and cvp.product = cp.vulnerable_product""")
    table = sql.fetchall()

    text_file = open("output/3.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46} {:<7}\n'.format(table[i][0], table[i][1], table[i][2])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

#runs sqlite query to populate file
def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")

    sql = _conn.execute("""select cvp.vendor, count(ci.cve_id)
                          from cveitems as ci, `cve-products` as cp, `cve-vendors-products` as cvp
                          where ci.cve_id = cp.cve_id and cp.vulnerable_product = cvp.product
                          group by cvp.vendor
                          ORDER BY COUNT(ci.cve_id) DESC""")
    table = sql.fetchall()

    text_file = open("output/4.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46} \n'.format(table[i][0], table[i][1])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

#runs sqlite query to populate file
def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")

    sql = _conn.execute("""select distinct count(product) 
                          from `cve-vendors-products` 
                          """)         
    table = sql.fetchall()

    text_file = open("output/5.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} \n'.format(table[i][0])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

#runs sqlite query to populate file
def Q6(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")

    sql = _conn.execute("""SELECT 'cveitems'.cve_id
                            FROM 'cveitems'
                            WHERE 'cveitems'.cve_id  NOT IN
                                (SELECT cve-vendor.cve_id 
                                FROM 'cve-vendors-products'
                                UNION
                                SELECT 'cve-vendors-products'.cve_id 
                                FROM cveitems)""")
    table = sql.fetchall()

    text_file = open("output/6.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46}\n'.format(table[i][0], table[i][1])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

#runs sql query to DELETE from db
#deletes summary if empty
def Q7(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q7")

    sql = _conn.execute("""DELETE FROM cveitems 
                          WHERE 
                            summary = ''""")
    table = sql.fetchall()

    text_file = open("output/7.out", "a")

    #for loop
    text_file.write("deleted")

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

#runs sql query to DELETE from db
def Q8(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q6")

    sql = _conn.execute("""DELETE FROM cveitems 
                          WHERE 
                            summary = ''""")
    table = sql.fetchall()

    text_file = open("output/6.out", "a")

    text_file.write("deletion complete") #writes
    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

#runs sql query to DELETE
def Q9(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q9")

    sql = _conn.execute("""DELETE FROM 'cve-vendors-products' 
                          WHERE 
                            product = 'smarty'""")
    table = sql.fetchall()

    text_file = open("output/7.out", "a")

    text_file.write("deletion complete") #writes
    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q10(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q10")

    sql = _conn.execute("""DELETE FROM 'cve-vendors-products' 
                          WHERE 
                            product = 'openfind'""")

    text_file = open("output/10.out", "a")

    text_file.write("deletion complete") #writes
    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q11(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q11")

    sql = _conn.execute("""DELETE FROM cveitems
                          WHERE 
                            cwe_code = ' '""")

    text_file = open("output/11.out", "a")


    #close file
    text_file.write("deleted.")
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q12(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q12")

    sql = _conn.execute('SELECT cve_id, summary FROM cveitems WHERE cvss > 7;')
    table = sql.fetchall()

    text_file = open("output/12.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46} \n'.format(table[i][0], table[i][1])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q13(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q13")

    sql = _conn.execute("""SELECT cve_id, mod_date, cwe_name 
                            FROM cveitems 
                            WHERE access_authentication = "NONE";""")
    table = sql.fetchall()

    text_file = open("output/13.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46} {:<7}\n'.format(table[i][0], table[i][1], table[i][2])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q14(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q14")

    sql = _conn.execute("""SELECT cve_id, pub_date 
                            FROM cveitems 
                            WHERE impact_integrity = "HIGH";""")
    table = sql.fetchall()

    text_file = open("output/14.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46}\n'.format(table[i][0], table[i][1])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q15(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q15")

    sql = _conn.execute("""SELECT cve_id, cwe_name 
                        FROM cveitems 
                        WHERE summary 
                        LIKE "%vulnerability%"; """)
    table = sql.fetchall()

    text_file = open("output/15.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46}\n'.format(table[i][0], table[i][1])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q16(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q16")

    sql = _conn.execute("""SELECT vendor, product 
                            FROM 'cve-vendors-products'
                            WHERE product LIKE "%security%";""")
    table = sql.fetchall()

    text_file = open("output/16.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46} \n'.format(table[i][0], table[i][1])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q17(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q17")

    sql = _conn.execute("""SELECT product 
                            FROM 'cve-vendors-products'
                            WHERE vendor = "cobblerd";""")
    table = sql.fetchall()

    text_file = open("output/17.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10}\n'.format(table[i][0])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")



#insert function
def Q18(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q18")

    sql = _conn.execute("""INSERT INTO 'cve-vendors-products' (vendor, product) VALUES ("Microsoft", "Windows");
    """)
    table = sql.fetchall()

    text_file = open("output/18.out", "a")

    text_file.write("inserted!") #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q19(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q19")

    sql = _conn.execute("""SELECT cve_id, mod_date FROM cveitems WHERE access_complexity = "HIGH";
                          
    """)
    table = sql.fetchall()

    text_file = open("output/19.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46}\n'.format(table[i][0], table[i][1])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")


def Q20(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q20")

    sql = _conn.execute("""SELECT cve_id, cwe_code, summary FROM cveitems WHERE access_vector = "NETWORK";""")
    table = sql.fetchall()

    text_file = open("output/20.out", "a")

    #for loop
    for i in range(len(table)):
      row = '{:>10} {:<46} {:<7}\n'.format(table[i][0], table[i][1], table[i][2])
      text_file.write(row) #writes

    #close file
    text_file.close()

    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"cve.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        Q1(conn)
        Q2(conn)
        Q3(conn)
        Q4(conn)
        Q5(conn)
        # Q6(conn)
        Q7(conn)
        Q8(conn)
        Q9(conn)
        Q10(conn)
        Q11(conn)
        Q12(conn)
        Q13(conn)
        Q14(conn)
        Q15(conn)
        Q16(conn)
        Q17(conn)
        Q18(conn)
        Q19(conn)
        Q20(conn)

    closeConnection(conn, database)


if __name__ == '__main__':
    main()
