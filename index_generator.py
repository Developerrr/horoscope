# coding: utf-8

from horoscope import generate_prophecies
from datetime import datetime as dt

def generate_page(head, body, a):
	page = "<html>" + head + body + a + "</html>"
	return page

def generate_head(title):
	head = "<meta charset='utf-8'>" + "<title>" + title + "</title>"
	return "<head>" + head + "</head>"

def generate_body(header, paragraphs):
	body = "<h1>" + header + "</h1>"
	i = 0
	while i < len(paragraphs):
		body = body + "<p>" + paragraphs[i] + "</p>"
		i = i + 1
	return "<body>" + body + "</body>"

def generate_hyperlink(link, title):
	a = "<a href="+ link + ">" + title + "</a>"
	return a

def save_page(title, header, paragraphs, link, link_title, output="index.html"):
	fp = open(output, "w")
	today = dt.now().date()
	page = generate_page(
		head=generate_head(title),
		body=generate_body(header=header, paragraphs=paragraphs),
		a = generate_hyperlink(link=link, title=link_title)
	)
	print(page, file=fp)
	fp.close()

title = "Гороскоп"
header = "Ваши предсказания на" + dt.now().strftime("%Y-%m-%d") 
link = "https://developerrr.github.io/horoscope/about.html"
link_title = "О реализации"

save_page(title, header, generate_prophecies(3,4), link, link_title,)