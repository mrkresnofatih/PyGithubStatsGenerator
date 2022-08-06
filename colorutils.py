import random

def get_random_color_palette():
    randomnumber = random.uniform(0, 100)
    if randomnumber < 25:
        return ['#f94144', '#f3722c', '#f8961e', '#f9844a', '#f9c74f', '#90be6d', '#43aa8b', '#4d908e', '#577590', '#277da1']
    elif randomnumber >= 25 and randomnumber < 50:
        return ["#ff5400","#ff6d00","#ff8500","#ff9100","#ff9e00","#00b4d8","#0096c7","#0077b6","#023e8a","#03045e"]
    elif randomnumber >= 50 and randomnumber < 75:
        return ["#03071e","#370617","#6a040f","#9d0208","#d00000","#dc2f02","#e85d04","#f48c06","#faa307","#ffba08"]
    elif randomnumber >= 75 and randomnumber <= 100:
        return ["#7400b8","#6930c3","#5e60ce","#5390d9","#4ea8de","#48bfe3","#56cfe1","#64dfdf","#72efdd","#80ffdb"]