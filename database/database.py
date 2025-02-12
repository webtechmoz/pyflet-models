import multiprocessing.process
from manage_sql import SQLITE
from manage_sql.Utils.SQLITE import Column, Filter, ColumnData
import multiprocessing

class Database:
    def __init__(
        self,
        database: str
    ):
        self.db = SQLITE(
            database=database
        )

        if database == 'database':
            self.create_table(
                table_name='users',
                columns=[
                    self.db.Column(
                        name='username',
                        not_null=True,
                        column_type=self.db.Column_types.text
                    ),
                    self.db.Column(
                        name='email',
                        not_null=True,
                        column_type=self.db.Column_types.text
                    ),
                    self.db.Column(
                        name='usertype',
                        not_null=True,
                        column_type=self.db.Column_types.text
                    ),
                    self.db.Column(
                        name='password',
                        not_null=True,
                        column_type=self.db.Column_types.text
                    ),
                    self.db.Column(
                        name='status',
                        not_null=True,
                        column_type=self.db.Column_types.text
                    )
                ]
            )
    
    def create_table(self, table_name: str, columns: list[Column]):
        process = multiprocessing.Process(
            target=self.db.create_table,
            args=(table_name, columns),
            daemon=True
        )
        process.start()
    
    def insert_data(self, table_name: str, data_query: list[ColumnData]):
        process = multiprocessing.Process(
            target=self.db.insert_data,
            args=(table_name,data_query),
            daemon=True
        )
        process.start()
    
    def select_data(self, table_name: str, columns: list[str] = ['*'], condition: Filter = None):
        return self.db.select_data(
            tablename=table_name,
            columns=columns,
            condition=condition
        )