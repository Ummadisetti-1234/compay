# print('hi')
# f=open("c:\\Users\\Admin\\Desktop\\python\\demo.txt","r")
# # print(f.read())
# #f=open("c:\\Users\\Admin\\Desktop\\demo.py","r")
# #f=open("c:\Users\Admin\Desktop\\clerk.pdf","r")
# print(f.read())
# print("welcome")
# f.close()
# print('closed')
f=open("c:\\Users\\Admin\\Desktop\\demo1.json","x")
print("created")
import json 
student = {"Name": "Indrani", "Roll_no": "1", "Grade": "A", "Age": 27, "Subject": ["Html", "css", "Python"], "Job":None } 
# Open the file 'p.json' in write mode
with open("demo1.json", "w") as write_file: # Serialize the 'student' dictionary to JSON and write it to the file 
  json.dump(student, write_file)
print("finished")   