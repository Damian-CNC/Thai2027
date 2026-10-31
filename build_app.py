import sys, os, json

slides_data = [
    {
        "id": "intro",
        "isIntro": True,
        "title": "Tajlandia 2027",
        "subtitle": "Bangkok • Kanchanaburi • Ko Samui",
        "dateRange": "8 – 24 Stycznia 2027",
        "bgImage": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(135deg, #090d16 0%, #1e1b4b 50%, #0f172a 100%)",
        "stats": [
            {"num": "17", "label": "Dni podróży"},
            {"num": "4", "label": "Bazy hotelowe"},
            {"num": "3", "label": "Krainy Tajlandii"}
        ],
        "hotelsSummary": [
            {"name": "Mövenpick Sukhumvit 15", "loc": "Bangkok", "nights": "3 noce"},
            {"name": "Hilltop Erawan Camp", "loc": "Erawan / Si Sawat", "nights": "1 noc"},
            {"name": "Lake Hill Resort", "loc": "Jezioro Srinakarin", "nights": "1 noc"},
            {"name": "Impiana Chaweng Noi", "loc": "Ko Samui", "nights": "9 nocy"},
            {"name": "lebua at State Tower", "loc": "Bangkok (Finał)", "nights": "1 noc"}
        ]
    },
    {
        "id": "day-1",
        "dayNum": 1,
        "date": "9 stycznia 2027 (Sobota)",
        "badgeDate": "9 STY",
        "type": "🛬 PRZYLOT & CHINATOWN",
        "typeClass": "tag-arrival",
        "title": "Witaj w Krainie Uśmiechu!",
        "subtitle": "Przylot do Bangkoku i neonowe Chinatown",
        "hotel": "Mövenpick Hotel Sukhumvit 15 (5★)",
        "hotelTip": "Darmowy tuk-tuk ze ślepej uliczki Soi 15 do stacji BTS Asok / Terminal 21.",
        "bgImage": "https://images.unsplash.com/photo-1552465011-b4e21bf6e79a?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #180926 0%, #090d16 100%)",
        "items": [
            {
                "time": "14:50",
                "title": "Lądowanie w Bangkoku (BKK)",
                "desc": "Odbiór bagażu, zakup karty eSIM (AIS / TrueMove) i wypłata gotówki z bankomatu (najlepiej jednorazowo min. 10 000–20 000 THB na opłaty i street food, prowizja 220 THB).",
                "price": "Koszty własne",
                "query": "Suvarnabhumi Airport Bangkok",
                "tip": "Oficjalne taksówki z lotniska bierze się z biletomatu na poziomie 1."
            },
            {
                "time": "17:30",
                "title": "Check-in w Mövenpick Sukhumvit 15",
                "desc": "Zameldowanie w 5★ hotelu w sercu tętniącej życiem dzielnicy Sukhumvit. Szybki relaks i odświeżenie po locie.",
                "price": "W cenie rezerwacji",
                "query": "Mövenpick Hotel Sukhumvit 15 Bangkok",
                "tip": "Hotel ma świetny basen na dachu i bar Rainforest."
            },
            {
                "time": "19:30",
                "title": "Chinatown (Yaowarat Road)",
                "desc": "Zderzenie z kulinarną stolicą świata: feeria neonów, kłęby pary z woków, pieczone krewetki, Pad Thai i deser ze słodkiego mango ze sticky rice.",
                "price": "Street food ~150–300 THB",
                "query": "Yaowarat Road Chinatown Bangkok",
                "tip": "Najlepszy klimat zaczyna się po godz. 19:00, gdy gasną światła dnia."
            },
            {
                "time": "22:00",
                "title": "Drink nad rzeką Chao Phraya",
                "desc": "Powitalny koktajl w nadrzecznym barze (np. Eagle Cafe / The Deck) z widokiem na podświetloną majestatyczną iglicę Wat Arun odbijającą się w rzece.",
                "price": "Koktajle ~250–350 THB",
                "query": "Eagle Cafe Bangkok",
                "tip": "Idealny relaks na walkę z jet lagiem."
            }
        ]
    },
    {
        "id": "day-2",
        "dayNum": 2,
        "date": "10 stycznia 2027 (Niedziela)",
        "badgeDate": "10 STY",
        "type": "🏛️ ZWIEDZANIE INTENSYWNIE",
        "typeClass": "tag-explore",
        "title": "Złote Świątynie & Kanały Thonburi",
        "subtitle": "Klasyczne ikony dawnego i dzisiejszego Bangkoku",
        "hotel": "Mövenpick Hotel Sukhumvit 15",
        "hotelTip": "Śniadanie o 07:15 – startujemy w miasto o 07:45!",
        "bgImage": "https://images.unsplash.com/photo-1563492065599-3520f775eeed?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #1e1305 0%, #090d16 100%)",
        "items": [
            {
                "time": "08:30",
                "title": "Wielki Pałac Królewski & Wat Phra Kaew",
                "desc": "Najświętsze miejsce w Tajlandii ze słynnym Szmaragdowym Buddą. Przybycie na 08:30 gwarantuje brak upału i autokarów z turystami.",
                "price": "500 THB / os.",
                "query": "The Grand Palace Bangkok",
                "tip": "Rygorystyczny dress code: zakryte ramiona, długie spodnie/spódnice."
            },
            {
                "time": "10:45",
                "title": "Wat Pho – Leżący Budda",
                "desc": "46-metrowy monumentalny posąg pokryty płatkowym złotem oraz historyczna kolebka masażu tajskiego.",
                "price": "300 THB / os. (w tym butelka wody)",
                "query": "Wat Pho Bangkok",
                "tip": "Warto wrzucić po 1 monecie do 108 mis z brązu na szczęście."
            },
            {
                "time": "12:00",
                "title": "Przeprawa promem i Wat Arun (Świątynia Świtu)",
                "desc": "Krótki rejs promem rzecznym (5 THB) na drugi brzeg rzeki. Spacer wokół wieży prang zdobionej potłuczoną chińską porcelaną.",
                "price": "200 THB / os.",
                "query": "Wat Arun Bangkok",
                "tip": "Obiad w restauracji nadrzecznej z widokiem na rzekę."
            },
            {
                "time": "13:30",
                "title": "Prywatny rejs łodzią z długim ogonem (Khlongs)",
                "desc": "Wyprawa w labirynt kanałów Thonburi. Zobaczycie tradycyjne drewniane domy na palach oraz gigantycznego 69-metrowego Złotego Buddę w Wat Paknam z wody.",
                "price": "~1000–1500 THB za całą prywatną łódź",
                "query": "Wat Paknam Phasi Charoen Bangkok",
                "tip": "Cenę wynajmu prywatnej łodzi ustala się bezpośrednio na przystani."
            },
            {
                "time": "16:30",
                "title": "Mahanakhon SkyWalk (314 m) na zachód słońca",
                "desc": "Wjazd na najwyższy punkt widokowy Bangkoku ze szklaną podłogą zawieszoną w chmurach. Spektakularny zachód słońca.",
                "price": "~880–1080 THB / os.",
                "query": "King Power Mahanakhon Bangkok",
                "tip": "Kupcie bilet 1 dzień wcześniej na Klook, by uniknąć stania w kolejce do kasy."
            },
            {
                "time": "20:30",
                "title": "Tichuca Rooftop Bar",
                "desc": "Słynny bar na 46. piętrze z pulsującym, świecącym drzewem z filmu Avatar i panoramicznym widokiem na drapacze chmur Sukhumvit.",
                "price": "Drinki ~400–500 THB",
                "query": "Tichuca Rooftop Bar Bangkok",
                "tip": "Wspaniałe zakończenie intensywnego dnia!"
            }
        ]
    },
    {
        "id": "day-3",
        "dayNum": 3,
        "date": "11 stycznia 2027 (Poniedziałek)",
        "badgeDate": "11 STY",
        "type": "🌆 ODKRYWANIE & KONTRASTY",
        "typeClass": "tag-explore",
        "title": "Złota Góra, Kanał Saen Saep & ICONSIAM",
        "subtitle": "Sekrety jedwabiu, tradycyjny transport i luksus nad rzeką",
        "hotel": "Mövenpick Hotel Sukhumvit 15",
        "hotelTip": "Codziennie w godz. 16:00–17:00 w hotelu trwa bezpłatny Chocolate Hour!",
        "bgImage": "https://images.unsplash.com/photo-1542051841857-5f90071e7989?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #111a2e 0%, #090d16 100%)",
        "items": [
            {
                "time": "08:15",
                "title": "Wat Saket (Złota Góra / Golden Mount)",
                "desc": "Wspinaczka po 344 schodkach otoczonych mgiełką wodną i dzwonami modlitewnymi na szczyt sztucznego wzgórza z widokiem 360° na panoramę miasta.",
                "price": "100 THB / os.",
                "query": "Wat Saket Bangkok",
                "tip": "Rano jest tu cudowny chłód i słychać śpiew mnichów."
            },
            {
                "time": "10:00",
                "title": "Dom Jima Thompsona (Jim Thompson House)",
                "desc": "Kompleks zabytkowych domów z ciemnego drewna tekowego pośród bujnego ogrodu w centrum metropolii, związany z tajemniczym zniknięciem twórcy tajskiego jedwabiu.",
                "price": "200 THB / os. (z przewodnikiem)",
                "query": "Jim Thompson House Bangkok",
                "tip": "Prawdziwa zielona oaza spokoju."
            },
            {
                "time": "11:45",
                "title": "Rejs lokalnym tramwajem po kanale Khlong Saen Saep",
                "desc": "Ekscytujący przejazd szybką łodzią kanałową – autentyczny transport mieszkańców Bangkoku pozwalający błyskawicznie ominąć miejskie korki.",
                "price": "15 THB / os.",
                "query": "Pratunam Pier Bangkok",
                "tip": "Trzymajcie się lin i uważajcie na rozpryski wody – wspaniała przygoda!"
            },
            {
                "time": "13:00",
                "title": "ICONSIAM & SookSiam (Obiad)",
                "desc": "Jeden z najbardziej spektakularnych kompleksów świata. Wewnątrz znajduje się klimatyzowany pływający targ ze specjałami ze wszystkich regionów Tajlandii.",
                "price": "Wstęp wolny / dania ~80–150 THB",
                "query": "ICONSIAM Bangkok",
                "tip": "Znakomity moment na obiad w przyjemnym chłodzie klimatyzacji."
            },
            {
                "time": "16:00",
                "title": "Chocolate Hour & Relaks w Mövenpick",
                "desc": "Powrót do hotelu na słynną darmową godzinę szwajcarskiej czekolady, relaks na leżakach przy basenie na dachu i przygotowanie do jutrzejszej wyprawy autem.",
                "price": "W cenie hotelu",
                "query": "Mövenpick Hotel Sukhumvit 15 Bangkok",
                "tip": "Czekoladowe fontanny, owoce i ciasta codziennie o 16:00!"
            },
            {
                "time": "19:30",
                "title": "Nocny targ Jodd Fairs Rama 9",
                "desc": "Tętniący życiem nocny targ słynący z gigantycznych żeberek wieprzowych w pikantnym bulionie (Leng Saap) i owocowych smoothie.",
                "price": "Kolacja ~200–350 THB",
                "query": "JODD FAIRS Rama 9 Bangkok",
                "tip": "Spróbujcie deseru w postaci lodów kokosowych lub bingsu."
            }
        ]
    },
    {
        "id": "day-4",
        "dayNum": 4,
        "date": "12 stycznia 2027 (Wtorek)",
        "badgeDate": "12 STY",
        "type": "🚗 WYPRAWA SAMOCHODOWA",
        "typeClass": "tag-drive",
        "title": "Auto z BKK ➔ Targ na Torach ➔ Hilltop Erawan",
        "subtitle": "Kolej przecinająca stragany, gigantyczny Budda i Most na rzece Kwai",
        "hotel": "Hilltop Erawan Camp (Tha Kradan, Si Sawat)",
        "hotelTip": "Glamping na wzgórzu z panoramicznym widokiem na jezioro Srinakarin i góry.",
        "bgImage": "https://images.unsplash.com/photo-1528181304800-259b08848526?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #1c1409 0%, #090d16 100%)",
        "items": [
            {
                "time": "07:15",
                "title": "Przejazd z hotelu na lotnisko BKK",
                "desc": "Wymeldowanie z Mövenpick i transfer na lotnisko Suvarnabhumi (BKK) po odbiór samochodu z wypożyczalni.",
                "price": "Bolt ~350 THB",
                "query": "Suvarnabhumi Airport Bangkok",
                "tip": "Odbiór auta na BKK pozwala wjechać od razu na autostradę obwodową i ominąć korki!"
            },
            {
                "time": "08:15",
                "title": "Odbiór samochodu & Start trasy na zachód",
                "desc": "Formalności w wypożyczalni (wymagane Międzynarodowe Prawo Jazdy Konwencja 1949 r., paszport, karta kredytowa). Ruszamy w trasę!",
                "price": "Wynajem auta",
                "query": "Suvarnabhumi Airport Car Rental",
                "tip": "Ruch lewostronny – automatyczna skrzynia biegów bardzo ułatwia jazdę."
            },
            {
                "time": "10:00",
                "title": "Maeklong Railway Market (Targ na Torach)",
                "desc": "Kultowy targ, gdzie tory kolejowe biegną przez środek stoisk warzywnych. Na dźwięk syreny kupcy w ułamku sekundy składają markizy, a pociąg ociera się o arbuzy.",
                "price": "Wstęp wolny",
                "query": "Maeklong Railway Market",
                "tip": "Przejazdy pociągu: ok. 09:00, 11:10, 11:30. Stójcie bezpiecznie za czerwoną linią!"
            },
            {
                "time": "13:00",
                "title": "Świątynia Wat Tham Suea (Tiger Cave Temple)",
                "desc": "Jedna z najbardziej fotogenicznych świątyń Tajlandii. Olbrzymi, lśniący w słońcu Złoty Budda wznosi się na szczycie wzgórza pośród szmaragdowych pól ryżowych.",
                "price": "Wstęp wolny (kolejka szynowa na szczyt 20 THB)",
                "query": "Wat Tham Suea Kanchanaburi",
                "tip": "Na dole można wstąpić do kawiarni z pomostami nad polami ryżowymi."
            },
            {
                "time": "14:30",
                "title": "Most na rzece Kwai w Kanchanaburi",
                "desc": "Słynny historyczny most Kolei Śmierci. Spacer po torach i nadrzeczny obiad w pływającej restauracji nad rzeką Kwai.",
                "price": "Wstęp wolny / obiad ~250–400 THB",
                "query": "The Bridge of the River Kwai",
                "tip": "Piękne pamiątkowe zdjęcia z mostu."
            },
            {
                "time": "16:15",
                "title": "Malownicza trasa 3199 w góry do Hilltop Erawan",
                "desc": "Przepiękna górska droga prowadząca wzdłuż rzeki i lasów deszczowych do dystryktu Si Sawat.",
                "price": "Paliwo",
                "query": "Hilltop Erawan Camp",
                "tip": "Czas jazdy: ok. 1 godzina 15 minut."
            },
            {
                "time": "17:30",
                "title": "Check-in w Hilltop Erawan Camp",
                "desc": "Powitanie w luksusowym namiocie glampingowym / domku na zboczu wzgórza. Zachód słońca nad jeziorem Srinakarin, kolacja pod gwiazdami i cisza natury.",
                "price": "W cenie rezerwacji",
                "query": "Hilltop Erawan Camp",
                "tip": "Zaledwie 10 minut jazdy od bramy Parku Erawan na jutrzejszy poranek!"
            }
        ]
    },
    {
        "id": "day-5",
        "dayNum": 5,
        "date": "13 stycznia 2027 (Środa)",
        "badgeDate": "13 STY",
        "type": "🌿 WODOSPADY & JEZIORO",
        "typeClass": "tag-nature",
        "title": "Park Erawan ➔ Zapora Srinakarin ➔ Lake Hill",
        "subtitle": "Kąpiele w 7 turkusowych kaskadach i nocleg nad samą taflą wody",
        "hotel": "Lake Hill Kanchanaburi Resort (Tha Kradan)",
        "hotelTip": "Pokoje/domki nad samym jeziorem, darmowe kajaki i prywatny pomost do wody.",
        "bgImage": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #051e17 0%, #090d16 100%)",
        "items": [
            {
                "time": "08:00",
                "title": "Park Narodowy Erawan (Wodospady 1–7)",
                "desc": "Wejście o 08:00 – zanim przyjadą wycieczki z Bangkoku! 7 poziomów kaskad wapiennych z krystaliczną szmaragdową wodą. Kąpiel w naturalnych basenach z rybkami.",
                "price": "300 THB / os. + 30 THB auto (GOTÓWKA!)",
                "query": "Erawan National Park",
                "tip": "Zabierzcie buty ze stabilną podeszwą i kostiumy. Najlepsze baseny są na poziomach 3, 4 i 7."
            },
            {
                "time": "12:30",
                "title": "Tajski obiad przy parku",
                "desc": "Świeże curry, pieczony kurczak Gai Yang z sosem tamaryndowym i kleistym ryżem w lokalnej knajpce.",
                "price": "Obiad ~150–250 THB",
                "query": "Erawan National Park Restaurant",
                "tip": "Znakomite, proste lokalne jedzenie."
            },
            {
                "time": "13:30",
                "title": "Zapora Srinakarin & Punkt Widokowy",
                "desc": "Zaledwie 10 minut od Erawanu. Potężna zapora hydroelektryczna z zadbanym ogrodem i spektakularną panoramą jeziora pośród zielonych gór.",
                "price": "Wstęp wolny",
                "query": "Srinagarind Dam Viewpoint",
                "tip": "Wspaniałe miejsce na zdjęcia – krajobraz przypomina norweskie fiordy!"
            },
            {
                "time": "14:45",
                "title": "Kawiarnia nad jeziorem (Lakeview Cafe / Z9)",
                "desc": "Relaks przy mrożonej tajskiej herbacie z mlekiem (Cha Yen) i kokosowych deserach z widokiem na gładką taflę wody.",
                "price": "Kawa ~80–120 THB",
                "query": "Lakeview Cafe Kanchanaburi",
                "tip": "Cudowna atmosfera sprzyjająca wyciszeniu."
            },
            {
                "time": "16:30",
                "title": "Check-in w Lake Hill Kanchanaburi Resort",
                "desc": "Przyjazd do Waszego drugiego resortu w Tha Kradan. Pokoje tuż nad taflą wody.",
                "price": "W cenie rezerwacji",
                "query": "Lake Hill Resort Kanchanaburi",
                "tip": "Wypożyczcie darmowe kajaki i popływajcie o zachodzie słońca!"
            },
            {
                "time": "18:30",
                "title": "Kolacja na tarasie nad wodą",
                "desc": "Romantyczny wieczór w ciszy natury. Świeże ryby z jeziora, tajskie zioła i szum delikatnych fal pod tarasem.",
                "price": "Kolacja ~300–500 THB",
                "query": "Lake Hill Resort Kanchanaburi",
                "tip": "Wczesny sen przed jutrzejszym porannym powrotem na lotnisko BKK."
            }
        ]
    },
    {
        "id": "day-6",
        "dayNum": 6,
        "date": "14 stycznia 2027 (Czwartek)",
        "badgeDate": "14 STY",
        "type": "✈️ LOT NA KO SAMUI",
        "typeClass": "tag-flight",
        "title": "Powrót na BKK ➔ Lot PG155 (14:55) ➔ Ko Samui",
        "subtitle": "Z krainy rzek do tropikalnego raju Zatoki Tajlandzkiej",
        "hotel": "Impiana Resort Chaweng Noi (4★)",
        "hotelTip": "Bezpośrednio przy plaży Chaweng Noi – najdrobniejszy, jasny piasek na wyspie.",
        "bgImage": "https://images.unsplash.com/photo-1537956965359-7573183d1f57?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #091f2c 0%, #090d16 100%)",
        "items": [
            {
                "time": "07:30",
                "title": "Wyjazd samochodem na lotnisko BKK",
                "desc": "Spokojna podróż powrotna autostradami w kierunku Bangkoku (ok. 235 km, ok. 3.5–4 h jazdy).",
                "price": "Opłaty drogowe ~100 THB",
                "query": "Suvarnabhumi Airport Bangkok",
                "tip": "Start o 07:30–08:00 daje pełen bufor czasowy bez stresu."
            },
            {
                "time": "12:00",
                "title": "Zwrot samochodu na lotnisku BKK",
                "desc": "Oddanie kluczyków w wypożyczalni, szybki protokół zwrotu i przejście schodami ruchomymi do hali odlotów krajowych.",
                "price": "Rozliczenie wypożyczalni",
                "query": "Suvarnabhumi Airport Car Rental",
                "tip": "Zatankujcie auto do pełna na stacji benzynowej tuż przed lotniskiem."
            },
            {
                "time": "13:00",
                "title": "Odprawa & Bangkok Airways Lounge",
                "desc": "Wszyscy pasażerowie Bangkok Airways mają darmowy wstęp do saloniku Boutique Lounge z darmową kawą, sokami i przekąskami (np. tradycyjne ciastka ryżowe Khao Tom Mud).",
                "price": "Darmowe w cenie biletu",
                "query": "Bangkok Airways Boutique Lounge BKK",
                "tip": "Relaks w klimatyzowanym saloniku przed boardingiem."
            },
            {
                "time": "14:55",
                "title": "Wylot na Ko Samui (Lot PG155)",
                "desc": "Malowniczy lot nad Zatoką Tajlandzką. Lądowanie o 16:05 na bajkowym lotnisku na Samui (ogród tropikalny bez tradycyjnych ścian).",
                "price": "Bilet lotniczy PG155",
                "query": "Samui International Airport",
                "tip": "Jedno z najpiękniejszych lotnisk świata!"
            },
            {
                "time": "17:00",
                "title": "Check-in w Impiana Resort Chaweng Noi",
                "desc": "Zameldowanie w Waszym resorcie. Powitanie chłodnym ręcznikiem i świeżym napojem.",
                "price": "W cenie rezerwacji",
                "query": "Impiana Resort Chaweng Noi Koh Samui",
                "tip": "Wyjście na plażę dosłownie kilkanaście kroków od pokoju."
            },
            {
                "time": "18:30",
                "title": "Powitalna kolacja na piasku",
                "desc": "Szum ciepłych fal, świeży kokos i kolacja przy świecach na plaży Chaweng Noi.",
                "price": "Kolacja ~500–800 THB",
                "query": "Impiana Resort Chaweng Noi Koh Samui",
                "tip": "Rozpoczynamy 9 dni wyspiarskiego relaksu!"
            }
        ]
    },
    {
        "id": "day-7",
        "dayNum": 7,
        "date": "15 stycznia 2027 (Piątek)",
        "badgeDate": "15 STY",
        "type": "🧘 RELAKS #1",
        "typeClass": "tag-relax",
        "title": "Wyspiarski Reset na Chaweng Noi",
        "subtitle": "Brak budzika, ciepłe morze i masaże pod palmami",
        "hotel": "Impiana Resort Chaweng Noi",
        "hotelTip": "Śniadanie serwowane jest na zadaszonym tarasie nad samym morzem.",
        "bgImage": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #06222b 0%, #090d16 100%)",
        "items": [
            {
                "time": "09:30",
                "title": "Leniwe śniadanie z widokiem na Zatokę",
                "desc": "Owoce marakui, mango, świeżo parzona kawa i naleśniki z bananem.",
                "price": "W cenie hotelu",
                "query": "Impiana Resort Chaweng Noi Koh Samui",
                "tip": "Żadnego pośpiechu – dziś pełny reset."
            },
            {
                "time": "11:00",
                "title": "Kąpiele i plażowanie na Chaweng Noi",
                "desc": "Chaweng Noi słynie z braku ostrych koralowców i łagodnego wejścia do głębokiej wody. Cudowny, jasny piasek i ciepłe morze.",
                "price": "Wstęp wolny",
                "query": "Chaweng Noi Beach Koh Samui",
                "tip": "Pamiętajcie o kremie z filtrem UV 50+ – słońce w styczniu jest zdradliwe!"
            },
            {
                "time": "15:00",
                "title": "Tradycyjny masaż olejkowy na plaży",
                "desc": "Relaksujący masaż kokosowy w zadaszonej altanie na piasku. Szum fal w tle tworzy najpiękniejszą muzykę.",
                "price": "~300–400 THB / os.",
                "query": "Chaweng Noi Beach Koh Samui",
                "tip": "Masażystki na plaży robią doskonały masaż karku i stóp."
            },
            {
                "time": "18:30",
                "title": "Zachód słońca i spacer",
                "desc": "Koktajle z owoców tropikalnych i romantyczna kolacja w restauracji plażowej.",
                "price": "Kolacja ~400–700 THB",
                "query": "Chaweng Noi Beach Koh Samui",
                "tip": "Wspaniałe wyciszenie przed jutrzejszym zwiedzaniem."
            }
        ]
    },
    {
        "id": "day-8",
        "dayNum": 8,
        "date": "16 stycznia 2027 (Sobota)",
        "badgeDate": "16 STY",
        "type": "🛕 ZWIEDZANIE #1",
        "typeClass": "tag-explore",
        "title": "Big Buddha, Wat Plai Laem & Coco Tam's",
        "subtitle": "Kultura wyspy, niezwykłe skały i legendarny pokaz ognia",
        "hotel": "Impiana Resort Chaweng Noi",
        "hotelTip": "Transport: małe auto na ten dzień lub aplikacja Bolt.",
        "bgImage": "https://images.unsplash.com/photo-1544644181-1484b3fdfc62?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #1c1507 0%, #090d16 100%)",
        "items": [
            {
                "time": "09:00",
                "title": "Wielki Budda (Wat Phra Yai)",
                "desc": "12-metrowy Złoty Budda wznoszący się na małej wysepce połączonej z lądem groblą. Święte miejsce mieszkańców wyspy.",
                "price": "Wstęp wolny",
                "query": "Wat Phra Yai Koh Samui",
                "tip": "Pamiętajcie o zakrytych ramionach i kolanach."
            },
            {
                "time": "10:30",
                "title": "Wat Plai Laem – Świątynia na Jeziorze",
                "desc": "Kolorowy kompleks świątynny ze spektakularną 18-ramienną statuą Bogini Guanyin wznoszącą się pośrodku jeziora.",
                "price": "Wstęp wolny (karma dla ryb 10 THB)",
                "query": "Wat Plai Laem Koh Samui",
                "tip": "Kupcie paczkę karmy i nakarmcie potężne sumy pływające w wodzie!"
            },
            {
                "time": "12:30",
                "title": "Obiad w The Jungle Club z widokiem",
                "desc": "Słynna restauracja zawieszona na zboczu góry nad Chaweng. Pufy, leżaki i zapierająca dech panorama całej zatoki.",
                "price": "Obiad ~350–600 THB",
                "query": "The Jungle Club Samui",
                "tip": "Stromy podjazd – jeśli jedziecie autem, jedźcie ostrożnie na 1. biegu."
            },
            {
                "time": "14:45",
                "title": "Skały Hin Ta & Hin Yai (Dziadek i Babcia)",
                "desc": "Słynne formacje skalne uformowane przez naturę w Lamai. Przy wejściu targowisko z lokalnymi słodyczami.",
                "price": "Wstęp wolny (parking 20 THB)",
                "query": "Hin Ta Hin Yai Koh Samui",
                "tip": "Koniecznie spróbujcie lodów kokosowych w orzechu i karmelków Kalamae."
            },
            {
                "time": "18:00",
                "title": "Fisherman's Village w Bophut",
                "desc": "Nastrojowy deptak w dawnej osadzie rybackiej z drewnianą architekturą, butikami i nadrzecznymi restauracjami.",
                "price": "Wstęp wolny",
                "query": "Fisherman's Village Bophut",
                "tip": "Cudowna atmosfera na wieczorny spacer."
            },
            {
                "time": "20:30",
                "title": "Coco Tam's & Fire Show na plaży",
                "desc": "Kultowy klub plażowy z pufami i hamakami na piasku. Widowiskowy, profesjonalny taniec z ogniem nad brzegiem morza.",
                "price": "Koktajle ~280–380 THB",
                "query": "Coco Tam's Bophut",
                "tip": "Pokazy ognia odbywają się o 21:00 i 22:30 – spektakl jest oszałamiający!"
            }
        ]
    },
    {
        "id": "day-9",
        "dayNum": 9,
        "date": "17 stycznia 2027 (Niedziela)",
        "badgeDate": "17 STY",
        "type": "🧘 RELAKS #2",
        "typeClass": "tag-relax",
        "title": "Seszelskie Klimaty Silver Beach",
        "subtitle": "Krystaliczna zatoka Crystal Bay i snorkeling z brzegu",
        "hotel": "Impiana Resort Chaweng Noi",
        "hotelTip": "Zaledwie 7 minut jazdy samochodem lub Boltem z Waszego hotelu!",
        "bgImage": "https://images.unsplash.com/photo-1510414842594-a61c69b5ae57?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #092026 0%, #090d16 100%)",
        "items": [
            {
                "time": "09:30",
                "title": "Przejazd na Silver Beach (Crystal Bay)",
                "desc": "Jedna z najbardziej malowniczych plaż w całej Tajlandii, otoczona potężnymi, gładkimi głazami granitowymi niczym na Seszelach.",
                "price": "Wstęp wolny (Bolt ~150 THB)",
                "query": "Silver Beach Crystal Bay Samui",
                "tip": "Woda jest tu niewiarygodnie przezroczysta i spokojna."
            },
            {
                "time": "11:00",
                "title": "Snorkeling wśród granitowych skał",
                "desc": "Wystarczy założyć maskę i zanurzyć się tuż przy brzegu – wokół głazów pływają setki kolorowych rybek i ławice morskich stworzeń.",
                "price": "Darmowe (wypożyczenie maski ~100 THB)",
                "query": "Silver Beach Crystal Bay Samui",
                "tip": "Idealne, bezpieczne warunki do snorkelingu dla każdego."
            },
            {
                "time": "13:30",
                "title": "Lunch w cieniu palm na plaży",
                "desc": "Chłodne shake'i z arbuza i ananasa, sałatka Som Tam i krewetki w chrupiącym cieście.",
                "price": "Lunch ~250–400 THB",
                "query": "Crystal Bay Beach Club Samui",
                "tip": "Stoliki stoją w cieniu tropikalnych drzew tuż nad wodą."
            },
            {
                "time": "16:30",
                "title": "Popołudnie przy hotelowym basenie",
                "desc": "Powrót do Impiana Resort. Kąpiel w basenie, czytanie książki i chillout o zachodzie słońca.",
                "price": "W cenie hotelu",
                "query": "Impiana Resort Chaweng Noi Koh Samui",
                "tip": "Spokojny wieczór i wczesny sen przed jutrzejszym rejsem morskim."
            }
        ]
    },
    {
        "id": "day-10",
        "dayNum": 10,
        "date": "18 stycznia 2027 (Poniedziałek)",
        "badgeDate": "18 STY",
        "type": "🚤 MORSKA WYPRAWA",
        "typeClass": "tag-boat",
        "title": "Morski Park Narodowy Ang Thong",
        "subtitle": "Archipelag 42 bezludnych wysp, Szmaragdowe Jezioro i kajaki",
        "hotel": "Impiana Resort Chaweng Noi",
        "hotelTip": "Wycieczkę motorówką zarezerwujcie 2 dni wcześniej w recepcji lub na Klook.",
        "bgImage": "https://images.unsplash.com/photo-1533105079780-92b9be482077?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #071c24 0%, #090d16 100%)",
        "items": [
            {
                "time": "08:00",
                "title": "Odbiór z hotelu Impiana i transfer na przystań",
                "desc": "Klimatyzowany busik odbiera Was bezpośrednio z lobby hotelu i wiezie do przystani motorówek na północy wyspy.",
                "price": "W cenie wycieczki",
                "query": "Impiana Resort Chaweng Noi Koh Samui",
                "tip": "Załóżcie wygodne sandały/buty do wody i zabierzcie wodoodporny worek na telefon."
            },
            {
                "time": "10:00",
                "title": "Punkt widokowy Pha Jun Jaras (Koh Wua Talap)",
                "desc": "Wejście drewnianymi schodkami na szczyt wyspy – z platformy roztacza się jeden z najbardziej pocztówkowych widoków w Azji na 42 wapienne wyspy.",
                "price": "Wstęp do parku 300 THB / os. (GOTÓWKA)",
                "query": "Ang Thong National Marine Park",
                "tip": "Wspinaczka trwa ok. 30 minut – widok ze szczytu rekompensuje każdy wysiłek!"
            },
            {
                "time": "12:00",
                "title": "Szmaragdowa Laguna (Emerald Lake / Talay Nai)",
                "desc": "Przejście na wyspę Koh Mae Ko. Schody prowadzą do ukrytego w starym kraterze jeziora o jaskrawozielonej, szmaragdowej barwie.",
                "price": "W cenie wycieczki",
                "query": "Emerald Lake Koh Mae Ko",
                "tip": "Niezwykłe zjawisko geologiczne połączone podziemnymi tunelami z morzem."
            },
            {
                "time": "13:30",
                "title": "Kajaki morskie i snorkeling w jaskiniach",
                "desc": "Pływanie dwuosobowym kajakiem wzdłuż wapiennych klifów krasowych i snorkeling nad rafą pełną koralowców.",
                "price": "W cenie wycieczki",
                "query": "Ang Thong National Marine Park",
                "tip": "Tajski lunch w formie bufetu serwowany na bezludnej plaży."
            },
            {
                "time": "16:30",
                "title": "Powrót do Impiana Resort",
                "desc": "Rejs powrotny motorówką na Samui, transfer do hotelu, gorący prysznic i regeneracja po dniu pełnym przygód.",
                "price": "W cenie",
                "query": "Impiana Resort Chaweng Noi Koh Samui",
                "tip": "Pyszna, lekka kolacja w hotelu i relaksujący sen."
            }
        ]
    },
    {
        "id": "day-11",
        "dayNum": 11,
        "date": "19 stycznia 2027 (Wtorek)",
        "badgeDate": "19 STY",
        "type": "🧘 RELAKS #3",
        "typeClass": "tag-relax",
        "title": "Dzień Tajskiego SPA & Plaża Mae Nam",
        "subtitle": "Królewski rytuał dla dwojga i oaza spokoju na północy",
        "hotel": "Impiana Resort Chaweng Noi",
        "hotelTip": "Pakiet spa warto zarezerwować dzień wcześniej.",
        "bgImage": "https://images.unsplash.com/photo-1540555700478-4be289fbecef?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #1f101f 0%, #090d16 100%)",
        "items": [
            {
                "time": "10:00",
                "title": "Królewski Rytuał Day-SPA dla Dwojga",
                "desc": "2.5-godzinna sesja w renomowanym tajskim spa: peeling kokosowy, aromaterapeutyczny masaż całego ciała ciepłym olejkiem i kąpiel w płatkach kwiatów.",
                "price": "~1500–2500 THB / os.",
                "query": "Eranda Herbal Spa Koh Samui",
                "tip": "Ciało i umysł zrelaksują się w 100%."
            },
            {
                "time": "14:00",
                "title": "Plaża Mae Nam – Ucieczka od Zgiełku",
                "desc": "Przejazd na plażę Mae Nam na północy wyspy. Szeroka, spokojna plaża z głębszą wodą i pięknym widokiem na góry wyspy Koh Phangan.",
                "price": "Wstęp wolny",
                "query": "Mae Nam Beach Samui",
                "tip": "Brak tłumów i głośnych skuterów wodnych – idealna na spacer i czytanie."
            },
            {
                "time": "18:30",
                "title": "Kolacja z rybą pieczoną w soli (Pla Pao)",
                "desc": "Tradycyjna tajska kolacja w plażowej restauracji. Cała świeża ryba pieczona w grubej skorupie soli morskiej z trawą cytrynową i sosem z limonki.",
                "price": "Kolacja ~300–450 THB",
                "query": "Mae Nam Beach Samui",
                "tip": "Pla Pao to absolutny przysmak tajskiego wybrzeża!"
            }
        ]
    },
    {
        "id": "day-12",
        "dayNum": 12,
        "date": "20 stycznia 2027 (Środa)",
        "badgeDate": "20 STY",
        "type": "🌴 DŻUNGLA LUB ŚWINKI",
        "typeClass": "tag-explore",
        "title": "Wodospady Na Muang & Ogród w Chmurach",
        "subtitle": "Kąpiel w basenie skalnym i tajemniczy Secret Buddha Garden",
        "hotel": "Impiana Resort Chaweng Noi",
        "hotelTip": "Dzień pełen zieleni i górskiego chłodu we wnętrzu wyspy.",
        "bgImage": "https://images.unsplash.com/photo-1544735716-392fe2489ffa?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #0f1c0f 0%, #090d16 100%)",
        "items": [
            {
                "time": "09:00",
                "title": "Wodospady Na Muang 1 i 2",
                "desc": "Trekking przez las deszczowy do majestatycznych wodospadów spływających po fioletowych skałach. Kąpiel w chłodnym, naturalnym basenie pod kaskadą.",
                "price": "Wstęp wolny (parking 30 THB)",
                "query": "Na Muang Waterfall Koh Samui",
                "tip": "Wybierzcie Na Muang 2 dla bardziej kameralnej atmosfery."
            },
            {
                "time": "11:30",
                "title": "Tarnim Magic Garden (Secret Buddha Garden)",
                "desc": "Mistyczny ogród rzeźb ukryty wysoko na najwyższych wzgórzach wyspy pośród mgieł i dżungli. Stworzony przez 77-letniego mnicha i farmera.",
                "price": "80 THB / os.",
                "query": "Secret Buddha Garden Koh Samui",
                "tip": "Niezwykła energia, kamienne posągi buddyjskie i strumyki."
            },
            {
                "time": "13:30",
                "title": "Lunch w restauracji Giant Summit",
                "desc": "Posiłek w restauracji zawieszonej nad przepaścią z widokiem na południowy kraniec wyspy i sąsiednie wysepki.",
                "price": "Lunch ~250–400 THB",
                "query": "Giant Summit Samui",
                "tip": "Cudowna panorama i orzeźwiający górski wiaterek."
            },
            {
                "time": "Alternatywa",
                "title": "Wyspa Świnek (Koh Madsum) – opcjonalnie",
                "desc": "Zamiast gór możecie wybrać popołudniowy rejs drewnianą łodzią z Thong Krut na plażę z oswojonymi, pływającymi świnkami.",
                "price": "Łódź ~1500 THB za dwoje",
                "query": "Koh Madsum Pig Island",
                "tip": "Zabawne zdjęcia ze świnkami spacerującymi po białym piasku!"
            }
        ]
    },
    {
        "id": "day-13",
        "dayNum": 13,
        "date": "21 stycznia 2027 (Czwartek)",
        "badgeDate": "21 STY",
        "type": "🧘 RELAKS #4",
        "typeClass": "tag-relax",
        "title": "Coral Cove & Krwisty Zachód Słońca",
        "subtitle": "Kameralna zatoczka i pożegnanie dnia w Lipa Noi",
        "hotel": "Impiana Resort Chaweng Noi",
        "hotelTip": "Zatoczka Coral Cove znajduje się dosłownie 3 minuty od Chaweng Noi.",
        "bgImage": "https://images.unsplash.com/photo-1506744038136-46273834b3fb?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #1f0a14 0%, #090d16 100%)",
        "items": [
            {
                "time": "10:00",
                "title": "Zatoczka Coral Cove",
                "desc": "Mała, urocza zatoczka wciśnięta między skaliste cyple. Płytka, szmaragdowa woda, głazy i cień palm.",
                "price": "Wstęp wolny",
                "query": "Coral Cove Beach Samui",
                "tip": "Świetne miejsce na ustronne plażowanie z dala od jakichkolwiek tłumów."
            },
            {
                "time": "16:00",
                "title": "Wyjazd na zachodnie wybrzeże (Lipa Noi / Taling Ngam)",
                "desc": "Przejazd na zachodnią stronę wyspy, gdzie słońce chowa się bezpośrednio za horyzontem Zatoki Tajlandzkiej.",
                "price": "Bolt ~400 THB",
                "query": "Lipa Noi Beach Samui",
                "tip": "To tu powstają najwspanialsze zachody słońca w całej Tajlandii."
            },
            {
                "time": "17:30",
                "title": "Drink w Air Bar (InterContinental)",
                "desc": "Elegancki taras zawieszony na klifie nad morzem. Muzyka na żywo i widok na mieniące się purpurą i złotem morze.",
                "price": "Drinki ~350–500 THB",
                "query": "Air Bar Koh Samui",
                "tip": "Niezwykle romantyczna chwila."
            },
            {
                "time": "19:30",
                "title": "Kolacja przy świecach na plaży Lipa Noi",
                "desc": "Stolik w piasku oświetlony lampionami, pieczone kalmary, krewetki tygrysie i białe wino.",
                "price": "Kolacja ~600–900 THB",
                "query": "Lipa Noi Beach Samui",
                "tip": "Magiczny wieczór."
            }
        ]
    },
    {
        "id": "day-14",
        "dayNum": 14,
        "date": "22 stycznia 2027 (Piątek)",
        "badgeDate": "22 STY",
        "type": "🐘 SŁONIE & KULINARIA",
        "typeClass": "tag-explore",
        "title": "Etyczne Słonie & Lekcja Gotowania",
        "subtitle": "Bliskie spotkanie z olbrzymami i sekrety tajskich przypraw",
        "hotel": "Impiana Resort Chaweng Noi",
        "hotelTip": "Ostatnia noc na Ko Samui – jutro powrót do Bangkoku!",
        "bgImage": "https://images.unsplash.com/photo-1557050543-4d5f4e07ef46?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #1c1809 0%, #090d16 100%)",
        "items": [
            {
                "time": "09:00",
                "title": "Samui Elephant Sanctuary (Etyczne Sanktuarium)",
                "desc": "Certyfikowany rezerwat ratujący słonie z niewoli. Przygotowywanie kul witaminowych, karmienie bananami z ręki, wspólny spacer przez dżunglę i podglądanie ich kąpieli w błocie.",
                "price": "~3000 THB / os. (REZERWACJA ONLINE!)",
                "query": "Samui Elephant Sanctuary",
                "tip": "Żadnego ujeżdżania czy łańcuchów – 100% szacunku i etyki. Zarezerwujcie min. 2 tyg. wcześniej!"
            },
            {
                "time": "14:00",
                "title": "Warsztaty Gotowania Kuchni Tajskiej dla Par",
                "desc": "Prywatna lekcja z szefem kuchni: wizyta na targu po zioła, gotowanie autentycznego Pad Thaia, zupy Tom Kha Gai i mango sticky rice.",
                "price": "~1200–1600 THB / os.",
                "query": "Samui Cooking Class",
                "tip": "Zabierzecie do domu książkę kucharską i umiejętności na całe życie!"
            },
            {
                "time": "18:30",
                "title": "Ostatni wieczór na plaży Chaweng Noi",
                "desc": "Pożegnalny koktajl w barze Impiana Resort, spacer brzegiem ciepłego morza i pakowanie walizek.",
                "price": "Koszty własne",
                "query": "Impiana Resort Chaweng Noi Koh Samui",
                "tip": "Sprawdźcie bilety lotnicze na jutrzejszy lot PG1190 o 11:35."
            }
        ]
    },
    {
        "id": "day-15",
        "dayNum": 15,
        "date": "23 stycznia 2027 (Sobota)",
        "badgeDate": "23 STY",
        "type": "👑 KRÓLEWSKI FINAŁ",
        "typeClass": "tag-luxury",
        "title": "Lot do Bangkoku (11:35) & lebua at State Tower",
        "subtitle": "Apartament nad rzeką i legendarny Sky Bar na 63. piętrze",
        "hotel": "lebua at State Tower Bangkok (5★ Luxury)",
        "hotelTip": "The Dome & Sky Bar na 63. piętrze – sceneria z filmu Kac Vegas w Bangkoku!",
        "bgImage": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #181124 0%, #090d16 100%)",
        "items": [
            {
                "time": "09:30",
                "title": "Przejazd na lotnisko Ko Samui (USM)",
                "desc": "Wymeldowanie z Impiana Resort i krótki transfer na lotnisko Samui (ok. 15 minut jazdy).",
                "price": "Bolt ~300 THB",
                "query": "Samui International Airport",
                "tip": "Klimatyczny spacer wśród palm w otwartym terminalu ogrodowym."
            },
            {
                "time": "11:35",
                "title": "Wylot do Bangkoku (Lot PG1190)",
                "desc": "Rejsowy lot Bangkok Airways. Lądowanie o 12:55 na lotnisku Suvarnabhumi (BKK).",
                "price": "Bilet lotniczy PG1190",
                "query": "Suvarnabhumi Airport Bangkok",
                "tip": "Odbiór bagażu i przejazd taksówką do serca Bangkoku."
            },
            {
                "time": "14:30",
                "title": "Check-in w lebua at State Tower",
                "desc": "Zameldowanie w 5★ wieżowcu. Wasz luksusowy apartament z prywatnym balkonem oferuje zapierający dech widok na meandry rzeki Chao Phraya i morze wieżowców.",
                "price": "W cenie rezerwacji",
                "query": "lebua at State Tower Bangkok",
                "tip": "Wyjdźcie na balkon i poczujcie potęgę tej metropolii!"
            },
            {
                "time": "16:30",
                "title": "Ostatnie zakupy pamiątek",
                "desc": "Krótki wypad na zakupy wysokiej jakości pamiątek (tajski jedwab, kosmetyki kokosowe, herbata Blue Butterfly Pea, suszone mango).",
                "price": "Koszty własne",
                "query": "Siam Paragon Bangkok",
                "tip": "Możliwość uzyskania zwrotu podatku VAT (formularz VAT Refund w sklepach)."
            },
            {
                "time": "18:00",
                "title": "The Dome at lebua: Toast w Sky Barze",
                "desc": "Wjazd na 63. piętro pod słynną Złotą Kopułę. Toast kieliszkiem szampana na otwartej platformie zawieszonej setki metrów nad ziemią o zachodzie słońca.",
                "price": "Koktajle ~800–1200 THB",
                "query": "Sky Bar lebua Bangkok",
                "tip": "OBOWIĄZKOWY DRESS CODE SMART CASUAL: Mężczyźni: długie spodnie, kryte buty, koszula/polo. Kobiety: elegancka sukienka."
            },
            {
                "time": "20:30",
                "title": "Wykwintna Pożegnalna Kolacja",
                "desc": "Królewski finał podróży pod rozgwieżdżonym niebem Bangkoku. Wspomnienia, które zostaną z Wami na całe życie.",
                "price": "Koszty własne",
                "query": "Sirocco Restaurant Bangkok",
                "tip": "Niezapomniane zwieńczenie wyprawy."
            }
        ]
    },
    {
        "id": "day-16",
        "dayNum": 16,
        "date": "24 stycznia 2027 (Niedziela)",
        "badgeDate": "24 STY",
        "type": "🛫 POWRÓT DO POLSKI",
        "typeClass": "tag-flight",
        "title": "Do Zobaczenia, Tajlandio!",
        "subtitle": "Królewskie śniadanie i lot powrotny z BKK o 10:50",
        "hotel": "Wylot do Polski",
        "hotelTip": "Bądźcie na lotnisku BKK o 08:00 (dokładnie 2h50m przed startem).",
        "bgImage": "https://images.unsplash.com/photo-1436491865332-7a61a109cc05?auto=format&fit=crop&w=1200&q=80",
        "bgFallback": "linear-gradient(180deg, #111a2e 0%, #090d16 100%)",
        "items": [
            {
                "time": "07:00",
                "title": "Królewskie śniadanie w restauracji Cafe Mozu",
                "desc": "Jedno z najbardziej renomowanych śniadań hotelowych w Azji z widokiem na basen w stylu marokańskim.",
                "price": "W cenie rezerwacji",
                "query": "lebua at State Tower Bangkok",
                "tip": "Wspaniały wybór owoców, pieczywa i dań z całego świata."
            },
            {
                "time": "07:30",
                "title": "Wymeldowanie i transfer na lotnisko BKK",
                "desc": "Taksówka autostradą Sirat Expressway na lotnisko Suvarnabhumi. Niedzielny poranek gwarantuje brak jakichkolwiek korków (ok. 30–35 min jazdy).",
                "price": "Taksówka ~400 THB",
                "query": "Suvarnabhumi Airport Bangkok",
                "tip": "Poproście boya hotelowego o wezwanie taksówki z włączonym taksometrem lub zamówcie Bolt."
            },
            {
                "time": "08:15",
                "title": "Terminal BKK: Odprawa i Kontrola",
                "desc": "Nadanie bagaży rejestrowanych, ewentualne podbicie pieczątek VAT Refund w urzędzie celnym, kontrola bezpieczeństwa i paszportowa.",
                "price": "W cenie biletu",
                "query": "Suvarnabhumi Airport Departures",
                "tip": "W strefie bezcłowej King Power możecie wydać ostatnie bahty na pamiątki."
            },
            {
                "time": "10:50",
                "title": "Wylot do Polski",
                "desc": "Start samolotu powrotnego. Szczęśliwy powrót do domu z tysiącem zdjęć, opalenizną i wspaniałymi wspomnieniami!",
                "price": "Lot powrotny",
                "query": "Suvarnabhumi Airport Bangkok",
                "tip": "Khai Khup Khun Krap – dziękujemy, Tajlandio!"
            }
        ]
    }
]


html_head = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
  <title>Tajlandia 2027 • Harmonogram Podróży</title>
  <meta name="theme-color" content="#090d16">
  <link rel="manifest" href="./manifest.json">
  <meta name="apple-mobile-web-app-capable" content="yes">
  <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
  <meta name="apple-mobile-web-app-title" content="Tajlandia 2027">
  <link rel="apple-touch-icon" sizes="192x192" href="./icon-192.png">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  <style>
    :root {
      --bg-dark: #090d16;
      --card-bg: rgba(15, 23, 42, 0.90);
      --card-border: rgba(255, 255, 255, 0.16);
      --gold: #f59e0b;
      --gold-light: #fef3c7;
      --gold-gradient: linear-gradient(135deg, #fbbf24 0%, #d97706 100%);
      --text-main: #f8fafc;
      --text-muted: #94a3b8;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      -webkit-tap-highlight-color: transparent;
    }

    /* NATURAL FULLSCREEN (EXACT SAME AS CNC-KALKULATOR) */
    html {
      overflow-y: auto;
      scrollbar-gutter: stable;
      overscroll-behavior-y: none;
      background-color: #090d16;
    }

    body {
      min-height: 100vh;
      margin: 0;
      padding: 0;
      overflow-x: hidden;
      overflow-y: visible;
      background-color: #090d16;
      font-family: 'Plus Jakarta Sans', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      color: var(--text-main);
      -webkit-font-smoothing: antialiased;
      -webkit-text-size-adjust: 100%;
    }

    #root, .app-root {
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      position: relative;
    }

    /* Fixed 100% Solid Header */
    .top-bar {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      z-index: 100;
      height: calc(max(env(safe-area-inset-top, 20px), 20px) + 52px);
      padding-top: max(env(safe-area-inset-top, 20px), 20px);
      padding-left: 16px;
      padding-right: 16px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: #090d16;
      border-bottom: 1px solid rgba(255, 255, 255, 0.12);
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.85);
      box-sizing: border-box;
    }

    .top-bar-inner {
      width: 100%;
      max-width: 600px;
      margin: 0 auto;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }

    .nav-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: #1e293b;
      border: 1px solid rgba(245, 158, 11, 0.5);
      padding: 6px 14px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 700;
      color: #ffffff;
      line-height: 1;
    }

    .nav-badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: #10b981;
      flex-shrink: 0;
    }

    .icon-btn {
      background: #1e293b;
      border: 1px solid rgba(245, 158, 11, 0.5);
      color: #fbbf24;
      width: 38px;
      height: 38px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: transform 0.15s, background 0.15s;
    }

    .icon-btn:active {
      transform: scale(0.92);
      background: rgba(245, 158, 11, 0.25);
    }

    .progress-track {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      height: 3px;
      background: rgba(255, 255, 255, 0.1);
      z-index: 101;
    }

    .progress-fill {
      height: 100%;
      width: 0%;
      background: var(--gold-gradient);
      transition: width 0.3s ease-out;
    }

    /* SLIDE CONTAINERS (NATURAL DOCUMENT FLOW) */
    .slide {
      display: none;
      width: 100%;
      min-height: 100vh;
      position: relative;
      box-sizing: border-box;
    }

    .slide.active {
      display: block;
      animation: slideFadeIn 0.25s ease-out forwards;
    }

    @keyframes slideFadeIn {
      from {
        opacity: 0;
        transform: translateY(8px);
      }
      to {
        opacity: 1;
        transform: translateY(0);
      }
    }

    /* Fixed Background Layer (Covers Physical Glass 100%) */
    .slide-bg {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      width: 100vw;
      height: 100vh;
      background-size: cover;
      background-position: center;
      z-index: 1;
      pointer-events: none;
    }

    .slide-overlay {
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      width: 100vw;
      height: 100vh;
      z-index: 2;
      pointer-events: none;
      background: linear-gradient(
        180deg,
        rgba(9, 13, 22, 0.30) 0%,
        rgba(9, 13, 22, 0.60) 45%,
        rgba(9, 13, 22, 0.85) 100%
      );
    }

    /* Content Layout - Natural Scroll & Safe Area Padding */
    .slide-content {
      position: relative;
      z-index: 10;
      width: 100%;
      max-width: 600px;
      min-height: 100vh;
      margin: 0 auto;
      box-sizing: border-box;
      padding-top: calc(max(env(safe-area-inset-top, 20px), 20px) + 64px);
      padding-bottom: max(2.5rem, env(safe-area-inset-bottom, 24px));
      padding-left: 16px;
      padding-right: 16px;
      display: flex;
      flex-direction: column;
    }

    /* INTRO SLIDE SPECIALS */
    .intro-hero {
      margin-top: auto;
      margin-bottom: auto;
      text-align: center;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 14px;
      padding-top: 20px;
      padding-bottom: 20px;
    }

    .intro-tag {
      background: rgba(245, 158, 11, 0.2);
      border: 1px solid rgba(245, 158, 11, 0.5);
      color: #fbbf24;
      padding: 6px 16px;
      border-radius: 999px;
      font-size: 13px;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .intro-title {
      font-size: 40px;
      font-weight: 800;
      line-height: 1.1;
      background: linear-gradient(135deg, #ffffff 30%, #fef3c7 70%, #f59e0b 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      letter-spacing: -0.5px;
    }

    .intro-subtitle {
      font-size: 16px;
      color: var(--text-muted);
      font-weight: 600;
    }

    /* Countdown Widget */
    .countdown-card {
      width: 100%;
      max-width: 360px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 24px;
      padding: 20px;
      margin-top: 4px;
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.5);
    }

    .countdown-label {
      font-size: 12px;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #fbbf24;
      margin-bottom: 12px;
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 6px;
    }

    .countdown-grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 8px;
    }

    .countdown-box {
      background: rgba(0, 0, 0, 0.45);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 14px;
      padding: 10px 4px;
      text-align: center;
    }

    .countdown-num {
      font-size: 26px;
      font-weight: 800;
      color: #fff;
      line-height: 1;
    }

    .countdown-unit {
      font-size: 10px;
      color: var(--text-muted);
      text-transform: uppercase;
      font-weight: 600;
      margin-top: 4px;
    }

    /* Stats bar */
    .stats-row {
      display: flex;
      gap: 10px;
      width: 100%;
      max-width: 360px;
      margin-top: 4px;
    }

    .stat-pill {
      flex: 1;
      background: rgba(15, 23, 42, 0.75);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 16px;
      padding: 10px 6px;
      text-align: center;
    }

    .stat-pill-num {
      font-size: 18px;
      font-weight: 800;
      color: #fbbf24;
    }

    .stat-pill-label {
      font-size: 11px;
      color: var(--text-muted);
    }

    .intro-footer {
      margin-top: auto;
      text-align: center;
      padding-top: 16px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
    }

    .start-btn {
      background: var(--gold-gradient);
      color: #090d16;
      border: none;
      padding: 14px 34px;
      border-radius: 999px;
      font-size: 16px;
      font-weight: 800;
      cursor: pointer;
      box-shadow: 0 10px 25px rgba(245, 158, 11, 0.4);
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: transform 0.15s;
    }

    .start-btn:active {
      transform: scale(0.95);
    }

    .swipe-hint {
      font-size: 13px;
      color: rgba(255, 255, 255, 0.7);
      display: flex;
      align-items: center;
      gap: 6px;
      font-weight: 600;
      animation: bounce 2s infinite;
    }

    @keyframes bounce {
      0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
      40% { transform: translateY(-7px); }
      60% { transform: translateY(-3px); }
    }

    /* DAY SLIDE HEADERS */
    .day-header {
      margin-bottom: 12px;
    }

    .day-top-meta {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-bottom: 8px;
      flex-wrap: wrap;
    }

    .day-pill {
      background: rgba(255, 255, 255, 0.14);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      font-size: 12px;
      font-weight: 700;
      padding: 4px 10px;
      border-radius: 8px;
    }

    .tag-arrival { background: rgba(59, 130, 246, 0.25); border-color: rgba(59, 130, 246, 0.5); color: #93c5fd; }
    .tag-explore { background: rgba(245, 158, 11, 0.25); border-color: rgba(245, 158, 11, 0.5); color: #fbbf24; }
    .tag-drive { background: rgba(168, 85, 247, 0.25); border-color: rgba(168, 85, 247, 0.5); color: #d8b4fe; }
    .tag-nature { background: rgba(16, 185, 129, 0.25); border-color: rgba(16, 185, 129, 0.5); color: #6ee7b7; }
    .tag-flight { background: rgba(14, 165, 233, 0.25); border-color: rgba(14, 165, 233, 0.5); color: #7dd3fc; }

    .day-date-text {
      font-size: 13px;
      color: var(--text-muted);
      font-weight: 600;
    }

    .day-title {
      font-size: 26px;
      font-weight: 800;
      line-height: 1.15;
      color: #fff;
      margin-bottom: 4px;
    }

    .day-subtitle {
      font-size: 14px;
      color: #cbd5e1;
      line-height: 1.4;
    }

    /* Hotel Card */
    .hotel-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 16px;
      padding: 12px 14px;
      margin-bottom: 14px;
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }

    .hotel-icon {
      font-size: 22px;
      flex-shrink: 0;
      margin-top: 2px;
    }

    .hotel-info-name {
      font-size: 14px;
      font-weight: 700;
      color: #fff;
    }

    .hotel-info-tip {
      font-size: 12px;
      color: var(--text-muted);
      margin-top: 2px;
      line-height: 1.35;
    }

    /* Timeline Items */
    .timeline-container {
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-bottom: 14px;
    }

    .timeline-card {
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 18px;
      padding: 16px;
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.4);
    }

    .timeline-card-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 8px;
    }

    .time-badge {
      background: var(--gold-gradient);
      color: #090d16;
      font-size: 12px;
      font-weight: 800;
      padding: 3px 8px;
      border-radius: 6px;
      letter-spacing: 0.5px;
    }

    .timeline-price-tag {
      font-size: 12px;
      font-weight: 700;
      color: #38bdf8;
      background: rgba(14, 165, 233, 0.2);
      border: 1px solid rgba(14, 165, 233, 0.4);
      padding: 3px 8px;
      border-radius: 6px;
    }

    .timeline-title {
      font-size: 17px;
      font-weight: 700;
      color: #fff;
      line-height: 1.25;
      margin-bottom: 6px;
    }

    .timeline-desc {
      font-size: 13px;
      color: #cbd5e1;
      line-height: 1.45;
      margin-bottom: 12px;
    }

    .timeline-tip-box {
      background: rgba(0, 0, 0, 0.35);
      border-left: 3px solid #fbbf24;
      padding: 8px 10px;
      border-radius: 0 8px 8px 0;
      font-size: 12px;
      color: #e2e8f0;
      line-height: 1.35;
      margin-bottom: 12px;
      display: flex;
      gap: 6px;
    }

    .timeline-actions {
      display: flex;
      justify-content: flex-end;
    }

    .maps-btn {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(255, 255, 255, 0.2);
      color: #fff;
      padding: 7px 14px;
      border-radius: 10px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      transition: background 0.15s, transform 0.15s;
    }

    .maps-btn:active {
      transform: scale(0.95);
      background: rgba(245, 158, 11, 0.3);
    }

    /* Bottom Navigation Bar for Days */
    .day-nav-bar {
      display: flex;
      gap: 8px;
      margin-top: 14px;
      justify-content: space-between;
      align-items: center;
    }

    .day-nav-btn {
      flex: 1;
      background: rgba(15, 23, 42, 0.85);
      border: 1px solid rgba(255, 255, 255, 0.16);
      color: #fff;
      padding: 13px 10px;
      border-radius: 14px;
      font-size: 13px;
      font-weight: 700;
      cursor: pointer;
      text-align: center;
      transition: background 0.15s, transform 0.15s;
    }

    .day-nav-btn:active {
      transform: scale(0.96);
      background: rgba(245, 158, 11, 0.25);
    }

    .day-nav-btn-main {
      border-color: rgba(245, 158, 11, 0.5);
      color: #fbbf24;
    }

    /* Modal / Bottom Drawer for Day Selection */
    .drawer-backdrop {
      position: fixed;
      inset: 0;
      width: 100vw;
      height: 100vh;
      background: rgba(0, 0, 0, 0.75);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      z-index: 200;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }

    .drawer-backdrop.active {
      opacity: 1;
      pointer-events: auto;
    }

    .drawer-sheet {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      max-height: 85vh;
      background: #0f172a;
      border-top: 1px solid rgba(255, 255, 255, 0.15);
      border-radius: 28px 28px 0 0;
      padding: 20px 20px calc(max(env(safe-area-inset-bottom, 20px), 20px) + 16px);
      z-index: 201;
      transform: translateY(100%);
      transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
      display: none;
      flex-direction: column;
    }

    .drawer-sheet.active {
      display: flex;
      transform: translateY(0);
    }

    .drawer-handle {
      width: 44px;
      height: 5px;
      background: rgba(255, 255, 255, 0.35);
      border-radius: 999px;
      margin: 0 auto 16px;
    }

    .drawer-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      margin-bottom: 16px;
    }

    .drawer-title {
      font-size: 20px;
      font-weight: 800;
      color: #fff;
    }

    .drawer-close {
      background: rgba(255, 255, 255, 0.12);
      border: none;
      color: #fff;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      cursor: pointer;
      font-size: 16px;
    }

    .drawer-list {
      overflow-y: auto;
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding-right: 4px;
    }

    .drawer-item {
      display: flex;
      align-items: center;
      justify-content: space-between;
      background: rgba(255, 255, 255, 0.05);
      border: 1px solid rgba(255, 255, 255, 0.08);
      border-radius: 14px;
      padding: 12px 14px;
      cursor: pointer;
      text-decoration: none;
      color: #fff;
      transition: background 0.15s;
    }

    .drawer-item:active {
      background: rgba(245, 158, 11, 0.25);
    }

    .drawer-item-title {
      font-size: 14px;
      font-weight: 700;
    }

    .drawer-item-sub {
      font-size: 12px;
      color: var(--text-muted);
    }

    .drawer-item-badge {
      font-size: 11px;
      font-weight: 800;
      padding: 4px 8px;
      border-radius: 6px;
      background: rgba(245, 158, 11, 0.2);
      color: #fbbf24;
    }
  </style>
</head>
<body style="margin:0;background-color:#090d16;">

  <!-- Fixed Top Header -->
  <header class="top-bar">
    <div class="progress-track"><div class="progress-fill" id="progressFill"></div></div>
    <div class="top-bar-inner">
      <div class="nav-badge" id="navBadge" role="status" aria-live="polite">
        <span class="nav-badge-dot"></span>
        <span id="navBadgeText">🇹🇭 Tajlandia '27</span>
      </div>
      <div style="display: flex; gap: 8px; align-items: center;">
        <button class="icon-btn" onclick="forceAppRefresh()" title="Wymuś odświeżenie" aria-label="Odśwież aplikację">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21.5 2v6h-6M2.5 22v-6h6M2 11.5a10 10 0 0 1 18.8-4.3M22 12.5a10 10 0 0 1-18.8 4.2"/>
          </svg>
        </button>
        <button class="icon-btn" id="btnDrawer" title="Harmonogram dni" aria-label="Wybierz dzień z listy">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#fbbf24" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
            <line x1="16" y1="2" x2="16" y2="6"></line>
            <line x1="8" y1="2" x2="8" y2="6"></line>
            <line x1="3" y1="10" x2="21" y2="10"></line>
          </svg>
        </button>
      </div>
    </div>
  </header>

  <!-- NATURAL SCROLL ROOT (LIKE CNC-KALKULATOR) -->
  <main id="root" class="app-root">
"""

html_body_slides = ""
for idx, s in enumerate(slides_data):
    is_active = " active" if idx == 0 else ""
    if s.get("isIntro"):
        html_body_slides += f"""
    <!-- SLIDE 0: INTRO & COUNTDOWN -->
    <section class="slide{is_active}" id="slide-intro" data-index="0" data-label="🇹🇭 Start">
      <div class="slide-bg" style="background-image: url('{s["bgImage"]}');"></div>
      <div class="slide-overlay"></div>
      <div class="slide-content">
        <div class="intro-hero">
          <div class="intro-tag">🌴 TAJLANDIA 2027</div>
          <h1 class="intro-title">{s["title"]}</h1>
          <p class="intro-subtitle">{s["subtitle"]}</p>

          <!-- Live Countdown Card -->
          <div class="countdown-card">
            <div class="countdown-label">⏳ Odliczanie do Wylotu (8 Sty 2027)</div>
            <div class="countdown-grid" id="countdownGrid">
              <div class="countdown-box">
                <div class="countdown-num" id="cDays">--</div>
                <div class="countdown-unit">Dni</div>
              </div>
              <div class="countdown-box">
                <div class="countdown-num" id="cHours">--</div>
                <div class="countdown-unit">Godz</div>
              </div>
              <div class="countdown-box">
                <div class="countdown-num" id="cMins">--</div>
                <div class="countdown-unit">Min</div>
              </div>
              <div class="countdown-box">
                <div class="countdown-num" id="cSecs">--</div>
                <div class="countdown-unit">Sek</div>
              </div>
            </div>
          </div>

          <!-- Trip Stats -->
          <div class="stats-row">
            <div class="stat-pill">
              <div class="stat-pill-num">17</div>
              <div class="stat-pill-label">Dni podróży</div>
            </div>
            <div class="stat-pill">
              <div class="stat-pill-num">4</div>
              <div class="stat-pill-label">Bazy hotelowe</div>
            </div>
            <div class="stat-pill">
              <div class="stat-pill-num">3</div>
              <div class="stat-pill-label">Krainy</div>
            </div>
          </div>
        </div>

        <div class="intro-footer">
          <button class="start-btn" onclick="goToSlide(1)">Rozpocznij Podróż ➔</button>
          <div class="swipe-hint">
            <span>👆 Przesuń w górę, aby przejść do Dnia 1</span>
          </div>
        </div>
      </div>
    </section>
"""
    else:
        day_num = s["dayNum"]
        slide_idx = day_num
        prev_idx = slide_idx - 1
        next_idx = slide_idx + 1
        prev_label = f"Dzień {prev_idx}" if prev_idx > 0 else "Odliczanie"
        next_label = f"Dzień {next_idx}" if next_idx <= 16 else "Początek"

        html_body_slides += f"""
    <!-- SLIDE {slide_idx}: DZIEŃ {day_num} -->
    <section class="slide{is_active}" id="{s["id"]}" data-index="{slide_idx}" data-label="Dzień {day_num} / 16 • {s["badgeDate"]}">
      <div class="slide-bg" style="background-image: url('{s["bgImage"]}');"></div>
      <div class="slide-overlay"></div>
      <div class="slide-content">
        
        <!-- Header -->
        <div class="day-header">
          <div class="day-top-meta">
            <span class="day-pill">Dzień {day_num} z 16</span>
            <span class="day-pill {s.get('typeClass', 'tag-explore')}">{s["type"]}</span>
            <span class="day-date-text">{s["date"]}</span>
          </div>
          <h2 class="day-title">{s["title"]}</h2>
          <p class="day-subtitle">{s["subtitle"]}</p>
        </div>

        <!-- Hotel Card -->
        <div class="hotel-card">
          <div class="hotel-icon">🏨</div>
          <div class="hotel-info">
            <div class="hotel-info-name">{s["hotel"]}</div>
            <div class="hotel-info-tip">{s["hotelTip"]}</div>
          </div>
        </div>

        <!-- Timeline Items -->
        <div class="timeline-container">
"""
        for it in s["items"]:
            encoded_query = it["query"].replace(" ", "+")
            maps_url = f"https://www.google.com/maps/search/?api=1&query={encoded_query}"
            html_body_slides += f"""
          <div class="timeline-card">
            <div class="timeline-card-header">
              <span class="time-badge">{it["time"]}</span>
              <span class="timeline-price-tag">{it["price"]}</span>
            </div>
            <h3 class="timeline-title">{it["title"]}</h3>
            <p class="timeline-desc">{it["desc"]}</p>
            <div class="timeline-tip-box">
              <span>💡</span>
              <div>{it["tip"]}</div>
            </div>
            <div class="timeline-actions">
              <a href="{maps_url}" target="_blank" rel="noopener" class="maps-btn">
                <span>📍</span>
                <span>Otwórz w Google Maps</span>
              </a>
            </div>
          </div>
"""
        html_body_slides += f"""
        </div>

        <!-- Bottom Day Switcher Navigation -->
        <div class="day-nav-bar">
          <button class="day-nav-btn" onclick="goToSlide({prev_idx})">◀ {prev_label}</button>
          <button class="day-nav-btn day-nav-btn-main" onclick="openDrawer()">📅 Spis dni</button>
          <button class="day-nav-btn" onclick="goToSlide({next_idx if next_idx <= 16 else 0})">{next_label} ▶</button>
        </div>

      </div>
    </section>
"""

html_drawer_and_script = """
  </main>

  <!-- Backdrop for drawer -->
  <div class="drawer-backdrop" id="backdrop"></div>

  <!-- Day Selection Drawer -->
  <div class="drawer-sheet" id="drawerSheet" role="dialog" aria-modal="true" aria-label="Wybierz dzień podróży">
    <div class="drawer-handle"></div>
    <div class="drawer-header">
      <h3 class="drawer-title">📅 Harmonogram Dni</h3>
      <button class="drawer-close" id="btnCloseDrawer" aria-label="Zamknij">✕</button>
    </div>
    <div class="drawer-list">
      <a class="drawer-item" onclick="selectDay(0)">
        <div>
          <div class="drawer-item-title">Odliczanie do Wylotu</div>
          <div class="drawer-item-sub">8 – 24 Stycznia 2027 • Start</div>
        </div>
        <span class="drawer-item-badge">START</span>
      </a>
"""

for idx, s in enumerate(slides_data):
    if not s.get("isIntro"):
        d_num = s["dayNum"]
        html_drawer_and_script += f"""
      <a class="drawer-item" onclick="selectDay({d_num})">
        <div>
          <div class="drawer-item-title">Dzień {d_num}: {s["title"]}</div>
          <div class="drawer-item-sub">{s["date"]} • {s["hotel"].split('(')[0].strip()}</div>
        </div>
        <span class="drawer-item-badge">{s["badgeDate"]}</span>
      </a>
"""

html_drawer_and_script += """
    </div>
  </div>

  <script>
    // Live Countdown Timer to Departure (8 Jan 2027 00:00:00 CET)
    const departureDate = new Date('2027-01-08T00:00:00').getTime();

    function updateCountdown() {
      const now = new Date().getTime();
      const diff = departureDate - now;

      if (diff > 0) {
        const days = Math.floor(diff / (1000 * 60 * 60 * 24));
        const hours = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const mins = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
        const secs = Math.floor((diff % (1000 * 60)) / 1000);

        const elDays = document.getElementById('cDays');
        const elHours = document.getElementById('cHours');
        const elMins = document.getElementById('cMins');
        const elSecs = document.getElementById('cSecs');

        if (elDays) elDays.innerText = days;
        if (elHours) elHours.innerText = hours.toString().padStart(2, '0');
        if (elMins) elMins.innerText = mins.toString().padStart(2, '0');
        if (elSecs) elSecs.innerText = secs.toString().padStart(2, '0');
      }
    }
    setInterval(updateCountdown, 1000);
    updateCountdown();

    // SLIDE DECK ENGINE (NATURAL FULLSCREEN)
    const slides = document.querySelectorAll('.slide');
    const navBadgeText = document.getElementById('navBadgeText');
    const progressFill = document.getElementById('progressFill');
    const totalSlides = slides.length;
    let currentSlideIndex = 0;

    function updateSlideClasses(targetIndex) {
      slides.forEach((slide, i) => {
        if (i === targetIndex) {
          slide.classList.add('active');
        } else {
          slide.classList.remove('active');
        }
      });

      // Update Header Badge and Progress Track
      const targetSlide = slides[targetIndex];
      const label = targetSlide.getAttribute('data-label');
      if (label && navBadgeText) {
        navBadgeText.innerText = label;
      }
      if (progressFill) {
        const pct = Math.round((targetIndex / (totalSlides - 1)) * 100);
        progressFill.style.width = pct + '%';
      }
    }

    function goToSlide(targetIndex) {
      if (targetIndex < 0 || targetIndex >= totalSlides || targetIndex === currentSlideIndex) return;
      currentSlideIndex = targetIndex;
      updateSlideClasses(targetIndex);
      window.scrollTo({ top: 0, behavior: 'instant' });
    }

    // Initialize slide positions
    updateSlideClasses(0);

    // TOUCH SWIPE UP / DOWN GESTURES
    let touchStartY = 0;
    let touchStartX = 0;
    let touchStartTime = 0;

    window.addEventListener('touchstart', (e) => {
      touchStartY = e.touches[0].clientY;
      touchStartX = e.touches[0].clientX;
      touchStartTime = Date.now();
    }, { passive: true });

    window.addEventListener('touchend', (e) => {
      if (drawerSheet && drawerSheet.classList.contains('active')) return;

      const touchEndY = e.changedTouches[0].clientY;
      const touchEndX = e.changedTouches[0].clientX;
      const deltaY = touchEndY - touchStartY;
      const deltaX = touchEndX - touchStartX;
      const duration = Date.now() - touchStartTime;

      if (Math.abs(deltaY) > 50 && Math.abs(deltaY) > Math.abs(deltaX) * 1.3 && duration < 500) {
        const scrollY = window.scrollY || window.pageYOffset || document.documentElement.scrollTop;
        const windowHeight = window.innerHeight;
        const docHeight = document.documentElement.scrollHeight;
        const isAtBottom = (windowHeight + scrollY) >= (docHeight - 35);
        const isAtTop = scrollY <= 15;

        if (deltaY < -50) {
          // Swiped UP ➔ Next Day (if at bottom of page or on intro)
          if (isAtBottom || currentSlideIndex === 0) {
            goToSlide(currentSlideIndex + 1);
          }
        } else if (deltaY > 50) {
          // Swiped DOWN ➔ Prev Day (if at top of page)
          if (isAtTop) {
            goToSlide(currentSlideIndex - 1);
          }
        }
      }
    }, { passive: true });

    // Drawer Logic
    const backdrop = document.getElementById('backdrop');
    const drawerSheet = document.getElementById('drawerSheet');
    const btnDrawer = document.getElementById('btnDrawer');
    const btnCloseDrawer = document.getElementById('btnCloseDrawer');

    function openDrawer() {
      backdrop.classList.add('active');
      drawerSheet.classList.add('active');
    }

    function closeDrawer() {
      backdrop.classList.remove('active');
      drawerSheet.classList.remove('active');
    }

    btnDrawer.addEventListener('click', openDrawer);
    btnCloseDrawer.addEventListener('click', closeDrawer);
    backdrop.addEventListener('click', closeDrawer);

    function selectDay(index) {
      closeDrawer();
      setTimeout(() => {
        goToSlide(index);
      }, 150);
    }

    // Keyboard navigation (for desktop testing)
    window.addEventListener('keydown', (e) => {
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown' || e.key === 'PageDown') {
        goToSlide(currentSlideIndex + 1);
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp' || e.key === 'PageUp') {
        goToSlide(currentSlideIndex - 1);
      }
    });

    // Force Update Handler (identical to cnc-kalkulator-main AppFooter)
    async function forceAppRefresh() {
      try {
        if ('caches' in window) {
          const cacheNames = await caches.keys();
          await Promise.all(cacheNames.map((name) => caches.delete(name)));
        }
        if ('serviceWorker' in navigator) {
          const registrations = await navigator.serviceWorker.getRegistrations();
          for (const registration of registrations) {
            await registration.unregister();
          }
        }
        window.location.reload();
      } catch (e) {
        window.location.reload();
      }
    }

    // Auto-update Service Worker listener (identical to cnc-kalkulator-main main.tsx)
    let refreshing = false;
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.addEventListener('controllerchange', () => {
        if (!refreshing) {
          refreshing = true;
          window.location.reload();
        }
      });

      window.addEventListener('load', () => {
        navigator.serviceWorker.register('./sw.js?v=13')
          .then(reg => {
            console.log('SW registered');
            reg.update();
          })
          .catch(err => console.log('SW error:', err));
      });
    }
  </script>
</body>
</html>
"""

full_html = html_head + html_body_slides + html_drawer_and_script

# Write index.html to Thai2027 and Thai
with open(r'c:\Users\mosan\Desktop\Thai\Thai2027\index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

with open(r'c:\Users\mosan\Desktop\Thai\index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print("Generated natural fullscreen index.html successfully! Length:", len(full_html))
