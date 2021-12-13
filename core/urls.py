from django.urls import path
from .views import BuildingListTemplate, DataCollectionView, DataVisualizationView


urlpatterns = [
    path('building/<int:resource_id>', BuildingListTemplate.as_view(), name="building_list"),
    path('visualization/<int:resource_id>/<int:building_id>', DataVisualizationView.as_view(), name="visualization"),
    path('', DataCollectionView.as_view(), name="data_collection"),

]
