"""..."""

import sqlite3
import typing as tp

from config.env import DATABASE

from models.tenders import TenderRow


class Database:
    """..."""

    def __init__(self, db_name: str = DATABASE):
        self.name = db_name
        self.cnxn = sqlite3.connect(
            db_name,
            check_same_thread=False,
        )
        self.cursor = self.cnxn.cursor()
        self.run_migrations()
        self.commit()

    def run_migrations(self):
        """DB Migrations"""
        self.create_tables()
        self.seed()

    def create_tables(self):
        """Create tables"""
        sql_qs = """
            CREATE TABLE
                IF NOT EXISTS tenders (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    number VARCHAR(255) NOT NULL,
                    link VARCHAR(255) NOT NULL,
                    description VARCHAR(255) NOT NULL,
                    end_date VARCHAR(255) NOT NULL,
                    starting_price VARCHAR(255) NOT NULL,
                    region VARCHAR(255) NOT NULL
                );
            CREATE INDEX IF NOT EXISTS
            idx_tender_numbers ON tenders (
                    number
                );
        """
        self.cursor.executescript(sql_qs)

    def seed(self):
        """Load initial data"""
        print("Creating dummy data")

    def insert_tenders(self, rows: tp.List[TenderRow]):
        """
        Description:
        ---
        Insert Tenders in bulk

        Parameters
        ---
        tenders: [TenderRow]
        """
        id_rows = self.cursor.execute("SELECT number FROM tenders;").fetchall()
        ids = [id_row[0] for id_row in id_rows]
        rows = [row for row in rows if row[0] not in ids]
        sql_qs = """
                INSERT INTO tenders (
                    number,
                    link,
                    description,
                    end_date,
                    starting_price,
                    region)
                VALUES
                    (?, ?, ?, ?, ?, ?);
        """
        self.cursor.executemany(
            sql_qs,
            rows,
        )

    def select_tenders(
        self,
        limit: int,
        offset: int = 0,
    ) -> tp.List[TenderRow]:
        """
        Description:
        ---
        Insert Tenders in bulk

        Parameters
        ---

        Returns
        ---
        [TenderRow]
        """
        sql_qs = """
                SELECT
                    id,
                    number,
                    link,
                    description,
                    end_date,
                    starting_price,
                    region
                FROM tenders
                LIMIT ? OFFSET ?
            """
        return self.cursor.execute(
            sql_qs,
            (limit, offset),
        ).fetchall()

    def count_tenders(self) -> int:
        """..."""
        sql_qs = "SELECT count(id) FROM tenders"
        return self.cursor.execute(sql_qs).fetchone()[0]

    def commit(self):
        """Commit database transactions"""
        self.cnxn.commit()

    def close(self):
        """Close databases connection"""
        self.cnxn.close()

    def rollback(self):
        """Rollback database transactions"""
        self.cnxn.rollback()
