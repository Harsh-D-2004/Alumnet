from models.company import Company

def create_company_node(tx , company : Company):

    query = """
    CREATE (a:Company {
    id: randomUUID(),
    name: $name,
    industry: $industry,
    location: $location,
    website: $website,
    hr_contact: $hr_contact,
    alumni_count: $alumni_count})
    RETURN a.id AS id
"""
    result = tx.run(query , **company.model_dump())
    if result is None:
        return None
    return result.single()['id']


def get_comapny_node(tx , id):

    query = """
        MATCH (a:Company {id: $id})
        RETURN a
    """

    result = tx.run(query , id = id)
    record = result.single()
    if record is None:
        return None
    return record['a']

def update_company_node(tx , id , company : Company):

    query = """
        MATCH (a:Company {id: $id})
        SET a.name = $name,
        a.industry = $industry,
        a.location = $location,
        a.website = $website,
        a.hr_contact = $hr_contact,
        a.alumni_count = $alumni_count
        RETURN a.id AS id
        """

    result = tx.run(query , id = id , **company.model_dump())
    return result.single()['id']

def delete_company_node(tx , id):

    query = """
    MATCH (a:Company {id: $id})
    DELETE a
    RETURN $id AS id
    """

    result = tx.run(query , id = id)
    return result.single()['id']



