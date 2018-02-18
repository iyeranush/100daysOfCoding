import random
import time


names = ['Jon', 'Matt', 'Casey', 'Julie', 'Ana']
subjects = ['Math', 'Statistics', 'Comp-Science', 'Engineering', 'Arts']

def people_list(num_people):
    results = []
    for i in range(num_people):
        person = {
            'name'   : random.choice(names),
            'major'  : random.choice(subjects),
            'id'     : i
        }
        results.append(person)
    return results

def people_generator(num_people):
    for i in range(num_people):
        person = {
            'name'   : random.choice(names),
            'major'  : random.choice(subjects),
            'id'     : i
        }
    yield person


def main():
    t1 = time.clock()
    people_list(1000000)
    t2 = time.clock()
    print("Time taken for the list implementation: ", t2-t1)

    t1 = time.clock()
    people_generator(1000000)
    t2 = time.clock()
    print("Time taken for the generator implementation: ", t2-t1)

if __name__ == '__main__':
    main()
