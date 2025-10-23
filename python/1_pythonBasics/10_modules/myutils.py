def find_tringle_area(base, height):
    return (base*height)/2

def find_cylinder_volume(radius, height=7):
    print("radius:", radius)
    print("height:", height)
    volume = 3.14*(radius**2)*height
    print(volume)
    return volume