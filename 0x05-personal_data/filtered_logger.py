#!/usr/bin/env python3
""" principal main """
from typing import List
import re
import logging
import os
import mysql.connector
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


class RedactingFormatter(logging.Formatter):
    """ Clase de formateador de redacción
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """ constructor """
        self.fields = fields
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        """ valores de filtro en registros de registro entrantes """
        return filter_datum(self.fields, self.REDACTION,
                            super().format(record), self.SEPARATOR)


def filter_datum(fields: List[str],                 redaction: str,
                 message: str,
                 separator: str) -> str:
    """ return the log
    message """
    for item in fields:
        message = re.sub(fr'{item}=.+?{separator}',
                         f'{item}={redaction}{separator}', message)
    return message


def get_logger() -> logging.Logger:
    """ metodo
    logger """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    handler.setFormatter(RedactingFormatter(PII_FIELDS))
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ funcion solicitud
    db """
    return mysql.connector.connect(
        host=os.environ.get('PERSONAL_DATA_DB_HOST', 'localhost'),
        database=os.environ.get('PERSONAL_DATA_DB_NAME', 'root'),
        user=os.environ.get('PERSONAL_DATA_DB_USERNAME'),
        password=os.environ.get('PERSONAL_DATA_DB_PASSWORD', ''))


def main():
    """ funcion 
    principal """
    d_b = get_db()
    curco = d_b.curco()
    curco.execute("SELECT * FROM users;")
    result = curco.fetchall()
    for row in result:
        message = f"name={row[0]}; " + \
                  f"email={row[1]}; " + \
                  f"phone={row[2]}; " + \
                  f"ssn={row[3]}; " + \
                  f"password={row[4]};"
        print(message)
        log_record = logging.LogRecord("my_logger", logging.INFO,
                                       None, None, message, None, None)
        formatter = RedactingFormatter(PII_FIELDS)
        formatter.format(log_record)
    curco.close()
    d_b.close()


if __name__ == "__main__":
    main()
