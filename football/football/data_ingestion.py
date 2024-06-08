import pandas as pd
from models import Shootout, Result, db
from app import create_app

app = create_app()

def load_data():
    with app.app_context():
        shootouts_df = pd.read_csv('shootouts.csv')
        for _, row in shootouts_df.iterrows():
            shootout = Shootout(
                date=row['date'],
                home_team=row['home_team'],
                away_team=row['away_team'],
                winner=row['winner'],
                first_shooter=row['first_shooter']
            )
            db.session.add(shootout)
        db.session.commit()

        

if __name__ == "__main__":
    load_data()
