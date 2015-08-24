import urllib2,sys
from bs4 import BeautifulSoup
from itertools import izip
import csv

GH_Data = []
f = open("gh_data.csv", "a+")
mywriter = csv.writer(f)

headers = ('Article_Title','Upvoted','Post_Link','Date_Posted','Source','Who_Posted','Topics','Commented','GH_Link','Summary')
mywriter.writerow(headers)
# 1030

hdr = {'User-Agent':'Mozilla/5.0'}

# for i in range(1,1030):

for i in range(982,1030):	
	address = ('http://growthhackers.com/latest/page/' + str(i))
	print i
	req = urllib2.Request(address,headers=hdr)
	soup = BeautifulSoup(urllib2.urlopen(req).read())

	titles = soup.select('.title > a')
	scores = soup.select('.score')
	item_info = soup.select('.post-item-info')
	sources = soup.select('.grey')
	topics = soup.select('.post-item-topics')
	comments = soup.select('.show-post-modal')
	summaries = soup.select('.post-details ')

	for title,score,item,source,topic,comment,summary in izip(titles, scores,item_info,sources,topics,comments,summaries):
		title_only = (title.getText()).encode('utf-8')
		if 'Ask ' in title_only:
			link_half = (((title.encode('utf-8')).split('href="')[1]).split('"')[0]).strip()
			link_only = 'https://growthhackers.com' + link_half
		else:	
			link_only = (((title.encode('utf-8')).split('href="')[1]).split('"')[0]).strip()
		# link_excel = ('=HYPERLINK("' + link_only + '")').encode('utf-8')
		score_only = (score.getText()).encode('utf-8')
		date_only = ((item.getText()).split('by')[0]).strip().encode('utf-8')
		source_only = (source.getText()).encode('utf-8')
		name_only = ((((item.getText()).split('by')[1]).split(' in ')[0]).strip()).encode('utf-8')
		topic_only = (((topic.getText()).split('in ')[1]).strip()).encode('utf-8')

		comment_string = ((str(comment.getText())))
		if comment_string == 'Start a discussion' or comment_string == 'Answer':
			comment_only = 0
		else:
			comment_only = ((str(comment_string)).split(' comment')[0]).strip().encode('utf-8')

		summary_string = ((summary.getText()).strip()).encode('utf-8')
		if summary_string == '':
			summary_only = 'None'
		else:
			summary_only = summary_string

		gh_link_end = ((str(comment).split('href="')[1]).split('"')[0]).strip().encode('utf-8')
		gh_link_only = 'https://growthhackers.com' + gh_link_end
		
		data = (title_only,score_only,link_only,date_only,source_only,name_only,topic_only,comment_only,gh_link_only, summary_only)
		mywriter.writerow(data)
f.close()