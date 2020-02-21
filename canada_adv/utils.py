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

    def populate_map(self):
        # where u at,   where you going: state, city.
        self.insert_left_at("Miami", "Florida", "Jacksonville")
        self.insert_right_at("Miami", 'Florida', 'Tallahassee')

        self.insert_left_at("Jacksonville", "Georgia", "Macon")
        self.insert_left_at("Macon", "Georgia", "Atlanta")
        self.insert_right_at("Macon", "Georgia", "Augusta")

        self.insert_left_at('Tallahassee', 'Alabama', 'Birmingham')
        self.insert_left_at('Birmingham', 'Alabama', 'Huntsville')
        self.insert_left_at('Huntsville', 'Tennessee', 'Selmer')

        self.insert_left_at('Atlanta', 'Tennessee', 'Chattanooga')
        self.insert_left_at('Augusta', 'South_Carolina', 'Columbia')
        self.insert_left_at('Chattanooga', 'Tennessee', 'Nashville')
        self.insert_right_at('Chattanooga', 'Tennessee', 'Knoxville')
        self.insert_left_at('Nashville', 'Kentucky', 'Bowling_Green')
        self.insert_left_at('Knoxville', 'Virginia', 'Abingdon')

        self.insert_left_at('Selmer', 'Tennessee', 'Memphis')
        self.insert_left_at('Memphis', 'Missouri', 'Springfield')
        self.insert_left_at('Springfield', 'Missouri', 'St_Louis')
        self.insert_right_at('Springfield', 'Missouri', 'Kansas_City')

        self.insert_left_at('St_Louis', 'Illinois', 'Champaign')
        self.insert_left_at('Champaign', 'Illinois', 'Chicago')
        self.insert_left_at('Chicago', 'Michigan', 'Grand_Rapids')
        self.insert_left_at('Grand_Rapids', 'Michigan', 'Port_Huron')
        self.insert_left_at('Port_Huron', 'Canada', 'Canada_2')

        self.insert_left_at('Kansas_City', 'Iowa', 'Des_Moines')
        self.insert_left_at('Des_Moines', 'Iowa', 'Mason_City')
        self.insert_left_at('Mason_City', 'Minnesota', 'Minneapolis')
        self.insert_left_at('Minneapolis', 'Minnesota', 'International_Falls')
        self.insert_left_at('International_Falls', 'Canada', 'Canada_1')

        self.insert_left_at('Bowling_Green', 'Kentucky', 'Louisville')
        self.insert_right_at('Bowling_Green', 'Kentucky', 'Lexington')
        self.insert_left_at('Louisville', 'Indiana', 'Indianapolis')
        self.insert_left_at('Indianapolis', 'Indiana', 'Fort_Wayne')
        self.insert_left_at('Fort_Wayne', 'Michigan', 'Ann_Arbor')
        self.insert_left_at('Ann_Arbor', 'Michigan', 'Detroit')
        self.insert_left_at('Detroit', 'Canada', 'Canada')

        self.insert_left_at('Lexington', 'Ohio', 'Cincinnati')
        self.insert_left_at('Cincinnati', 'Ohio', 'Toledo')
        self.insert_left_at('Toledo', 'Michigan', 'Detroit_2')
        self.insert_left_at('Detroit_2', 'Canada', 'Canada_3')

        self.insert_left_at('Columbia', 'South_Carolina', 'Florence')
        self.insert_left_at('Florence', 'North_Carolina', 'Raleigh')
        self.insert_left_at('Raleigh', 'Virginia', 'Richmond')
        self.insert_left_at('Richmond', 'Virginia', 'Charlottesville')
        self.insert_left_at('Charlottesville', 'West_Virginia', 'Green_Bank')
        self.insert_left_at('Green_Bank', 'West_Virginia', 'Bridgeport')
        self.insert_left_at('Bridgeport', 'Pennsylvania', 'Pittsburgh')
        self.insert_left_at('Pittsburgh', 'Pennsylvania', 'Clarion')
        self.insert_left_at('Clarion', 'New_York', 'Salamanca')
        self.insert_left_at('Salamanca', 'New_York', 'Buffalo_2')
        self.insert_left_at('Buffalo_2', 'Canada', 'Canada_5')

        self.insert_right_at('Richmond', 'Virginia', 'Fredericksburg')
        self.insert_left_at('Fredericksburg', 'Maryland', 'Baltimore')
        self.insert_left_at('Baltimore', 'Maryland', 'Westminster')
        self.insert_left_at('Westminster', 'Pennsylvania', 'Harrisburg')
        self.insert_left_at('Harrisburg', 'Pennsylvania', 'Mansfield')
        self.insert_left_at('Mansfield', 'New_York', 'Elmira')
        self.insert_left_at('Elmira', 'Buffalo', 'Canada_4')

        self.insert_left_at('Abingdon', 'Virginia', 'Roanoke')
        self.insert_left_at('Roanoke', 'West_Virginia', 'Lewisburg')
        self.insert_left_at('Lewisburg', 'West_Virginia', 'Charleston')
        self.insert_left_at('Charleston', 'Ohio', 'Athens')
        self.insert_left_at('Athens', 'Ohio', 'Akron')
        self.insert_left_at('Akron', 'Pennsylvania', 'Erie')
        self.insert_left_at('Erie', 'New_York', 'Buffalo-3')
        self.insert_left_at('Buffalo-3', 'Canada', 'Canada_6')
