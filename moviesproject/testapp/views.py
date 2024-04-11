from django.shortcuts import render

# Create your views here.
def information(request):
    return render(request,"testapp/balu.html")
def news_info(request):
    return  render(request,'testapp/index.html')
def movies_info(request):
    hed_msg='movie information'
    sub_msg1='eagle was nice'
    sub_msg2='og will coming very soon'
    sub_msg3='planini for next movie'
    type='movies'
    my_dict={'head_msg':hed_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,'type':type}
    return  render(request,'testapp/index.html',my_dict,)
def sports_info(request):
    hed_msg='movie information'
    sub_msg1='eagle was nice'
    sub_msg2='og will coming very soon'
    sub_msg3='planini for next movie'
    type="sports"
    my_dict={'head_msg':hed_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,"type":type}
    return  render(request,'testapp/index.html',my_dict)
def politics_info(request):
    hed_msg='movie information'
    sub_msg1='eagle was nice'
    sub_msg2='og will coming very soon'
    sub_msg3='planini for next movie'
    type="politics"
    my_dict={'head_msg':hed_msg,'sub_msg1':sub_msg1,'sub_msg2':sub_msg2,'sub_msg3':sub_msg3,"type":type}
    return  render(request,'testapp/index.html',my_dict)



