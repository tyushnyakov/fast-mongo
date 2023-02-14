

def employeeEntity(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "email": employee["email"],
        "age": employee["age"],
        "company": employee["company"],
        "join_date": employee["join_date"],
        "job_title": employee["job_title"],
        "gender": employee["gender"],
        "salary": employee["salary"],
    }


def populatedEmployeeEntity(employee) -> dict:
    return {
        "id": str(employee["_id"]),
        "name": employee["name"],
        "email": employee["email"],
        "age": employee["age"],
        "company": employee["company"],
        "join_date": employee["join_date"],
        "job_title": employee["job_title"],
        "gender": employee["gender"],
        "salary": employee["salary"],
    }


def employeeListEntity(employees) -> list:
    return [populatedEmployeeEntity(employee) for employee in employees]



