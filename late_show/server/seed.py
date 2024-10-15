from app import app, db 
from models import Guest, Episode, Appearance , EpisodeSchema, GuestSchema, AppearanceSchema
from datetime import datetime

guest_data = [
        {"year": 1999, "occupation": "actor", "date": "1/11/99", "group": "Acting", "guest": "Michael J. Fox"},
        {"year": 1999, "occupation": "Comedian", "date": "1/12/99", "group": "Comedy", "guest": "Sandra Bernhard"},
        {"year": 1999, "occupation": "television actress", "date": "1/13/99", "group": "Acting", "guest": "Tracey Ullman"},
        {"year": 1999, "occupation": "actor", "date": "1/14/99", "group": "Acting", "guest": "John Stamos"},
        {"year": 1999, "occupation": "actor", "date": "1/15/99", "group": "Acting", "guest": "Hugh Jackman"},
        {"year": 1999, "occupation": "actor", "date": "1/16/99", "group": "Acting", "guest": "Leonardo DiCaprio"},
        {"year": 1999, "occupation": "actor", "date": "1/17/99", "group": "Acting", "guest": "David Schwimmer"},
        {"year": 1999, "occupation": "actor", "date": "1/18/99", "group": "Acting", "guest": "Matthew Perry"},
        {"year": 1999, "occupation": "musician", "date": "1/19/99", "group": "Music", "guest": "Tina Turner"},
        {"year": 1999, "occupation": "actor", "date": "1/20/99", "group": "Acting", "guest": "Ben Stiller"},
        {"year": 1999, "occupation": "actress", "date": "1/21/99", "group": "Acting", "guest": "Drew Barrymore"},
        {"year": 1999, "occupation": "television host", "date": "1/22/99", "group": "Television", "guest": "Oprah Winfrey"},
        {"year": 1999, "occupation": "actress", "date": "1/23/99", "group": "Acting", "guest": "Cameron Diaz"},
        {"year": 1999, "occupation": "musician", "date": "1/24/99", "group": "Music", "guest": "Will Smith"},
        {"year": 1999, "occupation": "comedian", "date": "1/25/99", "group": "Comedy", "guest": "Chris Rock"},
        {"year": 1999, "occupation": "television actor", "date": "1/26/99", "group": "Acting", "guest": "Matthew McConaughey"},
        {"year": 1999, "occupation": "actress", "date": "1/27/99", "group": "Acting", "guest": "Halle Berry"},
        {"year": 1999, "occupation": "actor", "date": "1/28/99", "group": "Acting", "guest": "Johnny Depp"},
        {"year": 1999, "occupation": "comedian", "date": "1/29/99", "group": "Comedy", "guest": "Jerry Seinfeld"},
        {"year": 1999, "occupation": "television host", "date": "1/30/99", "group": "Television", "guest": "David Letterman"},
        {"year": 1999, "occupation": "actor", "date": "1/31/99", "group": "Acting", "guest": "Will Ferrell"},
        {"year": 1999, "occupation": "actress", "date": "2/1/99", "group": "Acting", "guest": "Gwyneth Paltrow"},
        {"year": 1999, "occupation": "singer", "date": "2/2/99", "group": "Music", "guest": "Britney Spears"},
        {"year": 1999, "occupation": "actor", "date": "2/3/99", "group": "Acting", "guest": "Josh Hartnett"},
        {"year": 1999, "occupation": "actor", "date": "2/4/99", "group": "Acting", "guest": "Jude Law"},
        {"year": 1999, "occupation": "actor", "date": "2/5/99", "group": "Acting", "guest": "Owen Wilson"},
        {"year": 1999, "occupation": "singer", "date": "2/6/99", "group": "Music", "guest": "Backstreet Boys"},
        {"year": 1999, "occupation": "actress", "date": "2/7/99", "group": "Acting", "guest": "Scarlett Johansson"},
        {"year": 1999, "occupation": "actor", "date": "2/8/99", "group": "Acting", "guest": "Ben Affleck"},
        {"year": 1999, "occupation": "musician", "date": "2/9/99", "group": "Music", "guest": "Eminem"},
        {"year": 1999, "occupation": "actor", "date": "2/10/99", "group": "Acting", "guest": "Vince Vaughn"},
        {"year": 1999, "occupation": "singer", "date": "2/11/99", "group": "Music", "guest": "Christina Aguilera"},
        {"year": 1999, "occupation": "actor", "date": "2/12/99", "group": "Acting", "guest": "Jake Gyllenhaal"},
        {"year": 1999, "occupation": "comedian", "date": "2/13/99", "group": "Comedy", "guest": "Ricky Gervais"},
        {"year": 1999, "occupation": "television host", "date": "2/14/99", "group": "Television", "guest": "Ellen DeGeneres"},
        {"year": 1999, "occupation": "actor", "date": "2/15/99", "group": "Acting", "guest": "Ryan Reynolds"},
        {"year": 1999, "occupation": "singer", "date": "2/16/99", "group": "Music", "guest": "Alicia Keys"},
        {"year": 1999, "occupation": "musician", "date": "2/17/99", "group": "Music", "guest": "Shakira"},
        {"year": 1999, "occupation": "actor", "date": "2/18/99", "group": "Acting", "guest": "Natalie Portman"},
        {"year": 1999, "occupation": "actor", "date": "2/19/99", "group": "Acting", "guest": "Anne Hathaway"},
        {"year": 1999, "occupation": "television actress", "date": "2/20/99", "group": "Acting", "guest": "Megan Fox"},
        {"year": 1999, "occupation": "actor", "date": "2/21/99", "group": "Acting", "guest": "Tom Hanks"},
        {"year": 1999, "occupation": "comedian", "date": "2/22/99", "group": "Comedy", "guest": "Adam Sandler"},
        {"year": 1999, "occupation": "actor", "date": "2/23/99", "group": "Acting", "guest": "Denzel Washington"},
        {"year": 1999, "occupation": "singer", "date": "2/24/99", "group": "Music", "guest": "Rihanna"},
        {"year": 1999, "occupation": "actor", "date": "2/25/99", "group": "Acting", "guest": "Samuel L. Jackson"},
        {"year": 1999, "occupation": "actress", "date": "2/26/99", "group": "Acting", "guest": "Jennifer Aniston"},
        {"year": 1999, "occupation": "actor", "date": "2/27/99", "group": "Acting", "guest": "George Clooney"},
        {"year": 1999, "occupation": "musician", "date": "2/28/99", "group": "Music", "guest": "Katy Perry"},
    ]


with app.app_context():
    for guest in guest_data:
        # Check if the episode already exists
        episode_instance = Episode.query.filter_by(year=guest['year'], group=guest['group']).first()

        if not episode_instance:
            # Create a new Episode instance if it doesn't exist
            episode_instance = Episode(
                date=datetime.strptime(guest['date'], '%m/%d/%y').date(),
                number=len(Episode.query.all()) + 1,  # Generate a unique number
                year=guest['year'],
                group=guest['group']
            )
            db.session.add(episode_instance)
            db.session.commit()  # Commit to save the episode before adding the appearance
        
        # Check if the guest already exists
        guest_instance = Guest.query.filter_by(name=guest['guest']).first()

        if guest_instance:
            # Check if the appearance already exists
            appearance_instance = Appearance.query.filter_by(episode=episode_instance, guest=guest_instance).first()
            if not appearance_instance:
                new_appearance = Appearance(
                    rating=guest.get('rating', 5),  # Assuming a default rating if not provided
                    episode=episode_instance,
                    guest=guest_instance
                )
                db.session.add(new_appearance)

    db.session.commit()