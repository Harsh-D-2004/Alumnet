from neo4j import GraphDatabase

URI = "bolt://localhost:7687"
AUTH = ("neo4j", "harshroot")

def get_driver():
    with GraphDatabase.driver(URI, auth=AUTH) as driver:
        driver.verify_connectivity()
        return driver