import datetime
import pymysql
import csv

# Open database connection
from bitcoin import PADDING

domain = ""
user = ""
password = user
db_name = ""
start_date = '2017-04-19 18:50:47'
end_date = '2018-02-26 16:22:54'

db = pymysql.connect(domain, user, password, db_name)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "SELECT bd_user.id,bd_user.first_name as 'First Name'," \
      "bd_user.last_name as 'Last Name'," \
      "bd_address.address1 as 'Address 1'," \
      "bd_address.address2 as 'Address 2'," \
      "bd_country.name as 'Country', " \
      "bd_province.name as 'State',bd_address.zip as 'Zip Code',bd_user.email as 'Email',  bd_address.phone as 'Phone',bd_user.created_at as 'Created date' " \
      "FROM  bd_user " \
      " join bd_address  on bd_user.id=bd_address.user_id  " \
      "join bd_province on bd_province.id=bd_address.province_id " \
      "join bd_country on bd_country.id=bd_province.country_id where bd_user.created_at > '%s' " \
      "and bd_user.created_at < '%s'" % (start_date, end_date)
# try:
# Execute the SQL command
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
header = ['ID', 'First Name', 'Last Name', 'Address 1', 'Address 2', 'Country', 'State', 'Zip Code', 'Email', 'Phone',
          'Created date']
file_name = 'egrifta' + datetime.date.today().strftime("%Y-%m-%d") + '.csv'
with open(file_name, 'w') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',')
    spamwriter.writerow(header)
    for row in results:
        spamwriter.writerow(row)

# except:
#     print("Error: unable to fetch data")

db.close()
import base64

from Crypto.Cipher import AES
from Crypto import Random

key = b'Sixteen byte key'
iv = Random.new().read(AES.block_size)
cipher = AES.new(key, AES.MODE_CFB, iv)
msg = iv + cipher.encrypt(b'Attack at dawn')
print(msg)


import os, random, struct
def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CFB, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))
out_file='out'+file_name
encrypt_file(key,file_name,out_file)