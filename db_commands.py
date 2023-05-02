
def address_insert(connection, region, settlement, street, house, post_code):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM addresses ORDER BY address_id DESC LIMIT 1;
            """
        )
        last_id = cursor.fetchone()[0]
        if last_id is None:
            last_id = 0

        cursor.execute(
            """
            INSERT into addresses(address_id, region, settlement, street, house, post_code)
            values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
            """.format(last_id+1, region, settlement, street, house, post_code)
        )