from pyscript import document

def generate_message(event):
    
    name = str(document.getElementById("name").value).strip()
    age = str(document.getElementById("age").value).strip()
    school = str(document.getElementById("school").value).strip()

   
    if not name or not age or not school:
        message = "⚠️ Please fill in all fields before generating the message."
    else:
        message = f"Hello, my name is {name}. I am {age} years old and I currently study at {school}."

   
    document.getElementById("output").innerText = message
