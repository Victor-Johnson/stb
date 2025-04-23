from fastapi import APIRouter ,status
from typing import Optional
from utils import messages
from schemas import house

router = APIRouter(prefix='/v1/houses',
                   tags=['house'])

@router.get(
    '/{estate}/all',
    tags=['house','Estate'],
    status_code=status.HTTP_200_OK,
    summary='Retrieve all Houses Based on the Estate',
    response_description= 'List of Avaliable Houses within an Estate',
    description='This GET endpoint fetches all records of houses that are within the parsed estate'
)
def get_all_estate(request:house.estateFetch):
    """
    This endpoint fetches all Houses Dependent on the Estate being Called.
    """
    request.estate(['Admin.estate_id'])
    return {
        "status_code": status.HTTP_200_OK,
        "message": messages["1"],
        "Output" : request 
    }

@router.get(
    '/{estate}/{id}',
    tags =['house'],
    status_code= status.HTTP_200_OK,
    summary= 'Retrieve a House by ID in an Estate',
    response_description= 'List of Avaliable House within an Estate',
    description= 'GET endpoint to fetch a specific House by ID '
)
def fetch_house_id(estate:str,id:int):
    pass


@router.post('/{estate}/create_house',
             status_code= status.HTTP_201_CREATED,
             summary='Creating a House for an Estate',
             response_description='Success Message upon creating a user successfully',
             description='POST ENDPOINT to create Houses for owners')
def create_house(estate:str):
    pass

@router.patch('/{estate}/{id}',
              tags = ['house'],
              status_code= status.HTTP_200_OK,
              summary='Update or change the records of a House',
              description='PATCH ENDPOINT to change the records of a House')
def patch_house(estate:str,id=int):
    pass

