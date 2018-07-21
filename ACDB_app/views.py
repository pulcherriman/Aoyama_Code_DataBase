from django.shortcuts import render
import requests
import json
from .model import Source

# Create your views here.
def index(request):
	return render(request, 'ACDB_app/test.html', {})

def getSource(request):
	uri="https://judgeapi.u-aizu.ac.jp/solutions/users/tsuka325"
	r=requests.get(uri)
	results=[]
	for x in r.json():
		res=Source(
			judgeId=x['judgeId'],
			userId=x['userId'], 
			problemId=x['problemId'],
			language =x['language'],
			version =x['version'],
			submissionDate = x['submissionDate'],
			judgeDate = x['judgeDate'],
			cpuTime = x['cpuTime'],
			memory = x['memory'],
			codeSize = x['codeSize'],
			server = x['server'],
			policy = x['policy'],
			rating = x['rating'],
			review = x['review']
		)
		
		results.append(res)
	return render(request, 'ACDB_app/test.html',{'Sources':results})
	