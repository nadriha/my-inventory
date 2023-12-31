from django.urls import path
from main.views import create_product_flutter, register_flutter, show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user
from main.views import logout_user, delete_item, tambah_item, kurang_item, edit_product, get_product_json, add_item_ajax
from main.views import delete_item_ajax
app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'), 
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('register-flutter/', register_flutter, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('delete_item/<int:id>/', delete_item, name='delete_item'),
    path('tambah_item/<int:id>/', tambah_item, name='tambah_item'),
    path('kurang_item/<int:id>/', kurang_item, name='kurang_item'),
    path('edit-product/<int:id>', edit_product, name='edit_product'),
    path('get-product/', get_product_json, name='get_product_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete-item-ajax/<int:id>/', delete_item_ajax, name='delete_item_ajax'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
]