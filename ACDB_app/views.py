from django.shortcuts import render
import requests
import json
from .models import Source
from .forms import AccountForm
from django.shortcuts import *
from datetime import datetime

# Create your views here.
def index(request):
	if request.method=='POST':
		form=AccountForm(request.POST)
		if form.is_valid():
			return redirect('../user/'+request.POST['userId'])
	else:
		form=AccountForm()
		return render(request, 'ACDB_app/index.html',{'form': form})

def getUser(request,input):
	uri="https://judgeapi.u-aizu.ac.jp/solutions/users/"+input
	r=requests.get(uri)
	results=[]
	for x in r.json():
		res=Source(
			judgeId=x['judgeId'],
			userId=x['userId'],
			problemId=x['problemId'],
			language=x['language'],
			version=x['version'],
			submissionDate = x['submissionDate'],
			judgeDate=x['judgeDate'],
			cpuTime = x['cpuTime'],
			memory = x['memory'],
			codeSize=x['codeSize'],
			server=x['server'],
			policy = x['policy'],
			rating=x['rating'],
			review= x['review'],
		)
		res.submissionDateString=datetime.utcfromtimestamp(res.submissionDate/1000).strftime('%Y/%m/%d %H:%M:%S')
		res.cpuTimeString='{:.3f}'.format(res.cpuTime/1000)
		results.append(res)
	return render(request, 'ACDB_app/submissions.html',{'Input':input, 'Sources':results})
	
def getSubmission(request,id):
	uri="https://judgeapi.u-aizu.ac.jp/reviews/"+str(id)
	r=requests.get(uri).json()
	res=Source(
		judgeId=r['judgeId'],
		userId=r['userId'],
		problemId=r['problemId'],
		language=r['language'],
		submissionDate = r['submissionDate'],
		cpuTime = r['cpuTime'],
		memory = r['memory'],
		policy = r['policy'],
		sourceCode = r['sourceCode'],
	)
	res.submissionDateString=datetime.utcfromtimestamp(res.submissionDate/1000).strftime('%Y/%m/%d %H:%M:%S')
	res.cpuTimeString='{:.3f}'.format(res.cpuTime/1000)
	return render(request, 'ACDB_app/detail.html',{'Data':res})
	