"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from src.recommender import load_songs, recommend_songs, UserProfile, Song


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded  {len(songs)} songs")
    # Starter example profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "target_valence": 0.5,
        "target_dancebility": 0.5,
        "favorite_artists": set(["LoRoom"]),
    }

    user_profile_1 = {
        "favorite_genre": "lofi",
        "favorite_mood": "chill",
        "target_energy": 0.45,
        "target_valence": 0.6,
        "target_dancebility": 0.3,
        "favorite_artists": set(),
    }

    # Deep intense rock
    user_profile_2 = {
        "favorite_genre": "rock",
        "favorite_mood": "intense",
        "target_energy": 0.92,
        "target_valence": 0.38,
        "target_dancebility": 0.6,
        "favorite_artists": {"Voltline", "Crimson Riot"},
    }

    # Passionate country farmer
    user_profile_3 = {
        "favorite_genre": "country",
        "favorite_mood": "nostalgic",
        "target_energy": 0.4,
        "target_valence": 0.7,
        "target_dancebility": 0.48,
        "favorite_artists": {"Slow Stereo", "Paper Lanterns"},
    }

    # Dreamy electronic
    user_profile_4 = {
        "favorite_genre": "electronic",
        "favorite_mood": "dreamy",
        "target_energy": 0.55,
        "target_valence": 0.6,
        "target_dancebility": 0.7,
        "favorite_artists": {"LoRoom", "Orbit Bloom"},
    }
    # "happy" ↔ "melancholy" is NOT in MOOD_CLASHES
    adversarial_3 = {
        "favorite_genre": "classical",
        "favorite_mood": "happy",
        "target_energy": 0.3,
        "target_valence": 0.4,
        "target_dancebility": 0.3,
        "favorite_artists": set(),
    }
    # Genre doesn't exist in dataset, so no song gets the 26-pt bonus
    adversarial_2 = {
        "favorite_genre": "polka",
        "favorite_mood": "chill",
        "target_energy": 0.5,
        "target_valence": 0.5,
        "target_dancebility": 0.5,
        "favorite_artists": set(),
    }
    # Wants calm pop, but gets "Gym Hero" (energy 0.93) over acoustics/ambient
    adversarial_1 = {
        "favorite_genre": "pop",
        "favorite_mood": "chill",
        "target_energy": 0.1,
        "target_valence": 0.6,
        "target_dancebility": 0.3,
        "favorite_artists": set(),
    }

    all_profiles = [
        user_prefs,
        user_profile_1,
        user_profile_2,
        user_profile_3,
        user_profile_4,
        adversarial_3,
        adversarial_2,
        adversarial_1,
    ]
    for u_pref in all_profiles:
        output_recommendations(recommend_songs(u_pref, songs, k=5), u_pref)
    

def output_recommendations(recommendations, user_prefs):
    # recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 50)
    print("  User Preferences")
    print("=" * 50)
    for key, value in user_prefs.items():
        print(f"  {key}: {value}")

    print("\n" + "=" * 50)
    print("  Top Recommendations")
    print("=" * 50)
    for rank, (song, score, explanation) in enumerate(recommendations, 1):
        print(f"\n  #{rank}  {song['title']} by {song['artist']}")
        print(f"       Genre: {song['genre']}  |  Mood: {song['mood']}")
        print(f"       Score: {score:.2f}")
        print(f"       Reasons:")
        for reason in explanation.split("; "):
            print(f"         - {reason}")
    print("\n" + "=" * 50)
if __name__ == "__main__":
    main()
