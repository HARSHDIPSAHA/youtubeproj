import csv
from youtube_comment_downloader import YoutubeCommentDownloader, SORT_BY_POPULAR
from main import Url
'''def makeit():
    url = f"{Url}"  # Replace with your YouTube URL
    downloader = YoutubeCommentDownloader()
    comments = downloader.get_comments_from_url(url, sort_by=SORT_BY_POPULAR)

    # Open a CSV file to write the comments
    try:
        with open('youtube_comments.csv', mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Merged Comment'])  # Single header for the merged column

            for idx, comment in enumerate(comments, start=1):
                text = comment['text']
                likes = comment['votes']
                user_id = comment['author']
                published_at = comment['time']

                # Merge all columns into a single column with the specified format
                merged_comment = f"comment is {text} with likes {likes} with user_id {user_id} and published  {published_at}"

                writer.writerow([merged_comment])'''
               

  