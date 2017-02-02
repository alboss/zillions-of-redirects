import os,errno

# declare the CSV file. It should be in the same directory as this script.
csv = '2files.csv'

# The static code that precedes the URL
part1 = '<%@ Language=\"VBScript\" %> \
\n \
<% \
\n \
Response.Status = \"301 Moved Permanently\" \
\n \
Response.AddHeader \"Location\", \"'

# the static code that follows the URL
part2 = '" \
\n \
Response.End \
\n \
%>'

# the URL we use if nothing is specified in the CSV
defaultURL = 'http://kingcounty.gov/depts/dnrp/solid-waste'

# open the CSV
with open(csv, 'r') as f:
	# loop through each line of the CSV
	for line in f:
		# split out the columns
		s = line.split(',')
		# make the directories if they don't exist
		os.makedirs(os.path.dirname(s[1]), exist_ok=True)
		# get the path and filename from column 2 so we cansave this
		with open(s[1], 'w') as w:
			# get the redirect URL from column 3
			specialURL = s[2].strip()
			# if there is a redirect URL then write it into the redirect file
			if s[2].strip():
				w.write(str(part1) + str(specialURL) + str(part2))
			# otherwise write the default URL into the redirect file
			else:
				w.write(str(part1) + str(defaultURL) + str(part2))