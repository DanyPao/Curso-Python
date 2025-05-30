from django.urls import path
from .views import home,  pedidos,  detalle_pedido,  crear_pedido, buscar, about, logout_view#, clientes
from .views import ClienteCreateView, ClienteListView, ClienteDetailView, ClienteUpdateView, ClienteDeleteView
from .views import UserRegisterView, UserLoginView
from .views import UserChangeView, AvatarUpdateView
from .views import perfil

urlpatterns = [
    path("home/", home, name="home"),
    #path("clientes/", clientes, name="clientes"),
    path("pedidos/", pedidos, name="pedidos"),
    #path("clientes/<int:cliente_id>/", detalle_cliente, name="detalle_cliente"),
    path("pedidos/<int:pedido_id>/", detalle_pedido, name="detalle_pedido"),
    #path("crear_cliente/", crear_cliente, name="crear_cliente"),
    path("crear_pedido/", crear_pedido, name="crear_pedido"),
    path('buscar/', buscar, name='buscar'),
    path("about/", about, name="about"),

    path("externo/cbv/alta_cliente/", ClienteCreateView.as_view(), name="cbv_alta_cliente"),
    path("externo/cbv/lista_clientes/", ClienteListView.as_view(), name="cbv_lista_clientes"),
    path("externo/cbv/cliente/<int:pk>/", ClienteDetailView.as_view(), name="cbv_detalle_cliente"),
    path("externo/cbv/cliente/<int:pk>/actualizar/", ClienteUpdateView.as_view(), name="cbv_actualizar_cliente"),
    path("externo/cbv/cliente/<int:pk>/eliminar/", ClienteDeleteView.as_view(), name="cbv_eliminar_cliente"),

    path("", UserLoginView.as_view(), name="index"),
    path("externo/registration/signup/", UserRegisterView.as_view(), name="signup"),
    path("externo/registration/login/", UserLoginView.as_view(), name="login"),
    path("externo/registration/logout/", logout_view, name="logout"),

    path("externo/registration/change_user/", UserChangeView.as_view(), name="change_user"),
    path("externo/registration/upload_avatar/", AvatarUpdateView.as_view(), name="upload_avatar"),
    path("perfil/", perfil, name="perfil"),
]

