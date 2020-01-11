import random


def random_generator_pick_2():
    places = ['gas_station', 'hotel', 'fast_food', 'bank', 'store']
    random_place_1 = random.choice(places)
    places.remove(random_place_1)
    random_place_2 = random.choice(places)
    return [random_place_1, random_place_2]


class City:
    def __init__(self, state, city):
        self.state = state
        self.city = city
        self.left = None
        self.right = None
        self.previous = None


class Map:
    def __init__(self):
        self.start = City("Florida", "Miami")

    def search_map(self, city_name):
        data = []
        queue = []
        queue.append(self.start)
        while len(queue) != 0:
            city_viewed = queue.pop(0)
            data.append(city_viewed.city)
            if city_viewed.city.lower() == city_name.lower():
                return city_viewed
            if city_viewed.left:
                queue.append(city_viewed.left)
            if city_viewed.right: queue.append(city_viewed.right)
        return -1

    def insert_left_at(self, current_city, new_state, new_city):
        current_city = self.search_map(current_city)
        if current_city == -1:
            return "City not Found"
        elif current_city != -1:
            if current_city.left:
                return "this city already has a left"
            else:
                new_city = City(new_state, new_city)
                current_city.left = new_city
                new_city.previous = current_city
                return "Success!"

    def insert_right_at(self, current_city, new_state, new_city):
        current_city = self.search_map(current_city)
        if current_city == -1:
            return "City not Found"
        elif current_city != -1:
            if current_city.right:
                return "this city already has a right"
            else:
                new_city = City(new_state, new_city)

                current_city.right = new_city
                new_city.previous = current_city
                return "Success!"

    def to_dict(self, current_city):
        if current_city is None: return
        data = {}
        data['name'] = current_city.city
        data['attributes'] = {'state': current_city.state}

        data['children'] = []
        child_1 = self.to_dict(current_city.left) if current_city.left is not None else None
        child_2 = self.to_dict(current_city.right) if current_city.right is not None else None
        if child_1 is not None: data['children'].append(child_1)
        if child_2 is not None: data['children'].append(child_2)

        return data


us_map = Map()
# where u at,   where you going: state, city.
us_map.insert_left_at("Miami", "Florida", "Jacksonville")
us_map.insert_right_at("Miami", 'Florida', 'Tallahassee')

us_map.insert_left_at("Jacksonville", "Georgia", "Macon")
us_map.insert_left_at("Macon", "Georgia", "Atlanta")
us_map.insert_right_at("Macon", "Georgia", "Augusta")

us_map.insert_left_at('Tallahassee', 'Alabama', 'Birmingham')
us_map.insert_left_at('Birmingham', 'Alabama', 'Huntsville')
us_map.insert_left_at('Huntsville', 'Tennessee', 'Selmer')

us_map.insert_left_at('Atlanta', 'Tennessee', 'Chattanooga')
us_map.insert_left_at('Augusta', 'South_Carolina', 'Columbia')
us_map.insert_left_at('Chattanooga', 'Tennessee', 'Nashville')
us_map.insert_right_at('Chattanooga', 'Tennessee', 'Knoxville')
us_map.insert_left_at('Nashville', 'Kentucky', 'Bowling_Green')
us_map.insert_left_at('Knoxville', 'Virginia', 'Abingdon')

us_map.insert_left_at('Selmer', 'Tennessee', 'Memphis')
us_map.insert_left_at('Memphis', 'Missouri', 'Springfield')
us_map.insert_left_at('Springfield', 'Missouri', 'St_Louis')
us_map.insert_right_at('Springfield', 'Missouri', 'Kansas_City')

us_map.insert_left_at('St_Louis', 'Illinois', 'Champaign')
us_map.insert_left_at('Champaign', 'Illinois', 'Chicago')
us_map.insert_left_at('Chicago', 'Michigan', 'Grand_Rapids')
us_map.insert_left_at('Grand_Rapids', 'Michigan', 'Port_Huron')
us_map.insert_left_at('Port_Huron', 'Canada', 'Canada_2')

us_map.insert_left_at('Kansas_City', 'Iowa', 'Des_Moines')
us_map.insert_left_at('Des_Moines', 'Iowa', 'Mason_City')
us_map.insert_left_at('Mason_City', 'Minnesota', 'Minneapolis')
us_map.insert_left_at('Minneapolis', 'Minnesota', 'International_Falls')
us_map.insert_left_at('International_Falls', 'Canada', 'Canada_1')

us_map.insert_left_at('Bowling_Green', 'Kentucky', 'Louisville')
us_map.insert_right_at('Bowling_Green', 'Kentucky', 'Lexington')
us_map.insert_left_at('Louisville', 'Indiana', 'Indianapolis')
us_map.insert_left_at('Indianapolis', 'Indiana', 'Fort_Wayne')
us_map.insert_left_at('Fort_Wayne', 'Michigan', 'Ann_Arbor')
us_map.insert_left_at('Ann_Arbor', 'Michigan', 'Detroit')
us_map.insert_left_at('Detroit', 'Canada', 'Canada')

us_map.insert_left_at('Lexington', 'Ohio', 'Cincinnati')
us_map.insert_left_at('Cincinnati', 'Ohio', 'Toledo')
us_map.insert_left_at('Toledo', 'Michigan', 'Detroit_2')
us_map.insert_left_at('Detroit_2', 'Canada', 'Canada_3')

us_map.insert_left_at('Columbia', 'South_Carolina', 'Florence')
us_map.insert_left_at('Florence', 'North_Carolina', 'Raleigh')
us_map.insert_left_at('Raleigh', 'Virginia', 'Richmond')
us_map.insert_left_at('Richmond', 'Virginia', 'Charlottesville')
us_map.insert_left_at('Charlottesville', 'West_Virginia', 'Green_Bank')
us_map.insert_left_at('Green_Bank', 'West_Virginia', 'Bridgeport')
us_map.insert_left_at('Bridgeport', 'Pennsylvania', 'Pittsburgh')
us_map.insert_left_at('Pittsburgh', 'Pennsylvania', 'Clarion')
us_map.insert_left_at('Clarion', 'New_York', 'Salamanca')
us_map.insert_left_at('Salamanca', 'New_York', 'Buffalo_2')
us_map.insert_left_at('Buffalo_2', 'Canada', 'Canada_5')

us_map.insert_right_at('Richmond', 'Virginia', 'Fredericksburg')
us_map.insert_left_at('Fredericksburg', 'Maryland', 'Baltimore')
us_map.insert_left_at('Baltimore', 'Maryland', 'Westminster')
us_map.insert_left_at('Westminster', 'Pennsylvania', 'Harrisburg')
us_map.insert_left_at('Harrisburg', 'Pennsylvania', 'Mansfield')
us_map.insert_left_at('Mansfield', 'New_York', 'Elmira')
us_map.insert_left_at('Elmira', 'Buffalo', 'Canada_4')

us_map.insert_left_at('Abingdon', 'Virginia', 'Roanoke')
us_map.insert_left_at('Roanoke', 'West_Virginia', 'Lewisburg')
us_map.insert_left_at('Lewisburg', 'West_Virginia', 'Charleston')
us_map.insert_left_at('Charleston', 'Ohio', 'Athens')
us_map.insert_left_at('Athens', 'Ohio', 'Akron')
us_map.insert_left_at('Akron', 'Pennsylvania', 'Erie')
us_map.insert_left_at('Erie', 'New_York', 'Buffalo-3')
us_map.insert_left_at('Buffalo-3', 'Canada', 'Canada_6')
