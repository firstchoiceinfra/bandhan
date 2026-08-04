import pandas as pd

# --- THE AI MATCHMAKING ENGINE ---

def calculate_compatibility_score(user_profile, potential_matches_list):
    """
    Analyzes multiple data points to generate an AI Match Score.
    """
    match_results = []
    
    for match in potential_matches_list:
        score = 0
        
        # 1. Religion & Core Values (High Priority: 40 Points)
        if user_profile['religion'] == match['religion']:
            score += 40
            
        # 2. Age Compatibility (Medium Priority: 30 Points)
        # Assuming the ideal age gap is between 0 to 4 years
        age_diff = abs(user_profile['age'] - match['age'])
        if age_diff <= 3:
            score += 30
        elif age_diff <= 5:
            score += 15
            
        # 3. Location / City Preference (20 Points)
        if user_profile['preferred_location'] == match['location']:
            score += 20
            
        # 4. Ecosystem & Lifestyle Match (10 Points)
        # Matching lifestyle choices like premium vs standard
        if user_profile['lifestyle_budget'] == match['lifestyle_budget']:
            score += 10
            
        match_results.append({
            "name": match['name'],
            "age": match['age'],
            "profession": match['profession'],
            "match_percentage": score,
            "image_url": match['image_url']
        })
        
    # Sort the results so the highest percentage match appears first
    sorted_matches = sorted(match_results, key=lambda x: x['match_percentage'], reverse=True)
    return sorted_matches

# --- EXAMPLE USAGE IN STREAMLIT ---
# (This runs when user clicks 'Run AI Smart Search')

user_data = {
    "age": 28, "religion": "Hindu", 
    "preferred_location": "Mumbai", "lifestyle_budget": "Premium"
}

mock_database_profiles = [
    {"name": "Priya", "age": 27, "religion": "Hindu", "location": "Mumbai", "lifestyle_budget": "Premium", "profession": "Doctor", "image_url": "..."},
    {"name": "Neha", "age": 25, "religion": "Hindu", "location": "Pune", "lifestyle_budget": "Standard", "profession": "Engineer", "image_url": "..."}
]

# Run the Engine
top_matches = calculate_compatibility_score(user_data, mock_database_profiles)

# Now loop through 'top_matches' and display them in your Streamlit Profile Cards!
