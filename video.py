import csv

class Video:
    def __init__(self, creator, music, likes, comments, saved, tags, date_watched, video_url):
        self.creator = creator
        self.music = music
        self.likes = likes
        self.comments = comments
        self.saved = saved
        self.tags = tags
        self.date_watched = date_watched
        self.video_url = video_url

    def save_to_csv(self, filename):
        with open(f'video_watch_info/{filename}', 'a', newline='', encoding="utf-8") as csvfile:
            fieldnames = ['creator', 'music', 'likes', 'comments', 'saved', 'tags', 'date_watched', 'video_url']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow(
                {'creator': self.creator, 'music': self.music, 'likes': self.likes, 'comments': self.comments,
                 'saved': self.saved, 'tags': self.tags, 'date_watched': self.date_watched, 'video_url': self.video_url})

    def __str__(self):
        return ("Creator: {0}, Music: {1}, Likes: {2}, Comments: {3}, Saved: {4}, Tags: {5}, Date Watched: {6}, Video URL: "
                "{7}").format(self.creator, self.music, self.likes, self.comments, self.saved, str(self.tags),
                              self.date_watched, self.video_url)
