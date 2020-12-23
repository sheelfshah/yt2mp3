import pafy
import urllib.request
import re
from pydub import AudioSegment
import os

def yt_search(s):
	html = urllib.request.urlopen(
		"https://www.youtube.com/results?search_query="+s.replace(" ", "+"))
	video_id = re.search(r"watch\?v=(\S{11})", html.read().decode())
	url = "https://www.youtube.com/" + video_id.group(0)
	return url

def download_url(url, folder="vids/"):
	vid = pafy.new(url)
	stream = vid.getbestaudio()
	stream.download(filepath=folder, quiet=True)
	return folder+stream.filename

def convert(f, format_="mp3"):
	song = AudioSegment.from_file(f)
	new_f = ".".join(f.split(".")[:-1]) + "." + format_
	song.export(new_f, format=format_) 
	return new_f

def get_song(s, folder="vids/", format_="mp3"):
	url =yt_search(s)
	f = download_url(url, folder)
	f = f.replace("../","")
	new_f = convert(f, format_)
	os.remove(f)
	return new_f