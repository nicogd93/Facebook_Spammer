import mechanize,cookielib,re
br=mechanize.Browser()
cookie_jar=cookielib.CookieJar()
br.set_cookiejar(cookie_jar)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
br.set_handle_referer(True)
br.set_handle_robots(False)
br.open("http://m.facebook.com/login.php")
br.select_form(nr=0)
br.form['email']=raw_input("Email please: ")
br.form['pass']=raw_input("Password please: ")
br.submit()
if "Logout" in br.response().read():
  print "Successfuly Logged in...May the Spam Process Begin ;) "
else:
	print "Something is wrong with logging in.Sorry :( "
	quit()
link_to_spam=raw_input("Enter the messages link for the one you want to spam(m.facebook.com link only)\n: ")
def message(message):
		#Until now the link you have to use m.facebook.com Sorry.I'll fix that later
		global link_to_spam,br
		br.open(link_to_spam)
		html=br.response().read()
		fb_dtsg=re.search(r'name="fb_dtsg" value=.+" autocomplete?',html).group().replace('name="fb_dtsg" value=',"").replace('" autocomplete',"").replace('"',"")
		fb_dtsg=fb_dtsg[:fb_dtsg.find("=")]
		tids=re.search(r'tid=.+&?',link_to_spam).group().replace("tid=","").replace("&_rdr","")
		if "#!" in tids:
			tids=tids[:tids.find("#!")]
		data="fb_dtsg="+fb_dtsg+"&body="+message+"&send=Reply&tids="+tids
		br.addheaders=[('Referer',link_to_spam)]
		br.open("https://m.facebook.com/messages/send/?refid=12",data)
message1=raw_input("Message to send?: ")
print "\n"
for x in xrange(input("How many messages do you want to send?: ")):
	message(message1)
print "Spamming done :D"
