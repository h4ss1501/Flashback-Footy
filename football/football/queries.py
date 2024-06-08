from models import Result, db

def get_top_scorers():
    query = """
    SELECT scorer, COUNT(*) as goals
    FROM goalscorers
    GROUP BY scorer
    ORDER BY goals DESC
    LIMIT 10;
    """
    result = db.session.execute(query)
    return [row for row in result]

def get_most_successful_teams():
    query = """
    SELECT winner, COUNT(*) as wins
    FROM results
    WHERE tournament = 'FIFA World Cup'
    GROUP BY winner
    ORDER BY wins DESC
    LIMIT 10;
    """
    result = db.session.execute(query)
    return [row for row in result]

