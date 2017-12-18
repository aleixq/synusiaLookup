import csv
import sys
sys.path.insert(0, './googlebooks')
import googlebooks


api = googlebooks.Api()
#api.list('isbn:0596007973')

'''
input from a csv like:
$cat titleAuthor.csv
author,title,publisher
Jack London, Martin Eden,akal
Alexander Berkman, El mito bolchevique,

outs to titleAuthor-out.csv

'''

isbns = []
csv_fields_in = ['author','title','publisher']
csv_fields_out = ['author','title','publisher','isbn','metainfo']
with open('titleAuthor-out.csv', 'w') as csvout:
  writer = csv.DictWriter(csvout, fieldnames=csv_fields_out)
  writer.writeheader()
  with open('titleAuthor.csv', newline='', encoding='utf8') as csvin:
    reader = csv.DictReader(csvin, delimiter=',')
    for row in reader:
      author = row['author'].strip()
      title = row['title'].strip()
      publisher = row['publisher'].strip()
      # query of https://developers.google.com/books/docs/v1/using#q
      results = api.list('inauthor:"'+author+'"+intitle:"'+ title+'"+inpublisher:"'+ publisher+'"',)
      #print('inauthor:"' + author + '"+intitle:"' + title + '"')
      #print(results)
      if results['totalItems'] > 0:
	# Gets something like: https://www.googleapis.com/books/v1/volumes?q=inauthor:%22Jack%20London%22+intitle:%22%20Martin%20Eden%22
        out_row = {'author' : author, 'title' : title, 'isbn' : results['items'][0]['volumeInfo']['industryIdentifiers'][0]['identifier'],'metainfo' : results['items'][0]['volumeInfo']['title'] + " - " + results['items'][0]['volumeInfo']['authors'][0]}
      else:
        out_row = {'author' : author, 'title' : title, 'isbn' : '!!!!'}
      isbns.append(out_row)
      writer.writerow(out_row)
#print(isbns)

