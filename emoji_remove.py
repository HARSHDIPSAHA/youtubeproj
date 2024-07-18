import pandas as pd
import emoji
import re

def remove_emoji(text):
    # Use regex to remove emojis
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # emoticons
        u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        u"\U0001F680-\U0001F6FF"  # transport & map symbols
        u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        u"\U00002700-\U000027BF"  # Dingbats
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U00002600-\U000026FF"  # Miscellaneous Symbols
        u"\U0001F700-\U0001F77F"  # Alchemical Symbols
        u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
        u"\U0001F680-\U0001F6FF"  # Transport and Map Symbols
        u"\U0001F600-\U0001F64F"  # Emoticons
        u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
        u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
        u"\U00002700-\U000027BF"  # Dingbats
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

# Read the CSV file
df = pd.read_csv('H:\data science roadmap\langchain\youtubeproj\youtube_comments.csv')

# Remove emojis from the 'Comment' column
df['Comment Text'] = df['Comment Text'].astype(str).apply(remove_emoji)

# Save the cleaned DataFrame to a new CSV file with UTF-8 encoding
df.to_csv('cleaned_file.csv', index=False, encoding='utf-8')
