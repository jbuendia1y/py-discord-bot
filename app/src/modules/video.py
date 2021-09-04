from urllib import parse, request
import re


def get_youtube_video(video_name: str) -> str:
    query = parse.urlencode({"search_query": video_name})
    url = "https://www.youtube.com/results?" + query

    html_content = request.urlopen(url)
    regex = r'url":"\/watch\?v=(.{11})'
    # Links in tag(script) on Html_Content
    video_id_list = re.findall(regex, html_content.read().decode())
    return "https://youtube.com/watch?v=" + video_id_list[0]
