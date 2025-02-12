from manage_sql import SQLITE
from manage_sql.Utils.SQLITE import Column, Filter, ColumnData

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

            if not self.select_data(table_name='users'):
                self.insert_data(
                    table_name='users',
                    data_query=[
                        self.db.ColumnData(
                            column='username',
                            value='Admin'
                        ),
                        self.db.ColumnData(
                            column='password',
                            value=self.db.encrypt_value(
                                value='Admin'
                            )
                        ),
                        self.db.ColumnData(
                            column='status',
                            value='Active'
                        )
                    ]
                )
    
    def create_table(self, table_name: str, columns: list[Column]):
        self.db.create_table(
            tablename=table_name,
            columns=columns
        )
    
    def insert_data(self, table_name: str, data_query: list[ColumnData]):
        self.db.insert_data(
            tablename=table_name,
            insert_query=data_query
        )
    
    def select_data(self, table_name: str, columns: list[str] = ['*'], condition: Filter = None):
        return self.db.select_data(
            tablename=table_name,
            columns=columns,
            condition=condition
        )