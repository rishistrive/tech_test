from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from .models import ResourceCollection
from .forms import ResourceCollectionForm
import pandas as pd
import json
from django.shortcuts import redirect


class DataCollectionView(TemplateView):
    template_name = "core/data_collections.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        data['form'] = ResourceCollectionForm()
        data['resource_qs'] = ResourceCollection.objects.filter()
        return data

    def post(self, request):
        form = ResourceCollectionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('data_collection', permanent=True)
        else:
            return render(request, self.template_name, {'form': form})


class BuildingListTemplate(TemplateView):
    template_name = "core/building_list.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        resource_id = self.kwargs.get('resource_id')
        resource = get_object_or_404(ResourceCollection, pk=resource_id)
        df = pd.read_csv(resource.building_csv.path)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df = df.dropna(how='any', axis=0)
        df['id'] = df.loc[:, 'id'].map(int)
        data_dict = df.to_dict(orient="records")
        data['resource_id'] = resource_id
        data['buildings'] = data_dict
        return data


class DataVisualizationView(TemplateView):
    template_name = "core/visualization.html"

    def get_context_data(self, **kwargs):
        data = super().get_context_data()
        resource_id = self.kwargs.get('resource_id')
        building_id = self.kwargs.get('building_id')
        resource = get_object_or_404(ResourceCollection, pk=resource_id)
        res_df = pd.read_csv(resource.resource_csv.path)
        meters = res_df[res_df.building_id == building_id]
        data['units'] = meters.to_dict(orient="records")
        usage_df = pd.read_csv(resource.resource_usage_csv.path)
        res_list = list()
        new_data_units = list()
        for index, unit in enumerate(data['units']):
            tmp_df = usage_df
            tmp_df = tmp_df[tmp_df.meter_id == unit['id']]
            consumption = tmp_df.loc[:, 'consumption'].to_list()
            datetime = tmp_df.loc[:, 'reading_date_time'].to_list()
            if consumption and datetime:
                new_data_units.append(data["units"][index])
                res_list.append({'meter_id': unit['id'],
                                 'meter_type': unit['unit'],
                                 "data": {
                                     'consumption': consumption,
                                     'datetime': datetime,
                                 }})
        data['resources'] = json.dumps(res_list)
        data['units'] = new_data_units
        return data
