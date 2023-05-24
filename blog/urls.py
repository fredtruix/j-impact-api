from django.urls import path
from .apis import BlogListView, UserBlogList, blog_update_delete, Group_list_create, read_update_delete_group


urlpatterns = [
  path("blogs/", BlogListView.as_view(), name="blogs"),
  path("blogs/<int:id>/", UserBlogList, name="user-blogs"),
  path("blog/<int:user_id>/<int:blog_id>/", blog_update_delete, name="user-blog"),
  path('groups/', Group_list_create, name='groups'),
  path('group/<int:user_id>/<int:group_id>/', read_update_delete_group, name='groups')
]
