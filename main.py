from fastapi import FastAPI
app = FastAPI()
l = []
#get
@app.get("/courses")
def available_courses():
    return{"message":"the following are the courses available","courses":l}
@app.post("/add_course/{course_name}")
def add_course(course_name:str):
    l.append(course_name)
    return{"message",f"course added:{course_name}"}
@app.put("/update_course/{old_course_name}/{new_course_name}")
def update_course(old_course_name:str, new_course_name: str):
    if old_course_name in l:
        index = l.index(old_course_name)
        l[index] = new_course_name
        return{"message": f"course update: {old_course_name}to {new_course_name}"}
    else:
        return{"message": f"course not found: {old_course_name}"}
@app.delete("/delete_course/{course_name}")
def delete_course(course_name:str):
    if course_name in l:
        l.remove(course_name)
        return{"message": f"course deleted:{course_name}"}
    else:
        return{"message": f"course not found:{course_name}"}

