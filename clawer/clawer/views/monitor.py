#encoding=utf-8


from html5helper.decorator import render_template


def realtime_dashboard(request):
    return render_template("clawer/monitor/realtime_dashboard.html", request=request)
