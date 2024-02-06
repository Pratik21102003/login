import mysql.connector
class DB:
      def __init__(self):
         # connect to database
         try:
            self.conn=mysql.connector.connect(
            host='127.0.0.1',
         user='root',
            password=''
            )
            self.mycursor=self.conn.cursor()
         except:
            print('Connection error')
      def insert(self,name,email,password):
         self.mycursor.execute("""INSERT INTO coustomers.coustomer(name,email,password)
                              VALUES('{}','{}','{}')""".format(name,email,password))
         self.conn.commit()
      
      def check(self,email,password):
         self.mycursor.execute("""SELECT name FROM coustomers.coustomer
                               WHERE email='{}' AND password='{}' """.format(email,password))
         return self.mycursor.fetchall()
      
      def delete(self,email,password):
         self.mycursor.execute("""DELETE  FROM coustomers.coustomer
                               WHERE email='{}' AND password='{}' """.format(email,password))
         self.conn.commit()