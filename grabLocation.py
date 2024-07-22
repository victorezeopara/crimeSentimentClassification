import spacy

def extract_locations(sentence):
    # Load the spaCy English NER model
    nlp = spacy.load("en_core_web_sm")

    # Process the sentence with the NER model
    doc = nlp(sentence)

    # Extract locations identified by the NER model
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]

    return locations

# Example usage
