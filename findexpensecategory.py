def findExpenseCategory(supplier):
    expense_category = {
        'bombora': 'Business',
        'woolworth': 'Grocery',
        'supermarket': 'Grocery',
        'MYPOST BUSINESS': 'Business',
        'my post business':'Business',
        'THORNLEIGH POST OFFICE': 'Lottery',
        'adobesystem': 'Business',
        'optus': 'Telcom',
        'bunnings': 'Home',
        'ikea': 'Home',
        'xbox': 'Subscribe',
        'algoexpert': 'Learning',
        'Gazman': 'Clothing',
        'Lululemon': 'Clothing',
        'Coles': 'Grocery',
        'New Yen Yen': 'Grocery',
        'Telstra': 'Telcom',
        'Cafe': 'Dine Out',
        'Newsagency': 'Lottery',
        'Telco': 'Business',
        'Shopify': 'Business',
        'Kennards': 'Business',
        'Seocho': 'Dine Out',
        'Costco': 'Business',
        'Opera': 'Entertainment',
        'Apple': 'Electronics',
        'JB Hi fi': 'Electronics',
        'Wheniwork': 'Business',
        'Allianz': 'Insurance',
        'Petrol': 'Transport',
        'Dolcettini': 'Dine Out',
        'Seed': 'Clothing',
        'Butchery': 'Grocery',
        'Speedw': 'Transport',
        'Deli': 'Grocery',
        'Bob and Petes': 'Business',
        'Carmen': 'Entertainment',
        'Fresh Technology': 'Business',
        'Opal': 'Transport',
        'Googleaustr': 'Business',
        'Service NSW': 'Transport',
        'QBE Insurance': 'Insruance',
        'Udacity': 'Learning',
        'GlenworthOutdoorAdvent': 'Entertainment',
        'InkStation': 'Business',
        'SephoraAU': 'Daily',
        'Blue Fishmonger': 'Grocery',
        'Pork rolls': 'Dine Out',
        'Franks Automotive': 'Transport',
        'Amazon': 'Electronics',
        'Carlingford Court NE': 'Dine Out',
        'AustralianP': 'Business',
        'John Wiley': 'Learning',
        'North Shore Hi-tech': 'Transport',
        'Damee':'Dine Out',
        'AMZNPRIMEAU': 'Subscribe',
        'Kiehlsau': 'Daily',
        'Sabre Drummoyne': 'Clothing',
        'Godaddy': 'Business',
        'Sugarhill': 'Dine Out',
        'CA ANZ': 'Learning',
        'Medco Carlingford': 'Transport',
        'Foodpackagi': 'Business',
        'Officeworks': 'Business',
        'AGL': 'Utility',
        'Chemist warehouse': 'Daily',
        'Ampol': 'Transport',
        'Waverley Council Bondi Junct': 'Parking',
        'Smelly Cheesecak': 'Dine Out',
        'Goodwood Bakeshop': 'Dine Out',
        'La trobe': 'Learning',
        'Typo 2743 Macquarie': 'Daily',
        'Aromatic House': 'Dine Out',
        'Pet Circle': 'Pet',
        'Petcultureg': 'Pet',
        'Coursra': 'Learning',
        'Uniqlo': 'Clothing',
        'Mecca': 'Daily',
        'Hong Kong St Food': 'Dine Out',
        'Top Impression Bakery': 'Dine Out',
        'Microsoft Ulti': 'Subscribe',
        'Quillbot': 'Business',
        'Catevolution': 'Pet',
        'Cherrybrook Bakery': 'Dine Out',
        'Fedder': 'Business',
        'Karargy pty ltd': 'Dine Out',
        'Mannus2': 'Dine Out',
        'Wok Inn': 'Dine Out',
        'LuneBurger': 'Dine Out',
        'Nike': 'Clothing',
        'Farmers Direct': 'Grocery',
        'Metro Ryde': 'Transport',
        'Eastwood Seafood': 'Grocery',
        'EG Group': 'Transport',
        'Seek Business': 'Business',
        'Bare Witness':'Dine Out',
        'Unigas': 'Transport',
        'Council Parki North Sydne': 'Parking',
        'The growers pty ltd ryde': 'Grocery',
        'Mels German Bakery': 'Dine Out',
        'Kmall09': 'Grocery',
        'Authentic Turkish Paddington':'Dine Out',
        'Brooklyn Boy Bage': 'Dine Out',
        'Gediminas Mudeanas Paddington': 'Dine Out',
        '1Password': 'Subscribe',
        '7-Eleven': 'Transport',
        'A1 Restaurant': 'Business',
        'ASIC Sydney':'Business',
        'Aus Post Online': 'Business',
        'Hertz': 'Travel',
        'Gelato': 'Dine Out',
        'Benbry Burger':'Dine Out',
        'netflix': 'Subscribe',
        'BP': 'Transport',
        'Breeze Valley':'Business',
        'Bruny Island': 'Travel',
        'Bonbons Bakry': 'Dine Out',
        'Bupa':'Insurance',
        'BWS':'Grocery',
        'Bakerie': 'Dine Out',
        'Bing Lee': 'Business',
        'Burger Urge': 'Dine Out',
        'C M Fresh Seafood Carlingford': 'Grocery',
        'Caltex': 'Transport',
        'Chill Bar': 'Dine Out',
        'Coffee Tools Distrib': 'Business',
        'CK Underwear': 'Clothing',
        'Cityofsydney parking': 'Parking',
        'Cumberland Council Auburn': 'Parking',
        'Cycleworld Concord': 'Entertainment',
        'Dan Murphy':'Grocery',
        'Daojia': 'Daily',
        'Cocoa & Bean': 'Dine Out',
        'Crowne Plaza': 'Travel',
        'Anytime Fitness': 'Fitness',
        'De Bortoli': 'Dine Out',
        'Decathlon': 'Fitness',
        'EB Games': 'Electronics',
        'FACEBK': 'Business',
        'Fair Trading Licensn': 'Business',
        'Fitness Chullora': 'Fitness',
        'Fresh Asiana': 'Grocery',
        'Frank Restaurant': 'Dine Out',
        'Harris Farm': 'Grocery',
        'ICARE': 'Business',
        'Pharmacy': 'Daily',
        'Ji Yun Chinese': 'Dine Out',
        'KMART Tyre': 'Transport',
        'Kounta': 'Business',
        'Lidcombe Service': 'Transport',
        'Liquorland': 'Grocery',
        'THEGOODGUYS': 'Business',
        'WW Metro': 'Grocery',
        'Xiangyao asian superma': 'Grocery',
        'yi xuan pty ltd': 'Dine Out',
        'Zara':'Clothing',
        'mycar':'Transport',
        'zinan pty ltd':'Dine Out',
        'wilson parking':'Parking',
        'Western plains zoo dubbo':'Travel',
        'visy':'Business',
        'United Yagoona':'Transport',
        'pig & pastry':'Dine Out',
        'creamery&co':'Dine Out',
        'typeform':'Business',
        'Barewitness':'Dine Out',
        'Transportfornsw': 'Transport',
        'Trappers Bakery': 'Dine Out',
        'Total Tools':'Home',
        'Monday Morning Caf':'Dine Out',
        'Kitchen HBA':'Dine Out',
        'TDP Fuels': 'Transport',
        'Target':'Home',
        'Taobao':'Home',
        'Silo Espresso':'Dine Out',
        'Freshwater': 'Dine Out',
        'Sealink': 'Transport',
        'Superdry':'Clothing',
        'Squarespace':'Business',
        'Mini Espresso':'Dine Out',
        'Teatooptylt':'Business',
        'Thegoodguys': 'Business',
        'Skype':'Business',
        'Nisbetsaust':'Business',
        'Nintendo':'Subscribe',
        'new pack':'Business',
        'mwave':'Electronics',
        'microsoft':'Subscribe',
        'Lancomeau':'Daily',
        'Bingleeelec':'Business',
        'Alt Brewing':'Business',
        'IP Australia':'Business',
        'Burberry':'Clothing',



    }
    for key, value in expense_category.items():
        if key.lower() in supplier.lower():
            return value
