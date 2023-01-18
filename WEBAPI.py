from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

studentDB =[
{
"rollNo" : "11",
"name" : "John Dennis",
'section' : 'A'
},
{
"rollNo" : "12",
"name" : "Phil Coulson",
'section' : 'B'
}
]


@app.route("/",methods=['GET'])    
def welcome() :
    return "Welcome to Python Webservices"


@app.route("/student/getStudents",methods=['GET'])
def getStudents():
    return jsonify({"stud":studentDB})


@app.route("/student/getStudent/<rollNo>",methods=['GET'])
def getStudentDetails(rollNo) :
    student = [stud for stud in studentDB if(stud['rollNo']==rollNo)]
    print(student)
    return jsonify({"stud":student})


@app.route("/student/updateStudent/<rollNo>",methods=['PUT'])
def updateStudentDetails(rollNo) :
    student = [stud for stud in studentDB if(stud['rollNo']==rollNo)]

    if('rollNo' in request.json) :
        print("Student Available")
    if('name' in request.json) :
        student[0]['name'] = request.json['name']
    return jsonify({"stud":student[0]})



@app.route("/student/addStudent",methods=['POST'])
def addStudent() :
    student = {
        "rollNo" : request.json['rollNo'],
        "name" :  request.json['name'],
        'section' : request.json['section']
    }
    studentDB.append(student)
    return jsonify({"stud":studentDB})
    
@app.route("/student/removeStudent/<rollNo>",methods=['DELETE'])
def removeStudent(rollNo) :
    student = [stud for stud in studentDB if(stud['rollNo']==rollNo)]
    if(len(student) > 0):
        studentDB.remove(student[0])
    return jsonify({"stud":student})





if(__name__=="__main__") :
    app.run()