from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('homepage/',homepage,name="homepage"),
    path('signup/',signup,name="signup"),
    path('activate/<uidb64>/<token>/',activate,name="activate"),
    path('subject/<unique_id>/',subjects,name="subjects"),

    path('subjects/<str:unique_id>/<str:username>/makeAdmin/',make_admin, name="make_admin"),
    path('subjects/<str:unique_id>/<str:username>/removeAdmin/',remove_admin, name="remove_admin"),
    path('subjects/<str:unique_id>/<str:username>/removeMember/',remove_member, name="remove_member"),

    path('<unique_id>/<int:subject_id>/',subject_page,name="subject_page"),
    path('<unique_id>/<int:subject_id>/delete/',delete_subject,name="delete_subject"),

    path('<unique_id>/<subject_id>/resource/',resource,name="resources"),
    path('<unique_id>/<subject_id>/<id>/read/',read_note,name="read_note"),
    path('<unique_id>/<subject_id>/<id>/resource/update/',resource_update,name="update_resource"),
    path('<unique_id>/<subject_id>/<id>/resource/delete/',resource_delete,name="delete_resource"),
    
    path('<unique_id>/<subject_id>/announcement/',announcement,name="announcement"),
    path('<unique_id>/<subject_id>/<id>/announcement/',announcement_page,name="announcement_page"),
    path('<unique_id>/<subject_id>/<id>/announcement/update/',announcement_update,name="update_announcement"),
    path('<unique_id>/<subject_id>/<id>/announcement/delete/',announcement_delete,name="delete_announcement"),

    path('<unique_id>/<subject_id>/assignments/',assignment,name="assignments"),
    path('<unique_id>/<subject_id>/<id>/assignment/',assignment_page,name="assignment_page"),
    path('<unique_id>/<subject_id>/<id>/assignment/update/',assignment_update,name="update_assignment"),
    path('<unique_id>/<subject_id>/<id>/assignment/delete/',assignment_delete,name="delete_assignment"),

    path('<unique_id>/<subject_id>/this_subject/',this_subject,name="this_subject")
]