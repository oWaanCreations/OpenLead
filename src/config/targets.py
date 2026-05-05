"""
Worldwide cities and business niches for OpenLead 1.0.
Edit this file to customize your scraping targets.
"""

# ─── Business Categories / Niches ────────────────────────────────────────────
# Ordered by yield: HIGH yield (rarely have websites) first, LOW yield (tech companies) last
NICHES = [
    # ═══ HIGH YIELD — Local services that rarely have websites ═══
    "Dental Clinic",
    "Medical Clinic",
    "Cafe",
    "Bakery",
    "Restaurant",
    "Florist",
    "Auto Repair Shop",
    "Beauty Salon",
    "Gym",
    "Fitness Center",
    "Cleaning Service",
    "Plumbing Service",
    "Electrician",
    "Daycare Center",
    "Pet Shop",
    "Towing Service",
    "Pest Control",
    "Roofing Contractor",
    "Landscaping Service",
    "Printing Service",
    "Moving Company",
    "Security Company",
    "Construction Company",

    # ═══ MEDIUM YIELD — May or may not have websites ═══
    "Hotel",
    "Real Estate Agency",
    "Law Firm",
    "Accounting Firm",
    "Travel Agency",
    "Event Planner",
    "Interior Designer",
    "Video Production",
    "Photography Studio",

    # ═══ LOW YIELD — Tech companies that almost always have websites ═══
    "Web Design Agency",
    "Software Company",
    "Digital Marketing Agency",
    "App Development Company",
    "SEO Company",
    "Graphic Design Studio",
    "IT Company",
    "Cloud Services",
]

# ─── Worldwide Cities (Optimized for Speed & Yield) ─────────────────────────
# Strategy: Medium-sized cities (100k-1M pop) first — they have more small 
# local businesses without websites. Large megacities (5M+) are more digitized.
# Small cities load faster on Google Maps, yielding more leads per search.
CITIES = [
    # 🇩🇪 GERMANY
    "Berlin, Germany", "Munich, Germany", "Hamburg, Germany", "Frankfurt, Germany", "Cologne, Germany",
    "Stuttgart, Germany", "Dusseldorf, Germany", "Dortmund, Germany", "Essen, Germany", "Leipzig, Germany",
    "Bremen, Germany", "Dresden, Germany", "Hanover, Germany", "Nuremberg, Germany", "Duisburg, Germany",

    # 🇫🇷 FRANCE
    "Paris, France", "Lyon, France", "Marseille, France", "Toulouse, France", "Nice, France",
    "Nantes, France", "Strasbourg, France", "Montpellier, France", "Bordeaux, France", "Lille, France",
    "Rennes, France", "Reims, France", "Le Havre, France", "Saint-Etienne, France", "Toulon, France",

    # 🇪🇸 SPAIN
    "Madrid, Spain", "Barcelona, Spain", "Valencia, Spain", "Seville, Spain", "Zaragoza, Spain",
    "Malaga, Spain", "Murcia, Spain", "Palma, Spain", "Las Palmas, Spain", "Bilbao, Spain",
    "Alicante, Spain", "Cordoba, Spain", "Valladolid, Spain", "Vigo, Spain", "Gijon, Spain",

    # 🇮🇹 ITALY
    "Rome, Italy", "Milan, Italy", "Naples, Italy", "Turin, Italy", "Palermo, Italy",
    "Genoa, Italy", "Bologna, Italy", "Florence, Italy", "Bari, Italy", "Catania, Italy",
    "Venice, Italy", "Verona, Italy", "Messina, Italy", "Padua, Italy", "Trieste, Italy",

    # 🇳🇱 NETHERLANDS
    "Amsterdam, Netherlands", "Rotterdam, Netherlands", "The Hague, Netherlands", "Utrecht, Netherlands", "Eindhoven, Netherlands",
    "Tilburg, Netherlands", "Groningen, Netherlands", "Breda, Netherlands", "Nijmegen, Netherlands", "Enschede, Netherlands",

    # 🇧🇪 BELGIUM
    "Brussels, Belgium", "Antwerp, Belgium", "Ghent, Belgium", "Charleroi, Belgium", "Liege, Belgium",
    "Bruges, Belgium", "Namur, Belgium", "Leuven, Belgium", "Mons, Belgium", "Aalst, Belgium",

    # 🇨🇭 SWITZERLAND
    "Zurich, Switzerland", "Geneva, Switzerland", "Basel, Switzerland", "Bern, Switzerland", "Lausanne, Switzerland",
    "Lucerne, Switzerland", "St Gallen, Switzerland", "Lugano, Switzerland", "Thun, Switzerland", "Bellinzona, Switzerland",

    # 🇦🇹 AUSTRIA
    "Vienna, Austria", "Graz, Austria", "Linz, Austria", "Salzburg, Austria", "Innsbruck, Austria",
    "Klagenfurt, Austria", "Villach, Austria", "Wels, Austria", "St Polten, Austria", "Dornbirn, Austria",

    # 🇸🇪 SWEDEN
    "Stockholm, Sweden", "Gothenburg, Sweden", "Malmo, Sweden", "Uppsala, Sweden", "Vasteras, Sweden",
    "Orebro, Sweden", "Linkoping, Sweden", "Helsingborg, Sweden", "Jonkoping, Sweden", "Norrkoping, Sweden",

    # 🇳🇴 NORWAY
    "Oslo, Norway", "Bergen, Norway", "Trondheim, Norway", "Stavanger, Norway", "Baerum, Norway",
    "Kristiansand, Norway", "Tromso, Norway", "Drammen, Norway", "Skien, Norway", "Sandnes, Norway",

    # 🇩🇰 DENMARK
    "Copenhagen, Denmark", "Aarhus, Denmark", "Odense, Denmark", "Aalborg, Denmark", "Esbjerg, Denmark",
    "Randers, Denmark", "Kolding, Denmark", "Horsens, Denmark", "Vejle, Denmark", "Roskilde, Denmark",

    # 🇫🇮 FINLAND
    "Helsinki, Finland", "Espoo, Finland", "Tampere, Finland", "Vantaa, Finland", "Oulu, Finland",
    "Turku, Finland", "Jyvaskyla, Finland", "Lahti, Finland", "Kuopio, Finland", "Pori, Finland",

    # 🇮🇪 IRELAND
    "Dublin, Ireland", "Cork, Ireland", "Limerick, Ireland", "Galway, Ireland", "Waterford, Ireland",
    "Drogheda, Ireland", "Dundalk, Ireland", "Swords, Ireland", "Bray, Ireland", "Navan, Ireland",

    # 🇵🇹 PORTUGAL
    "Lisbon, Portugal", "Porto, Portugal", "Vila Nova de Gaia, Portugal", "Amadora, Portugal", "Braga, Portugal",
    "Funchal, Portugal", "Coimbra, Portugal", "Setubal, Portugal", "Almada, Portugal", "Agualva-Cacem, Portugal",

    # 🇬🇷 GREECE
    "Athens, Greece", "Thessaloniki, Greece", "Patras, Greece", "Heraklion, Greece", "Larissa, Greece",
    "Volos, Greece", "Rhodes, Greece", "Ioannina, Greece", "Chania, Greece", "Agrinio, Greece",

    # 🇵🇱 POLAND
    "Warsaw, Poland", "Krakow, Poland", "Lodz, Poland", "Wroclaw, Poland", "Poznan, Poland",
    "Gdansk, Poland", "Szczecin, Poland", "Bydgoszcz, Poland", "Lublin, Poland", "Katowice, Poland",

    # 🇨🇿 CZECH REPUBLIC
    "Prague, Czech Republic", "Brno, Czech Republic", "Ostrava, Czech Republic", "Plzen, Czech Republic", "Liberec, Czech Republic",
    "Olomouc, Czech Republic", "Ceske Budejovice, Czech Republic", "Hradec Kralove, Czech Republic", "Usti nad Labem, Czech Republic", "Pardubice, Czech Republic",

    # 🇭🇺 HUNGARY
    "Budapest, Hungary", "Debrecen, Hungary", "Szeged, Hungary", "Miskolc, Hungary", "Pecs, Hungary",
    "Gyor, Hungary", "Nyiregyhaza, Hungary", "Kecskemet, Hungary", "Szkesfehervar, Hungary", "Szombathely, Hungary",

    # 🇷🇴 ROMANIA
    "Bucharest, Romania", "Cluj-Napoca, Romania", "Timisoara, Romania", "Iasi, Romania", "Constanta, Romania",
    "Craiova, Romania", "Brasov, Romania", "Galati, Romania", "Ploiesti, Romania", "Oradea, Romania",

    # 🇧🇬 BULGARIA
    "Sofia, Bulgaria", "Plovdiv, Bulgaria", "Varna, Bulgaria", "Burgas, Bulgaria", "Ruse, Bulgaria",
    "Stara Zagora, Bulgaria", "Pleven, Bulgaria", "Sliven, Bulgaria", "Dobrich, Bulgaria", "Shumen, Bulgaria",

    # 🇭🇷 CROATIA
    "Zagreb, Croatia", "Split, Croatia", "Rijeka, Croatia", "Osijek, Croatia", "Zadar, Croatia",
    "Pula, Croatia", "Slavonski Brod, Croatia", "Karlovac, Croatia", "Varazdin, Croatia", "Sisak, Croatia",

    # 🇷🇸 SERBIA
    "Belgrade, Serbia", "Novi Sad, Serbia", "Nis, Serbia", "Kragujevac, Serbia", "Subotica, Serbia",
    "Zrenjanin, Serbia", "Pancevo, Serbia", "Cacak, Serbia", "Novi Pazar, Serbia", "Kraljevo, Serbia",

    # 🇸🇮 SLOVENIA
    "Ljubljana, Slovenia", "Maribor, Slovenia", "Celje, Slovenia", "Kranj, Slovenia", "Velenje, Slovenia",
    "Koper, Slovenia", "Novo Mesto, Slovenia", "Murska Sobota, Slovenia", "Ptuj, Slovenia", "Trbovlje, Slovenia",

    # 🇸🇰 SLOVAKIA
    "Bratislava, Slovakia", "Kosice, Slovakia", "Presov, Slovakia", "Zilina, Slovakia", "Banska Bystrica, Slovakia",
    "Nitra, Slovakia", "Trnava, Slovakia", "Martin, Slovakia", "Trencin, Slovakia", "Poprad, Slovakia",

    # 🇺🇦 UKRAINE
    "Kyiv, Ukraine", "Kharkiv, Ukraine", "Odesa, Ukraine", "Dnipro, Ukraine", "Donetsk, Ukraine",
    "Zaporizhzhia, Ukraine", "Lviv, Ukraine", "Kryvyi Rih, Ukraine", "Mykolaiv, Ukraine", "Mariupol, Ukraine",

    # 🇷🇺 RUSSIA
    "Moscow, Russia", "Saint Petersburg, Russia", "Novosibirsk, Russia", "Yekaterinburg, Russia", "Kazan, Russia",
    "Nizhny Novgorod, Russia", "Chelyabinsk, Russia", "Samara, Russia", "Omsk, Russia", "Rostov-on-Don, Russia",

    # 🇹🇷 TURKEY
    "Istanbul, Turkey", "Ankara, Turkey", "Izmir, Turkey", "Bursa, Turkey", "Adana, Turkey",
    "Gaziantep, Turkey", "Konya, Turkey", "Antalya, Turkey", "Kayseri, Turkey", "Mersin, Turkey",

    # 🇬🇧 UNITED KINGDOM
    "London, UK", "Manchester, UK", "Birmingham, UK", "Leeds, UK", "Glasgow, UK",
    "Sheffield, UK", "Bradford, UK", "Liverpool, UK", "Edinburgh, UK", "Bristol, UK",
    "Cardiff, UK", "Leicester, UK", "Coventry, UK", "Nottingham, UK", "Newcastle, UK",
    "Hull, UK", "Stoke-on-Trent, UK", "Southampton, UK", "Derby, UK", "Portsmouth, UK",

    # ─── 🇺🇸 UNITED STATES ──────────────────────────────────────────────────────
    "New York, USA", "Los Angeles, USA", "Chicago, USA", "Houston, USA", "Phoenix, USA",
    "Philadelphia, USA", "San Antonio, USA", "San Diego, USA", "Dallas, USA", "San Jose, USA",
    "Austin, USA", "Jacksonville, USA", "Fort Worth, USA", "Columbus, USA", "Charlotte, USA",
    "San Francisco, USA", "Indianapolis, USA", "Seattle, USA", "Denver, USA", "Washington, USA",
    "Boston, USA", "El Paso, USA", "Nashville, USA", "Detroit, USA", "Oklahoma City, USA",
    "Portland, USA", "Las Vegas, USA", "Louisville, USA", "Baltimore, USA", "Milwaukee, USA",
    "Albuquerque, USA", "Tucson, USA", "Fresno, USA", "Sacramento, USA", "Mesa, USA",
    "Kansas City, USA", "Atlanta, USA", "Long Beach, USA", "Colorado Springs, USA", "Raleigh, USA",
    "Miami, USA", "Virginia Beach, USA", "Omaha, USA", "Oakland, USA", "Minneapolis, USA",
    "Tulsa, USA", "Arlington, USA", "Wichita, USA", "Bakersfield, USA", "New Orleans, USA",

    # ─── 🇨🇦 CANADA ─────────────────────────────────────────────────────────────
    "Toronto, Canada", "Vancouver, Canada", "Montreal, Canada", "Calgary, Canada", "Ottawa, Canada",
    "Edmonton, Canada", "Winnipeg, Canada", "Quebec City, Canada", "Hamilton, Canada", "Kitchener, Canada",

    # ─── 🇦🇺 AUSTRALIA ──────────────────────────────────────────────────────────
    "Sydney, Australia", "Melbourne, Australia", "Brisbane, Australia", "Perth, Australia", "Adelaide, Australia",
    "Gold Coast, Australia", "Newcastle, Australia", "Canberra, Australia", "Wollongong, Australia", "Hobart, Australia",

    # ─── ASIA ──────────────────────────────────────────────────────────────────
    # 🇮🇳 INDIA
    "Mumbai, India", "Delhi, India", "Bangalore, India", "Hyderabad, India", "Ahmedabad, India",
    "Chennai, India", "Kolkata, India", "Surat, India", "Pune, India", "Jaipur, India",
    "Lucknow, India", "Kanpur, India", "Nagpur, India", "Indore, India", "Thane, India",
    "Bhopal, India", "Visakhapatnam, India", "Patna, India", "Vadodara, India", "Ghaziabad, India",

    # 🇵🇰 PAKISTAN
    "Karachi, Pakistan", "Lahore, Pakistan", "Islamabad, Pakistan", "Faisalabad, Pakistan", "Rawalpindi, Pakistan",
    "Gujranwala, Pakistan", "Multan, Pakistan", "Peshawar, Pakistan", "Quetta, Pakistan", "Sialkot, Pakistan",
    "Hyderabad, Pakistan", "Multan, Pakistan", "Gujranwala, Pakistan", "Peshawar, Pakistan", "Quetta, Pakistan",

    # 🇧🇩 BANGLADESH
    "Dhaka, Bangladesh", "Chittagong, Bangladesh", "Khulna, Bangladesh", "Rajshahi, Bangladesh", "Sylhet, Bangladesh",
    "Barisal, Bangladesh", "Rangpur, Bangladesh", "Comilla, Bangladesh", "Narayanganj, Bangladesh", "Gazipur, Bangladesh",

    # 🇱🇰 SRI LANKA
    "Colombo, Sri Lanka", "Kandy, Sri Lanka", "Galle, Sri Lanka", "Jaffna, Sri Lanka", "Negombo, Sri Lanka",
    "Anuradhapura, Sri Lanka", "Trincomalee, Sri Lanka", "Batticaloa, Sri Lanka", "Matara, Sri Lanka", "Ratnapura, Sri Lanka",

    # 🇳🇵 NEPAL
    "Kathmandu, Nepal", "Pokhara, Nepal", "Lalitpur, Nepal", "Bharatpur, Nepal", "Birgunj, Nepal",
    "Dharan, Nepal", "Biratnagar, Nepal", "Janakpur, Nepal", "Hetauda, Nepal", "Butwal, Nepal",

    # 🇲🇾 MALAYSIA
    "Kuala Lumpur, Malaysia", "George Town, Malaysia", "Ipoh, Malaysia", "Shah Alam, Malaysia", "Petaling Jaya, Malaysia",
    "Johor Bahru, Malaysia", "Kota Kinabalu, Malaysia", "Malacca City, Malaysia", "Kuching, Malaysia", "Miri, Malaysia",

    # 🇸🇬 SINGAPORE
    "Singapore, Singapore", "Jurong, Singapore", "Tampines, Singapore", "Woodlands, Singapore", "Sengkang, Singapore",
    "Yishun, Singapore", "Ang Mo Kio, Singapore", "Bedok, Singapore", "Bukit Batok, Singapore", "Clementi, Singapore",

    # 🇮🇩 INDONESIA
    "Jakarta, Indonesia", "Surabaya, Indonesia", "Bandung, Indonesia", "Medan, Indonesia", "Bekasi, Indonesia",
    "Tangerang, Indonesia", "Depok, Indonesia", "Semarang, Indonesia", "Palembang, Indonesia", "Makassar, Indonesia",

    # 🇹🇭 THAILAND
    "Bangkok, Thailand", "Chiang Mai, Thailand", "Phuket, Thailand", "Pattaya, Thailand", "Hat Yai, Thailand",
    "Udon Thani, Thailand", "Nakhon Ratchasima, Thailand", "Khon Kaen, Thailand", "Ubon Ratchathani, Thailand", "Surat Thani, Thailand",

    # 🇵🇭 PHILIPPINES
    "Manila, Philippines", "Quezon City, Philippines", "Cebu City, Philippines", "Davao City, Philippines", "Caloocan, Philippines",
    "Zamboanga City, Philippines", "Antipolo, Philippines", "Taguig, Philippines", "Pasig, Philippines", "Cagayan de Oro, Philippines",

    # 🇻🇳 VIETNAM
    "Ho Chi Minh City, Vietnam", "Hanoi, Vietnam", "Da Nang, Vietnam", "Hai Phong, Vietnam", "Can Tho, Vietnam",
    "Bien Hoa, Vietnam", "Hue, Vietnam", "Nha Trang, Vietnam", "Buon Ma Thuot, Vietnam", "Nam Dinh, Vietnam",

    # 🇯🇵 JAPAN
    "Tokyo, Japan", "Yokohama, Japan", "Osaka, Japan", "Nagoya, Japan", "Sapporo, Japan",
    "Fukuoka, Japan", "Kobe, Japan", "Kawasaki, Japan", "Kyoto, Japan", "Saitama, Japan",
    "Hiroshima, Japan", "Sendai, Japan", "Kitakyushu, Japan", "Chiba, Japan", "Sakai, Japan",

    # 🇰🇷 SOUTH KOREA
    "Seoul, South Korea", "Busan, South Korea", "Incheon, South Korea", "Daegu, South Korea", "Daejeon, South Korea",
    "Gwangju, South Korea", "Ulsan, South Korea", "Suwon, South Korea", "Changwon, South Korea", "Seongnam, South Korea",

    # 🇨🇳 CHINA
    "Shanghai, China", "Beijing, China", "Shenzhen, China", "Guangzhou, China", "Chengdu, China",
    "Tianjin, China", "Wuhan, China", "Dongguan, China", "Foshan, China", "Hangzhou, China",
    "Nanjing, China", "Chongqing, China", "Shenyang, China", "Xi'an, China", "Suzhou, China",

    # 🇭🇰 HONG KONG
    "Hong Kong, Hong Kong", "Kowloon, Hong Kong", "Tsuen Wan, Hong Kong", "Sha Tin, Hong Kong", "Tuen Mun, Hong Kong",
    "Tai Po, Hong Kong", "Sai Kung, Hong Kong", "Yuen Long, Hong Kong", "Tseung Kwan O, Hong Kong", "Fanling, Hong Kong",

    # 🇹🇼 TAIWAN
    "Taipei, Taiwan", "Kaohsiung, Taiwan", "Taichung, Taiwan", "Tainan, Taiwan", "Banqiao, Taiwan",
    "Hsinchu, Taiwan", "Keelung, Taiwan", "Zhongli, Taiwan", "Chiayi, Taiwan", "Pingtung, Taiwan",

    # ─── LATIN AMERICA ─────────────────────────────────────────────────────────
    # 🇲🇽 MEXICO
    "Mexico City, Mexico", "Guadalajara, Mexico", "Monterrey, Mexico", "Puebla, Mexico", "Tijuana, Mexico",
    "Leon, Mexico", "Juarez, Mexico", "Cancun, Mexico", "Merida, Mexico", "Queretaro, Mexico",

    # 🇧🇷 BRAZIL
    "Sao Paulo, Brazil", "Rio de Janeiro, Brazil", "Brasilia, Brazil", "Salvador, Brazil", "Fortaleza, Brazil",
    "Belo Horizonte, Brazil", "Manaus, Brazil", "Curitiba, Brazil", "Recife, Brazil", "Goiania, Brazil",
    "Belem, Brazil", "Porto Alegre, Brazil", "Guarulhos, Brazil", "Campinas, Brazil", "Sao Luis, Brazil",

    # 🇦🇷 ARGENTINA
    "Buenos Aires, Argentina", "Cordoba, Argentina", "Rosario, Argentina", "Mendoza, Argentina", "La Plata, Argentina",
    "Tucuman, Argentina", "Mar del Plata, Argentina", "Salta, Argentina", "Santa Fe, Argentina", "San Juan, Argentina",

    # 🇨🇱 CHILE
    "Santiago, Chile", "Valparaiso, Chile", "Concepcion, Chile", "La Serena, Chile", "Antofagasta, Chile",
    "Temuco, Chile", "Rancagua, Chile", "Talca, Chile", "Arica, Chile", "Puerto Montt, Chile",

    # 🇨🇴 COLOMBIA
    "Bogota, Colombia", "Medellin, Colombia", "Cali, Colombia", "Barranquilla, Colombia", "Cartagena, Colombia",
    "Cucuta, Colombia", "Bucaramanga, Colombia", "Pereira, Colombia", "Santa Marta, Colombia", "Ibague, Colombia",

    # 🇵🇪 PERU
    "Lima, Peru", "Arequipa, Peru", "Trujillo, Peru", "Chiclayo, Peru", "Huancayo, Peru",
    "Piura, Peru", "Cusco, Peru", "Chimbote, Peru", "Iquitos, Peru", "Juliaca, Peru",

    # 🇻🇪 VENEZUELA
    "Caracas, Venezuela", "Maracaibo, Venezuela", "Valencia, Venezuela", "Barquisimeto, Venezuela", "Maracay, Venezuela",
    "Ciudad Guayana, Venezuela", "San Cristobal, Venezuela", "Maturin, Venezuela", "Barcelona, Venezuela", "Cumana, Venezuela",

    # 🇪🇨 ECUADOR
    "Quito, Ecuador", "Guayaquil, Ecuador", "Cuenca, Ecuador", "Santo Domingo, Ecuador", "Machala, Ecuador",
    "Duran, Ecuador", "Portoviejo, Ecuador", "Manta, Ecuador", "Loja, Ecuador", "Ambato, Ecuador",

    # 🇺🇾 URUGUAY
    "Montevideo, Uruguay", "Salto, Uruguay", "Ciudad de la Costa, Uruguay", "Paysandu, Uruguay", "Las Piedras, Uruguay",
    "Rivera, Uruguay", "Maldonado, Uruguay", "Tacuarembo, Uruguay", "Melo, Uruguay", "Artigas, Uruguay",

    # 🇵🇾 PARAGUAY
    "Asuncion, Paraguay", "Ciudad del Este, Paraguay", "San Lorenzo, Paraguay", "Luque, Paraguay", "Capiata, Paraguay",
    "Lambare, Paraguay", "Fernando de la Mora, Paraguay", "Limpio, Paraguay", "Nemby, Paraguay", "Encarnacion, Paraguay",

    # ─── AFRICA ────────────────────────────────────────────────────────────────
    # 🇿🇦 SOUTH AFRICA
    "Johannesburg, South Africa", "Cape Town, South Africa", "Durban, South Africa", "Pretoria, South Africa", "Port Elizabeth, South Africa",
    "Bloemfontein, South Africa", "East London, South Africa", "Polokwane, South Africa", "Nelspruit, South Africa", "Kimberley, South Africa",

    # 🇪🇬 EGYPT
    "Cairo, Egypt", "Alexandria, Egypt", "Giza, Egypt", "Shubra El Kheima, Egypt", "Port Said, Egypt",
    "Suez, Egypt", "Luxor, Egypt", "Mansoura, Egypt", "El Mahalla, Egypt", "Tanta, Egypt",

    # 🇳🇬 NIGERIA
    "Lagos, Nigeria", "Kano, Nigeria", "Ibadan, Nigeria", "Abuja, Nigeria", "Port Harcourt, Nigeria",
    "Benin City, Nigeria", "Maiduguri, Nigeria", "Zaria, Nigeria", "Aba, Nigeria", "Jos, Nigeria",

    # 🇰🇪 KENYA
    "Nairobi, Kenya", "Mombasa, Kenya", "Kisumu, Kenya", "Nakuru, Kenya", "Eldoret, Kenya",
    "Kehancha, Kenya", "Ruiru, Kenya", "Kikuyu, Kenya", "Kangundo-Tala, Kenya", "Malindi, Kenya",

    # 🇪🇹 ETHIOPIA
    "Addis Ababa, Ethiopia", "Dire Dawa, Ethiopia", "Mekelle, Ethiopia", "Adama, Ethiopia", "Gondar, Ethiopia",
    "Hawassa, Ethiopia", "Bahir Dar, Ethiopia", "Jimma, Ethiopia", "Dessie, Ethiopia", "Jijiga, Ethiopia",

    # 🇬🇭 GHANA
    "Accra, Ghana", "Kumasi, Ghana", "Tamale, Ghana", "Sekondi-Takoradi, Ghana", "Sunyani, Ghana",
    "Cape Coast, Ghana", "Obuasi, Ghana", "Teshie, Ghana", "Tema, Ghana", "Madina, Ghana",

    # 🇹🇿 TANZANIA
    "Dar es Salaam, Tanzania", "Mwanza, Tanzania", "Arusha, Tanzania", "Dodoma, Tanzania", "Mbeya, Tanzania",
    "Morogoro, Tanzania", "Tanga, Tanzania", "Kahama, Tanzania", "Tabora, Tanzania", "Zanzibar City, Tanzania",

    # 🇺🇬 UGANDA
    "Kampala, Uganda", "Nansana, Uganda", "Kira, Uganda", "Ssabagabo, Uganda", "Mukono, Uganda",
    "Njeru, Uganda", "Gulu, Uganda", "Lugazi, Uganda", "Mbarara, Uganda", "Entebbe, Uganda",

    # 🇲🇦 MOROCCO
    "Casablanca, Morocco", "Fez, Morocco", "Tangier, Morocco", "Marrakesh, Morocco", "Sale, Morocco",
    "Meknes, Morocco", "Rabat, Morocco", "Oujda, Morocco", "Kenitra, Morocco", "Agadir, Morocco",

    # 🇩🇿 ALGERIA
    "Algiers, Algeria", "Oran, Algeria", "Constantine, Algeria", "Annaba, Algeria", "Blida, Algeria",
    "Batna, Algeria", "Djelfa, Algeria", "Setif, Algeria", "Sidi Bel Abbes, Algeria", "Biskra, Algeria",

    # 🇹🇳 TUNISIA
    "Tunis, Tunisia", "Sfax, Tunisia", "Sousse, Tunisia", "Kairouan, Tunisia", "Bizerte, Tunisia",
    "Gabes, Tunisia", "Ariana, Tunisia", "Gafsa, Tunisia", "Monastir, Tunisia", "Ben Arous, Tunisia",

    # ─── MIDDLE EAST ───────────────────────────────────────────────────────────
    # 🇸🇦 SAUDI ARABIA
    "Riyadh, Saudi Arabia", "Jeddah, Saudi Arabia", "Mecca, Saudi Arabia", "Medina, Saudi Arabia", "Dammam, Saudi Arabia",
    "Taif, Saudi Arabia", "Tabuk, Saudi Arabia", "Buraidah, Saudi Arabia", "Khamis Mushait, Saudi Arabia", "Hail, Saudi Arabia",

    # 🇦🇪 UAE
    "Dubai, UAE", "Abu Dhabi, UAE", "Sharjah, UAE", "Al Ain, UAE", "Ajman, UAE",
    "Ras Al Khaimah, UAE", "Fujairah, UAE", "Umm Al Quwain, UAE", "Dibba, UAE", "Khor Fakkan, UAE",

    # 🇶🇦 QATAR
    "Doha, Qatar", "Al Rayyan, Qatar", "Umm Salal, Qatar", "Al Khor, Qatar", "Al Wakrah, Qatar",
    "Lusail, Qatar", "Mesaieed, Qatar", "Al Shamal, Qatar", "Dukhan, Qatar", "Al Ruwais, Qatar",

    # 🇰🇼 KUWAIT
    "Kuwait City, Kuwait", "Al Ahmadi, Kuwait", "Hawalli, Kuwait", "Salmiya, Kuwait", "Al Jahra, Kuwait",
    "Al Farwaniyah, Kuwait", "Mubarak Al Kabeer, Kuwait", "Al Fahaheel, Kuwait", "Ar Riqqah, Kuwait", "Jleeb Al-Shuyoukh, Kuwait",

    # 🇧🇭 BAHRAIN
    "Manama, Bahrain", "Riffa, Bahrain", "Muharraq, Bahrain", "Hamad Town, Bahrain", "A'ali, Bahrain",
    "Isa Town, Bahrain", "Sitra, Bahrain", "Budaiya, Bahrain", "Jidhafs, Bahrain", "Al-Malikiyah, Bahrain",

    # 🇴🇲 OMAN
    "Muscat, Oman", "Seeb, Oman", "Salalah, Oman", "Bawshar, Oman", "Sohar, Oman",
    "As Suwayq, Oman", "Ibri, Oman", "Saham, Oman", "Barka, Oman", "Rustaq, Oman",

    # 🇯🇴 JORDAN
    "Amman, Jordan", "Zarqa, Jordan", "Irbid, Jordan", "Russeifa, Jordan", "Wadi Al Seer, Jordan",
    "Aqaba, Jordan", "Madaba, Jordan", "Al Jubayhah, Jordan", "Salt, Jordan", "Ain Al Basha, Jordan",

    # 🇮🇶 IRAQ
    "Baghdad, Iraq", "Basra, Iraq", "Mosul, Iraq", "Erbil, Iraq", "Sulaymaniyah, Iraq",
    "Najaf, Iraq", "Karbala, Iraq", "Nasiriyah, Iraq", "Amara, Iraq", "Diwaniyah, Iraq",

    # 🇮🇷 IRAN
    "Tehran, Iran", "Mashhad, Iran", "Isfahan, Iran", "Karaj, Iran", "Shiraz, Iran",
    "Tabriz, Iran", "Qom, Iran", "Ahvaz, Iran", "Kermanshah, Iran", "Urmia, Iran",

    # 🇮🇱 ISRAEL
    "Jerusalem, Israel", "Tel Aviv, Israel", "Haifa, Israel", "Rishon LeZion, Israel", "Petah Tikva, Israel",
    "Ashdod, Israel", "Netanya, Israel", "Beersheba, Israel", "Bnei Brak, Israel", "Holon, Israel",

    # 🇱🇧 LEBANON
    "Beirut, Lebanon", "Tripoli, Lebanon", "Sidon, Lebanon", "Tyre, Lebanon", "Nabatieh, Lebanon",
    "Zahle, Lebanon", "Jounieh, Lebanon", "Byblos, Lebanon", "Baabda, Lebanon", "Aley, Lebanon",

    # 🇸🇾 SYRIA
    "Damascus, Syria", "Aleppo, Syria", "Homs, Syria", "Latakia, Syria", "Hama, Syria",
    "Raqqa, Syria", "Deir ez-Zor, Syria", "Al-Hasakah, Syria", "Qamishli, Syria", "Daraa, Syria",

    # 🇦🇫 AFGHANISTAN
    "Kabul, Afghanistan", "Herat, Afghanistan", "Kandahar, Afghanistan", "Mazar-i-Sharif, Afghanistan", "Jalalabad, Afghanistan",
    "Kunduz, Afghanistan", "Taloqan, Afghanistan", "Puli Khumri, Afghanistan", "Charikar, Afghanistan", "Sheberghan, Afghanistan",

    # ─── OCEANIA ───────────────────────────────────────────────────────────────
    # 🇳🇿 NEW ZEALAND
    "Auckland, New Zealand", "Wellington, New Zealand", "Christchurch, New Zealand", "Hamilton, New Zealand", "Tauranga, New Zealand",
    "Napier, New Zealand", "Dunedin, New Zealand", "Palmerston North, New Zealand", "Nelson, New Zealand", "Rotorua, New Zealand",

    # 🇫🇯 FIJI
    "Suva, Fiji", "Nadi, Fiji", "Lautoka, Fiji", "Labasa, Fiji", "Ba, Fiji",
    "Levuka, Fiji", "Sigatoka, Fiji", "Savusavu, Fiji", "Rakiraki, Fiji", "Tavua, Fiji",

    # 🇵🇬 PAPUA NEW GUINEA
    "Port Moresby, Papua New Guinea", "Lae, Papua New Guinea", "Arawa, Papua New Guinea", "Mount Hagen, Papua New Guinea", "Madang, Papua New Guinea",
    "Wewak, Papua New Guinea", "Goroka, Papua New Guinea", "Kokopo, Papua New Guinea", "Daru, Papua New Guinea", "Kimbe, Papua New Guinea",

    # ─── CARIBBEAN / CENTRAL AMERICA ───────────────────────────────────────────
    # 🇨🇷 COSTA RICA
    "San Jose, Costa Rica", "Limon, Costa Rica", "San Francisco, Costa Rica", "Alajuela, Costa Rica", "Liberia, Costa Rica",
    "Paraiso, Costa Rica", "Puntarenas, Costa Rica", "San Isidro, Costa Rica", "Curridabat, Costa Rica", "Heredia, Costa Rica",

    # 🇵🇦 PANAMA
    "Panama City, Panama", "San Miguelito, Panama", "Tocumen, Panama", "David, Panama", "Arraijan, Panama",
    "Colon, Panama", "La Chorrera, Panama", "Santiago, Panama", "Chitre, Panama", "Penonome, Panama",

    # 🇬🇹 GUATEMALA
    "Guatemala City, Guatemala", "Villa Nueva, Guatemala", "Mixco, Guatemala", "Coban, Guatemala", "Quetzaltenango, Guatemala",
    "San Pedro Carcha, Guatemala", "Totonicapan, Guatemala", "San Juan Sacatepequez, Guatemala", "Huehuetenango, Guatemala", "Escuintla, Guatemala",

    # 🇭🇳 HONDURAS
    "Tegucigalpa, Honduras", "San Pedro Sula, Honduras", "Choloma, Honduras", "La Ceiba, Honduras", "El Progreso, Honduras",
    "Comayagua, Honduras", "Choluteca, Honduras", "Puerto Cortes, Honduras", "La Lima, Honduras", "Danli, Honduras",

    # 🇳🇮 NICARAGUA
    "Managua, Nicaragua", "Leon, Nicaragua", "Masaya, Nicaragua", "Matagalpa, Nicaragua", "Chinandega, Nicaragua",
    "Esteli, Nicaragua", "Tipitapa, Nicaragua", "Granada, Nicaragua", "Juigalpa, Nicaragua", "Jinotega, Nicaragua",

    # 🇸🇻 EL SALVADOR
    "San Salvador, El Salvador", "Santa Ana, El Salvador", "Soyapango, El Salvador", "San Miguel, El Salvador", "Mejicanos, El Salvador",
    "Apopa, El Salvador", "Delgado, El Salvador", "Ahuachapan, El Salvador", "Ilopango, El Salvador", "Colon, El Salvador",

    # 🇨🇺 CUBA
    "Havana, Cuba", "Santiago de Cuba, Cuba", "Camaguey, Cuba", "Holguin, Cuba", "Santa Clara, Cuba",
    "Guantanamo, Cuba", "Bayamo, Cuba", "Victoria de Las Tunas, Cuba", "Cienfuegos, Cuba", "Pinar del Rio, Cuba",

    # 🇩🇴 DOMINICAN REPUBLIC
    "Santo Domingo, Dominican Republic", "Santiago, Dominican Republic", "Santo Domingo Este, Dominican Republic", "Santo Domingo Norte, Dominican Republic", "San Pedro de Macoris, Dominican Republic",
    "La Romana, Dominican Republic", "San Cristobal, Dominican Republic", "Puerto Plata, Dominican Republic", "Mao, Dominican Republic", "Moca, Dominican Republic",

    # 🇵🇷 PUERTO RICO
    "San Juan, Puerto Rico", "Bayamon, Puerto Rico", "Carolina, Puerto Rico", "Ponce, Puerto Rico", "Caguas, Puerto Rico",
    "Guaynabo, Puerto Rico", "Arecibo, Puerto Rico", "Toa Baja, Puerto Rico", "Mayaguez, Puerto Rico", "Trujillo Alto, Puerto Rico",

    # 🇯🇲 JAMAICA
    "Kingston, Jamaica", "New Kingston, Jamaica", "Spanish Town, Jamaica", "Portmore, Jamaica", "Montego Bay, Jamaica",
    "Mandeville, Jamaica", "May Pen, Jamaica", "Old Harbour, Jamaica", "Savanna-la-Mar, Jamaica", "Ocho Rios, Jamaica",

    # 🇹🇹 TRINIDAD AND TOBAGO
    "Port of Spain, Trinidad and Tobago", "Chaguanas, Trinidad and Tobago", "San Fernando, Trinidad and Tobago", "Arima, Trinidad and Tobago", "Marabella, Trinidad and Tobago",
    "Point Fortin, Trinidad and Tobago", "Tunapuna, Trinidad and Tobago", "Scarborough, Trinidad and Tobago", "Sangre Grande, Trinidad and Tobago", "Penal, Trinidad and Tobago",

    # 🇧🇸 BAHAMAS
    "Nassau, Bahamas", "Freeport, Bahamas", "West End, Bahamas", "Coopers Town, Bahamas", "Marsh Harbour, Bahamas",
    "Freetown, Bahamas", "High Rock, Bahamas", "Andros Town, Bahamas", "Spanish Wells, Bahamas", "Clarence Town, Bahamas",

    # 🇧🇧 BARBADOS
    "Bridgetown, Barbados", "Speightstown, Barbados", "Oistins, Barbados", "Bathsheba, Barbados", "Holetown, Barbados",
    "Crane, Barbados", "Greenland, Barbados", "Hillaby, Barbados", "Four Cross Roads, Barbados", "Black Rock, Barbados",

    # 🇬🇾 GUYANA
    "Georgetown, Guyana", "Linden, Guyana", "New Amsterdam, Guyana", "Anna Regina, Guyana", "Bartica, Guyana",
    "Skeldon, Guyana", "Rosignol, Guyana", "Mahaicony, Guyana", "Parika, Guyana", "Vreed en Hoop, Guyana",

    # 🇸🇷 SURINAME
    "Paramaribo, Suriname", "Lelydorp, Suriname", "Nieuw Nickerie, Suriname", "Moengo, Suriname", "Marienburg, Suriname",
    "Wageningen, Suriname", "Albina, Suriname", "Groningen, Suriname", "Brownsweg, Suriname", "Onverwacht, Suriname",

    # 🇧🇿 BELIZE
    "Belize City, Belize", "San Ignacio, Belize", "Belmopan, Belize", "Orange Walk, Belize", "San Pedro, Belize",
    "Corozal, Belize", "Dangriga, Belize", "Benque Viejo, Belize", "Ladyville, Belize", "Punta Gorda, Belize",
]
