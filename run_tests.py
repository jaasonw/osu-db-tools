from buffer import WriteBuffer
import buffer
import struct
import os
import unittest


class TestReadAndWriteBuffers(unittest.TestCase):

    buf = WriteBuffer()

    def clean_db(self):
        try:
            os.remove("test.db")
        except OSError:
            pass

    def test_bytes(self):
        print("testing read/write bytes")
        self.buf = WriteBuffer()
        test = 0x80
        self.buf.write_ubyte(test)

        self.clean_db()

        db = open("test.db", "wb")
        db.write(self.buf.data)
        db.close()

        with open("test.db", "rb") as db:
            read = buffer.read_ubyte(db)
        db.close()

        print(test, " : ", read)
        if (test == read):
            print("pass")
        else:
            print("fail")


    def test_string(self):
        print("testing read/write string")
        self.buf = WriteBuffer()
        test = "asdfasdfasdfasdf"
        self.buf.write_string(test)

        self.clean_db()

        db = open("test.db", "wb")
        db.write(self.buf.data)
        db.close()

        with open("test.db", "rb") as db:
            read = buffer.read_string(db)
        db.close()

        print(test, " : ", read)
        if (test == read):
            print("pass")
        else:
            print("fail")

    
