# crimeSentimentClassification
This program is designed to crawl Nigerian news websites, retrieve recent crime data, and assign a severity score to each incident. The severity score ranges from 1 to 10, with 10 indicating cases involving fatalities or serious injuries. This program is part of a broader security application aimed at combating kidnapping and other severe crimes in Nigeria.

This is the dataset that was used in this project; The crime severity was determined from of the nigerian police force.

existing_crime_data = [
    ("Armed robbery in progress", 9),
    ("Vandalism in a deserted area", 4),
    ("Assault in a crowded street", 7),
    ("Burglary at a residential property", 8),
    ("Drug dealing near a school", 6),
    ("Shoplifting at a local store", 3),
    ("Carjacking in a parking lot", 9),
    ("Graffiti on public buildings", 2),
    ("Kidnapping near a playground", 10),
    ("Pickpocketing in a crowded market", 5),
    ("Breaking and entering into a business", 7),
    ("Domestic violence incident", 6),
    ("Cybercrime involving financial fraud", 8),
    ("Public intoxication and disorderly conduct", 3),
    ("Hate crime against a minority group", 7),
    ("Fraudulent online scheme", 8),
    ("Homicide in a residential neighborhood", 10),
    ("Arson at a community center", 9),
    ("Assault on a public official", 8),
    ("Embezzlement at a corporate office", 6),
    ("Hit and run accident involving pedestrians", 7),
    ("Illegal dumping in a nature reserve", 2),
    ("Stalking and harassment", 6),
    ("Counterfeiting operation discovered", 5),
    ("Robbery at a convenience store", 8),
    ("Extortion attempt against a business owner", 7),
    ("Trespassing on government property", 4),
    ("Identity theft and credit card fraud", 8),
    ("Noise complaints and disturbance", 2),
    # Add more examples as needed
]

# Additional data without using a loop
additional_crime_data = [
    ("Assault on public transportation", 6),
    ("Forgery at a local bank", 5),
    ("Illegal street racing", 3),
    ("Riot in a public square", 8),
    ("Animal cruelty in a park", 4),
    ("Fraudulent charity scam", 7),
    ("Assault at a sports event", 6),
    ("Embezzlement at a non-profit organization", 5),
    ("Arson at a forest reserve", 9),
    ("Drug trafficking operation uncovered", 8),
    # Add more examples as needed
]

# Additional data (continued)
more_additional_crime_data = [
    ("Cyberstalking and online harassment", 6),
    ("Counterfeit goods manufacturing", 5),
    ("Assault on a healthcare worker", 7),
    ("Illegal fishing in protected waters", 4),
    ("Bribery and corruption in government", 9),
    ("Extensive tax evasion scheme", 8),
    ("Environmental pollution violation", 5),
    ("Unlicensed gambling operation", 6),
    ("Hostage situation at a bank", 10),
    ("Insurance fraud scheme", 7),
    # Add more examples as needed
]

# Additional data (even more)
even_more_additional_crime_data = [
    ("Terrorist attack in a public place", 10),
    ("Child exploitation and abuse", 9),
    ("Human trafficking operation", 10),
    ("Large-scale drug production facility", 8),
    ("Major data breach and cyber attack", 9),
    ("Corruption within law enforcement", 8),
    ("Organized crime syndicate activity", 9),
    ("Illegal weapons trafficking", 8),
    ("Biohazardous material mishandling", 7),
    ("Mass public disturbance and rioting", 8),
    # Add more examples as needed
]
