#
#import mysql.connector
# from mysql.connector import Error
# from mysql.connector import errorcode
# def convertToBinaryData(filename):
#     #Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#     return binaryData
# def insertBLOB(emp_id, name, photo, biodataFile):
#     print("Inserting BLOB into python_employee table")
#     try:
#         connection = mysql.connector.connect(host='localhost',
#                              database='python_db',
#                              user='pynative',
#                              password='pynative@#29')
#         cursor = connection.cursor(prepared=True)
#         sql_insert_blob_query = """ INSERT INTO `python_employee`
#                           (`id`, `name`, `photo`, `biodata`) VALUES (%s,%s,%s,%s)"""
#         empPicture = convertToBinaryData(photo)
#         file = convertToBinaryData(biodataFile)
#         # Convert data into tuple format
#         insert_blob_tuple = (emp_id, name, empPicture, file)
#         result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
#         connection.commit()
#         print("Image and file inserted successfully as a BLOB into python_employee table", result)
#
# except mysql.connector.Error as error:
# connection.rollback()
# print("Failed inserting BLOB data into MySQL table {}".format(error))
# finally:
# # closing database connection.
# if (connection.is_connected()):
#     cursor.close()
#     connection.close()
#     print("MySQL connection is closed")