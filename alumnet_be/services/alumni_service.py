from models.alumni import Alumni

def create_alumni_node(tx , alumni: Alumni):

    query = """
        CREATE (a:Alumni {
        id: randomUUID(),
        name: $name,
        passout_year: $passout_year,
        contact: $contact,
        email: $email,
        linkedin: $linkedin
    })
    RETURN a.id AS id
"""

    result = tx.run(query , **alumni.model_dump())
    return result.single()['id']

def get_alumni_node(tx , alumni_id):

    query = """
        MATCH (a:Alumni {id: $id})
        RETURN a
        """

    result = tx.run(query , id=alumni_id)
    record = result.single()
    if(record is None):
        return None
    return record['a']

def update_alumni_node(tx , alumni_id , alumni:Alumni):

    query = """
        MATCH (a:Alumni {id: $id})
        SET a.name = $name,
        a.passout_year = $passout_year,
        a.contact = $contact,
        a.email = $email,
        a.linkedin = $linkedin
        RETURN a.id AS id
        """

    result = tx.run(query , id=alumni_id , **alumni.model_dump())
    return result.single()['id']

def delete_alumni_node(tx , alumni_id):

    query = """
        MATCH (a:Alumni {id: $id})
        DELETE a
        RETURN $id AS id
        """

    result = tx.run(query , id=alumni_id)
    return result.single()['id']