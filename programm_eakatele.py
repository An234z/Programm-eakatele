import json
import random
import datetime
import sqlite3

def huvitavad_faktid():
    # Data containing facts
    data = {
        "facts": [
            "99 % Maal eksisteerinud elusolenditest on välja surnud.",
            "Ainuke koduloom, keda Piiblis ei mainita, on – kass.",
            "Jaanalinnu muna kõvakskeetmiseks kulub 4 tundi.",
            "9/10 lõvikarja saagist hangivad emalõvid.",
            "Laiskloomadel möödub 75% elust unes.",
            "Koolibriid ei saa käia.",
            "Sääsetõukudel ei ole magu.",
            "Austraaliasse tulnud eurooplased küsisid aborigeenide käest: «Mis kummalised loomad teil siin ringi hüppavad?» Kohalikud vastasid: «Känguru», - mis tähendas: «Ei saa aru!»",
            "Kõige lihtsam moodus taimetoidulise looma lihasööjast eristamiseks on järgmine: saaklooma avastamiseks asuvad kiskjatel silmad koonu esiosas. Taimetoidulistel aga asuvad silmad vaenlase avastamiseks kahel pool pead.",
            "Nahkhiir – ainuke lennuvõimeline imetaja.",
            "Ühe kilo mee saamiseks peab mesilane külastama 2 miljonit õit.",
            "Rohutirtsu veri on valget värvi, vähil – helesinine.",
            "Viimase 4000 aasta jooksul pole kodustatud ühtegi uut metslooma.",
            "Pingviinid võivad hüpata pooleteisest meetrist kõrgemale.",
            "Šimpansid on ainukesed loomad, kes võivad ennast peeglis ära tunda.",
            "Elevandid ja inimesed on ainukesed imetajad, kes suudavad pea peal seista.",
            "Krokodillid neelavad sügavamale sukeldumiseks kive.",
            "Polaarkarud suudavad joosta kiirusega 40 km/h.",
            "Dünamiidi valmistamisel kasutatakse maapähkleid.",
            "Maailma esimest odekolonni kasutati profülaktikavahendina katku vastu.",
            "Iga sekund on 1% Maa elanikkonnast maani täis.",
            "Habe koosneb 7-15 tuhandest karvast. Ja tema kasvukiiruseks on 14 cm aastas.",
            "Elusolenditest on sipelgal kõige suurem aju. Seda loomulikult kehakaaluga võrreldes.",
            "Selleks, et kohvi abil enesetappu sooritada, peab jooma järjest 100 tassitäit kohvi.",
            "Hans Christian Andersen ei osanud grammatikavigadeta kirjutada praktiliselt ühtegi sõna.",
            "Esmaspäeviti toimub seljavigastusi 25% ja südameatakke 33% tavalisest rohkem.",
            "Maailmas valmib iga päev keskmiselt 33 uut toodet. Millest 13 – on mänguasjad.",
            "Keskmine inimene veedab kogu elu jooksul valgusfoori taga lubavat tuld oodates ligi kaks nädalat.",
            "Inimene harjub teega kiiremini kui heroiiniga.",
            "Tualettpaber leiutati 1857 aastal.",
            "Ameeriklased viskavad iga päev ära 20 tuhat televiisorit, 150 tuhat tonni pakkimismaterjale ja 43 tuhat tonni toitu.",
            "Päevas paki sigarettide suitsetamine on võrdväärne aasta jooksul tassitäie nikotiini joomisega.",
            "Magava inimese keha on ärkveloleva omast pool sentimeetrit pikem.",
            "Sääskedele meeldib hiljuti banaane söönud nende inimeste lõhn.",
            "Hokilitter võib lennata kiirusega 160 km/h.",
            "Neandertaallase aju oli meie omast suurem.",
            "Mõnedes Singapuri avalikes käimlates saab karaoket laulda.",
            "Jakkidel on roosa piim.",
            "Statistiliselt keskmine pangaautomaat eksib aasta jooksul 250 dollariga ja seda mitte teie kasuks.",
            "Christopher Kolumbus oli blond.",
            "Kui arvu 111.111.111 korrutada 111.111.111-ga, saadakse 12345678987654321.",
            "Jules Verne kirjutas 1863 aastal raamatu \"Pariis XX sajandil\", milles kirjeldas üksikasjaliselt autot, faksi ja elektritooli. Kirjastaja tagastas talle käsikirja, nimetades teda idioodiks.",
            "Maailma kõige suurema käibega toode on bensiin. Teisel kohal on kohv"
        ]
    }
    
    # Ask user if they want to hear a fact
    vastus = input("Kas soovite kuulda huvitavat fakti? (jah/ei): ").lower()
    if vastus == "jah":
        # Accessing a random fact
        random_fact = random.choice(data["facts"])
        print("Siin on üks huvitav fakt:")
        print(random_fact)
    elif vastus == "ei":
        print("Head päeva!")



class Kasutaja:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.health_indicators = {}

    def add_health_indicator(self, indicator_type, value):
        self.health_indicators[indicator_type] = value


def analüüs_südame_löögisagedus(pulse):
    if 60 <= pulse <= 90:
        print("PULSS ON NORMAALNE:))")
    elif 50 <= pulse < 60:
        print("VÕTA ÜHENDUST ARSTIGA, TEIE PULSS ON LIIGA MADAL!!")
    elif pulse >= 100:
        print("VÕTA ÜHENDUST ARSTIGA, TEIE PULSS ON LIIGA KÕRGE!!")
    else:
        print("VÕTA ÜHENDUST ARSTIGA!!")


def analüüs_vererõhk(süstoolne, diastoolne):
    if süstoolne < 120 and diastoolne < 80:
        print("VÕTA ÜHENDUST ARSTIGA, TEIE VERERÕHK ON LIIGA MADAL!!")
    elif (süstoolne >= 120 and süstoolne <= 129) and (diastoolne >= 80 and diastoolne <= 84):
        print("TEIE VERERÕHK ON NORMAALNE:))")
    elif (süstoolne >= 130 and süstoolne <= 139) and (diastoolne >= 85 and diastoolne <= 89):
        print("TEIE VERERÕHK ON KÕRGE-NORMAALNE:))")
    elif (süstoolne >= 140 and süstoolne <= 159) and (diastoolne >= 90 and diastoolne <= 99):
        print("TEIL ON ILMSELT 1.ASTME HÜPERTENSIOON, VÕTKE ÜHENDUST ARSTIGA")
    elif (süstoolne >= 160 and süstoolne <= 179) and (diastoolne >= 100 and diastoolne <= 109):
        print("TEIL ON ILMSELT 2.ASTME HÜPERTENSIOON, VÕTKE ÜHENDUST ARSTIGA")
    elif süstoolne > 180 and diastoolne > 110:
        print("TEIL ON ILMSELT 3.ASTME HÜPERTENSIOON, VÕTKE ÜHENDUST ARSTIGA")
    else:
        print("TEIL ON EBANORMAALNE VERERÕHK, VÕTA ÜHENDUST ARSTIGA")
    

def initialize_database():
    connection = sqlite3.connect('user_data.db')
    cursor = connection.cursor()

    # Create a table if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS Tervise_naitajad (
                      id INTEGER PRIMARY KEY,
                      name TEXT,
                      age INTEGER,
                      health_indicators TEXT)''')

    connection.commit()
    connection.close()

# Function to insert a user into the SQLite database
def insert_user(user):
    connection = sqlite3.connect('user_data.db')
    cursor = connection.cursor()

    cursor.execute("INSERT INTO Tervise_naitajad (name, age, health_indicators) VALUES (?, ?, ?)",
                   (user.name, user.age, json.dumps(user.health_indicators)))

    connection.commit()
    connection.close()
    
    
    
    
def main():
    # Küsin kasutaja nime ja vanust
    name = input("Sisestage oma nimi: ")
    print(f"Tere, {name}!")
    age = int(input("Sisestage oma vanus: "))

    user = Kasutaja(name, age)

    # Küsin kasutaja tervisenäitajaid
    pulse = float(input("Sisestage oma pulss (lööke minutis, puhkeolekus): "))
    user.add_health_indicator("pulss", pulse)
    analüüs_südame_löögisagedus(pulse)

    vererõhk = input("Sisestage oma vererõhk (formaadis 'süstoolne/diastoolne', nt '120/80'): ")
    süstoolne, diastoolne = map(float, vererõhk.split('/'))
    user.add_health_indicator("vererõhk_süstoolne", süstoolne)
    user.add_health_indicator("vererõhk_diastoolne", diastoolne)
    analüüs_vererõhk(süstoolne, diastoolne)
    huvitavad_faktid()
    initialize_database()
    insert_user(user)
    
    # Väljastan kasutaja tervisenäitajad
    print("\nTeie tervisenäitajad:")
    for indicator_type, value in user.health_indicators.items():
        print(f"{indicator_type.capitalize()}: {value}")
        
if __name__ == "__main__":
    main()
    
  