katz_deli = []
def line(katz_deli):
    if not katz_deli:
        print('The line is currently empty.')
    else:
        inform='The line is currently:'
        i=1
        for element in katz_deli:
            inform+=f' {i}. {element}'
            i+=1
        print(inform)
    
def take_a_number(katz_deli, person_name):
    katz_deli.append(person_name)
    print(f'Welcome, {person_name}. You are number {katz_deli.index(person_name)+1} in line.')

def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {katz_deli[0]}.')
        katz_deli.pop(0)

    