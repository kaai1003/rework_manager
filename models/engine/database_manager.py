#!/usr/bin/python3
"""Database connection module"""

import psycopg2
from psycopg2 import sql

DB_CONFIG = {
    "dbname": "rework_db",
    "user": "postgres",
    "password": "postgres",
    "host": "localhost",
    "port": 5432,
}

def get_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print(f"Error connecting to PostgreSQL: {e}")
        return None
