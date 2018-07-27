    #This program is free software: you can redistribute it and/or modify
    #it under the terms of the GNU General Public License as published by
    #the Free Software Foundation, either version 3 of the License, or
    #(at your option) any later version.

    #This program is distributed in the hope that it will be useful,
    #but WITHOUT ANY WARRANTY; without even the implied warranty of
    #MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #GNU General Public License for more details.

    #You should have received a copy of the GNU General Public License
    #along with this program.  If not, see <https://www.gnu.org/licenses/>.
    #----------------------------------------------------------------------
    
    #INCDFP isi declina orice responsabilitate fata de utilizarea programelor sau aplicatiilor existente in aceasta pagina. 
    #Toate programele sunt in testare iar serviciu de transmitere a informatiei depinde de conexiunile de internet.
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    
    # NU SUNTEM RESPONSABILI PENTRU ORICE "EROARE" A PROGRAMULUI, NICI NOI SI NICI INCDFP
    # CA ORICE SOFTWARE OPEN-SOURCE, FOLOSIT-L LA RISCUL DUMNEAVOASTRA IN CAZ DE URGENTA
    # !!! NOI NU DAM GARANTIE !!!

#Inits
name = "alertaseism"
try:
    import requests
    from bs4 import BeautifulSoup
except ImportError:
    print("Niste libs iti lipsesc. Instaleaza requirements.txt cu PyPi din repo")

    # XML unde zice magnitudinea este hard-codat in index.html
    # si se schimba odata la 1 minut 
    # deci asta inseamna ca
    # trebuie facut putin de data parsing

def mag():
    try:
        #descarcarea html
        html = requests.get("http://alerta.infp.ro/")
        #parsarea cu beautifulsoup
        site = BeautifulSoup(html.text, "html.parser")
        htmlpars = site.prettify()
        #cutting the index.html
        xml = htmlpars[7294:]
        xml = xml[:49:]
        #adaugam adresa de la INFP dupa ce XML a fost parsat
        xml = ("http://alerta.infp.ro/%s" % (xml))
        #descarcarea XML
        solutie = requests.get(xml)
        solutie = str(solutie.content)
        #cutting the XML
        mag = solutie[16:]
        mag = mag[:3:]
        mag = float(mag)
        mag = int(mag)
        return mag
    except RuntimeError:
            return("A fost intalnita o eroare")
    except KeyboardInterrupt:
            sys.exit(0)
        

def heart():
    try:
        #descarcarea html
        html = requests.get("http://alerta.infp.ro/")
        #parsarea cu beautifulsoup
        site = BeautifulSoup(html.text, "html.parser")
        htmlpars = site.prettify()
        #cutting the index.html
        xml = htmlpars[7294:]
        xml = xml[:49:]
        #adaugam adresa de la INFP dupa ce XML a fost parsat
        xml = ("http://alerta.infp.ro/%s" % (xml))
        #descarcarea XML
        solutie = requests.get(xml)
        solutie = str(solutie.content)
        #cutting the XML
        heart = solutie[30:]
        heart = heart[:29:]
        heart = str(heart)
        return heart
    except RuntimeError:
            return("A fost intalnita o eroare")
    except KeyboardInterrupt:
            sys.exit(0)


