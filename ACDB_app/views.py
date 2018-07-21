from django.shortcuts import render
import requests
import json
from .models import Source

# Create your views here.
def index(request):
	if request.method=='POST':
		form=AccountForm(request.POST)
		if form.is_valid():
			return redirect('../getsource/'+request.POST['userId'])
	else:
		form=AccountForm()
		return render(request, 'ACDB_app/index.html',{'form': form})

def getSource(request,input):
	uri="https://judgeapi.u-aizu.ac.jp/solutions/users/"+input
	r=requests.get(uri)
	results=[]
	for x in r.json():
		res=getCode(x['judgeId'])
		res.version=x['version']
		res.judgeDate=x['judgeDate']
		res.codeSize=x['codeSize']
		res.server=x['server']
		res.rating=x['rating']
		results.append(res)
	return render(request, 'ACDB_app/test.html',{'Input':input, 'Sources':results})
	
def getCode(id):
	uri="https://judgeapi.u-aizu.ac.jp/reviews/"+str(id)
	r=requests.get(uri).json()
	res=Source(
			judgeId=r['judgeId'],
			userId=r['userId'], 
			problemId=r['problemId'],
			language =r['language'],
			cpuTime = r['cpuTime'],
			memory = r['memory'],
			submissionDate = r['submissionDate'],
			policy = r['policy'],
			sourceCode = r['sourceCode'],
			reviewed = r['reviewed'],
		)
	return res