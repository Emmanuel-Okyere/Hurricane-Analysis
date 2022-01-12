# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# write your update damages function here:
def update_damages(damages):
  update_damages_list = []
  conversion = {"M": 1000000,
              "B": 1000000000}
  for i in damages:
    if i =="Damages not recorded":
      update_damages_list.append(i)
    elif i[-1] in conversion.keys():
      update = float(i[:-1]) * conversion[i[-1]]
      update_damages_list.append(update)
  return update_damages_list
test_update = update_damages(damages)
print(test_update)

# write your construct hurricane dictionary function here:
updated_combined_data = {}
def combined_data(names, months, years, max_sustained_winds, areas_affected,damages, deaths):
  for i in range(0,len(names)):
    updated_combined_data[names[i]] = {"Name": names[i], "Month": months[i], "Years": years[i], "Max Sustained Wind": max_sustained_winds[i], "Area Affected": areas_affected[i], "Damage": damages[i], "Deaths": deaths[i]}
  return updated_combined_data

print(combined_data(names, months, years, max_sustained_winds, areas_affected,test_update, deaths))




# write your construct hurricane by year dictionary function here:
current_Hurricane = combined_data(names, months, years, max_sustained_winds, areas_affected,test_update, deaths)
print(current_Hurricane["Cuba I"])

# Organizing by Year
def by_year(hurricane):
  new = {}
  for key, value in hurricane.items():
    new.update({hurricane[key].get("Years"): value})
  return new
# create a new dictionary of hurricanes with year and key
by_years = by_year(current_Hurricane)
print(by_years[1924])

# write your count affected areas function here:
def count_Number(current_Hurricane):
  new = {}
  for i in current_Hurricane:
    for j in current_Hurricane[i].get("Area Affected"):
      if j in new:
        new[j] += 1
      else:
        new[j] = 1
  return new

# create dictionary of areas to store the number of hurricanes involved in
affected_area_count = count_Number(current_Hurricane)
print(affected_area_count["Central America"])

# write your find most affected area function here:
def calc_max_count(affected_area):
  lists = []
  for key, value in affected_area.items():
    lists.append(value)
  maxim = max(lists)
  for key, value in affected_area.items():
    if maxim == value:
      return key, maxim
# find most frequently affected area and the number of hurricanes involved in
maxom =calc_max_count(affected_area_count)
print(maxom)

# write your greatest number of deaths function here:
def calc_max_death(current_Hurricane):
  max_number = 0
  max_key = ""
  for key, value in current_Hurricane.items():
    num = current_Hurricane[key].get("Deaths")
    if num > max_number:
      max_number = num
      max_key  = key
  return {max_key: max_number}

max_mortality = calc_max_death(current_Hurricane)
print(max_mortality)
# write your catgeorize by mortality function here:
def group_by_motal(current_Hurricane):
  new =dict()
  for key, value in current_Hurricane.items():
    new.update({current_Hurricane[key].get("Deaths") : value})
  return new
groupby_mortal = group_by_motal(current_Hurricane)
print(groupby_mortal[90])

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}
def calula(groupby_mortal):
  list0 = []
  list1 = []
  list2 = []
  list3 = []
  list4 = []
  list5 = []
  new = {}
  for key, value in groupby_mortal.items():
    if key > 0 and key <= 100:
      list1.append(value)
    elif key <=0:
      list0.append(value)
    elif key >100 and key <= 500:
      list2.append(value)
    elif key >500 and key <= 1000:
      list3.append(value)
    elif key > 1000 and key <= 10000:
      list4.append(value)
    else:
      list5.append(value)
  new.update({0:list0,1:list1, 2: list2, 3:list3, 4:list4, 5:list5})
  return new
# find highest damage inducing hurricane and its total cost
new  = calula(groupby_mortal)
print(new[5])
# write your greatest damage function here:
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
# write your catgeorize by damage function here:
def cat_by_dam(current_Hurricane):
  new={0:[], 1:[], 2:[], 3:[],4:[], 5:[]}
  for key, value in current_Hurricane.items():
    if current_Hurricane[key].get("Damage") == "Damages not recorded":
      new[0].append(value)
    elif current_Hurricane[key].get("Damage") ==0:
      new[0].append(value)
    elif current_Hurricane[key].get("Damage") > damage_scale[0] and current_Hurricane[key].get("Damage") < damage_scale[0]:
      new[1].append(value)
    elif current_Hurricane[key].get("Damage") >= damage_scale[1] and current_Hurricane[key].get("Damage") < damage_scale[2]:
      new[2].append(value)
    elif current_Hurricane[key].get("Damage") >= damage_scale[2] and current_Hurricane[key].get("Damage") < damage_scale[3]:
      new[3].append(value)
    elif current_Hurricane[key].get("Damage") >= damage_scale[3] and current_Hurricane[key].get("Damage") <= damage_scale[4]:
      new[4].append(value)
    elif current_Hurricane[key].get("Damage") >= damage_scale[4]:
      new[5].append(value)
  return new

new = cat_by_dam(current_Hurricane)
print(new)
