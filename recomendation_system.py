import pandas as pd # type: ignore
from faker import Faker # type: ignore
import random

# Initialize Faker
fake = Faker()

# Define a list of sample movie titles
sample_movie_titles = [
    "The Great Adventure", "Mystery of the Stars", "Love in the Rain", 
    "Alien Invasion", "Journey Through Time", "The Dark Knight Returns", 
    "Underwater Secrets", "Space Odyssey", "Sunset Boulevard", "The Last Stand"
]

# Generate synthetic data
def generate_synthetic_data(num_users=100, num_items=50, num_interactions=1000):
    user_ids = [fake.user_name() for _ in range(num_users)]  # Generate fake user names
    movie_ids = random.choices(sample_movie_titles, k=num_items)  # Use sample movie titles
    
    # Generate random ratings between 1 and 5
    ratings = [random.randint(1, 5) for _ in range(num_interactions)]
    
    # Create data entries
    interactions = {
        'userId': random.choices(user_ids, k=num_interactions),
        'movieId': random.choices(movie_ids, k=num_interactions),
        'rating': ratings,
        'timestamp': [fake.date_time_this_year() for _ in range(num_interactions)]  # Generate timestamps
    }
    
    return pd.DataFrame(interactions)

# Generate synthetic data
num_users = 100  # Number of users
num_items = 50   # Number of movies/items
num_interactions = 1000  # Number of interactions (ratings)
synthetic_data = generate_synthetic_data(num_users, num_items, num_interactions)

# Save the synthetic data to a CSV file
synthetic_data.to_csv('synthetic_data.csv', index=False)

# Load the synthetic data
synthetic_data = pd.read_csv('synthetic_data.csv')

# Display the first few rows
print(synthetic_data.head())
