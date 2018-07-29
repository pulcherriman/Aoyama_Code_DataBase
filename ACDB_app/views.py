from django.shortcuts import render
import requests
import json
from .models import Source
from .forms import AccountForm
from django.shortcuts import *
from datetime import datetime
import re

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

	#雑な問題名抽出
	uri="https://judgeapi.u-aizu.ac.jp/resources/descriptions/en/"+str(res.problemId)
	r=requests.get(uri).json()['html']
	res.problemName=re.search(">.*</(h|H)1>" ,r).group()[1:-5]
	
	return render(request, 'ACDB_app/detail.html',{'Data':res})

def submit(request):
	code='''
#include <bits/stdc++.h>
using namespace std;
int main(){
	cout<<"Hello, world!"<<endl;
	return 0;
}
'''
	lang='cpp'
	r=execute(code,lang)
	if(r.status_code==200):
		return render(request, 'ACDB_app/submit.html',{"res":r.json()})
	else:
		return render(request, 'ACDB_app/submit.html',{"res":"Failed"})

def execute(code,lang):
	r=requests.post('http://api.paiza.io/runners/create',
		{
			'source_code' : code,
			'language' : lang,
			'api_key' : 'guest',
		}
	)
	if r.status_code == 200:
		while True:
			r=requests.get('http://api.paiza.io/runners/get_status',
				params={
					'id' : r.json()['id'],
					'api_key' : 'guest'
				}
			)
			if r.json()['status'] == 'completed':
				break;

		r=requests.get('http://api.paiza.io/runners/get_details',
			params={
				'id' : r.json()['id'],
				'api_key' : 'guest'
			}
		)
	return r;