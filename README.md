# Task Management API

## Endpoints

### CREATE TASK

Creating a new task and posting it to the **tasks** table

#### Example request body:

```json
{
  "title": "new task",
  "description": "example for documentation purposes",
  "status": "pending",
  "assigned_to": 2
}
```

#### Response body:

```json
{
  "id": 4,
  "title": "new task",
  "description": "example for documentation purposes",
  "status": "pending",
  "assigned_to": 2
}
```
#### Response headers:
```text
 content-length: 113 
 content-type: application/json 
 date: Fri,12 Jun 2026 09:09:30 GMT 
 server: uvicorn 
 ```

 #### Status codes:

---

### UPDATE TASK

Updating a task and posting changes the **tasks** table

#### Example request body:

```json
{
  "title": "updated task",
  "description": "updated task for documentation purposes",
  "status": "in_progress",
  "assigned_to": 1
}
```

#### Response body:

```json
{
  "id": 4,
  "title": "updated task",
  "description": "updated task for documentation purposes",
  "status": "in_progress",
  "assigned_to": 1
}
```
#### Response headers:
```text
 content-length: 126 
 content-type: application/json 
 date: Fri,12 Jun 2026 09:28:48 GMT 
 server: uvicorn 
 ```

---

### GET TASK BY ID

Returning the task matching the inputted task id from the **tasks** table

#### Example request body:

```json
{
  "task_id": 4
}
```

#### Response body:

```json
{
  "id": 4,
  "title": "updated task",
  "description": "updated task for documentation purposes",
  "status": "in_progress",
  "assigned_to": 1
}
```
#### Response headers:
```text
 content-length: 126 
 content-type: application/json 
 date: Fri,12 Jun 2026 09:34:48 GMT 
 server: uvicorn 
 ```

---

### LIST TASKS

Returning all the tasks from the **tasks** table

#### Response body:

```json
[
  {
    "id": 4,
    "title": "updated task",
    "description": "updated task for documentation purposes",
    "status": "in_progress",
    "assigned_to": 1
  },
  {
    "id": 3,
    "title": "fill form",
    "description": "fill and submit completion form",
    "status": "completed",
    "assigned_to": 2
  }
]
```
#### Response headers:
```text
 content-length: 242 
 content-type: application/json 
 date: Fri,12 Jun 2026 09:37:14 GMT 
 server: uvicorn 
 ```
---

### DELETE TASK

Deleting the task matching the inputted task id from the **tasks** table

#### Example request body:

```json
{
  "task_id": 4
}
```

#### Response body:

```json
null
```
#### Response headers:
```text
 content-length: 4 
 content-type: application/json 
 date: Fri,12 Jun 2026 09:38:50 GMT 
 server: uvicorn 
 ```

---

 ## Status codes:

**201**: Successful Response<br>
**422**: Validation Error<br>
**400**: User Assignment Error<br>
**404**: Not Found

---

## Architecture Diagram

[ Client Request ]<br>
↓<br>
[ FastAPI Route Layer ]<br>
↓<br>
[ Service Layer (Business Logic) ]<br>
↓<br>
[ Repository Layer (DB Operations) ]<br>
↓<br>
[ PostgreSQL Database ]