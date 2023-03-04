from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all() # Esto consulta todos los datos de una tabla
    permission_classes = [permissions.AllowAny] # Allow any va a decir que cualquier cliente o usuario va poder preguntar datos al servidor
    serializer_class = ProjectSerializer