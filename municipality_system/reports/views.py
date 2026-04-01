from django.shortcuts import render
from .models import Issue

def report_issue(request):
    if request.method == 'POST':
        issue = Issue.objects.create(
            issue_type=request.POST.get('issue_type'),
            description=request.POST.get('description'),
            location=request.POST.get('location'),
        )
        return render(request, 'report_success.html', {'issue': issue})
    
   
    return render(request, 'report_issue.html')


def track_issue(request):
    issue = None

    if request.method == 'POST':
        issue_id = request.POST.get('issue_id')
        try:
            issue = Issue.objects.get(id=issue_id)
        except Issue.DoesNotExist:
            issue = None
    
   
    return render(request, 'track_issue.html', {'issue': issue})


