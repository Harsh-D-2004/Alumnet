import json


def get_graph_context(tx):
    query = """
    MATCH (a:Alumni)-[r:WORKED_AT]->(c:Company)
    RETURN 
        a.id AS alumni_id,
        a.name AS alumni_name,
        a.passout_year AS passout_year,
        a.contact AS contact,
        a.email AS email,
        a.linkedin AS linkedin,
        
        c.id AS company_id,
        c.name AS company_name,
        c.industry AS industry,
        c.location AS location,
        c.website AS website,
        c.hr_contact AS hr_contact,
        c.alumni_count AS alumni_count,

        r.from AS start_year,
        r.to AS end_year,
        r.placement_type AS placement_type,
        r.job_title AS job_title,
        r.department AS department
    """
    results = tx.run(query)

    context = []
    for row in results:
        record = {
            "alumni": {
                "id": row["alumni_id"],
                "name": row["alumni_name"],
                "passout_year": row["passout_year"],
                "contact": row["contact"],
                "email": row["email"],
                "linkedin": row["linkedin"],
            },
            "company": {
                "id": row["company_id"],
                "name": row["company_name"],
                "industry": row["industry"],
                "location": row["location"],
                "website": row["website"],
                "hr_contact": row["hr_contact"],
                "alumni_count": row["alumni_count"],
            },
            "employment": {
                "from": row["start_year"],
                "to": row["end_year"],
                "placement_type": row["placement_type"],
                "job_title": row["job_title"],
                "department": row["department"],
            }
        }
        context.append(record)
    return context

def preprocess_context(record):
    print(type(record))
    # record = json.loads(record)
    alumni = record['alumni']
    company = record['company']
    emp = record['employment']

    return (
        f"{alumni['name']}, who graduated in {alumni['passout_year']}, worked at "
        f"{company['name']} ({company['industry']} industry, located in {company['location']}) "
        f"as a {emp['job_title']} in the {emp['department']} department from {emp['from']} to {emp['to']} "
        f"via {emp['placement_type']} placement. "
        f"Contact: {alumni['email']}, Phone: {alumni['contact']}, LinkedIn: {alumni['linkedin']}. "
        f"Company HR: {company['hr_contact']}."
    )