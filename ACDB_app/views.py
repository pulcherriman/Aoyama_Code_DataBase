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
		)
		
		results.append(res)
	return render(request, 'ACDB_app/test.html',{'Sources':results})
	