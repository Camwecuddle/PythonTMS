
# List of user objects {name lastName ID}
users = []

# List of task objects {task userID}
tasks = []

# Start at ID 1 and increment for every new user
nextID = 1

# create a new user, id defaults to nextID unless specified
def createUser(fName, lName) :
    global nextID
    users.append({
        'firstName': fName,
        'lastName': lName,
        'userID': nextID
    })
    nextID += 1

def deleteUser(userID) :
    for x in users :
        if x['userID'] == userID :
            users.remove(x)

# If this task is not already in the list, add it
def createTask(taskName) :
    if taskName in map(lambda x: x['taskName'], tasks) :
        print('Task already exists')
    else :
        tasks.append({'taskName': taskName, 'userID': None}) 

# If this task is in the list remove it
def deleteTask(taskName) :
    if tasks : # Check for empty tasks list
        for x in tasks :
            if x['taskName'] == taskName :
                tasks.remove(x)
    else :
        pass

# If this task has been created, assign it to this userID
def assignTask(taskName, userID) :
    for x in tasks :
        if x['taskName'] == taskName :
            x['userID'] = userID

# If this task exists delete it
def removeTaskAssignment(taskName) :
    for x in tasks :
        if x['taskName'] == taskName :
            x['userID'] = None

# Get all the tasks assigned to a user
def getTasks(userID) :
    global tasks
    hold = []
    for x in tasks :
        if x['userID'] == userID :
            hold.append(x)
    return hold

# For testing
def reset() :
    global nextID
    users.clear()
    tasks.clear()
    nextID = 1
