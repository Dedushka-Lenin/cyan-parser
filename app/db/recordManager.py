from app.db.dbConnector import DbConnector

class RecordManager():
    def __init__(self, table_name):
        
        self.connection, self.cursor = DbConnector().get()

        self.table_name = table_name


    def check(self, conditions):
        columns = conditions.keys()
        values = [conditions[column] for column in columns]

        condition_str = " AND ".join([f"{col} = ?" for col in columns])

        query = f"SELECT 1 FROM {self.table_name} WHERE {condition_str} LIMIT 1"
        self.cursor.execute(query, values)
        exists = self.cursor.fetchone() is not None
        return exists


    def create(self, data):
        columns = data.keys()
        values = [data[column] for column in columns]

        placeholders = ", ".join(["?"] * len(values))
        columns_str = ", ".join(columns)

        query = f"INSERT INTO {self.table_name} ({columns_str}) VALUES ({placeholders})"
        self.cursor.execute(query, values)
        self.connection.commit()

        return self.cursor.lastrowid


    def delete(self, id):
        query = f"DELETE FROM {self.table_name} WHERE id = ?"
        self.cursor.execute(query, (id,))
        self.connection.commit()


    def update(self, update_fields, id):
        set_clause = ", ".join([f"{k} = ?" for k in update_fields.keys()])
        values = list(update_fields.values()) + [id]
        query = f"UPDATE {self.table_name} SET {set_clause} WHERE id = ?"
        self.cursor.execute(query, values)
        self.connection.commit()


    def get(self, conditions=None):
        if conditions:
            condition_clauses = []
            values = []
            for col, val in conditions.items():
                condition_clauses.append(f"{col} = ?")
                values.append(val)
            where_clause = " WHERE " + " AND ".join(condition_clauses)
        else:
            where_clause = ""
            values = []

        query = f"SELECT * FROM {self.table_name}{where_clause}"
        self.cursor.execute(query, values)
        rows = self.cursor.fetchall()

        col_names = [description[0] for description in self.cursor.description]

        result_list = [dict(zip(col_names, row)) for row in rows]
        return result_list