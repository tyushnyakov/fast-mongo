from fastapi import HTTPException, status, APIRouter
from app import schemas
from app.database import Employee
from app.serializers.employeeSerializers import employeeListEntity
from pymongo.errors import DuplicateKeyError


router = APIRouter()


# Get All Employees
@router.get('/')
async def get_employees(limit: int = 10, page: int = 1, search: str = ''):
    skip = (page - 1) * limit
    pipeline = [
        {'$match': {}},
        {
            '$skip': skip
        }, {
            '$limit': limit
        }
    ]
    employees = employeeListEntity(Employee.aggregate(pipeline))
    return {
        'status': 'success',
        'results': len(employees),
        'employees': employees
    }


# Create Employee
@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_employee(employee: schemas.CreateEmployeeSchema):
    try:
        result = Employee.insert_one(employee.dict())
        pipeline = [
            {'$match': {'_id': result.inserted_id}},
        ]
        new_employee = employeeListEntity(Employee.aggregate(pipeline))[0]
        return new_employee
    except DuplicateKeyError:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=f"Employee with email: '{employee.email}' already exists")
