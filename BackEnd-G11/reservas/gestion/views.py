from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from .models import Categoria, Producto
from .serializers  import PruebaSerializer, CategoriaSerializer, ProductoSerializer, paginationSerializer, ProductoConCategoriaSerializer

class PruebaView(APIView):
    def get(self, request):
        data =[{
            'nombre':'diversion',
            'id':1
        },{
            'nombre':'entretenimiento',
            'id':2
        }]

        return Response(data=data)
    
    def post(self, request: Request):
        print(request.data)
        data= request.data
        data_serializada= PruebaSerializer(data=data)
        resultado = data_serializada.is_valid()
        if resultado is True :
            return Response(data={
            'message':'Se recibio la prueba'
            })
        else:
            return Response(data={
            'message':'La data es invalida',
            'content': data_serializada.errors
            })

        
    
class CategoriaView(APIView):
    def post(self,request:Request):
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(request.data)
        data = request.data
        print(data)
        data_serializada =  CategoriaSerializer(data=data)
        resultado= data_serializada.is_valid()

        if resultado:
            print(data_serializada.validated_data)
            #nueva_categoria = Categoria(nombre= data.get('nombre'), habilitado=data.get('habilitado'))
            nueva_categoria = Categoria(**data_serializada.validated_data)
            nueva_categoria.save()

            return Response(data={
                'message':'Categoria creada exitosamente'
            })
        else:
            return Response(data={
                'message':'Error al crear la categoria',
                'content': data_serializada.errors
            })
        
    def get(self, request:Request):
        categorias=Categoria.objects.all()
        data_serializada= CategoriaSerializer(instance=categorias, many=True)

        return Response(data={            
            'content': data_serializada.data
        })
    
class UnaCategoriaView (APIView):
    def get(self, request:Request, id):
        print(id)
        categoria_encontrada=Categoria.objects.filter(id=id).first()
        if not categoria_encontrada:
            return Response(data={
                'message':'categoria no existe'
            },status=404)
        
        resultado=CategoriaSerializer(instance=categoria_encontrada)

        return Response(data={
            'content':resultado.data
        })
            
    def put(self, request:Request, id):
        categoria_encontrada=Categoria.objects.filter(id=id).first()
        if not categoria_encontrada:
            return Response(data={
                'message':'categoria no existe'
            },status=404)
        data=request.data
        data_serializada=CategoriaSerializer(data=data)
        if data_serializada.is_valid():
            categoria_encontrada.nombre=data_serializada.validated_data.get('nombre')
            categoria_encontrada.habilitado= data_serializada.validated_data.get('habilitado')
            categoria_encontrada.save()
            return Response(data={
                'message':'Categoria actualizada'
            })
        else:
            return Response(data={
                'message':'Error al actualizar la categoria',
                'content': data_serializada.errors
            })

        
    def delete(self, request:Request, id):
        categoria_encontrada=Categoria.objects.filter(id=id).first()
        if not categoria_encontrada:
            return Response(data={
                'message':'categoria no existe'
            },status=404)
        
        resultado = Categoria.objects.filter(id=id).delete()

        return Response(data={
                'message':'Categoria eliminada exitosamente'
                
            })



class ProductosView(APIView):
    def post(self, request:Request):
        data = request.data
        data_serializada=ProductoSerializer(data=data)
        if data_serializada.is_valid():
            nuevo_producto=data_serializada.save()
            resultado= ProductoSerializer(instance=nuevo_producto)
            return Response(data={
                'message':'Producto creado exitosamente',
                'content': resultado.data
            },status=status.HTTP_201_CREATED)
        else:
            return Response(data={
                'message':'Error al crear el producto',
                'content': data_serializada.errors
            },status=status.HTTP_400_BAD_REQUEST)
        
    def get(self, request:Request):
        print(request.query_params)

        page = int(request.query_params.get('page'))
        perPage = int(request.query_params.get('perPage',10))

        skip = (page-1 ) * perPage
        take = perPage * page

        print(skip)
        print(take)
        total_productos= Producto.objects.count()
        productos=Producto.objects.all()[skip:take]
        informacion_paginacion = paginationSerializer(total_productos, page, perPage)
        data_serializada=ProductoSerializer(instance=productos, many=True)
        return Response(data={
                'content': data_serializada.data,
                'pageInfo': informacion_paginacion
            },status=status.HTTP_200_OK)


class ProductosGenericView(ListAPIView):
    serializer_class= ProductoSerializer
    queryset= Producto.objects.all()

# Create your views here.

class unProductoView(APIView):
    def get(self, reques:Request, id):
        producto=Producto.objects.filter(id=id).first()
        if not producto:
                return Response(data={
                    'content':''
                }, status=status.HTTP_404_NOT_FOUND)
        resultado=ProductoConCategoriaSerializer(instance=producto)
        return Response(data={
            'content':resultado.data
        })
