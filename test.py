import tms

def testCreateUser() :
    tms.reset()
    tms.createUser('camron', 'vick')

    print ('testCreateUser Pass:', (tms.users == [{
            'firstName': 'camron',
            'lastName': 'vick',
            'userID': 1 
        }]))

def testDeleteUser() :
    tms.reset()
    tms.createUser('camron', 'vick')
    tms.createUser('michael', 'vick')
    tms.createUser('kristin', 'vick')
    tms.deleteUser(2)

    print ('testDeleteUser Pass:', (tms.users == [{
            'firstName': 'camron',
            'lastName': 'vick',
            'userID': 1
        }, {
            'firstName': 'kristin',
            'lastName': 'vick',
            'userID': 3
        }]))

def testCreateTask() :
    tms.reset()
    tms.createTask('task1')

    print ('testCreateTask Pass:', (tms.tasks == [{
            'taskName': 'task1',
            'userID': None
        }]))


def testDeleteTask() :
    tms.reset()
    tms.createTask('task1')
    tms.createTask('task2')
    tms.createTask('task3')
    tms.deleteTask('task2')

    print ('testDeleteTask Pass:', (tms.tasks == [{
            'taskName': 'task1',
            'userID': None
        }, {
            'taskName': 'task3',
            'userID': None
        }]))

def testAssignTask() :
    tms.reset()
    tms.createTask('task1')
    tms.createTask('task2')
    tms.createTask('task3')
    tms.createUser('camron', 'vick')
    tms.createUser('michael', 'vick')
    tms.createUser('kristin', 'vick')
    tms.assignTask('task1', 1)
    tms.assignTask('task2', 2)
    tms.assignTask('task3', 3)
    # print(tms.tasks)
    print ('testAssignTask Pass:', (tms.tasks == [{
            'taskName': 'task1',
            'userID': 1
        }, {
            'taskName': 'task2',
            'userID': 2
        }, {
            'taskName': 'task3',
            'userID': 3
        }]))

def testRemoveTaskAssignment() :
    tms.reset()
    tms.createTask('task1')
    tms.createTask('task2')
    tms.createTask('task3')
    tms.createUser('camron', 'vick')
    tms.createUser('michael', 'vick')
    tms.createUser('kristin', 'vick')
    tms.assignTask('task1', 1)
    tms.assignTask('task2', 2)
    tms.assignTask('task3', 3)
    tms.removeTaskAssignment('task2')
    tms.removeTaskAssignment('task1')
    # print(tms.tasks)
    print ('testRemoveTaskAssignment Pass:', (tms.tasks == [{
            'taskName': 'task1',
            'userID': None
        }, {
            'taskName': 'task2',
            'userID': None
        }, {
            'taskName': 'task3',
            'userID': 3
        }]))

def testGetTasks() :
    tms.reset()
    tms.createTask('task1')
    tms.createTask('task2')
    tms.createTask('task3')
    tms.createTask('task4')
    tms.createTask('task5')
    tms.createTask('task6')
    tms.createUser('camron', 'vick')
    tms.createUser('michael', 'vick')
    tms.createUser('kristin', 'vick')
    tms.assignTask('task1', 1)
    tms.assignTask('task2', 2)
    tms.assignTask('task3', 3)
    tms.assignTask('task4', 2)
    tms.assignTask('task5', 2)
    tms.assignTask('task6', 2)

    print ('testGetTasks Pass:', (tms.getTasks(2) == [{
            'taskName': 'task2',
            'userID': 2
        }, {
            'taskName': 'task4',
            'userID': 2
        }, {
            'taskName': 'task5',
            'userID': 2
        }, {
            'taskName': 'task6',
            'userID': 2
        }]))

# Uncomment the tests you want to run

testCreateUser()
testDeleteUser()
testCreateTask()
testDeleteTask()
testAssignTask()
testRemoveTaskAssignment()
testGetTasks()