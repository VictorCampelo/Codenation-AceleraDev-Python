from rest_framework.decorators import api_view
from rest_framework.response import Response
from collections import Counter, OrderedDict

@api_view(['POST'])
def lambda_function(request):
    request_data = request.data.get('question')

    request_data = OrderedDict(Counter(request_data).most_common())

    sorted_qtd_list = []
    for value in request_data:
        for x in range(request_data[value]):
            sorted_qtd_list.append(value)

    return Response({"solution": sorted_qtd_list})