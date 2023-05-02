
def address_insert(connection, region, settlement, street, house, post_code):
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM addresses ORDER BY address_id DESC LIMIT 1;
            """
        )
        last_id = cursor.fetchone()
        if last_id is None:
            last_id = 0
        else:
            last_id = last_id[0]

        cursor.execute(
            """
            INSERT into addresses(address_id, region, settlement, street, house, post_code)
            values ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')
            """.format(last_id+1, region, settlement, street, house, post_code)
        )

def address_selection(connection, region='', settlement='', street='', house='', post_code=''):
    with connection.cursor() as cursor:
        cursor.execute(
            f"""
            SELECT * 
            from addresses 
            where region LIKE '%{region}%' and settlement LIKE '%{settlement}%' and street LIKE '%{street}%' and house LIKE '%{house}%' and post_code LIKE '%{post_code}%'
            """
        )
        all_addresses = cursor.fetchall()
        return all_addresses