import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

#########
######### lu = language used
#########
sorry = [
  "Sorry - to see you go",
  "Es tut uns leid, dass Sie gehen",
  "Es tut uns leid, dass Du gehst",
  "Désolé de vous voir partir",
  "Beklager - å se deg gå",
  "_last_"  
]
privacy_str_title_str = [
  "Privacy",
  "Privatsphäre",
  "Privatsphäre",
  "Confidentialité",
  "Personvern",
  "_last_"  
]
regi_privacy_str = [
  "If the game is interrupted, either accidentally or intentionally (for example, because the rounds are played on different days), we need to load the page where the interruption occurred for each player. To do this, we need a unique ID. You choose this yourself. It can consist of any digits, letters or characters. It must be at least 3 characters long. 90 days after the last log-in all data associated with your registration name is completely deleted, meaning neither you, nor nobody else, will be able to access your game data.\nTake good note of what you enter, nothing can be recovered.",
  "Sollte das Spiel unterbrochen werden, versehentlich oder absichtlich (weil zum Beispiel die Runden an verschiedenen Tagen gespielt werden), müssen wir für jede:n Spieler:in die Seite laden bei der der Unterbruch stattfand. Dazu brauchen wir eine eindeutige ID. Diese wählst Du selbst aus. Sie kann aus irgendwelchen Ziffern, Buchstaben oder Zeichen bestehen. Sie muss mindestens 3 Zeichen lang sein.  90 Tage nach der letzten Anmeldung werden alle mit Ihrem Registrierungsnamen verbundenen Daten vollständig gelöscht, sodass weder Sie noch andere Personen auf Ihre Spieldaten zugreifen können.\nNotieren Sie sich genau, was Sie eingeben, es gibt keine Möglichkeit der Wiederherstellung.",
  "Sollte das Spiel unterbrochen werden, versehentlich oder absichtlich (weil zum Beispiel die Runden an verschiedenen Tagen gespielt werden), müssen wir für jede:n Spieler:in die Seite laden bei der der Unterbruch stattfand. Dazu brauchen wir eine eindeutige ID. Diese wählen Sie selbst aus. Sie kann aus irgendwelchen Ziffern, Buchstaben oder Zeichen bestehen. Sie muss mindestens 3 Zeichen lang sein.  90 Tage nach der letzten Anmeldung werden alle mit Ihrem Registrierungsnamen verbundenen Daten vollständig gelöscht, sodass weder Sie noch andere Personen auf Ihre Spieldaten zugreifen können.\nNotieren Sie sich genau, was Sie eingeben, es gibt keine Möglichkeit der Wiederherstellung.",
  "Si le partie est interrompue, accidentellement ou intentionnellement (par exemple parce que les manches sont jouées à des jours différents), nous devons charger la page où l'interruption s'est produite pour chaque joueur. Pour cela, nous avons besoin d'un identifiant unique. Vous le choisissez vous-même. Il peut être composé de n'importe quels chiffres, lettres ou caractères. Il doit comporter au moins 3 caractères.  90 jours après votre dernière connexion, toutes les données associées à votre nom d'utilisateur seront définitivement supprimées, ce qui signifie que ni vous, ni personne d'autre, ne pourrez plus accéder à vos données de jeu.\nPrenez bien note de ce que vous saisissez, rien ne peut être récupéré.",
  "Hvis spillet blir avbrutt, enten ved et uhell eller med vilje (for eksempel fordi rundene spilles på forskjellige dager), må vi laste inn siden der avbruddet skjedde for hver spiller. For å gjøre dette trenger vi en unik ID. Du velger denne selv. Den kan bestå av hvilke som helst tall, bokstaver eller tegn. Den må være minst 3 tegn lang.  90 dager etter siste innlogging blir alle data knyttet til ditt registreringsnavn fullstendig slettet, noe som betyr at verken du eller noen andre vil kunne få tilgang til spilldataene dine.\nVær nøye med hva du skriver inn, ingenting kan gjenopprettes.",
  "_last_"  
]
privacy_str = [
  "We do not collect any personal data – period! \n\nAll game data will be irrevocably deleted 90 days after the last log-in to a game, including your registration name.",
  "Wir sammeln keine persönlichen Daten - Punkt! \n\nAlle Spieldaten werden 90 Tage nach der letzten Anmeldung bei einem Spiel unwiderruflich gelöscht, einschließlich Ihres Registrierungsnamens.",
  "Wir sammeln keine persönlichen Daten - Punkt! \n\nAlle Spieldaten werden 90 Tage nach der letzten Anmeldung bei einem Spiel unwiderruflich gelöscht, einschließlich Ihres Registrierungsnamens.",
  "Nous ne collectons aucune donnée personnelle, point final ! \n\nToutes les données de jeu seront irrévocablement supprimées 90 jours après la dernière connexion à un jeu, y compris votre nom d'enregistrement.",
  "Vi samler ikke inn personopplysninger – punktum! \n\nAlle spilldata vil bli slettet uigenkallelig 90 dager etter siste innlogging i et spill, inkludert ditt registreringsnavn.",
  "_last_"  
]

bye_tx = [
  "Thanks for stopping by - maybe another time ...",
  "Danke für Ihren Besuch – vielleicht ein anderes Mal ...",
  "Danke für Deinen Besuch – vielleicht ein anderes Mal ...",
  "Merci d'être passé, peut-être une autre fois...",
  "Takk for at du kom innom – kanskje en annen gang ...",
  "Bedankt voor uw bezoek – misschien een andere keer ...",
  "_last_"  
]
jga_t = [
  "Try another ID",
  "Andere ID ausprobieren",
  "Andere ID ausprobieren",
  "Essayer un autre ID",
  "Prøv en ny ID",
  "_last_"
]
jga_f = [
  "Cancel Joining",
  "Beitritt abbrechen", 
  "Beitritt abbrechen", 
  "Annuler Joindre",
  "Avbryt",
  "_last_"
]
nbr_confirm_t = [
  "Yes",
  "Ja",
  "Ja",
  "Oui",
  "Ja",
  "_last_"
]
nbr_confirm_f = [
  "No",
  "Nein",
  "Nein",
  "Non",
  "Nei",
  "_last_"
]
nat_graph_1_title = [
  "Trust in institutions",
  "Vertrauen in Institutionen",
  "Vertrauen in Institutionen",
  "Confiance dans les institutions",
  "Tillit til institusjoner",
  "_last_"
]
nat_graph_2_title = [
  "Energy intensity in terms of primary energy & GDP",
  "Energieintensität in Bezug auf Primärenergie und BIP",
  "Energieintensität in Bezug auf Primärenergie und BIP",
  "Intensité énergétique en termes d'énergie primaire et de PIB",
  "Energiintensitet målt i primærenergi og BNP",
  "_last_"
]
nat_graph_3_title = [
  "Emissions per person",
  "Emissionen pro Person",
  "Emissionen pro Person",
  "Émissions par personne",
  "Utslipp per person",
  "_last_"
]
nat_graph_4_title = [
  "Perceived global warming",
  "Wahrgenommene globale Erwärmung",
  "Wahrgenommene globale Erwärmung",
  "Réchauffement climatique perçu",
  "Oppfattet global oppvarming",
  "_last_"
]
nat_graph_5_title = [
  "Average well-being",
  "Durchschnittliches Wohlergehen",
  "Durchschnittliches Wohlergehen",
  "Bien-être moyen",
  "Gjennomsnittlig trivsel",
  "_last_"
]
nat_graph_6_title = [
  "Inequality",
  "Ungleichheit",
  "Ungleichheit",
  "Inégalité",
  "Ulikhet",
  "_last_"
]
nat_graph_7_title = [
  "Social tension",
  "Soziale Spannungen",
  "Soziale Spannungen",
  "Tension sociale",
  "Sosiale spenninger",
  "_last_"
]
nat_graph_8_title = [
  "Nbr of people earning less than 15 000 $/year",
  "Anzahl der Personen, die weniger als 15.000 $ pro Jahr verdienen",
  "Anzahl der Personen, die weniger als 15.000 $ pro Jahr verdienen",
  "Nombre de personnes gagnant moins de 15 000 $ par an",
  "Antall personer som tjener mindre enn 15 000 dollar per år",
  "_last_"
]
nat_graph_9_title = [
  "Population",
  "Bevölkerung",
  "Bevölkerung",
  "Population",
  "Befolkning",
  "_last_"
]
nat_graph_11_title = [
  "GDP per person",
  "BIP pro Kopf",
  "BIP pro Kopf",
  "PIB par habitant",
  "BNP per person",
  "_last_"
]
nat_graph_10_title = [
  "Global Overview",
  "Globaler Überblick",
  "Globaler Überblick",
  "Aperçu global",
  "Global oversikt",
  "_last_"
]
nat_graph_1_subtitle = [
  "Global social trust (higher is better)",
  "Globales soziales Vertrauen (höher ist besser)",
  "Globales soziales Vertrauen (höher ist besser)",
  "Confiance sociale mondiale (plus le chiffre est élevé, mieux c'est)",
  "Global sosial tillit (høyere er bedre)",
  "_last_"
]
nat_graph_2_subtitle = [
  "Global energy use / Global GDP (kwh/$)  - lower is better",
  "Globaler Energieverbrauch / Globales BIP (kWh/$) - niedriger ist besser",
  "Globaler Energieverbrauch / Globales BIP (kWh/$) - niedriger ist besser",
  "Consommation mondiale d'énergie / PIB mondial (kWh/$) - plus bas, mieux c'est",
  "Globalt energiforbruk / Globalt BNP (kWh/$) - lavere er bedre",
  "_last_"
]
nat_graph_3_subtitle = [
  "Global emissions / Global population (tCO2/person/year) - lower is better",
  "Globale Emissionen / Weltbevölkerung (tCO2/Person/Jahr) - niedriger ist besser",
  "Globale Emissionen / Weltbevölkerung (tCO2/Person/Jahr) - niedriger ist besser",
  "Émissions mondiales / Population mondiale (tCO2/personne/an) - plus bas, mieux c'est",
  "Globale utslipp / Global befolkning (tCO2/person/år) - lavere er bedre",
  "_last_"
]
nat_graph_4_subtitle = [
  "°C over 1850 - higher is worse",
  "°C über 1850 - höher ist schlechter",
  "°C über 1850 - höher ist schlechter",
  "°C depuis 1850 - plus c'est élevé, plus c'est mauvais",
  "°C over 1850 - plus c'est élevé, plus c'est mauvais",
  "_last_"
]
nat_graph_5_subtitle = [
  "index (higher is better)",
  "Index (höher ist besser)",
  "Index (höher ist besser)",
  "indice (plus il est élevé, mieux c'est)",
  "indeks (høyere er bedre)",
  "_last_"
]
nat_graph_6_subtitle = [
  "index (higher is more unequal)",
  "Index (je höher, desto ungleicher)",
  "Index (je höher, desto ungleicher)",
  "indice (plus il est élevé, plus l'inégalité est grande)",
  "indeks (høyere er mer ulik)",
  "_last_"
]
nat_graph_7_subtitle = [
  "index (higher is worse)",
  "Index (höher ist schlechter)",
  "Index (höher ist schlechter)",
  "indice (plus le chiffre est élevé, plus la situation est grave)",
  "indeks (høyere er dårligere)",
  "_last_"
]
nat_graph_8_subtitle = [
  "Million people - lower is better",
  "Millionen Menschen - niedriger ist besser",
  "Millionen Menschen - niedriger ist besser",
  "Des millions de personnes - plus bas, mieux c'est",
  "Millioner mennesker - lavere er bedre",
  "_last_"
]
nat_graph_9_subtitle = [
  "Million people - are fewer better or worse?",
  "Millionen Menschen - Sind weniger besser oder schlechter?",
  "Millionen Menschen - Sind weniger besser oder schlechter?",
  "Des millions de personnes - Est-ce que moins, c'est mieux ou pire ?",
  "Millioner mennesker - Er færre bedre eller dårligere?",
  "_last_"
]
nat_graph_10_subtitle = [
  "Variable names and scales on the sides",
  "Variablennamen und Skalen an den Seiten",
  "Variablennamen und Skalen an den Seiten",
  "Noms des variables et échelles sur les côtés",
  "Variabelnavn og skalaer på sidene",
  "_last_"
]
nat_graph_11_subtitle = [
  "thousand USD per person per year - higher is better",
  "Tausend US-Dollar pro Person und Jahr",
  "Tausend US-Dollar pro Person und Jahr",
  "mille USD par personne et par an",
  "tusen USD per person per år - høyere er bedre",
  "_last_"
]
regi_first_tx = [
  "Register, after all?",
  "Doch erst registrieren?",
  "Doch erst registrieren?",
  "Il faut d'abord s'inscrire, après tout ?",
  "Registrere seg, tross alt?",
  "_last_"
]
regi_user_tt = [
  "Why register? Because the game can be interrupted, by accident or by choice. To rejoin the game at exactly the same page just before the interruption, you need a unique username. Write it down, it cannot be recovered.",
  "Warum registrieren? Weil das Spiel unterbrochen werden kann, entweder versehentlich oder absichtlich. Um das Spiel genau an der Stelle fortzusetzen, an der es unterbrochen wurde, benötigen Sie einen eindeutigen Benutzernamen. Schreiben Sie sich ihn auf, da er nicht wiederhergestellt werden kann.",
  "Warum registrieren? Weil das Spiel unterbrochen werden kann, entweder versehentlich oder absichtlich. Um das Spiel genau an der Stelle fortzusetzen, an der es unterbrochen wurde, benötigst Du einen eindeutigen Benutzernamen. Schreib ihn auf, da er nicht wiederhergestellt werden kann.",
  "Pourquoi s'inscrire ? Parce que le jeu peut être interrompu, accidentellement ou volontairement. Pour rejoindre le jeu exactement à la même page qu'avant l'interruption, vous avez besoin d'un nom d'utilisateur unique. Notez-le, car il ne peut pas être récupéré.",
  "Hvorfor registrere seg? Fordi spillet kan bli avbrutt, enten ved et uhell eller ved valg. For å kunne fortsette spillet på nøyaktig samme side som før avbruddet, trenger du et unikt brukernavn. Skriv det ned, det kan ikke gjenopprettes.",
  "_last_"
]

err_user_not_exits = [
  "A user with this name does not exist",
  "Ein Benutzer mit diesem Namen existiert nicht.",
  "Ein Benutzer mit diesem Namen existiert nicht.",
  "Il n'existe aucun utilisateur portant ce nom.",
  "Det finnes ingen bruker med dette navnet.",
  "_last_"
]
sign_up = [
  "Thank you for taking the time to explore some of the big issues of our time – poverty, inequality, equal rights, food and agriculture, and energy – in a playful manner. The game invites you to create a different future from the one we are currently on track for: less poverty, less inequality, more social freedom within the limits set by our planet, and greater well-being for all. For us, our children, our grandchildren. \n\nThis is not easy, but firstly, you have smart and committed fellow players, and secondly, the game accompanies you every step of the way with hints, tips and instructions. Further help, background information and a glossary can be found (once you start the game) by clicking on the *Help* button at the top right. (still under development)\n\nYou can intervene three times in the course of events to create a different (game) reality for the future: better, more dignified and happier. Good luck and enjoy.",
  "Vielen Dank, dass Sie sich die Zeit genommen haben, sich mit einigen der großen Themen unserer Zeit auseinanderzusetzen - denen zwischen Armut, Ungleichheit, Gleichstellung, Ernährung und Landwirtschaft sowie Energie - spielerisch zu erkunden. Das Spiel lädt Sie ein, eine andere Zukunft zu gestalten, als die, auf dessen Pfad wir uns momentan befinden: Weniger Armut, weniger Ungleichheit, mehr soziale Freiheit innerhalb der Grenzen, die unser Planet uns gesetzt hat, zu mehr Wohlergehen Aller. Für uns, unsere Kinder, unsere Enkel.\n\nDas ist nicht einfach, aber erstens haben sie kluge und engagierte Mitspieler:innen, und zweitens begleitet Sie das Spiel bei jedem Schritt mit Hinweisen, Tipps und Instruktionen. Weitergehende Hilfe, Hintergründe und ein Glossar finden Sie (sobald Sie das Spiel starten), wenn Sie auf den *Hilfe* Knopft oben rechts klicken. (noch in der Entwicklungsphase)\n\nSie können dreimal in den Verlauf der Ereignisse eingreifen, um für die Zunkunft eine andere (Spiel-)Realität zu schaffen: besser, würdiger und fröhlicher.  Vielf Glück und Freude.",
  "Vielen Dank, dass Sie sich die Zeit genommen haben, sich mit einigen der großen Themen unserer Zeit auseinanderzusetzen - denen zwischen Armut, Ungleichheit, Gleichstellung, Ernährung und Landwirtschaft sowie Energie - spielerisch zu erkunden. Das Spiel lädt Sie ein, eine andere Zukunft zu gestalten, als die, auf dessen Pfad wir uns momentan befinden: Weniger Armut, weniger Ungleichheit, mehr soziale Freiheit innerhalb der Grenzen, die unser Planet uns gesetzt hat, zu mehr Wohlergehen Aller. Für uns, unsere Kinder, unsere Enkel.\n\nDas ist nicht einfach, aber erstens haben sie kluge und engagierte Mitspieler:innen, und zweitens begleitet Sie das Spiel bei jedem Schritt mit Hinweisen, Tipps und Instruktionen. Weitergehende Hilfe, Hintergründe und ein Glossar finden Sie (sobald Sie das Spiel starten), wenn Sie auf den *Hilfe* Knopft oben rechts klicken. (noch in der Entwicklungsphase)\n\nSie können dreimal in den Verlauf der Ereignisse eingreifen, um für die Zunkunft eine andere (Spiel-)Realität zu schaffen: besser, würdiger und fröhlicher.  Vielf Glück und Freude.",
  "Merci d'avoir pris le temps d'explorer certaines des grandes questions de notre époque : pauvreté, inégalités, égalité, alimentation, agriculture et énergie. Ce jeu vous invite à imaginer un avenir différent de celui vers lequel nous nous dirigeons actuellement : moins de pauvreté, moins d'inégalités, plus de liberté social dans les limites que nous impose notre planète, pour le bien-être de tous. Pour nous, nos enfants, nos petits-enfants. Ce n'est pas facile, mais d'une part, vous avez des coéquipiers intelligents et engagés, et d'autre part, le jeu vous accompagne à chaque étape avec des conseils, des astuces et des instructions. Vous trouverez une aide supplémentaire, des informations générales et un glossaire (une fois que vous avez lancé le jeu) en cliquant sur le bouton « Aide » en haut à droite. (encore en phase de développement)\n\nVous pouvez intervenir trois fois dans le cours des événements afin de créer une autre réalité (de jeu) pour l'avenir : meilleure, plus digne et plus joyeuse.  Bonne chance et beaucoup de plaisir.",
  "Takk for at du tok deg tid til å utforske noen av vår tids store spørsmål – mellom fattigdom, ulikhet, likestilling, ernæring og landbruk samt energi – på en lekende måte. Spillet inviterer deg til å skape en annen fremtid enn den vi er på vei mot nå: mindre fattigdom, mindre ulikhet, mer sosial frihet innenfor de grensene som planeten vår har satt oss, til større velferd for alle. For oss, våre barn og våre barnebarn. \n\nDet er ikke enkelt, men for det første har du kloke og engasjerte medspillere, og for det andre følger spillet deg gjennom hvert trinn med hint, tips og instruksjoner. Du finner mer hjelp, bakgrunnsinformasjon og en ordliste (når du starter spillet) ved å klikke på *Hjelp*-knappen øverst til høyre. (fremdeles under utvikling)\n\nDu kan gripe inn tre ganger i løpet av hendelsene for å skape en annen (spill-)virkelighet for fremtiden: bedre, verdigere og gladere.  Lykke til og ha det gøy.",
  "_last_"  
]
sign_up_title = [
  "New registration",
  "Neu registrieren",
  "Neu registrieren",
  "Nouvelle inscription",
  "Ny registrering",
  "_last_"  
]
all_regions_assigned = [
  "All regions and roles have been assigned",
  "Alle Regionen und Rollen wurden zugewiesen.",
  "Alle Regionen und Rollen wurden zugewiesen.",
  "Toutes les régions et tous les rôles ont été attribués.",
  "Alle regioner og roller er tildelt",
  "Alle regio's en rollen zijn toegewezen.",
  "_last_"  
]
all_regs_gone_title = [
  "No more region",
  "Keine Region mehr verfügbar",
  "Keine Region mehr verfügbar",
  "Désolé, il n'y a plus de région disponible.",
  "Ingen flere regioner",
  "_last_"  
]
why_sign_up_title = [
  "Welcome to the Different Reality Game",
  "Willkommen zum Different-Reality-Spiel",
  "Willkommen zum Different-Reality-Spiel",
  "Bienvenue dans le jeu en réalité alternée",
  "Velkommen til en Different Reality Game",
  "_last_"  
]

cancel_btn = [
  "Cancel",
  "Abbrechen",
  "Abbrechen",
  "Annuler",
  "Avbryt",
  "_last_"
]
loggedin = [
  "Logged in :)",
  "Angemeldet :)",
  "Angemeldet :)",
  "Connecté",
  "Pålogget",
  "_last_"
]

login_first_btn  = [
  "Already registered? Log in",
  "Bereits registriert? Einloggen",
  "Bereits registriert? Einloggen",
  "Déjà inscrit ? Connectez-vous.",
  "Allerede registrert? Logg inn",
  "_last_"
]
save_btn = [
  "Save",
  "Speichern",
  "Speichern",
  "Enregistrer",
  "Lagre",
  "_last_"
]
err_username_enter  = [
  "Enter a username to log in",
  "Geben Sie einen Benutzernamen ein, um sich anzumelden.",
  "Gibt einen Benutzernamen ein, um dich anzumelden.",
  "Entrez un nom d'utilisateur pour vous connecter.",
  "Skriv inn et brukernavn for å logge inn",
  "_last_"
]
saved = [
  "Registration has been saved - thanks",
  "Die Registrierung wurde gespeichert – vielen Dank.",
  "Die Registrierung wurde gespeichert – vielen Dank.",
  "L'inscription a été enregistrée - merci",
  "Registreringen er lagret – takk",
  "_last_"
]
user_placeholder = [
  "Enter username",
  "Benutzername",
  "Benutzername",
  "Entrez votre nom d'utilisateur",
  "brukernavn",
  "_last_"
]
err_username1 = [
  "The username must be at least 3 chars long",
  "Der Benutzername muss mindestens 3 Zeichen lang sein.",
  "Der Benutzername muss mindestens 3 Zeichen lang sein.",
  "Le nom d'utilisateur doit comporter au moins 3 caractères.",
  "Brukernavnet må være minst 3 tegn langt",
  "_last_"
]
err_username2 = [
  "The username cannot be longer than 15 chars",
  "Der Benutzername darf nicht länger als 15 Zeichen sein.",
  "Der Benutzername darf nicht länger als 15 Zeichen sein.",
  "Le nom d'utilisateur ne peut pas dépasser 15 caractères.",
  "Brukernavnet kan ikke være lengre enn 15 tegn.",
  "_last_"
]
err_username3 = [
  "You must enter a username",
  "Sie müssen einen Benutzernamen eingeben.",
  "Du musst einen Benutzernamen eingeben.",
  "Vous devez saisir un nom d'utilisateur.",
  "Du må oppgi et brukernavn",
  "_last_"
]
err_username_exists = [
  "The username already exists",
  "Der Benutzername existiert bereits.",
  "Der Benutzername existiert bereits.",
  "Le nom d'utilisateur existe déjà.",
  "Brukernavnet eksisterer allerede",
  "_last_"
]
err_username_alpha = [
  "The username cannot be all digits",
  "Der Benutzername darf nicht ausschließlich aus Ziffern bestehen.",
  "Der Benutzername darf nicht ausschließlich aus Ziffern bestehen.",
  "Le nom d'utilisateur ne peut pas être composé uniquement de chiffres.",
  "Brukernavnet kan ikke bestå av bare tall.",
  "_last_"
]
login_title_tx = [
  "Log-in",
  "Einloggen",
  "Einloggen",
  "Se connecter",
  "Logg inn",
  "_last_"
]
login_u_tx = [
  "Enter your username",
  "Benutzernamen eingeben",
  "Benutzernamen eingeben",
  "Entrez votre nom d'utilisateur",
  "Skriv inn brukernavn",
  "_last_"
]
poc_title = [
  "So far, this app is a Proof of Concept",
  "Bislang ist diese Anwendung nur ein Proof of Concept",
  "Bislang ist diese Anwendung nur ein Proof of Concept",
  "Pour l'instant, cette application n'est qu'une preuve de concept",
  "Så langt er denne applikasjonen bare et proof of concept",
  "_last_"
]
poc_str = [
  "Neither the user interface nor the server code is elegant, nor efficient, nor 'pythonic'. Contact us if you can help making it better.",
  "Weder die Benutzeroberfläche noch der Servercode sind elegant, effizient oder 'pythonisch'. Kontaktieren Sie uns, wenn Sie helfen können, es besser zu machen.",
  "Weder die Benutzeroberfläche noch der Servercode sind elegant, effizient oder 'pythonisch'. Kontaktieren Sie uns, wenn Sie helfen können, es besser zu machen.",
  "Ni l'interface utilisateur ni le code du serveur ne sont élégants, efficaces ou 'pythoniques'. Contactez-nous si vous pouvez nous aider à les améliorer.",
  "Verken brukergrensesnittet eller serverkoden er elegant, effektiv eller 'pythonisk'. Kontakt oss hvis du kan hjelpe oss med å gjøre det bedre.",
  "_last_"
]
show_hide_plots_tx = [
  "Toggle show / hide graphs and decision sheet",
  "Ein- und Ausblenden von Diagrammen und Entscheidungs-schiebern",
  "Ein- und Ausblenden von Diagrammen und Entscheidungs-schiebern",
  "Afficher / masquer les graphiques et la feuille de décision", 
  "Veksle mellom å vise/skjule grafer og beslutningsark", 
  "_last_"
]
reg_to_longreg_us_str = [
  "USA",
  "USA",
  "USA",
  "USA", 
  "USA", 
  "_last_"
]
reg_to_longreg_af_str = [
  "Africa South of Sahara",
  "Afrika südlich der Sahara",
  "Afrika südlich der Sahara",
  "Afrique au sud du Sahara", 
  "Afrika sør for Sahara", 
  "_last_"
]
reg_to_longreg_cn_str = [
  "China",
  "China",
  "China",
  "Chine", 
  "Kina", 
  "_last_"
]
reg_to_longreg_me_str = [
  "Middle East & North Africa",
  "Naher Osten und Nordafrika",
  "Naher Osten und Nordafrika",
  "Moyen-Orient et Afrique du Nord", 
  "Midtøsten og Nord -Afrika", 
  "_last_"
]
reg_to_longreg_sa_str = [
  "South Asia",
  "Südasien",
  "Südasien",
  "Asie du Sud", 
  "Sør -Asia", 
  "_last_"
]
reg_to_longreg_la_str = [
  "Latin America",
  "Lateinamerika",
  "Lateinamerika",
  "L'Amérique latine", 
  "Latin -Amerika", 
  "_last_"
]
reg_to_longreg_pa_str = [
  "Pacific Rim",
  "Pazifische Anrainerstaaten ",
  "Pazifische Anrainerstaaten ",
  "Pays riverains du Pacifique ", 
  "Landene rundt Stillehavet ", 
  "_last_"
]
reg_to_longreg_ec_str = [
  "East Europe & Central Asia",
  "Osteuropa und Zentralasien",
  "Osteuropa und Zentralasien",
  "Europe de l'Est et Asie centrale", 
  "Øst -Europa og Sentral -Asia", 
  "_last_"
]
reg_to_longreg_eu_str = [
  "Europe",
  "Europa",
  "Europa",
  "Europe", 
  "Europa", 
  "_last_"
]
reg_to_longreg_se_str = [
  "Southeast Asia",
  "Südostasien",
  "Südostasien",
  "Asie du Sud-Est", 
  "Sørøst-Asia", 
  "_last_"
]
ta_to_longmini_pov_str = [
  "Minister against Poverty",
  "Minister:in gegen Armut",
  "Minister:in gegen Armut",
  "Ministre contre la pauvreté", 
  "Minister mot fattigdom", 
  "_last_"
]
ta_to_longmini_ineq_str = [
  "Minister against Inequality",
  "Minister:in gegen Ungleichheit",
  "Minister:in gegen Ungleichheit",
  "Ministre contre les inégalités", 
  "Minister mot ulikhet", 
  "_last_"
]
ta_to_longmini_emp_str = [
  "Minister for Empowerment",
  "Minister:in für Empowerment/Befähigung",
  "Minister:in für Empowerment/Befähigung",
  "Ministre de l'autonomisation", 
  "Minister for Empowerment/Myndiggjøring", 
  "_last_"
]
ta_to_longmini_food_str = [
  "Minister for Food & Agriculture",
  "Minister:in für Ernährung und Landwirtschaft",
  "Minister:in für Ernährung und Landwirtschaft",
  "Ministre de l'alimentation et de l'agriculture", 
  "Minister for ernæring og landbruk", 
  "_last_"
]
ta_to_longmini_ener_str = [
  "Minister for Energy",
  "Minister:in für Energie",
  "Minister:in für Energie",
  "Ministre de l'Énergie", 
  "Minister for energi", 
  "_last_"
]
ta_to_longmini_fut_str = [
  "Minister for the Future",
  "Minister:in für die Zukunft",
  "Minister:in für die Zukunft",
  "Ministre pour le futur", 
  "Minister for fremtiden", 
  "_last_"
]
pol_to_expl_CCS_str = [
  "Percent of fossil use to be equipped with carbon capture and storage (CCS) at source. This means that you still emit CO2 but it does not get to the atmosphere where it causes warming because you capture it and store it underground.",
  "Prozentsatz der fossilen Brennstoffe der mit CO2-Abscheidung und -Speicherung (CCS) an der Quelle ausgestattet werden soll. Das bedeutet dass zwar weiterhin CO2 ausgestossen wird dieses aber nicht in die Atmosphäre gelangt wo es Erwärmung verursacht weil es vorher abgeschieden und unter der Erde gespeichert wird.",
  "Prozentsatz der fossilen Brennstoffe der mit CO2-Abscheidung und -Speicherung (CCS) an der Quelle ausgestattet werden soll. Das bedeutet dass zwar weiterhin CO2 ausgestossen wird dieses aber nicht in die Atmosphäre gelangt wo es Erwärmung verursacht weil es vorher abgeschieden und unter der Erde gespeichert wird.",
  "Pourcentage de combustibles fossiles devant être équipés d'un système de captage et de stockage du CO2 (CSC) à la source. Cela signifie que le CO2 continue d'être émis, mais qu'il n'est pas rejeté dans l'atmosphère où il provoque un réchauffement, car il est préalablement capturé et stocké dans le sol." ,
  "Prosent av fossil bruk til å være utstyrt med karbonfangst og lagring (CCS) ved kilden. Dette betyr at du fremdeles avgir CO2, men det kommer ikke til atmosfæren der det forårsaker oppvarming fordi du fanger den og lagrer den under jorden.", 
  "_last_"
]
pol_to_expl_TOW_str = [
  "0 means no wealth tax, 80 means 80% of accrued owners wealth is taxed away each year, 50 half of it. If you think of Elon Musk, the richest person in the world who owns roughly 300 billion USD, 0 would let him keep everything; entering '80' would tax away 240 billion - so he would still have 60 billion(!), and '50' would tax away 150 billion, letting him keep 150 billion - what is fair?",
  "0 bedeutet keine Vermögenssteuer 80 bedeutet dass jedes Jahr 80 % des angesammelten Vermögens des Eigentümers versteuert werden 50 bedeutet dass die Hälfte davon versteuert wird. Wenn man an Elon Musk denkt, den reichsten Menschen der Welt, der etwa 300 Milliarden US-Dollar besitzt, würde 0 ihm alles lassen; die Eingabe '80' bedeutet eine Steuerlast von 240 Milliarden – er hätte also noch 60 Milliarden (!) übrig, und 50 würde 150 Milliarden besteuern, sodass er 150 Milliarden behalten könnte – was ist fair?",
  "0 bedeutet keine Vermögenssteuer 80 bedeutet dass jedes Jahr 80 % des angesammelten Vermögens des Eigentümers versteuert werden 50 bedeutet dass die Hälfte davon versteuert wird. Wenn man an Elon Musk denkt, den reichsten Menschen der Welt, der etwa 300 Milliarden US-Dollar besitzt, würde 0 ihm alles lassen; die Eingabe '80' bedeutet eine Steuerlast von 240 Milliarden – er hätte also noch 60 Milliarden (!) übrig, und 50 würde 150 Milliarden besteuern, sodass er 150 Milliarden behalten könnte – was ist fair?",
  "0 signifie aucune taxe sur la richesse 80 signifie 80% des propriétaires accumulés La richesse est taxée chaque année 50 moitié. Si vous pensez à Elon Musk, l'homme le plus riche du monde qui possède environ 300 milliards de dollars, 0 lui permettrait de tout garder; en saisissant « 80 », cela entraînerait une perte fiscale de 240 milliards, il lui resterait donc 60 milliards (!), et 50 lui ferait payer 150 milliards d'impôts, lui laissant 150 milliards. Qu'est-ce qui est juste ?", 
  "0 betyr ingen formuesavgift 80 betyr 80% av påløpte eiere formue beskattes bort hvert år 50 halvparten av det.  Hvis du tenker på Elon Musk, den rikeste personen i verden som eier rundt 300 milliarder dollar, ville 0 la ham beholde alt; å skrive inn «80» ville medføre en skatt på 240 milliarder – så han ville fortsatt ha 60 milliarder (!), og 50 ville beskatte 150 milliarder, slik at han kunne beholde 150 milliarder – hva er rettferdig?", 
  "_last_"
]
pol_to_expl_FPGDC_str = [
  "Cancels a percentage of Govt debt outstanding to public lenders. 0 means nothing is cancelled, 100 all is cancelled, 50 half is cancelled --- in the policy start year. Imagine the government owes 180 billion USD to the World Bank - if you enter '30', 180 * .3 = 54 billion is forgiven and the government still owes 126 billion",
  "Diese Massnahme erlässt einen Prozentsatz der ausstehenden Staatsschulden gegenüber öffentlichen Kreditgebern. 0 bedeutet dass nichts erlassen wird, 100 bedeutet dass alles erlassen wird 50 bedeutet dass die Hälfte erlassen wird --- im ersten Jahr der Massnahmen. Stellen Sie sich vor, die Regierung schuldet der Weltbank 180 Milliarden US-Dollar – wenn Sie '30' eingeben, werden 180 * 0,3 = 54 Milliarden erlassen, und die Regierung schuldet weiterhin 126 Milliarden.",
  "Diese Massnahme erlässt einen Prozentsatz der ausstehenden Staatsschulden gegenüber öffentlichen Kreditgebern. 0 bedeutet dass nichts erlassen wird, 100 bedeutet dass alles erlassen wird 50 bedeutet dass die Hälfte erlassen wird --- im ersten Jahr der Massnahmen. Stell Dir vor, die Regierung schuldet der Weltbank 180 Milliarden US-Dollar – wenn Du '30' eingibst, werden 180 * 0,3 = 54 Milliarden erlassen, und die Regierung schuldet weiterhin 126 Milliarden.",
  "Annule un pourcentage de la dette du gouvernement en circulation aux prêteurs publics. 0 signifie que rien n'est annulé, 100 tout est annulé, 50 La moitié est annulé --- au cours de l'année de début de la politique. Imaginez que le gouvernement doive 180 milliards de dollars à la Banque mondiale. Si vous entrez « 30 », 180 * 0,3 = 54 milliards sont effacés et le gouvernement doit encore 126 milliards.",
  "Avbestill en prosentandel av utestående statsgjeld til offentlige långivere. 0 betyr at ingenting er kansellert, 100 alt er kansellert, 50 halvparten er kansellert --- i policyens startår.  Tenk deg at regjeringen skylder Verdensbanken 180 milliarder dollar – hvis du skriver inn «30», blir 180 * 0,3 = 54 milliarder ettergitt, og regjeringen skylder fortsatt 126 milliarder.",
  "_last_"
]
pol_to_expl_RMDR_str = [
  "Change in diet esp. a reduction in red meat consumption. 0 means red meat is consumed as before, 50 means 50% is replaced with lab meat, 100 means 100% is replaced with lab meat i.e. no more red meat is 'produced' by intensive livestock farming aka factory farming.",
  "Ernährungsumstellung insbesondere Reduzierung des Fleischkonsums. 0 bedeutet dass Fleisch wie bisher konsumiert wird, 50 bedeutet dass 50 % durch Laborfleisch ersetzt werden, 100 bedeutet dass 100 % durch Laborfleisch ersetzt werden d. h. dass in der Massentierhaltung kein Fleisch mehr 'produziert' wird.",
  "Ernährungsumstellung insbesondere Reduzierung des Fleischkonsums. 0 bedeutet dass Fleisch wie bisher konsumiert wird, 50 bedeutet dass 50 % durch Laborfleisch ersetzt werden, 100 bedeutet dass 100 % durch Laborfleisch ersetzt werden d. h. dass in der Massentierhaltung kein Fleisch mehr 'produziert' wird.",
  "Changement de régime en particulier. Une réduction de la consommation de viande rouge. 0 signifie que la viande rouge est consommée comme avant, 50 % signifie que 50% est remplacé par de la viande de laboratoire, 100 signifie que 100% est remplacé par de la viande de laboratoire, c'est-à-dire plus de viande rouge n'est` `produite '' par une agriculture de bétail intensive alias agricole.", 
  "Endring i kosthold, spesielt en reduksjon i rødt kjøttforbruk. 0 betyr at rødt kjøtt blir konsumert, da før, 50 betyr 50% erstattes med labmøtt kjøtt, 100 betyr 100% erstattes med laboratoriekjøtt, dvs. ikke mer rødt kjøtt blir produsert av intensivt husdyroppdrett aka fabrikkoppdrett.",
  "_last_"
]
pol_to_expl_REFOREST_str = [
  "Policy to reforest land i.e. plant new trees. 0 means no reforestation, 1 means you increase the forest area by 1 ‰ per yr (that is 1 promille), 3 = you increase the forest area by 3‰ per yr",
  "Massnahme zur Wiederaufforstung d.h. zum Pflanzen neuer Bäume. 0 bedeutet keine Wiederaufforstung, 1 bedeutet dass Sie die Waldfläche um 1 ‰ pro Jahr (das ist 1 Promille) vergrössern, 3 = Sie vergrössern die Waldfläche um 3 ‰ pro Jahr",
  "Massnahme zur Wiederaufforstung d.h. zum Pflanzen neuer Bäume. 0 bedeutet keine Wiederaufforstung, 1 bedeutet dass Sie die Waldfläche um 1 ‰ pro Jahr (das ist 1 Promille) vergrössern, 3 = Sie vergrössern die Waldfläche um 3 ‰ pro Jahr",
  "La politique de reboisement des terres, c'est-à-dire les nouveaux arbres de plante. 0 signifie qu'aucune reboisement, 1 signifie que vous augmentez la zone forestière de 1 ‰ par an (c'est 1 Promille), 3 = vous augmentez la zone forestière de 3 ‰ par an", 
  "Tiltak til Reforest land, dvs. plante nye trær. 0 betyr ingen skogplanting, 1 betyr at du øker skogområdet med 1 ‰ per år (det vil si 1 promille), 3 = du øker skogområdet med 3 ‰ per år", 
  "_last_"
]
pol_to_expl_FTPEE_str = [
  "Annual percentage increase in energy efficiency; 1% per yr is the historical value over the last 40 years. Beware of the power of compound interest!",
  "Jährliche prozentuale Steigerung der Energieeffizienz; 1 % pro Jahr ist der historische Wert der letzten 40 Jahre. Vorsicht vor der Macht des Zinseszinses!",
  "Jährliche prozentuale Steigerung der Energieeffizienz; 1 % pro Jahr ist der historische Wert der letzten 40 Jahre. Vorsicht vor der Macht des Zinseszinses!",
  "Augmentation annuelle de l'efficacité énergétique; 1% par an est la valeur historique au cours des 40 dernières années. Méfiez-vous de la puissance de l'intérêt composé!", 
  "Årlig prosentvis økning i energieffektivitet; 1% per år er den historiske verdien de siste 40 årene. Pass på kraften i sammensatt interesse!", 
  "_last_"
]
pol_to_expl_LPBsplit_str = [
  "0 means all LBP funding goes to consumption (eg child support subsidies for food or energy etc.) 100 means all goes to public investment like infrastructure security etc. NOTE This only has an effect if LPB is NOT set to zero",
  "0 bedeutet dass die gesamte LBP-Finanzierung in den Konsum fliesst (z. B. Kindergeld Subventionen für Lebensmittel oder Energie usw.). 100 bedeutet dass die gesamte Finanzierung in öffentliche Investitionen wie Infrastruktur Sicherheit usw. fliesst. HINWEIS Diese Massnahme hat nur dann eine Auswirkung wenn LPB NICHT auf Null gesetzt ist.",
  "0 bedeutet dass die gesamte LBP-Finanzierung in den Konsum fliesst (z. B. Kindergeld Subventionen für Lebensmittel oder Energie usw.). 100 bedeutet dass die gesamte Finanzierung in öffentliche Investitionen wie Infrastruktur Sicherheit usw. fliesst. HINWEIS Diese Massnahme hat nur dann eine Auswirkung wenn LPB NICHT auf Null gesetzt ist.",
  "0 signifie que tous les fonds LBP vont à la consommation (par exemple, les subventions aux enfants pour l'alimentation ou l'énergie, etc.) 100 signifie que tous les fonds vont à l'investissement public, comme la sécurité des infrastructures, etc. REMARQUE Ceci n'a d'effet que si le LPB n'est PAS fixé à zéro.", 
  "0 betyr at alle LBP-midler går til forbruk (f.eks. støtte til mat, energi osv.). 100 betyr at alle midler går til offentlige investeringer, f.eks. sikring av infrastruktur osv. MERK Dette har bare effekt hvis LPB IKKE er satt til null." ,
  "_last_"
]
pol_to_expl_ExPS_str = [
  "Cancels a percentage of Govt debt outstanding to private lenders --- in the policy start year",
  "Erlässt einen Prozentsatz der ausstehenden Staatsschulden gegenüber privaten Kreditgebern --- im ersten Jahr der Massnahmen",
  "Erlässt einen Prozentsatz der ausstehenden Staatsschulden gegenüber privaten Kreditgebern --- im ersten Jahr der Massnahmen",
  "Annule un pourcentage de la dette du gouvernement en circulation aux prêteurs privés --- dans l'année de début de la politique", 
  "Kobler en prosentandel av statsgjeld utestående til private långivere --- i policyens startår", 
  "_last_"
]
pol_to_expl_FMPLDD_str = [
  "Given your credit worthiness you have an amount you you can borrow from private lenders. Here you choose the fraction of credit you actually draw down each year.",
  "Angesichts Ihrer Kreditwürdigkeit steht Ihnen ein bestimmter Betrag zur Verfügung den Sie von privaten Kreditgebern leihen können. Hier wählen Sie den Anteil des Kredits den Sie tatsächlich jährlich in Anspruch nehmen.",
  "Angesichts Ihrer Kreditwürdigkeit steht Ihnen ein bestimmter Betrag zur Verfügung den Sie von privaten Kreditgebern leihen können. Hier wählen Sie den Anteil des Kredits den Sie tatsächlich jährlich in Anspruch nehmen.",
  "Compte tenu de votre solvabilité, vous avez un montant que vous pouvez emprunter auprès des prêteurs privés. Ici, vous choisissez la fraction de crédit que vous réalisez chaque année.", 
  "Med tanke på kredittverdigheten din har du et beløp du kan låne fra private långivere. Her velger du brøkdelen av kreditt du faktisk trekker ned hvert år.", 
  "_last_"
]
pol_to_expl_StrUP_str = [
  "In any economy the national income is shared between owners and workers. This policy changes the share going to workers. 1 multiplies the share with 1%, 2 with 2%, etc",
  "In jeder Volkswirtschaft wird das nationale Gesamtseinkommen zwischen Eigentümern und Arbeitnehmern aufgeteilt. Diese Massnahme verändert den Anteil der den Arbeitnehmern zusteht. 1 multipliziert den Anteil mit 1 %, 2 mit 2 %, usw.",
  "In jeder Volkswirtschaft wird das nationale Gesamtseinkommen zwischen Eigentümern und Arbeitnehmern aufgeteilt. Diese Massnahme verändert den Anteil der den Arbeitnehmern zusteht. 1 multipliziert den Anteil mit 1 %, 2 mit 2 %, usw.",
  "Dans toute économie, le revenu national est partagé entre les propriétaires et les travailleurs. Cette politique modifie la part des travailleurs. 1 multiplie la part avec 1%, 2 avec 2%, etc", 
  "I enhver økonomi deles nasjonalinntekten mellom eiere og arbeidere. Denne politikken endrer andelen som går til arbeidere. 1 multipliserer andelen med 1%, 2 med 2%, osv." ,
  "_last_"
]
pol_to_expl_Wreaction_str = [
  "In any economy there is a power struggle between workers and owners about the share of national income each gets. This policy strenghtens the workers negotiation position. 1 by 1% 2 by 2% etc.",
  "In jeder Volkswirtschaft gibt es einen Machtkampf zwischen Arbeitnehmern und Eigentümern um den Anteil am Gesamteinkommen den jeder erhält. Diese Massnahme stärkt die Verhandlungsposition der Arbeitnehmer. 1 um 1 % 2 um 2 % usw.",
  "In jeder Volkswirtschaft gibt es einen Machtkampf zwischen Arbeitnehmern und Eigentümern um den Anteil am Gesamteinkommen den jeder erhält. Diese Massnahme stärkt die Verhandlungsposition der Arbeitnehmer. 1 um 1 % 2 um 2 % usw.",
  "Dans toute économie, il y a une lutte de pouvoir entre les travailleurs et les propriétaires sur la part du revenu national chacun. Cette politique saisit la position de négociation des travailleurs. 1 par 1% 2 par 2% etc.", 
  "I enhver økonomi er det en maktkamp mellom arbeidere og eiere om andelen av nasjonalinntektene hver får. Denne politikken er i arbeidstakernes forhandlingsposisjon. 1 med 1% 2 med 2% etc.", 
  "_last_"
]
pol_to_expl_SGMP_str = [
  "To fight poverty in old age you can introduce pensions for all. The size of the pension is expressed as the percent of the GDP you want to invest. 0 means you invest nothing and leave things as they are. 5 means you invest 5 % of GDP; 10 = 10 % of GDP money is transferred to workers and paid for by owners",
  "Um Altersarmut zu bekämpfen können Renten für alle eingeführt werden. Die Höhe der Rente wird als Prozentsatz des BIP ausgedrückt den Sie investieren möchten. 0 bedeutet dass Sie nichts investieren und alles so lassen wie es ist. 5 bedeutet dass Sie 5 % des BIP investieren. 10 bedeutet dass 10 % des BIP an die Arbeitnehmer überwiesen und von den Eigentümern bezahlt werden.",
  "Um Altersarmut zu bekämpfen können Renten für alle eingeführt werden. Die Höhe der Rente wird als Prozentsatz des BIP ausgedrückt den Sie investieren möchten. 0 bedeutet dass Sie nichts investieren und alles so lassen wie es ist. 5 bedeutet dass Sie 5 % des BIP investieren. 10 bedeutet dass 10 % des BIP an die Arbeitnehmer überwiesen und von den Eigentümern bezahlt werden.",
  "Pour lutter contre la pauvreté dans la vieillesse, vous pouvez introduire des pensions pour tous. La taille de la pension est exprimée en pourcentage du PIB que vous souhaitez investir. 0 signifie que vous n'investissez rien et laissez les choses telles qu'elles sont. 5 signifie que vous investissez 5% du PIB; 10 = 10% de l'argent du PIB est transféré aux travailleurs et payé par les propriétaires",
  "For å bekjempe fattigdom i alderdommen kan du innføre pensjoner for alle. Størrelsen på pensjonen uttrykkes som prosent av BNP du vil investere. 0 betyr at du ikke investerer noe og legger igjen ting som de er. 5 betyr at du investerer 5 % av BNP; 10 = 10 % av BNP -pengene blir overført til arbeidere og betalt for eiere", 
  "_last_"
]
pol_to_expl_FWRP_str = [
  "Here you decide how much the percentage of 'normal' waste which is 30% is to be reduced. I.e. 100 means no more waste! 50 means waste is reduced by 50 % 0 means waste continues as always",
  "Hier legen Sie fest um wie viel der Anteil des 'normalen' Nahrungsverlustes von 30% reduziert werden soll. D.h. 100 bedeutet keinen Verlust mehr! 50 bedeutet dass der Verlust um 50 % reduziert wird 0 bedeutet dass der Verlust wie immer weitergeht",
  "Hier legen Sie fest um wie viel der Anteil des 'normalen' Nahrungsverlustes von 30% reduziert werden soll. D.h. 100 bedeutet keinen Verlust mehr! 50 bedeutet dass der Verlust um 50 % reduziert wird 0 bedeutet dass der Verlust wie immer weitergeht",
  "Ici, vous décidez combien le pourcentage de déchets« normaux »qui doit être réduit. C'est-à-dire que 100 signifie plus de déchets! 50 signifie que les déchets sont réduits de 50% 0 signifie que les déchets se poursuivent comme toujours", 
  "Her bestemmer du hvor mye prosentandelen av 'normalt' avfall som er 30 % skal reduseres. Dvs. 100 betyr ikke mer avfall! 50 betyr at avfall reduseres med 50 % 0 betyr at avfall fortsetter som alltid", 
  "_last_"
]
pol_to_expl_ICTR_str = [
  "This policy is an increase in the consumption tax (aka sales tax value added tax (VAT) etc. 0 means no increase 10 means an increase by 10 percentage points 5 by 5 percentage points; the money raised goes to general govt revenue.",
  "Bei dieser Massnahme handelt es sich um eine Erhöhung der Verbrauchssteuer (auch Umsatzsteuer Mehrwertsteuer usw. genannt). 0 bedeutet keine Erhöhung 10 bedeutet eine Erhöhung um 10 Prozentpunkte 5 um 5 Prozentpunkte; die eingenommenen Gelder fliessen in die allgemeinen Staatseinnahmen.",
  "Bei dieser Massnahme handelt es sich um eine Erhöhung der Verbrauchssteuer (auch Umsatzsteuer Mehrwertsteuer usw. genannt). 0 bedeutet keine Erhöhung 10 bedeutet eine Erhöhung um 10 Prozentpunkte 5 um 5 Prozentpunkte; die eingenommenen Gelder fliessen in die allgemeinen Staatseinnahmen.",
  "Cette mesur est une augmentation de la taxe sur la consommation (AKE Taxe de vente Taxe ajoutée à la valeur ajoutée (TVA), etc. 0 signifie aucune augmentation 10 signifie une augmentation de 10 points de pourcentage 5 sur 5 points de pourcentage; l'argent collecté va aux revenus du gouvernement général.", 
  "Denne tiltak er en økning i forbruksavgiften (aka omsetningsverdi (merverdiavgift (mva) osv. 0 betyr ingen økning 10 betyr en økning med 10 prosentpoeng 5 med 5 prosentpoeng; pengene som samles inn går til generelle regjeringsinntekter.", 
  "_last_"
]
pol_to_expl_XtaxCom_str = [
  "A universal basic dividend is created when a state taxes common goods like fishing rights mining rights the right to use airwaves etc. This policy sets this tax as a percent of GDP i.e. 0 = 0 % of GDP i.e. nothing; 5 = 5 % of GDP; 3 = 3 % of GDP money is transferred to general govt tax revenue.",
  "Eine universelle Grunddividende entsteht wenn ein Staat öffentliche Güter wie Fischereirechte Bergbaurechte das Recht zur Nutzung des Frequenzsprektrums usw. besteuert. Diese Richtlinie legt diese Steuer als Prozentsatz des BIP fest d. h. 0 = 0 % des BIP also nichts; 5 = 5 % des BIP; 3 = 3 % des BIP. Das Geld wird in die allgemeinen Steuereinnahmen des Staates überführt.",
  "Eine universelle Grunddividende entsteht wenn ein Staat öffentliche Güter wie Fischereirechte Bergbaurechte das Recht zur Nutzung des Frequenzsprektrums usw. besteuert. Diese Richtlinie legt diese Steuer als Prozentsatz des BIP fest d. h. 0 = 0 % des BIP also nichts; 5 = 5 % des BIP; 3 = 3 % des BIP. Das Geld wird in die allgemeinen Steuereinnahmen des Staates überführt.",
  "Un dividende de base universel est créé lorsqu'un État taxait des biens communs comme les droits des droits des droits de pêche le droit d'utiliser les ondes, etc. Cette politique établit cette taxe en pourcentage du PIB, soit 0 = 0% du PIB, c'est-à-dire que rien; 5 = 5% du PIB; 3 = 3% de l'argent du PIB est transféré au revenu fiscal général de l'État.", 
  "Et universelt grunnleggende utbytte opprettes når en stat skatter vanlige varer som fiskerettigheter gruvedrift rettigheter til å bruke luftbølger osv. Denne policyen setter denne skatten som en prosent av BNP, dvs. 0 = 0 % av BNP, dvs. ingenting; 5 = 5 % av BNP; 3 = 3 % av BNP -penger blir overført til generell inntekt av staten.", 
  "_last_"
]
pol_to_expl_Lfrac_str = [
  "Leakage describes the use of money for illicit purposes - Corruption bribery etc. The normal leakage is 20% - so a value of 0 reduction means that those 20% do in fact disappear - a 50 % reduction means 10% disappear and 100% reduction means nothing disappears and everyone in your region is totally honest!",
  "Leakage beschreibt das 'Versickern' von Geldern in illegale Kanäle - Korruption Bestechung usw. Der normale Verlust liegt bei 20 % - ein Wert von 0 bedeutet also dass diese 20 % tatsächlich verschwinden - eine Reduzierung von 50 % bedeutet dass 10 % verschwinden und eine Reduzierung von 100 % bedeutet dass nichts versickert und jeder in Ihrer Region absolut ehrlich ist!",
  "Leakage beschreibt das 'Versickern' von Geldern in illegale Kanäle - Korruption Bestechung usw. Der normale Verlust liegt bei 20 % - ein Wert von 0 bedeutet also dass diese 20 % tatsächlich verschwinden - eine Reduzierung von 50 % bedeutet dass 10 % verschwinden und eine Reduzierung von 100 % bedeutet dass nichts versickert und jeder in Ihrer Region absolut ehrlich ist!",
  "La fuite décrit l'utilisation de l'argent à des fins illicites - corruption corruption, etc. La fuite normale est de 20% - donc une valeur de 0 réduction signifie que ces 20% disparaissent en fait - une réduction de 50% signifie que 10% disparaissent et que la réduction de 100% signifie que rien ne disparaît et que tout le monde dans votre région est totalement honnête!", 
  "Lekkasje beskriver bruken av penger til ulovlige formål - korrupsjonsbestikkelse osv. Den normale lekkasjen er 20% - så en verdi av 0 reduksjon betyr at de 20% faktisk forsvinner - en reduksjon på 50% betyr at 10% forsvinner og 100% reduksjon betyr at ingenting forsvinner og alle i regionen din er helt ærlig!", 
  "_last_"
]
pol_to_expl_IOITR_str = [
  "This is an increase in the income tax paid by owners. 0 means no increase 10 means an increase by 10 percentage points 5 by 5 percentage points; the money raised goes to general govt revenue.",
  "Dies ist eine Erhöhung der von Eigentümern gezahlten Einkommensteuer. 0 bedeutet keine Erhöhung 10 bedeutet eine Erhöhung um 10 Prozentpunkte 5 um 5 Prozentpunkte; das eingenommene Geld fliesst in die allgemeinen Staatseinnahmen.",
  "Dies ist eine Erhöhung der von Eigentümern gezahlten Einkommensteuer. 0 bedeutet keine Erhöhung 10 bedeutet eine Erhöhung um 10 Prozentpunkte 5 um 5 Prozentpunkte; das eingenommene Geld fliesst in die allgemeinen Staatseinnahmen.",
  "Il s'agit d'une augmentation de l'impôt sur le revenu payé par les propriétaires. 0 signifie aucune augmentation 10 signifie une augmentation de 10 points de pourcentage 5 sur 5 points de pourcentage; l'argent collecté va aux revenus du gouvernement général.", 
  "Dette er en økning i inntektsskatten som eiere har betalt. 0 betyr ingen økning 10 betyr en økning med 10 prosentpoeng 5 med 5 prosentpoeng; pengene som er samlet inn, går til generelle regjeringsinntekter.", 
  "_last_"
]
pol_to_expl_IWITR_str = [
  "This is an increase in the income tax paid by workers. 0 means no increase 10 means an increase by 10 percentage points 5 by 5 percentage points; the money raised goes to general govt revenue.",
  "Dies ist eine Erhöhung der von Arbeitnehmern gezahlten Einkommenssteuer. 0 bedeutet keine Erhöhung 10 bedeutet eine Erhöhung um 10 Prozentpunkte 5 um 5 Prozentpunkte; das eingenommene Geld fliesst in die allgemeinen Staatseinnahmen.",
  "Dies ist eine Erhöhung der von Arbeitnehmern gezahlten Einkommenssteuer. 0 bedeutet keine Erhöhung 10 bedeutet eine Erhöhung um 10 Prozentpunkte 5 um 5 Prozentpunkte; das eingenommene Geld fliesst in die allgemeinen Staatseinnahmen.",
  "Il s'agit d'une augmentation de l'impôt sur le revenu payé par les travailleurs. 0 signifie aucune augmentation 10 signifie une augmentation de 10 points de pourcentage 5 sur 5 points de pourcentage; l'argent collecté va aux revenus du gouvernement général.", 
  "Dette er en økning i inntektsskatten som er betalt av arbeidere. 0 betyr ingen økning 10 betyr en økning med 10 prosentpoeng 5 med 5 prosentpoeng; pengene som samles inn går til generelle regjeringsinntekter.", 
  "_last_"
]
pol_to_expl_SGRPI_str = [
  "Governments choose how to use their spending - primarily for consumption (eg child support subsidies for food or energy etc.) or for public investment (education health care infrastructure etc.) This policy shifts spending from consumption to investment. 0 means no shift 10= 10% of consumption shifted to investment 25 = 25 % of consumption shifted to investment etc",
  "Regierungen entscheiden wie sie ihre Ausgaben einsetzen - vorrangig für Konsum (z. B. Kindergeld Subventionen für Nahrungsmittel oder Energie usw.) oder für öffentliche Investitionen (Bildung Gesundheitswesen Infrastruktur usw.). Diese Massnahme verlagert die Ausgaben vom Konsum auf Investitionen. 0 bedeutet keine Verschiebung 10 = 10 % des Konsums werden auf Investitionen umgeleitet 25 = 25 % des Konsums werden auf Investitionen umgeleitet usw.",
  "Regierungen entscheiden wie sie ihre Ausgaben einsetzen - vorrangig für Konsum (z. B. Kindergeld Subventionen für Nahrungsmittel oder Energie usw.) oder für öffentliche Investitionen (Bildung Gesundheitswesen Infrastruktur usw.). Diese Massnahme verlagert die Ausgaben vom Konsum auf Investitionen. 0 bedeutet keine Verschiebung 10 = 10 % des Konsums werden auf Investitionen umgeleitet 25 = 25 % des Konsums werden auf Investitionen umgeleitet usw.",
  "Les gouvernements choisissent comment utiliser leurs dépenses - principalement pour la consommation (par exemple, les subventions à la pension alimentaire pour enfants pour l'alimentation ou l'énergie, etc.) ou pour l'investissement public (infrastructure de soins de santé éducative, etc.) Cette politique passe de la consommation à l'investissement. 0 signifie aucun changement 10 = 10% de la consommation passée à l'investissement 25 = 25% de la consommation décalée à l'investissement et 10%", 
  "Regjeringer velger hvordan de skal bruke utgiftene sine - først og fremst til konsum (f.eks. Barnebidragsubsidier til mat eller energi etc.) eller for offentlige investeringer (utdanningshelseinfrastruktur osv.) Denne policyen flytter utgiftene fra forbruk til investering. 0 betyr ingen skift 10 = 10 % av forbruket skiftet til investering 25 = 25 % av forbruket skiftet til investering osv." ,
  "_last_"
]
pol_to_expl_FEHC_str = [
  "The higher the level of education esp. of women in a society the lower the birth rate. Thus education for all lowers the birth rate. By how much? You make an educated guess - 0 means no effect 10 means a 10% reduction 5 means a 5% reduction etc.",
  "Je höher das Bildungsniveau insbesondere der Frauen in einer Gesellschaft ist desto niedriger ist die Geburtenrate. Bildung für alle senkt also die Geburtenrate. Um wie viel? Sie können eine fundierte Schätzung abgeben - 0 bedeutet keine Auswirkung 10 bedeutet eine Verringerung um 10 % 5 bedeutet eine Verringerung um 5 % usw..",
  "Je höher das Bildungsniveau insbesondere der Frauen in einer Gesellschaft ist desto niedriger ist die Geburtenrate. Bildung für alle senkt also die Geburtenrate. Um wie viel? Sie können eine fundierte Schätzung abgeben - 0 bedeutet keine Auswirkung 10 bedeutet eine Verringerung um 10 % 5 bedeutet eine Verringerung um 5 % usw..",
  "Plus le niveau d'éducation est élevé, en particulier des femmes dans une société, plus le taux de natalité est faible. Ainsi, l'éducation pour tout abaisse le taux de natalité. De combien? Vous faites une supposition éclairée - 0 signifie aucun effet 10 signifie une réduction de 10% 5 signifie une réduction de 5% etc.", 
  "Jo høyere utdanningsnivå spesielt av kvinner i et samfunn, jo lavere fødselsrate. Dermed reduserer utdanning for alle fødselsraten. Med hvor mye? Du gjør en utdannet gjetning - 0 betyr ingen effekt 10 betyr en 10% reduksjon 5 betyr en 5% reduksjon osv.", 
  "_last_"
]
pol_to_expl_XtaxRateEmp_str = [
  "To support women to reach equality costs some money esp. to close the pay gender gap. How much do you want to spend as a pct of GDP? 0 means you spend nothing and leave things as they are; 5 means you spend= 5 % of GDP; 3 = 3 % of GDP. Money is transferred to general govt tax revenue",
  "Die Gleichstellung von Frauen zu fördern insbesondere die Verringerung des geschlechtsspezifischen Lohngefälles kostet Geld. Wie viel Prozent des BIP möchten Sie dafür ausgeben? 0 bedeutet Sie geben nichts aus und lassen alles so wie es ist; 5 bedeutet Sie geben 5 % des BIP aus; 3 bedeutet 3 % des BIP. Das Geld fliesst in die allgemeinen Steuereinnahmen des Staates.",
  "Die Gleichstellung von Frauen zu fördern insbesondere die Verringerung des geschlechtsspezifischen Lohngefälles kostet Geld. Wie viel Prozent des BIP möchten Sie dafür ausgeben? 0 bedeutet Sie geben nichts aus und lassen alles so wie es ist; 5 bedeutet Sie geben 5 % des BIP aus; 3 bedeutet 3 % des BIP. Das Geld fliesst in die allgemeinen Steuereinnahmen des Staates.",
  "Pour aider les femmes à atteindre l'égalité, des coûts de l'argent en particulier pour combler l'écart de rémunération des sexes. Combien voulez-vous dépenser en tant que pourcentage du PIB? 0 signifie que vous ne dépensez rien et laissez les choses telles qu'elles sont; 5 signifie que vous dépensez = 5% du PIB; 3 = 3% du PIB. L'argent est transféré aux recettes fiscales générales du gouvernement", 
  "Å støtte kvinner for å nå likestilling koster noen penger, spesielt å lukke lønnsgapet. Hvor mye vil du bruke som prosent av BNP? 0 betyr at du bruker ingenting og legger igjen ting som de er; 5 betyr at du bruker = 5 % av BNP; 3 = 3 % av BNP. Penger overføres til generelle Govt -skattinntekter", 
  "_last_"
]
pol_to_expl_FLWR_str = [
  "Here you decide the percentage of your cropland that is worked regeneratively (low or no tillage low or no fertilizers and pesticides etc.) 50 means 50 % cropland worked is regeneratively 100 = 100 % of cropland is worked regeneratively etc. 0 leaves things as they are.",
  "Hier legen Sie den Prozentsatz Ihrer Ackerfläche fest der regenerativ bearbeitet wird (geringe oder keine Bodenbearbeitung geringe oder keine Dünge- und Pestizidverwendung usw.). 50 bedeutet dass 50 % der Ackerfläche regenerativ bearbeitet werden 100 = 100 % der Ackerfläche werden regenerativ bearbeitet usw. 0 lässt alles so wie es ist.",
  "Hier legen Sie den Prozentsatz Ihrer Ackerfläche fest der regenerativ bearbeitet wird (geringe oder keine Bodenbearbeitung geringe oder keine Dünge- und Pestizidverwendung usw.). 50 bedeutet dass 50 % der Ackerfläche regenerativ bearbeitet werden 100 = 100 % der Ackerfläche werden regenerativ bearbeitet usw. 0 lässt alles so wie es ist.",
  "Ici, vous décidez que le pourcentage de vos terres cultivées qui est travaillé de manière régénérative (faible ou pas de travail bas ou pas d'engrais et de pesticides, etc.) 50 signifie que 50% de terres cultivées fonctionnantes sont régénérativement 100 = 100% des terres cultivées sont travaillées de manière régénérative, etc. 0 laisse les choses telles qu'elles sont.", 
  "Her angir du hvor stor prosentandel av åkerarealet som dyrkes med regenerative metoder (liten eller ingen jordbearbeiding, liten eller ingen bruk av kunstgjødsel og plantevernmidler osv.) 50 betyr at 50 % av åkerarealet dyrkes regenerativt 100 = 100 % av åkerarealet dyrkes regenerativt, osv. 0 betyr at alt er som det er." ,
  "_last_"
]
pol_to_expl_RIPLGF_str = [
  "Reduction in food imports. 0 means no reduction 10=10% reduction 50=50% reduction This policy reduces food available from elsewhere but strenghtens local producers",
  "Reduzierung der Lebensmittelimporte. 0 bedeutet keine Reduzierung 10=10% Reduzierung 50=50% Reduzierung. Diese Massnahme reduziert die Verfügbarkeit von Lebensmitteln aus anderen Ländern stärkt aber die lokalen Produzenten.",
  "Reduzierung der Lebensmittelimporte. 0 bedeutet keine Reduzierung 10=10% Reduzierung 50=50% Reduzierung. Diese Massnahme reduziert die Verfügbarkeit von Lebensmitteln aus anderen Ländern stärkt aber die lokalen Produzenten.",
  "Réduction des importations de denrées alimentaires. 0 signifie aucune réduction 10=10% de réduction 50=50% de réduction. Cette politique réduit la disponibilité des aliments provenant d'autres pays mais renforce les producteurs locaux.",
  "Reduksjon av matimport. 0 betyr ingen reduksjon 10=10 % reduksjon 50=50 % reduksjon. Denne politikken reduserer tilgangen på mat fra andre land, men styrker lokale produsenter.",
  "_last_"
]
pol_to_expl_FC_str = [
  "Policy to limit forest cutting. 0 means no limitation on cutting 10=10% reduction in the maximum amount that can be cut 50=50% reduction in max cut etc. all the way to 90 % reduction which is practically a ban on cutting",
  "Massnahme zur Begrenzung der Abholzung. 0 bedeutet keine Begrenzung der Abholzung 10 = 10 % Reduzierung der maximalen Abholzungsmenge 50 = 50 % Reduzierung der maximalen Abholzungsmenge usw. bis hin zu 90 % Reduzierung was praktisch einem Abholzungsverbot entspricht.",
  "Massnahme zur Begrenzung der Abholzung. 0 bedeutet keine Begrenzung der Abholzung 10 = 10 % Reduzierung der maximalen Abholzungsmenge 50 = 50 % Reduzierung der maximalen Abholzungsmenge usw. bis hin zu 90 % Reduzierung was praktisch einem Abholzungsverbot entspricht.",
  "Mesur pour limiter la coupe des forêts. 0 signifie aucune limitation à la réduction de 10 = 10% de réduction de la quantité maximale qui peut être réduite de 50 = 50% de réduction maximale, etc. jusqu'à 90% de réduction qui est pratiquement une interdiction de couper", 
  "Tiltak for å begrense skogskjæring. 0 betyr ingen begrensning på å kutte 10 = 10% reduksjon i den maksimale mengden som kan kuttes 50 = 50% reduksjon i maks kutt osv. Helt til 90% reduksjon som praktisk talt er et forbud mot å kutte", 
  "_last_"
]
pol_to_expl_NEP_str = [
  "Percent of fossil fuel (oil gas and coal) *not* used for electricity generation (mobility heating industrial use etc.) that you want to electrify.",
  "Prozentsatz der fossilen Brennstoffe (Öl Gas und Kohle) die *nicht* zur Stromerzeugung (Mobilität Heizung industrielle Nutzung usw.) verwendet werden und die Sie elektrifizieren möchten.",
  "Prozentsatz der fossilen Brennstoffe (Öl Gas und Kohle) die *nicht* zur Stromerzeugung (Mobilität Heizung industrielle Nutzung usw.) verwendet werden und die Sie elektrifizieren möchten.",
  "Pourcentage de combustibles fossiles (gaz pétrolier et charbon) *Pas* utilisé pour la production d'électricité (mobilité chauffant à usage industriel, etc.) que vous souhaitez électrifier.", 
  "Prosent av fossilt brensel (oljegass og kull) *ikke* brukt til elektrisitetsproduksjon (Mobilitetsoppvarming av industriell bruk osv.) Som du vil elektrifisere.", 
  "_last_"
]
pol_to_expl_Ctax_str = [
  "This is the carbon emission tax. 0 means no carbon tax 25 = 25 $/ton of CO2 emitted etc.",
  "Dies ist die CO2-Emissionssteuer. 0 bedeutet keine CO2-Steuer 25 = 25 $/Tonne emittiertes CO2 usw.",
  "Dies ist die CO2-Emissionssteuer. 0 bedeutet keine CO2-Steuer 25 = 25 $/Tonne emittiertes CO2 usw.",
  "Il s'agit de la taxe sur les émissions de carbone. 0 signifie aucune taxe sur le carbone 25 = 25 $ / tonne de CO2 émis, etc.", 
  "Dette er karbonutslippsskatten. 0 betyr ingen karbonavgift 25 = 25 $/tonn CO2 som sendes ut osv.", 
  "_last_"
]
pol_to_expl_DAC_str = [
  "Capturing CO2 that is already in the atmosphere and storing it underground  - in GtCO2/yr (Giga tons - giga is 10^9); In 2020 regional emissions were roughly as follows: USA 5, Africa south of Sahara 1, China 12, the rest all between 2 and 3 GtCO2/yr. You can capture more than you emit.",
  "Rückgewinnung von CO2 das sich bereits in der Atmosphäre befindet und dessen unterirdische Speicherung - in GtCO2/Jahr (Gigatonnen - Giga ist 10^9); Im Jahr 2020 betrugen die regionalen Emissionen ungefähr: USA 5, Afrika südlich der Sahara 1, China 12, alle anderen jeweils zwischen 2 und 3 GtCO2/Jahr. Man kann mehr rück gewinnen als man ausstösst.",
  "Rückgewinnung von CO2 das sich bereits in der Atmosphäre befindet und dessen unterirdische Speicherung - in GtCO2/Jahr (Gigatonnen - Giga ist 10^9); Im Jahr 2020 betrugen die regionalen Emissionen ungefähr: USA 5, Afrika südlich der Sahara 1, China 12, alle anderen jeweils zwischen 2 und 3 GtCO2/Jahr. Man kann mehr rück gewinnen als man ausstösst.",
  "Récupération du CO2 déjà présent dans l'atmosphère et son stockage souterrain & en GtCO2/an (gigatonnes - giga est 10^9) ; En 2020, les émissions régionales étaient d'environ: USA 5, Afrique subsaharienne 1, Chine 12, le reste entre 2 et 3 GtCO2/an chacun. On peut gagner plus de recul que l'on n'en émet.",
  "Gjenvinning av CO2 som allerede er i atmosfæren og lagring i undergrunnen & i GtCO2/år (Gigatonn - Giga er 10^9); I 2020 var de regionale utslippene omtrent: USA 5, Afrika sør for Sahara 1, Kina 12, resten mellom 2 og 3 GtCO2/år hver. Du kan gjenvinne mer enn du slipper ut.",
  "_last_"
]
pol_to_expl_XtaxFrac_str = [
  "The percentage of *extra* taxes paid by owners (owners pay 50% of extra taxes even under TLTL) I.e. 90 means owners pay 90 % of extra taxes 70 means owners pay 70 % of extra taxes etc. Extra taxes are those for empowerment and to give women equal pay.",
  "Der Prozentsatz der *zusätzlichen* Steuern die von Eigentümern gezahlt werden (Eigentümer zahlen 50 % der zusätzlichen Steuern sogar unter TLTL). D. h. 90 bedeutet dass Eigentümer 90 % der zusätzlichen Steuern zahlen 70 bedeutet dass Eigentümer 70 % der zusätzlichen Steuern zahlen usw. Zusätzliche Steuern dienen der Stärkung der Selbstbestimmung und der gleichen Bezahlung von Frauen.",
  "Der Prozentsatz der *zusätzlichen* Steuern die von Eigentümern gezahlt werden (Eigentümer zahlen 50 % der zusätzlichen Steuern sogar unter TLTL). D. h. 90 bedeutet dass Eigentümer 90 % der zusätzlichen Steuern zahlen 70 bedeutet dass Eigentümer 70 % der zusätzlichen Steuern zahlen usw. Zusätzliche Steuern dienen der Stärkung der Selbstbestimmung und der gleichen Bezahlung von Frauen.",
  "Le pourcentage de *taxes supplémentaires* payées par les propriétaires (les propriétaires paient 50% des taxes supplémentaires même en vertu de TLTL), soit 90 moyens de payer 90% des taxes supplémentaires 70 signifie que les propriétaires paient 70% des taxes supplémentaires, etc. Les taxes supplémentaires sont celles pour l'autonomisation et pour donner aux femmes une rémunération égale.", 
  "Andelen *ekstra* skatter betalt av eiere (eiere betaler 50 % av ekstra skatter selv under tltl), dvs. 90 betyr at eiere betaler 90 % av ekstra skatter 70 betyr at eiere betaler 70 % av ekstra skatter osv. Ekstra skatter er dem for myndighet og for å gi kvinner like lønn.", 
  "_last_"
]
pol_to_expl_LPBgrant_str = [
  "0 means all LPB funding is given as loans that must be repaid 100 means all is given as grants that carry no interest and must not be repaid. NOTE This only has an effect if LPB is NOT set to zero",
  "0 bedeutet dass die gesamte LPB-Finanzierung als Darlehen gewährt wird das sowohl zurückgezahlt als auch verzinst werden muss. 100 bedeutet dass die gesamte Finanzierung als zinslose Zuschüsse gewährt wird die nicht zurückgezahlt werden müssen. HINWEIS Diese Massnahme hat nur dann Auswirkungen wenn LPB NICHT auf Null gesetzt ist.",
  "0 bedeutet dass die gesamte LPB-Finanzierung als Darlehen gewährt wird das sowohl zurückgezahlt als auch verzinst werden muss. 100 bedeutet dass die gesamte Finanzierung als zinslose Zuschüsse gewährt wird die nicht zurückgezahlt werden müssen. HINWEIS Diese Massnahme hat nur dann Auswirkungen wenn LPB NICHT auf Null gesetzt ist.",
  "0 signifie que tout le financement LPB est accordé comme des prêts qui doivent être remboursés 100 signifie que tout est donné comme des subventions qui ne portent aucun intérêt et ne doivent pas être remboursées. Notez que cela n'a qu'un effet si LPB n'est pas réglé sur zéro", 
  "0 betyr at all LPB -finansiering gis som lån som må tilbakebetales 100 betyr at alt gis som tilskudd som ikke har noen renter og ikke må tilbakebetales. Merk at dette bare har en effekt hvis LPB ikke er satt til null", 
  "_last_"
]
pol_to_expl_LPB_str = [
  "The percentage of your GDP made available as financing from public bodies (WorldBank IMF off-balance funding) LPB= Lending from Public Bodies",
  "Der Prozentsatz Ihres BIP der als Finanzierung von öffentlichen Stellen (Weltbank IWF ausserbilanzielle Finanzierung Sondervermögen) zur Verfügung gestellt wird. LPB = Kreditvergabe von öffentlichen Stellen (lending from public bodies)",
  "Der Prozentsatz Ihres BIP der als Finanzierung von öffentlichen Stellen (Weltbank IWF ausserbilanzielle Finanzierung Sondervermögen) zur Verfügung gestellt wird. LPB = Kreditvergabe von öffentlichen Stellen (lending from public bodies)",
  "Le pourcentage de votre PIB mis à disposition en tant que financement auprès d'organismes publics (financement de la déséquilibre du FMI mondial)) LPB = prêts à partir d'organismes publics", 
  "Prosentandelen av BNP gjort tilgjengelig som finansiering fra offentlige organer (WorldBank IMF-finansiering utenfor balansen) LPB = utlån fra offentlige organer", 
  "_last_"
]
pol_to_expl_SSGDR_str = [
  "You can stretch repayment into the future so that each year you pay less but you do have to pay for a longer time. 1 means no stretching - 2 doubles repayment time - 3 trebles repayment time - and so on",
  "Sie können die Rückzahlung in die Zukunft strecken so dass Sie jedes Jahr weniger zahlen aber die Rückzahlungsdauer länger wird. 1 bedeutet keine Streckung - 2 verdoppelt die Rückzahlungsdauer - 3 verdreifacht die Rückzahlungsdauer - und so weiter",
  "Sie können die Rückzahlung in die Zukunft strecken so dass Sie jedes Jahr weniger zahlen aber die Rückzahlungsdauer länger wird. 1 bedeutet keine Streckung - 2 verdoppelt die Rückzahlungsdauer - 3 verdreifacht die Rückzahlungsdauer - und so weiter",
  "Vous pouvez étendre le remboursement dans le futur afin que chaque année, vous payez moins, mais vous devez payer plus longtemps. 1 signifie pas d'étirement - 2 du temps de remboursement en double - 3 temps de remboursement des aibles - et ainsi de suite", 
  "Du kan strekke tilbakebetaling inn i fremtiden slik at du hvert år betaler mindre, men du må betale i lengre tid. 1 betyr ingen strekk - 2 dobler tilbakebetalingstid - 3 Trebles tilbakebetalingstid - og så videre", 
  "_last_"
]
pol_to_expl_ISPV_str = [
  "Percent of electricity generation from renewable sources (40% is what we managed to achieve in the past)",
  "Anteil der Stromerzeugung aus erneuerbaren Energien (40 % haben wir in der Vergangenheit erreicht)",
  "Anteil der Stromerzeugung aus erneuerbaren Energien (40 % haben wir in der Vergangenheit erreicht)",
  "Pourcentage de la production d'électricité à partir de sources renouvelables (40% est ce que nous avons réussi à réaliser dans le passé)", 
  "Prosent av elektrisitetsproduksjon fra fornybare kilder (40% er det vi klarte å oppnå tidligere)", 
  "_last_"
]
pol_to_name_CCS_str = [
  "CCS is Carbon capture and storage at source",
  "CCS ist die CO2-Abscheidung und -Speicherung an der Quelle",
  "CCS ist die CO2-Abscheidung und -Speicherung an der Quelle",
  "CCS est la capture et le stockage du carbone à la source", 
  "CCS er karbonfangst og lagring ved kilden", 
  "_last_"
]
pol_to_name_TOW_str = [
  "Taxing Owners Wealth",
  "Besteuerung des Vermögens von Superreichen",
  "Besteuerung des Vermögens von Superreichen",
  "Taxer la richesse des propriétaires", 
  "Skattlegging av de superrikes formue", 
  "_last_"
]
pol_to_name_FPGDC_str = [
  "Cancel debt from public lenders",
  "Schuldenerlass von öffentlichen Kreditgebern",
  "Schuldenerlass von öffentlichen Kreditgebern",
  "Annulation de la dette des prêteurs publics", 
  "Ettergivelse av gjeld fra offentlige långivere", 
  "_last_"
]
pol_to_name_RMDR_str = [
  "Change diets",
  "Ernährung umstellen",
  "Ernährung umstellen",
  "Changer de régime alimentaire", 
  "Endre dietter", 
  "_last_"
]
pol_to_name_REFOREST_str = [
  "Reforestation",
  "Wiederaufforstung",
  "Wiederaufforstung",
  "Reboisement", 
  "Gjenplanting av skog", 
  "_last_"
]
pol_to_name_FTPEE_str = [
  "Energy system efficiency",
  "Energieeffizienz des Energiesystems",
  "Energieeffizienz des Energiesystems",
  "Efficacité du système énergétique", 
  "Effektivitet i energisystemet", 
  "_last_"
]
pol_to_name_LPBsplit_str = [
  "Breakdown of the use of funds by public-sector lenders (LPB)",
  "Aufteilung der Mittelverwendung öffentlicher Kreditgeber (LPB)",
  "Aufteilung der Mittelverwendung öffentlicher Kreditgeber (LPB)",
  "Répartition de l'utilisation des fonds des prêteurs publics (LPB)", 
  "Fordeling av offentlige långiveres bruk av midler (LPB)", 
  "_last_"
]
pol_to_name_ExPS_str = [
  "Expand policy space",
  "Den politischen Handlungsspielraum erweitern",
  "Den politischen Handlungsspielraum erweitern",
  "Élargir l'espace politique", 
  "Utvid politikkrommet", 
  "_last_"
]
pol_to_name_FMPLDD_str = [
  "Fraction of credit with private lenders NOT drawn down per y",
  "Anteil der Kredite bei privaten Kreditgebern die pro Jahr NICHT in Anspruch genommen werden",
  "Anteil der Kredite bei privaten Kreditgebern die pro Jahr NICHT in Anspruch genommen werden",
  "Fraction du crédit avec des prêteurs privés non abaissés par année", 
  "Brøkdel av kreditt med private långivere som ikke er trukket ned per år", 
  "_last_"
]
pol_to_name_StrUP_str = [
  "Strengthen Unions",
  "Gewerkschaften stärken",
  "Gewerkschaften stärken",
  "Renforcez les syndicats", 
  "Styrke fagforeninger", 
  "_last_"
]
pol_to_name_Wreaction_str = [
  "Worker reaction",
  "Verhandlungsmacht der Arbeitnehmer",
  "Verhandlungsmacht der Arbeitnehmer",
  "Réaction des travailleurs", 
  "Arbeiderreaksjon", 
  "_last_"
]
pol_to_name_SGMP_str = [
  "Pensions to all",
  "Renten für alle",
  "Renten für alle",
  "Pensions à tous", 
  "Pensjoner til alle", 
  "_last_"
]
pol_to_name_FWRP_str = [
  "Food waste reduction",
  "Reduzierung von Lebensmittelabfällen",
  "Reduzierung von Lebensmittelabfällen",
  "Réduction des déchets alimentaires", 
  "Reduksjon av matavfall", 
  "_last_"
]
pol_to_name_ICTR_str = [
  "Increase consumption tax rate",
  "Erhöhung der Mehrwertsteuer",
  "Erhöhung der Mehrwertsteuer",
  "Augmenter le taux d'imposition de la consommation", 
  "Øk forbruksskattesatsen", 
  "_last_"
]
pol_to_name_XtaxCom_str = [
  "Introduce a Universal basic dividend",
  "Einführung eines allgemeinen Grundeinkommen",
  "Einführung eines allgemeinen Grundeinkommen",
  "Introduction d'un revenu de base universel", 
  "Innføring av en universell grunninntekt", 
  "_last_"
]
pol_to_name_Lfrac_str = [
  "Leakage fraction reduction",
  "Reduzierung des Versickern von Geldern in illegale Kanäle",
  "Reduzierung des Versickern von Geldern in illegale Kanäle",
  "Réduction de la fraction de fuite", 
  "Lekkasjefraksjonsreduksjon", 
  "_last_"
]
pol_to_name_IOITR_str = [
  "Increase owner income tax rate",
  "Erhöhung des Einkommensteuersatzes für Eigentümer",
  "Erhöhung des Einkommensteuersatzes für Eigentümer",
  "Augmenter le taux d'imposition des propriétaires", 
  "Øk eierinntektsskattesatsen", 
  "_last_"
]
pol_to_name_IWITR_str = [
  "Increase worker income tax rate",
  "Erhöhung des Einkommensteuersatzes für Arbeitnehmer",
  "Erhöhung des Einkommensteuersatzes für Arbeitnehmer",
  "Augmenter le taux d'imposition des travailleurs", 
  "Øk arbeidstakerens inntektsskattesats", 
  "_last_"
]
pol_to_name_SGRPI_str = [
  "Shift govt spending to investment",
  "Staatliche Ausgaben auf Investitionen umstellen",
  "Staatliche Ausgaben auf Investitionen umstellen",
  "Déplacer les dépenses du gouvernement vers l'investissement", 
  "Omlegging av offentlige utgifter til investeringer", 
  "_last_"
]
pol_to_name_FEHC_str = [
  "Education to all",
  "Bildung für alle",
  "Bildung für alle",
  "Éducation à tous", 
  "Utdanning til alle", 
  "_last_"
]
pol_to_name_XtaxRateEmp_str = [
  "Female leadership",
  "Förderung weiblicher Führungskräfte",
  "Förderung weiblicher Führungskräfte",
  "Promotion des femmes cadres", 
  "Mer kvinnelig ledelse", 
  "_last_"
]
pol_to_name_FLWR_str = [
  "Regenerative agriculture",
  "Regenerative Landwirtschaft",
  "Regenerative Landwirtschaft",
  "Agriculture régénérative", 
  "Regenerativt jordbruk", 
  "_last_"
]
pol_to_name_RIPLGF_str = [
  "Reduce food imports",
  "Lebensmittelimporte reduzieren",
  "Lebensmittelimporte reduzieren",
  "Réduire les importations de nourriture", 
  "Reduser matimport", 
  "_last_"
]
pol_to_name_FC_str = [
  "Max forest cutting",
  "Max Waldrodung",
  "Max Waldrodung",
  "Coute maximale de la forêt", 
  "Max skogskjæring", 
  "_last_"
]
pol_to_name_NEP_str = [
  "Electrify everything",
  "Alles elektrifizieren",
  "Alles elektrifizieren",
  "Électrifier tout", 
  "Elektrifiser alt", 
  "_last_"
]
pol_to_name_Ctax_str = [
  "Introduce a Carbon tax",
  "Eine CO2-Steuer einführen",
  "Eine CO2-Steuer einführen",
  "Introduire une taxe sur le carbone", 
  "Innføre en karbonavgift", 
  "_last_"
]
pol_to_name_DAC_str = [
  "Direct air capture of CO2",
  "Rückgewinnung von CO2 aus der Luft",
  "Rückgewinnung von CO2 aus der Luft",
  "Récupération du CO2 de l'air", 
  "Gjenvinning av CO2 fra luften", 
  "_last_"
]
pol_to_name_XtaxFrac_str = [
  "Extra taxes paid by the super rich",
  "Zusätzliche Steuern die von den Superreichen gezahlt werden",
  "Zusätzliche Steuern die von den Superreichen gezahlt werden",
  "Taxes supplémentaires payées par les super riches", 
  "Ekstra skatter betalt av de superrike", 
  "_last_"
]
pol_to_name_LPBgrant_str = [
  "LPB funding is given as loans or grants",
  "LPB Mittel die als Darlehen oder Zuschüsse gewährt werden",
  "LPB Mittel die als Darlehen oder Zuschüsse gewährt werden",
  "Le financement LPB est accordé comme prêts ou subventions", 
  "LPB -finansiering gis som lån eller tilskudd", 
  "_last_"
]
pol_to_name_LPB_str = [
  "Lending from public bodies (LPB)",
  "Finanzierungen von öffentlichen Geldgebern (LPB)",
  "Finanzierungen von öffentlichen Geldgebern (LPB)",
  "Lending from Public Organes (LPB)", 
  "Utlån fra offentlige organer (LPB)", 
  "_last_"
]
pol_to_name_SSGDR_str = [
  "Stretch repayment",
  "Strecken von Rückzahlung",
  "Strecken von Rückzahlung",
  "Étirements de remboursement", 
  "Strekk i tilbakebetalingen", 
  "_last_"
]
pol_to_name_ISPV_str = [
  "Invest in Renewables",
  "In erneuerbare Energien investieren",
  "In erneuerbare Energien investieren",
  "Investir dans les énergies renouvelables", 
  "Invester i fornybar energi", 
  "_last_"
]
sdgvarID_to_subtitle_13_str = [
  "Worker disposable income (1000 $/person-year)",
  "Verfügbares Einkommen der Arbeitnehmer (1000 $/Personen-jahr)",
  "Verfügbares Einkommen der Arbeitnehmer (1000 $/Personen-jahr)",
  "Revenu disponible des travailleurs (1000 $/personne-année)", 
  "Arbeiderens disponible inntekt (1000 $/person-år)", 
  "_last_"
]
sdgvarID_to_subtitle_18_str = [
  "Fertilizer use per capita (Mt/y)",
  "Düngemittelverbrauch pro Kopf (Mt/Jahr)",
  "Düngemittelverbrauch pro Kopf (Mt/Jahr)",
  "Utilisation des engrais par habitant (Mt/anné)", 
  "Gjødselbruk per innbygger (mt/år)", 
  "_last_"
]
sdgvarID_to_subtitle_26_str = [
  "Population (million people)",
  "Bevölkerung (Millionen Menschen)",
  "Bevölkerung (Millionen Menschen)",
  "Population (millions de personnes)", 
  "Befolkning (millioner mennesker)", 
  "_last_"
]
sdgvarID_to_subtitle_19_str = [
  "Temperature rise (deg C above 1850)",
  "Temperaturanstieg (°C im Vergleich zu 1850)",
  "Temperaturanstieg (°C im Vergleich zu 1850)",
  "Élévation de la température (Deg C au-dessus de 1850)", 
  "Temperaturstigning (deg C over 1850)", 
  "_last_"
]
sdgvarID_to_subtitle_20_str = [
  "Total greenhouse gas emissions per year (GtCO2/yr)",
  "Gesamt-Treibhausgasemissionen pro Jahr (GtCO2/Jahr)",
  "Gesamt-Treibhausgasemissionen pro Jahr (GtCO2/Jahr)",
  "Émissions totales de gaz à effet de serre par an (GTCO2 / an)", 
  "Total klimagassutslipp per år (GTCO2/år)", 
  "_last_"
]
sdgvarID_to_subtitle_29_str = [
  "Number of SDGs, met 17 can be met",
  "Anzahl der erreichten SDGs, 17 können maximal erreicht werden",
  "Anzahl der erreichten SDGs, 17 können maximal erreicht werden",
  "Le nombre de ODD rencontrés, 17 peut être satisfait", 
  "Antall SDG-er møtt, 17 kan oppfylles", 
  "_last_"
]
sdgvarID_to_subtitle_4_str = [
  "Average wellbeing index",
  "Durchschnittlicher Wohlbefinden-index",
  "Durchschnittlicher Wohlbefinden-index",
  "Indice de bien-être moyen", 
  "Gjennomsnittlig velværeindeks", 
  "_last_"
]
sdgvarID_to_subtitle_24_str = [
  "Trust in institutions (1980=1)",
  "Vertrauen in Institutionen (1980=1)",
  "Vertrauen in Institutionen (1980=1)",
  "Trust in Institutions (1980 = 1)", 
  "Tillit til institusjoner (1980 = 1)", 
  "_last_"
]
sdgvarID_to_subtitle_31_str = [
  "Annual rate of change in city area (%)",
  "Jährliche Veränderungsrate der versiegelten Fläche (%)",
  "Jährliche Veränderungsrate der versiegelten Fläche (%)",
  "Taux annuel de variation de la région de la ville (%)", 
  "Årlig endringshastighet i byområdet (%)", 
  "_last_"
]
sdgvarID_to_subtitle_33_str = [
  "Annual change in forest area (%)",
  "Jährliche Veränderung der Waldfläche (%)",
  "Jährliche Veränderung der Waldfläche (%)",
  "Changement annuel de la zone forestière (%)", 
  "Årlig endring i skogsområdet (%)", 
  "_last_"
]
sdgvarID_to_subtitle_35_str = [
  "Planetary boundaries breached",
  "Planetarische Grenzen überschritten",
  "Planetarische Grenzen überschritten",
  "Les limites planétaires violées", 
  "Planetariske grenser brutt", 
  "_last_"
]
sdgvarID_to_subtitle_30_str = [
  "Private and govt investment share (% of GDP)",
  "Anteil privater und staatlicher Investitionen (% des BIP)",
  "Anteil privater und staatlicher Investitionen (% des BIP)",
  "Part d'investissement privé et gouvernemental (% du PIB)", 
  "Andel private og offentlige investeringer (% av BNP)", 
  "_last_"
]
sdgvarID_to_subtitle_9_str = [
  "Percent of population with access to safe sanitation (%)",
  "Prozent der Bevölkerung mit Zugang zu sicheren Sanitäreinrichtungen (%)",
  "Prozent der Bevölkerung mit Zugang zu sicheren Sanitäreinrichtungen (%)",
  "Pourcentage de la population ayant accès à un assainissement sûr (%)", 
  "Prosent av befolkningen med tilgang til sikker sanitet (%)", 
  "_last_"
]
sdgvarID_to_subtitle_16_str = [
  "Growth rate of GDP per capita (%/yr)",
  "Wachstumsrate des BIP pro Kopf (%/Jahr)",
  "Wachstumsrate des BIP pro Kopf (%/Jahr)",
  "Taux de croissance du PIB par habitant (% / an)", 
  "Veksthastigheten av BNP per innbygger (%/år)", 
  "_last_"
]
sdgvarID_to_subtitle_17_str = [
  "Emissions per person (tCO2/p/y)",
  "Emissionen pro Person (tCO2/p/J)",
  "Emissionen pro Person (tCO2/p/J)",
  "Émissions par personne (tCO2/P/A)", 
  "Utslipp per person (tCO2/P/år)", 
  "_last_"
]
sdgvarID_to_subtitle_34_str = [
  "Donor and off balance-sheet investment share (% of GDP)",
  "Anteil der Geber und ausserbilanziellen Investitionen (% des BIP)",
  "Anteil der Geber und ausserbilanziellen Investitionen (% des BIP)",
  "Part des donateurs et des investissements hors bilan (% du PIB)", 
  "Andel av donor- og ikke-balanseførte investeringer (% av BNP)", 
  "_last_"
]
sdgvarID_to_subtitle_14_str = [
  "Million unemployed",
  "Millionen Arbeitslose",
  "Millionen Arbeitslose",
  "Millions de chômeurs", 
  "Millioner arbeidsledige", 
  "_last_"
]
sdgvarID_to_subtitle_21_str = [
  "Ocean surface pH",
  "pH-Wert der Meeresoberfläche",
  "pH-Wert der Meeresoberfläche",
  "pH de la surface de la mer", 
  "pH-verdien på havoverflaten", 
  "_last_"
]
sdgvarID_to_subtitle_12_str = [
  "Energy intensity in terms of primary energy and GDP (kWh/$)",
  "Energieintensität in Bezug auf Primärenergie und BIP (kWh/$)",
  "Energieintensität in Bezug auf Primärenergie und BIP (kWh/$)",
  "Intensité énergétique en termes d'énergie primaire et de PIB (kwh/$)", 
  "Energiintensitet når det gjelder primær energi og BNP (kWh/$)", 
  "_last_"
]
sdgvarID_to_subtitle_22_str = [
  "Extent of tropical forest globally (Mha)",
  "Ausdehnung des tropischen Waldes weltweit (Mha)",
  "Ausdehnung des tropischen Waldes weltweit (Mha)",
  "Étendue de la forêt tropicale dans le monde (MHA)", 
  "Omfang av tropisk skog globalt (MHA)", 
  "_last_"
]
sdgvarID_to_subtitle_23_str = [
  "Public services per person (1000 $/person-yr)",
  "Öffentliche Dienstleistungen pro Person (1000 $/Person-Jahr)",
  "Öffentliche Dienstleistungen pro Person (1000 $/Person-Jahr)",
  "Services publics par personne (1000 $ / personne-an)", 
  "Offentlige tjenester per person (1000 $/person-år)", 
  "_last_"
]
sdgvarID_to_subtitle_2_str = [
  "Million people undernourished (Mp)",
  "Millionen unterernährte Menschen (Mp)",
  "Millionen unterernährte Menschen (Mp)",
  "Million de personnes sous-alimentées (MP)", 
  "Millioner mennesker underernært (MP)", 
  "_last_"
]
sdgvarID_to_subtitle_5_str = [
  "Life expectancy (years)",
  "Lebenserwartung (Jahre)",
  "Lebenserwartung (Jahre)",
  "Espérance de vie (années)", 
  "Forventet levealder (år)", 
  "_last_"
]
sdgvarID_to_subtitle_7_str = [
  "Female pre-tax labor income share (%)",
  "Anteil weiblicher Erwerbseinkommen vor Steuern (%)",
  "Anteil weiblicher Erwerbseinkommen vor Steuern (%)",
  "Part des revenus de travail avant impôt (%)", 
  "Kvinnelig arbeidsinntektsinntekt (%)", 
  "_last_"
]
sdgvarID_to_subtitle_1_str = [
  "Million people living in poverty (Mp)",
  "Millionen Menschen die in Armut leben (Mp)",
  "Millionen Menschen die in Armut leben (Mp)",
  "Million de personnes vivant dans la pauvreté (MP)", 
  "Millioner mennesker som lever i fattigdom (MP)", 
  "_last_"
]
sdgvarID_to_subtitle_3_str = [
  "Million hectars worked regeneratively",
  "Millionen Hektar regenerativ bewirtschaftet",
  "Millionen Hektar regenerativ bewirtschaftet",
  "Million Hectars a travaillé régénératif", 
  "Million hektarer fungerte regenerativt", 
  "_last_"
]
sdgvarID_to_subtitle_6_str = [
  "Years in school",
  "Schuljahre",
  "Schuljahre",
  "Années à l'école", 
  "År på skolen", 
  "_last_"
]
sdgvarID_to_subtitle_8_str = [
  "Percent of population with access to safe water (%)",
  "Prozent der Bevölkerung mit Zugang zu sauberem Wasser (%)",
  "Prozent der Bevölkerung mit Zugang zu sauberem Wasser (%)",
  "Pourcentage de population ayant accès à l'eau sûre (%)", 
  "Prosent av befolkningen med tilgang til trygt vann (%)", 
  "_last_"
]
sdgvarID_to_subtitle_10_str = [
  "Million people with no access to electricity (Mp)",
  "Millionen Menschen ohne Zugang zu Elektrizität (Mp)",
  "Millionen Menschen ohne Zugang zu Elektrizität (Mp)",
  "Million de personnes sans accès à l'électricité (MP)", 
  "Millioner mennesker uten tilgang til strøm (MP)", 
  "_last_"
]
sdgvarID_to_subtitle_15_str = [
  "Carbon intensity of production (kgCO2/$)",
  "Kohlenstoffintensität der Produktion (kgCO2/$)",
  "Kohlenstoffintensität der Produktion (kgCO2/$)",
  "Intensité du carbone de la production (KGCO2/$)", 
  "Karbonintensitet i produksjonen (KGCO2/$)", 
  "_last_"
]
sdgvarID_to_subtitle_25_str = [
  "Total government revenue as a proportion of GDP (%)",
  "Gesamteinnahmen des Staates als Anteil des BIP (%)",
  "Gesamteinnahmen des Staates als Anteil des BIP (%)",
  "Le chiffre d'affaires total du gouvernement en proportion du PIB (%)", 
  "Total statlige inntekter som en andel av BNP (%)", 
  "_last_"
]
sdgvarID_to_subtitle_27_str = [
  "Labour share of GDP (%)",
  "Arbeitnehmeranteil am BIP (%)",
  "Arbeitnehmeranteil am BIP (%)",
  "Part des travailleurs dans le PIB (%)", 
  "Arbeidstakernes andel av BNP (%)", 
  "_last_"
]
sdgvarID_to_subtitle_28_str = [
  "Wind and PV energy electricity (TWh/yr)",
  "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "Électricité éolienne et énergétique PV (TWH / an)", 
  "Vind og PV Energy Electricity (TWH/YR)", 
  "_last_"
]
sdgvarID_to_subtitle_37_str = [
  "Cropland (Mha)",
  "Ackerland (Mha)",
  "Ackerland (Mha)",
  "Terres cultivées (MHA)", 
  "Cropland (MHA)", 
  "_last_"
]
sdgvarID_to_subtitle_11_str = [
  "Wind and PV energy electricity (TWh/yr)",
  "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "Électricité éolienne et énergétique PV (TWH / an)", 
  "Vind og PV Energy Electricity (TWH/YR)", 
  "_last_"
]
sdgvarID_to_subtitle_36_str = [
  "GDP (G2017ppp$/yr)",
  "BIP (G2017ppp$/Jahr)",
  "BIP (G2017ppp$/Jahr)",
  "PIB (G2017PPP $ / an)", 
  "BNP (G2017PPP $/YR)", 
  "_last_"
]
sdgvarID_to_subtitle_32_str = [
  "Nitrogen use (kg/ha-year)",
  "Stickstoffverbrauch (kg/ha-Jahr)",
  "Stickstoffverbrauch (kg/ha-Jahr)",
  "Utilisation de l'azote (kg / ha-an)", 
  "Nitrogenbruk (kg/ha-år)", 
  "_last_"
]
sdgvarID_to_subtitle_39_str = [
  "nan",
  "nan",
  "nan",
  "Nan", 
  "Nan", 
  "_last_"
]
sdgvarID_to_subtitle_38_str = [
  "nan",
  "nan",
  "nan",
  "Nan", 
  "Nan", 
  "_last_"
]
sdgvarID_to_indicator_13_str = [
  "Worker disposable income (1000 USD per person and year)",
  "Verfügbares Einkommen der Arbeitnehmer (1000 USD pro Person pro Jahr)",
  "Verfügbares Einkommen der Arbeitnehmer (1000 USD pro Person pro Jahr)",
  "Revenu disponible des travailleurs (1000 USD par personne et par an)", 
  "Arbeiderens disponible inntekt (1000 USD per person per år)", 
  "_last_"
]
sdgvarID_to_indicator_18_str = [
  "Fertilizer use per capita (Mt/y)",
  "Düngemittelverbrauch pro Kopf (Mt/Jahr)",
  "Düngemittelverbrauch pro Kopf (Mt/Jahr)",
  "Utilisation des engrais par habitant (MT / Y)", 
  "Gjødselbruk per innbygger (mt/y)", 
  "_last_"
]
sdgvarID_to_indicator_26_str = [
  "Population (million people)",
  "Bevölkerung (Millionen Menschen)",
  "Bevölkerung (Millionen Menschen)",
  "Population (millions de personnes)", 
  "Befolkning (millioner mennesker)", 
  "_last_"
]
sdgvarID_to_indicator_19_str = [
  "Temperature rise (deg C above 1850)",
  "Temperaturanstieg (°C im Vergleich zu 1850)",
  "Temperaturanstieg (°C im Vergleich zu 1850)",
  "Élévation de la température (Deg C au-dessus de 1850)", 
  "Temperaturstigning (deg C over 1850)", 
  "_last_"
]
sdgvarID_to_indicator_20_str = [
  "Total greenhouse gas emissions per year (GtCO2/yr)",
  "Gesamt-Treibhausgasemissionen pro Jahr (GtCO2/Jahr)",
  "Gesamt-Treibhausgasemissionen pro Jahr (GtCO2/Jahr)",
  "Émissions totales de gaz à effet de serre par an (GTCO2 / an)", 
  "Total klimagassutslipp per år (GTCO2/år)", 
  "_last_"
]
sdgvarID_to_indicator_29_str = [
  "Number of SDGs met, 17 is the most you can meet",
  "Anzahl der erreichten SDGs, 17 können maximal erreicht werden",
  "Anzahl der erreichten SDGs, 17 können maximal erreicht werden",
  "Nombre d'ODD atteints, 17 est le maximum que vous pouvez atteindre.", 
  "Antall oppnådde SDG-mål, 17 er det høyeste du kan nå", 
  "_last_"
]
sdgvarID_to_indicator_4_str = [
  "Average wellbeing index",
  "Durchschnittlicher Wohlbefinden-index",
  "Durchschnittlicher Wohlbefinden-index",
  "Indice de bien-être moyen", 
  "Gjennomsnittlig velværeindeks", 
  "_last_"
]
sdgvarID_to_indicator_24_str = [
  "Trust in institutions (1980=1)",
  "Vertrauen in Institutionen (1980=1)",
  "Vertrauen in Institutionen (1980=1)",
  "Confiance dans les institutions (1980=1))", 
  "Tillit til institusjoner (1980 = 1)", 
  "_last_"
]
sdgvarID_to_indicator_31_str = [
  "Annual rate of change in city area (%)",
  "Jährliche Veränderungsrate der Stadtfläche (%)",
  "Jährliche Veränderungsrate der Stadtfläche (%)",
  "Taux de variation annuel de la superficie urbaine (%)", 
  "Årlig endringshastighet i byområdet (%)", 
  "_last_"
]
sdgvarID_to_indicator_33_str = [
  "Annual change in forest area (%)",
  "Jährliche Veränderung der Waldfläche (%)",
  "Jährliche Veränderung der Waldfläche (%)",
  "Variation annuelle de la superficie forestière (%)", 
  "Årlig endring i skogsområdet (%)", 
  "_last_"
]
sdgvarID_to_indicator_35_str = [
  "Planetary boundaries breached",
  "Planetarische Grenzen überschritten",
  "Planetarische Grenzen überschritten",
  "Les limites planétaires violées", 
  "Planetariske grenser brutt", 
  "_last_"
]
sdgvarID_to_indicator_30_str = [
  "Private and govt investment share (% of GDP)",
  "Anteil privater und staatlicher Investitionen (% des BIP)",
  "Anteil privater und staatlicher Investitionen (% des BIP)",
  "Part d'investissement privé et gouvernemental (% du PIB)", 
  "Privat og Govt investeringsandel (% av BNP)", 
  "_last_"
]
sdgvarID_to_indicator_9_str = [
  "Fraction of population with access to safe sanitation (%)",
  "Anteil der Bevölkerung mit Zugang zu sicheren Sanitäreinrichtungen (%)",
  "Anteil der Bevölkerung mit Zugang zu sicheren Sanitäreinrichtungen (%)",
  "Proportion de la population ayant accès à des installations sanitaires sûres (%)", 
  "Andel av befolkningen med tilgang til sikre sanitæranlegg (%)", 
  "_last_"
]
sdgvarID_to_indicator_16_str = [
  "Growth rate of GDP per capita (%/yr)",
  "Wachstumsrate des BIP pro Kopf (%/Jahr)",
  "Wachstumsrate des BIP pro Kopf (%/Jahr)",
  "Taux de croissance du PIB par habitant (% / an)", 
  "Veksthastigheten av BNP per innbygger (%/år)", 
  "_last_"
]
sdgvarID_to_indicator_17_str = [
  "Emissions per person (tCO2 per person and year)",
  "Emissionen pro Person (tCO2 pro Person pro Jahr)",
  "Emissionen pro Person (tCO2 pro Person pro Jahr)",
  "Émissions par personne (tCO2 par personne et par an)", 
  "Utslipp per person (tCO2 per person per år)", 
  "_last_"
]
sdgvarID_to_indicator_34_str = [
  "Donor and off balance-sheet investment share (% of GDP)",
  "Anteil an Investitionen der von Krediten und ausser-bilanziellen Sondervermögen kommt (% des BIP)",
  "Anteil an Investitionen der von Krediten und ausser-bilanziellen Sondervermögen kommt (% des BIP)",
  "Part des investissements provenant de crédits et de fonds spéciaux hors bilan (% du PIB)", 
  "Andel av investeringer fra lån og spesielle eiendeler utenfor balansen (% av BNP)", 
  "_last_"
]
sdgvarID_to_indicator_14_str = [
  "Unemployment rate (%)",
  "Arbeitslosenquote (%)",
  "Arbeitslosenquote (%)",
  "Taux de chômage (%)", 
  "Arbeidsledighet (%)", 
  "_last_"
]
sdgvarID_to_indicator_21_str = [
  "Ocean surface pH",
  "pH-Wert der Meeresoberfläche",
  "pH-Wert der Meeresoberfläche",
  "PH de la surface de l'océan", 
  "Ocean Surface Ph", 
  "_last_"
]
sdgvarID_to_indicator_12_str = [
  "Energy intensity in terms of primary energy and GDP (kWh/$)",
  "Energieintensität in Bezug auf Primärenergie und BIP (kWh/$)",
  "Energieintensität in Bezug auf Primärenergie und BIP (kWh/$)",
  "Intensité énergétique en termes d'énergie primaire et de PIB (kwh / $)", 
  "Energiintensitet når det gjelder primær energi og BNP (kWh/$)", 
  "_last_"
]
sdgvarID_to_indicator_22_str = [
  "Extent of tropical forest globally (Mha)",
  "Ausdehnung des tropischen Waldes weltweit (Mha)",
  "Ausdehnung des tropischen Waldes weltweit (Mha)",
  "Étendue de la forêt tropicale dans le monde (MHA)", 
  "Omfang av tropisk skog globalt (MHA)", 
  "_last_"
]
sdgvarID_to_indicator_23_str = [
  "Public services per person (1000 $/person-yr)",
  "Öffentliche Dienstleistungen pro Person (1000 $/Person-Jahr)",
  "Öffentliche Dienstleistungen pro Person (1000 $/Person-Jahr)",
  "Services publics par personne (1000 $ / personne-an)", 
  "Offentlige tjenester per person (1000 $/person-år)", 
  "_last_"
]
sdgvarID_to_indicator_2_str = [
  "Fraction of population undernourished (%)",
  "Anteil der unterernährten Bevölkerung (%)",
  "Anteil der unterernährten Bevölkerung (%)",
  "Fraction de la population sous-alimentée (%)", 
  "Brøkdel av befolkningen underernær (%)", 
  "_last_"
]
sdgvarID_to_indicator_5_str = [
  "Life expectancy (years)",
  "Lebenserwartung (Jahre)",
  "Lebenserwartung (Jahre)",
  "Espérance de vie (années)", 
  "Forventet levealder (år)", 
  "_last_"
]
sdgvarID_to_indicator_7_str = [
  "Female pre-tax labor income share (%)",
  "Anteil der weiblichen Erwerbseinkommen vor Steuern (%)",
  "Anteil der weiblichen Erwerbseinkommen vor Steuern (%)",
  "Part des revenus de travail avant impôt (%)", 
  "Kvinnelig arbeidsinntektsinntekt (%)", 
  "_last_"
]
sdgvarID_to_indicator_1_str = [
  "Fraction of population living below $6.85 per day (%)",
  "Anteil der Bevölkerung der weniger als 6,85 US-Dollar pro Tag verdient (%)",
  "Anteil der Bevölkerung der weniger als 6,85 US-Dollar pro Tag verdient (%)",
  "Pourcentage de la population gagnant moins de 6,85 dollars par jour (%)", 
  "Andel av befolkningen som tjener mindre enn 6,85 dollar per dag (%)", 
  "_last_"
]
sdgvarID_to_indicator_3_str = [
  "Proportion of agricultural area worked regeneratively (%)",
  "Anteil der regenerativ bewirtschafteten landwirtschaftlichen Fläche (%)",
  "Anteil der regenerativ bewirtschafteten landwirtschaftlichen Fläche (%)",
  "Part des surfaces agricoles exploitées selon les principes de l'agriculture régénérative (%)", 
  "Andel av landbruksarealet som drives på en bærekraftig måte (%)", 
  "_last_"
]
sdgvarID_to_indicator_6_str = [
  "Years in school",
  "Schuljahre",
  "Schuljahre",
  "Années à l'école", 
  "År på skolen", 
  "_last_"
]
sdgvarID_to_indicator_8_str = [
  "Fraction of population with access to safe water (%)",
  "Anteil der Bevölkerung mit Zugang zu sauberem Wasser (%)",
  "Anteil der Bevölkerung mit Zugang zu sauberem Wasser (%)",
  "Pourcentage de la population ayant accès à l'eau potable (%)", 
  "Andel av befolkningen med tilgang til rent vann (%)", 
  "_last_"
]
sdgvarID_to_indicator_10_str = [
  "Fraction of population with access to electricity (%)",
  "Anteil der Bevölkerung mit Zugang zu Elektrizität (%)",
  "Anteil der Bevölkerung mit Zugang zu Elektrizität (%)",
  "Pourcentage de la population ayant accès à l'électricité (%)", 
  "Andel av befolkningen med tilgang til elektrisitet (%)", 
  "_last_"
]
sdgvarID_to_indicator_15_str = [
  "Carbon intensity of production (kgCO2 per USD)",
  "Kohlenstoffintensität der Produktion (kgCO2 pro USD)",
  "Kohlenstoffintensität der Produktion (kgCO2 pro USD)",
  "Intensité du carbone de la production (KGCO2 par USD)", 
  "Karbonintensitet i produksjonen (KGCO2 per USD)", 
  "_last_"
]
sdgvarID_to_indicator_25_str = [
  "Total government revenue as a proportion of GDP (%)",
  "Gesamteinnahmen des Staates als Anteil des BIP (%)",
  "Gesamteinnahmen des Staates als Anteil des BIP (%)",
  "Le chiffre d'affaires total du gouvernement en proportion du PIB (%)", 
  "Total statlige inntekter som en andel av BNP (%)", 
  "_last_"
]
sdgvarID_to_indicator_27_str = [
  "Labour share of GDP (%)",
  "Arbeitnehmeranteil am BIP (%)",
  "Arbeitnehmeranteil am BIP (%)",
  "Part des salariés dans le PIB (%)", 
  "Arbeidstakerandel av BNP (%)", 
  "_last_"
]
sdgvarID_to_indicator_28_str = [
  "Wind and PV energy electricity (TWh/yr)",
  "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "Strom aus Wind- und Photovoltaikenergie (TWh/Jahr)",
  "Électricité produite à partir de l'énergie éolienne et photovoltaïque (TWh/an)", 
  "Strøm fra vind- og solcelleenergi (TWh/år)", 
  "_last_"
]
sdgvarID_to_indicator_37_str = [
  "Cropland (Mha)",
  "Ackerland (Mha)",
  "Ackerland (Mha)",
  "Terres cultivées (MHA)", 
  "Jordbruksareal (Mha)", 
  "_last_"
]
sdgvarID_to_indicator_11_str = [
  "Wind and PV energy share in total energy consumption (%)",
  "Anteil von Wind- und Photovoltaikenergie am Gesamtenergieverbrauch (%)",
  "Anteil von Wind- und Photovoltaikenergie am Gesamtenergieverbrauch (%)",
  "Part de l'énergie éolienne et photovoltaïque dans la consommation totale d'énergie (%)", 
  "Andel vind- og solcelleenergi av det totale energiforbruket (%)", 
  "_last_"
]
sdgvarID_to_indicator_36_str = [
  "GDP (G2017ppp$/yr)",
  "BIP (G2017ppp$/Jahr)",
  "BIP (G2017ppp$/Jahr)",
  "PIB (G2017PPP $ / an)", 
  "BNP (G2017PPP $/YR)", 
  "_last_"
]
sdgvarID_to_indicator_32_str = [
  "Nitrogen use (kg/ha-year)",
  "Stickstoffverbrauch (kg pro ha pro Jahr)",
  "Stickstoffverbrauch (kg pro ha pro Jahr)",
  "Consommation d'azote (kg par ha et par an)", 
  "Nitrogenforbruk (kg per hektar per år)", 
  "_last_"
]
sdgvarID_to_indicator_39_str = [
  "(index)",
  "(Index)",
  "(Index)",
  "(indice)", 
  "(indeks)", 
  "_last_"
]
sdgvarID_to_indicator_38_str = [
  "(index)",
  "(Index)",
  "(Index)",
  "(indice)", 
  "(indeks)", 
  "_last_"
]
sdgvarID_to_sdg_0_str = [
  "Population",
  "Einwohnerzahl",
  "Einwohnerzahl",
  "nombre d'habitants", 
  "Folketall", 
  "_last_"
]
sdgvarID_to_indicator_0_str = [
  "Million People",
  "Millionen Menschen",
  "Millionen Menschen",
  "Millions d'habitants", 
  "Millioner mennesker", 
  "_last_"
]
sdgvarID_to_sdg_13_str = [
  "Decent work and economic growth",
  "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "Travail décent et croissance économique", 
  "Anstendig arbeid og økonomisk vekst", 
  "_last_"
]
sdgvarID_to_sdg_18_str = [
  "Responsible consumption and production",
  "Verantwortungsvoller Konsum und Produktion",
  "Verantwortungsvoller Konsum und Produktion",
  "Consommation et production responsables", 
  "Ansvarlig forbruk og produksjon", 
  "_last_"
]
sdgvarID_to_sdg_26_str = [
  "Total population",
  "Gesamtbevölkerung",
  "Gesamtbevölkerung",
  "Population totale", 
  "Total befolkning", 
  "_last_"
]
sdgvarID_to_sdg_19_str = [
  "Climate action",
  "Massnahmen zum Klimaschutz",
  "Massnahmen zum Klimaschutz",
  "Action climatique", 
  "Klimahandling", 
  "_last_"
]
sdgvarID_to_sdg_20_str = [
  "Climate action",
  "Massnahmen zum Klimaschutz",
  "Massnahmen zum Klimaschutz",
  "Action climatique", 
  "Klimahandling", 
  "_last_"
]
sdgvarID_to_sdg_29_str = [
  "SDG scores",
  "SDG-Ergebnisse",
  "SDG-Ergebnisse",
  "Scores ODD", 
  "SDG -score", 
  "_last_"
]
sdgvarID_to_sdg_4_str = [
  "Good health and wellbeing",
  "Gute Gesundheit und Wohlbefinden",
  "Gute Gesundheit und Wohlbefinden",
  "Bonne santé et bien-être", 
  "God helse og velvære", 
  "_last_"
]
sdgvarID_to_sdg_24_str = [
  "Partnership for the Goals",
  "Partnerschaft zur Erreichung der Ziele",
  "Partnerschaft zur Erreichung der Ziele",
  "Partenariat pour les objectifs", 
  "Partnerskap for målene", 
  "_last_"
]
sdgvarID_to_sdg_31_str = [
  "Sustainable cities and communities",
  "Nachhaltige Städte und Gemeinden",
  "Nachhaltige Städte und Gemeinden",
  "Villes durables et communautés", 
  "Bærekraftige byer og lokalsamfunn", 
  "_last_"
]
sdgvarID_to_sdg_33_str = [
  "Life on land",
  "Leben an Land",
  "Leben an Land",
  "Vie sur terre", 
  "Livet på land", 
  "_last_"
]
sdgvarID_to_sdg_35_str = [
  "Planetary boundaries",
  "Planetarische Grenzen",
  "Planetarische Grenzen",
  "Limites planétaires", 
  "Planetariske grenser", 
  "_last_"
]
sdgvarID_to_sdg_30_str = [
  "Industry, innovation and infrastructure",
  "Industrie, Innovation und Infrastruktur",
  "Industrie, Innovation und Infrastruktur",
  "Industrie, innovation et infrastructures", 
  "Industri, innovasjon og infrastruktur", 
  "_last_"
]
sdgvarID_to_sdg_9_str = [
  "Access to clean sanitation",
  "Zugang zu sauberen Sanitäranlagen",
  "Zugang zu sauberen Sanitäranlagen",
  "Accès à l'assainissement propre", 
  "Tilgang til ren sanitet", 
  "_last_"
]
sdgvarID_to_sdg_16_str = [
  "Decent work and economic growth",
  "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "Travail décent et croissance économique", 
  "Anstendig arbeid og økonomisk vekst", 
  "_last_"
]
sdgvarID_to_sdg_17_str = [
  "Sustainable cities and communities",
  "Nachhaltige Städte und Gemeinden",
  "Nachhaltige Städte und Gemeinden",
  "Villes durables et communautés", 
  "Bærekraftige byer og lokalsamfunn", 
  "_last_"
]
sdgvarID_to_sdg_34_str = [
  "Industry, innovation and infrastructure",
  "Industrie, Innovation und Infrastruktur",
  "Industrie, Innovation und Infrastruktur",
  "Industrie, innovation et infrastructures", 
  "Industri, innovasjon og infrastruktur", 
  "_last_"
]
sdgvarID_to_sdg_14_str = [
  "Decent work and economic growth",
  "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "Menschenwürdige Arbeit und Wirtschaftswachstum",
  "Travail décent et croissance économique", 
  "Anstendig arbeid og økonomisk vekst", 
  "_last_"
]
sdgvarID_to_sdg_21_str = [
  "Life below water",
  "Leben unter Wasser",
  "Leben unter Wasser",
  "Vie sous l'eau", 
  "Livet under vann", 
  "_last_"
]
sdgvarID_to_sdg_12_str = [
  "Affordable and clean energy",
  "Bezahlbare und saubere Energie",
  "Bezahlbare und saubere Energie",
  "Énergie abordable et propre", 
  "Rimelig og ren energi", 
  "_last_"
]
sdgvarID_to_sdg_22_str = [
  "Life on land",
  "Leben an Land",
  "Leben an Land",
  "Vie sur terre", 
  "Livet på land", 
  "_last_"
]
sdgvarID_to_sdg_23_str = [
  "Peace, justice and strong institutions",
  "Frieden, Gerechtigkeit und starke Institutionen",
  "Frieden, Gerechtigkeit und starke Institutionen",
  "Paix, Justice et institutions fortes", 
  "Fred, rettferdighet og sterke institusjoner", 
  "_last_"
]
sdgvarID_to_sdg_2_str = [
  "No hunger",
  "Kein Hunger",
  "Kein Hunger",
  "Pas de faim", 
  "Ingen sult", 
  "_last_"
]
sdgvarID_to_sdg_5_str = [
  "Good health and wellbeing",
  "Gute Gesundheit und Wohlbefinden",
  "Gute Gesundheit und Wohlbefinden",
  "Bonne santé et bien-être", 
  "God helse og velvære", 
  "_last_"
]
sdgvarID_to_sdg_7_str = [
  "Gender equality",
  "Gleichstellung der Geschlechter",
  "Gleichstellung der Geschlechter",
  "L'égalité des sexes", 
  "Likestilling", 
  "_last_"
]
sdgvarID_to_sdg_1_str = [
  "No poverty",
  "Keine Armut",
  "Keine Armut",
  "Pas de pauvreté", 
  "Ingen fattigdom", 
  "_last_"
]
sdgvarID_to_sdg_3_str = [
  "No hunger",
  "Kein Hunger",
  "Kein Hunger",
  "Pas de faim", 
  "Ingen sult", 
  "_last_"
]
sdgvarID_to_sdg_6_str = [
  "Quality education",
  "Hochwertige Bildung",
  "Hochwertige Bildung",
  "Education de qualité", 
  "Kvalitetsutdanning", 
  "_last_"
]
sdgvarID_to_sdg_8_str = [
  "Access to clean water",
  "Zugang zu sauberem Wasser",
  "Zugang zu sauberem Wasser",
  "Accès à l'eau propre", 
  "Tilgang til rent vann", 
  "_last_"
]
sdgvarID_to_sdg_10_str = [
  "Affordable and clean energy",
  "Bezahlbare und saubere Energie",
  "Bezahlbare und saubere Energie",
  "Énergie abordable et propre", 
  "Rimelig og ren energi", 
  "_last_"
]
sdgvarID_to_sdg_15_str = [
  "Industry, innovation and infrastructure",
  "Industrie, Innovation und Infrastruktur",
  "Industrie, Innovation und Infrastruktur",
  "Industrie, innovation et infrastructures", 
  "Industri, innovasjon og infrastruktur", 
  "_last_"
]
sdgvarID_to_sdg_25_str = [
  "Partnership for the Goals",
  "Partnerschaft zur Erreichung der Ziele",
  "Partnerschaft zur Erreichung der Ziele",
  "Partenariat pour les objectifs", 
  "Partnerskap for målene", 
  "_last_"
]
sdgvarID_to_sdg_27_str = [
  "Reduced inequalities",
  "Verringerte Ungleichheiten",
  "Verringerte Ungleichheiten",
  "Inégalités réduites", 
  "Reduserte ulikheter", 
  "_last_"
]
sdgvarID_to_sdg_28_str = [
  "Affordable and clean energy",
  "Bezahlbare und saubere Energie",
  "Bezahlbare und saubere Energie",
  "Énergie abordable et propre", 
  "Rimelig og ren energi", 
  "_last_"
]
sdgvarID_to_sdg_37_str = [
  "Cropland",
  "Ackerland",
  "Ackerland",
  "Terres cultivées", 
  "jordbruksland", 
  "_last_"
]
sdgvarID_to_sdg_11_str = [
  "Affordable and clean energy",
  "Bezahlbare und saubere Energie",
  "Bezahlbare und saubere Energie",
  "Énergie abordable et propre", 
  "Rimelig og ren energi", 
  "_last_"
]
sdgvarID_to_sdg_36_str = [
  "GDP",
  "BIP",
  "BIP",
  "PIB", 
  "BNP", 
  "_last_"
]
sdgvarID_to_sdg_32_str = [
  "Responsible consumption and production",
  "Verantwortungsvoller Konsum und Produktion",
  "Verantwortungsvoller Konsum und Produktion",
  "Consommation et production responsables", 
  "Ansvarlig forbruk og produksjon", 
  "_last_"
]
sdgvarID_to_sdg_39_str = [
  "Social tension",
  "Soziale Spannungen",
  "Soziale Spannungen",
  "Tension sociale", 
  "Sosial spenning", 
  "_last_"
]
sdgvarID_to_sdg_38_str = [
  "Social trust",
  "Soziales Vertrauen",
  "Soziales Vertrauen",
  "Confiance sociale", 
  "Sosial tillit", 
  "_last_"
]
top_title_str = [
  "OC Game v0.3c",
  "Das WK Spiel v0.3c",
  "Das WK Spiel v0.3c",
  "Le Jeu OL v0.3c",
  "FL-spill v0.3c", 
  "_last_"
]
need_one_reg = [
  "You need at least one region played by human players.",
  "Sie benötigen mindestens eine Region, die von Menschen gespielt wird.",
  "Du brauchst mindestens eine Region, die von Menschen gespielt wird.",
  "Vous avez besoin d'au moins une région jouée par des joueurs humains.",
  "Du trenger minst én region som spilles av menneskelige spillere.",
    "_last_"
]
need_one_reg_title = [
  "No players?",
  "Keine Spieler:innen?",
  "Keine Spieler:innen?",
  "Pas de joueurs ?",
  "Ingen medspillere?",
  "_last_"
]
top_btn_thanks_str = [
  "Thanks ",
  "Danke ",
  "Danke ",
  "Merci ",
  "Takk", 
  "_last_"
]
top_btn_start_str = [
  "Start a new game as organizer ",
  "Starten Sie ein neues Spiel als Spielleiter:in ",
  "Starten Sie ein neues Spiel als Spielleiter:in ",
  "Démarrez un nouveau jeu en tant qu'organisateur", 
  "Start et nytt spill som arrangør", 
  "_last_"
]
top_btn_join_str = [
  "JOIN a game as player ",
  "Als Spieler:in einem Spiel beitreten ",
  "Als Spieler:in einem Spiel beitreten ",
  "Rejoignez un jeu en tant que joueur", 
  "Bli med på et spill som spiller", 
  "_last_"
]
top_btn_help_str = [
  "Help ",
  "Hilfe ",
  "Hilfe ",
  "Laide ",
  "Hjelp" ,
  "_last_"
]
top_join_game_str = [
  "JOIN a game as player ",
  "Als Spieler:in einem Spiel beitreten ",
  "Als Spieler:in einem Spiel beitreten ",
  "Rejoignez un jeu en tant que joueur", 
  "Bli med på et spill som spiller", 
  "_last_"
]
top_start_game_str = [
  "Start a game as organizer ",
  "Starten Sie ein Spiel als Spielleiter:in ",
  "Starten Sie ein Spiel als Spielleiter:in ",
  "Démarrez un jeu en tant qu'organisateur", 
  "Start et spill som arrangør", 
  "_last_"
]
p_lb_choose_game_str = [
  "Enter the game ID. Your game organizer will tell you what it is. Finish your entry by pressing <Enter>",
  "Geben Sie die Spiel-ID ein. Ihr:e Spielleiter:in sagt Ihnen, wie sie lautet. Beenden Sie Ihre Eingabe indem Sie auf <Eingabe> drücken.",
  "Gib Deine Spiel-ID ein. Dein:e Spielleiter:in sagt Dir, wie sie lautet. Beende Deine Eingabe indem Du auf <Eingabe> drückst.",
  "Saisissez l'identifiant du jeu. Votre organisateur de jeu vous dira de quoi il s'agit. Terminez votre saisie en appuyant sur <Enter>.", 
  "Skriv inn spill-ID-en. Spillarrangøren din vil fortelle deg hva det er. Avslutt inntastingen ved å trykke <Enter>.", 
  "_last_"
]
p_enter_id_str = [ # placeholder
  "Enter the game ID",
  "Geben Sie die Spiel ID ein",
  "Gib die Spiel ID ein",
  "Saisissez l'ID du jeu", 
  "Skriv inn spill-ID", 
  "_last_"
]
no_such_game_str = [
  "This game ID does not exist or a game with this ID has not been started.",
  "Diese Spiel-ID existiert nicht oder ein Spiel mit dieser ID wurde noch nicht gestartet.",
  "Diese Spiel-ID existiert nicht oder ein Spiel mit dieser ID wurde noch nicht gestartet.",
  "Cet identifiant de jeu n'existe pas ou un jeu avec cet identifiant n'a pas été lancé.",
  "Denne spill-ID-en finnes ikke, eller et spill med denne ID-en har ikke blitt startet.",
  "_last_"
]
nsg_t = [
  "ID issue",
  "ID-Problem",
  "ID-Problem",
  "Problème d'ID",
  "ID-problem",
  "_last_"
]
gm_id_msg1_str = [
  "Your game ID is ",
  "Ihre Spiel-ID ist ",
  "Ihre Spiel-ID ist ",
  "Votre jeu d'identité est ", 
  "Din spill -ID er ", 
  "_last_"
]
gm_id_msg2_str = [
  ". Make a note of it. ",
  ". Notieren Sie sich die ID. ",
  ". Notiere die ID. ",
  ". En prendre une note.", 
  ". Noter det.", 
  "_last_"
]
gm_id_title_str = [
  "Your game ID",
  "Ihre Spiel-ID",
  "Ihre Spiel-ID",
  "Votre jeu d'identité", 
  "Din spill-ID", 
  "_last_"
]
top_thanks_msg_str = [
  "... to our Alpha testers, the students in the SW101 course at the Realschule Baesweiler, Germany during April 2024 taught by René Langohr, and all the beta testers. ",
  "... an unsere Alpha-Tester, die Schüler des Kurses SW101 an der Realschule Baesweiler im April 2024, der von René Langohr unterrichtet wird, und alle Beta-Tester. ",
  "... an unsere Alpha-Tester, die Schüler des Kurses SW101 an der Realschule Baesweiler im April 2024, der von René Langohr unterrichtet wird, und alle Beta-Tester. ",
  "... À nos testeurs alpha, les étudiants du cours SW101 au Realschule Baesweiler, Allemagne, en avril 2024 enseigné par René Langohr, et tous les testeurs bêta.", 
  "... Til våre alfa -testere, studentene i SW101-kurset på Realschule Baesweiler i Tyskland i løpet av april 2024 undervist av René Langohr, og alle betatestere.", 
  "_last_"
]
top_thanks_title_str = [
  "Thank you ... ",
  "Vielen Dank ... ",
  "Vielen Dank ... ",
  "Merci ... ", 
  "Takk ...", 
  "_last_"
]
top_roles_setup_msg_str = [
  "Roles template has been set up for ",
  "Rollenvorlage wurde eingerichtet für ",
  "Rollenvorlage wurde eingerichtet für ",
  "Le modèle de rôles a été configuré pour ", 
  "Roller mal er satt opp for ", 
  "_last_"
]
title_you_are_joining_str = [
  "You are joining ",
  "Sie treten bei - ",
  "Sie treten bei - ",
  "Vous rejoignez ", 
  "Du blir med ", 
  "_last_"
]
msg_game_not_started_str = [  ##  not needed
  "The game organizer has not yet started a game. Please wait until he/she does ... ",
  "Der/Die Spielleiter:in hat noch kein Spiel gestartet. Bitte warten Sie, bis er/sie das tut ... ",
  "Der/Die Spielleiter:in hat noch kein Spiel gestartet. Bitte warten Sie, bis er/sie das tut ... ",
  "L'organisateur de jeu n'a pas encore commencé de jeu. Veuillez attendre qu'il / elle le fasse ...", 
  "Spillarrangøren har ennå ikke startet et spill. Vent til han/hun gjør ...", 
  "_last_"
]
msg_gm_board_head_str = [
  "Game Organizer Board for ",
  "Spielleiter:in-Brett für ",
  "Spielleiter:in-Brett für ",
  "Tableau de jeu pour ", 
  "Hovedspillbrett for ", 
  "_last_"
]
msg_gm_board_info_str = [
  "Now, click on **all** the regions **not** played by your players (eg if there are not enough players for all roles)",
  "Klicken Sie jetzt auf **alle** Regionen, die **nicht** von Ihren Spielern gespielt werden (z.B. wenn nicht genügend Spieler:innen für alle Rollen vorhanden sind)",
  "Klicken Sie jetzt auf **alle** Regionen, die **nicht** von Ihren Spielern gespielt werden (z.B. wenn nicht genügend Spieler:innen für alle Rollen vorhanden sind)",
  "Maintenant, cliquez sur **toutes** les régions **pas** jouées par vos joueurs (par exemple s'il n'y a pas assez de joueurs pour tous les rôles)", 
  "Nå, klikk på **alle** regionene **ikke** spilt av spillerne dine (f.eks. Hvis det ikke er nok spillere for alle roller)", 
  "_last_"
]
cb_us_tx_str = [
  "USA ",
  "USA ",
  "USA ",
  "USA", 
  "USA", 
  "_last_"
]
cb_af_tx_str = [
  "Africa, South of Sahara ",
  "Afrika, südlich der Sahara ",
  "Afrika, südlich der Sahara ",
  "Afrique, au sud du Sahara", 
  "Afrika, sør for Sahara", 
  "_last_"
]
cb_cn_tx_str = [
  "China ",
  "China ",
  "China ",
  "Chine ", 
  "Kina", 
  "_last_"
]
cb_me_tx_str = [
  "Middle East - North Africa ",
  "Naher Osten & Nordafrika ",
  "Naher Osten & Nordafrika ",
  "Moyen-Orient - Afrique du Nord", 
  "Midtøsten - Nord -Afrika", 
  "_last_"
]
cb_sa_tx_str = [
  "South Asia ",
  "Südasien ",
  "Südasien ",
  "Asie du Sud", 
  "Sør -Asia", 
  "_last_"
]
cb_la_tx_str = [
  "Latin America ",
  "Lateinamerika ",
  "Lateinamerika ",
  "L'Amérique latine ", 
  "Latin -Amerika", 
  "_last_"
]
cb_pa_tx_str = [
  "Pacific Rim ",
  "Pazifische Anrainerstaaten ",
  "Pazifische Anrainerstaaten ",
  "Pays riverains du Pacifique ", 
  "Landene rundt Stillehavet ", 
  "_last_"
]
cb_ec_tx_str = [
  "East Europe - Central Asia ",
  "Osteuropa & Zentralasien ",
  "Osteuropa & Zentralasien ",
  "Europe de l'Est - Asie centrale", 
  "Øst -Europa - Sentral -Asia", 
  "_last_"
]
cb_eu_tx_str = [
  "Europe ",
  "Europa ",
  "Europa ",
  "Europe", 
  "Europa", 
  "_last_"
]
cb_se_tx_str = [
  "Southeast Asia ",
  "Südostasien ",
  "Südostasien ",
  "Asie du Sud-Est", 
  "Sørøst -Asia", 
  "_last_"
]
cb_pov_tx_str = [
  "Poverty ",
  "Armut ",
  "Armut ",
  "Pauvreté ", 
  "Fattigdom", 
  "_last_"
]
cb_ineq_tx_str = [
  "Inequality ",
  "Ungleichheit ",
  "Ungleichheit ",
  "Inégalité", 
  "Ulikhet", 
  "_last_"
]
cb_emp_tx_str = [
  "Empowerment ",
  "Empowerment/Befähigung ",
  "Empowerment/Befähigung ",
  "Autonomisation ", 
  "Empowerment/Myndiggjøring", 
  "_last_"
]
cb_food_tx_str = [
  "Food & agriculture ",
  "Ernährung und Landwirtschaft ",
  "Ernährung und Landwirtschaft ",
  "Nourriture et agriculture", 
  "Mat og landbruk", 
  "_last_"
]
cbener_tx_str = [
  "Energy ",
  "Energie ",
  "Energie ",
  "Énergie ", 
  "Energi", 
  "_last_"
]
cb_fut_tx_str = [
  "Future ",
  "Zukunft ",
  "Zukunft ",
  "Avenir ", 
  "Fremtid", 
  "_last_"
]
pcr_title_tx_str = [
  "Player Board Game ",
  "SpielerInnen-Brett ",
  "SpielerInnen-Brett ",
  "Jeu de plateau", 
  "Player Board Game", 
  "_last_"
]
pcr_col_left_title_tx_str = [
  "First, log into your region ... ",
  "Melden Sie sich zunächst in Ihrer Region an ... ",
  "Melde Dich zunächst in Deiner Region an ... ",
  "Tout d'abord, connectez-vous à votre région ...", 
  "Først, logg inn i regionen din ...", 
  "_last_"
]
pcr_col_right_title_tx_str = [
  "... then into your role as minister ... ",
  "... dann in Ihrer Rolle als Minister:in ... ",
  "... dann in Deiner Rolle als Minister:in ... ",
  "... puis dans votre rôle de ministre ...", 
  "... så inn i din rolle som minister ...", 
  "_last_"
]
pcr_submit_tx_str = [
  "Once you have logged in to both your region and your ministry, click here to submit your choice ",
  "Nachdem Sie sich sowohl bei Ihrer Region als auch bei Ihrem Ministerium angemeldet haben, klicken Sie hier.",
  "Nachdem Du dich sowohl bei Deiner Region als auch bei Deinem Ministerium angemeldet haben, klicke hier.",
  "Une fois que vous vous êtes connecté à la fois à votre région et à votre ministère, cliquez ici pour soumettre votre choix", 
  "Når du har logget deg inn i både regionen og departementet ditt, klikker du her for å sende inn ditt valg ",
  "_last_"
]
fut_not_all_logged_in_tx_str = [
  "Not all of your regional ministerial colleagues have logged in yet. Wait until they have done so. ",
  "Noch sind nicht alle Ihrer regionalen Ministerkolleg:innen eingeloggt. Warten Sie, bis sie soweit sind. ",
  "Noch sind nicht alle Deiner regionalen Ministerkolleg:innen eingeloggt. Warte, bis sie soweit sind. ",
  "Tous vos collègues ministériels régionaux ne se sont pas encore connectés. Attendez qu'ils l'ont fait.", 
  "Ikke alle dine regionale ministerkolleger har logget inn ennå. Vent til de har gjort det.", 
  "_last_"
]
no_active_game_to_join_tx_str = [ ## not needed
  "no active game to join ... the game organizer has to start one ",
  "Kein aktives Spiel zum Beitreten ... der/die Spielleiter:in muss erst eins starten ",
  "Kein aktives Spiel zum Beitreten ... der/die Spielleiter:in muss erst eins starten ",
  "Pas de jeu actif à rejoindre ... l'organisateur de jeu doit en démarrer un", 
  "intet aktivt spill å bli med ... spillarrangøren må starte en", 
  "_last_"
]
gm_reg_npbp_tx_str = [
  "When you are done (and sure), click this button ",
  "Wenn Sie fertig (und sicher) sind, klicken Sie auf diese Schaltfläche. ",
  "Wenn DU fertig (und sicher) bist, klicke auf diese Schaltfläche. ",
  "Lorsque vous avez terminé (et bien sûr), cliquez sur ce bouton", 
  "Når du er ferdig (og sikker), klikker du på denne knappen", 
  "_last_"
]
topentry_label_tx_str = [
  "Hold on, setting up the database for the game ... ",
  "Moment, die Datenbank für das Spiel wird eingerichtet ... ",
  "Moment, die Datenbank für das Spiel wird eingerichtet ... ",
  "Attendez, la base de données du jeu est en cours de configuration ...", 
  "Hold på, databasen for spillet blir opprettet ...", 
  "_last_"
]
gm_card_wait_1_temp_title_tx1_str = [
  "Still waiting for the following ministers to log in ... Ask if they need help ... ",
  "Wir warten immer noch darauf, dass sich die folgenden Minister:innen anmelden ... Fragen Sie, ob sie Hilfe brauchen ... ",
  "Wir warten immer noch darauf, dass sich die folgenden Minister:innen anmelden ... Frage sie, ob sie Hilfe brauchen ... ",
  "Toujours en attente que les ministres suivants se connectent ... Demandez s'ils ont besoin d'aide ...", 
  "Venter fortsatt på at følgende ministre skal logge inn ... spør om de trenger hjelp ...", 
  "_last_"
]
gm_card_wait_1_temp_title_tx2_str = [
  "All logged in! When you are ready to accept your players decisions for this round, check the box above. Tell them how much time they have for this step. ",
  "Alle sind eingelogged! Wenn Sie so weit sind, die Entscheidungen Ihrer Spieler für diese Runde zu übernehmen, aktivieren Sie das Kontrollkästchen oben. Teilen Sie ihnen mit, wie viel Zeit sie haben. ",
  "Alle sind eingelogged! Wenn Sie so weit sind, die Entscheidungen Ihrer Spieler für diese Runde zu übernehmen, aktivieren Sie das Kontrollkästchen oben. Teilen Sie ihnen mit, wie viel Zeit sie haben. ",
  "Tout le monde est connecté ! Lorsque vous êtes prêt à accepter les décisions de vos joueurs pour ce tour, cochez la case ci-dessus. Indiquez-leur le temps dont ils disposent pour cette étape.",
  "Alt logget inn! Når du er klar til å godta spillernes beslutninger for denne runden, aktiverer du avmerkingsboksen øverst. Fortell dem hvor mye tid de har til rådighet for dette trinnet.", 
  "_last_"
]
gm_card_wait_1_info_tx_str = [
  "All roles have been set up now. Tell your players to log in **now**, using the Game ID shown above. \nInstruct them to look at the state of their region for last 45 years and discuss their decisions to improve the lives of their people. \nCheck repeatedly if all your players have logged in by clicking the **Check LogIn** button. \n\nOnce all logged in, you will see the checkbox to accept the players decisions for the next round. Before you check the box right away, think if you want to do a debrief / discussion first, or if you want to continue the game at a later time, i.e. after lunch, next week, during the next teaching period, etc. ",
  "Alle Rollen sind nun eingerichtet. Bitten Sie Ihre Spieler:innen, sich **jetzt** mit der oben angegebenen Spiel-ID anzumelden. \nWeisen Sie sie an, sich die Lage ihrer Region in den letzten 45 Jahren anzusehen und ihre Entscheidungen zur Verbesserung der Lebensbedingungen ihrer Bevölkerung zu diskutieren. \n\nÜberprüfen Sie wiederholt, ob sich alle Ihre Spieler angemeldet haben, indem Sie auf die Schaltfläche **Anmeldung überprüfen** klicken. \n\nSobald alle eingeloggt sind, wird ein Kontrollkästchen angezeigt, mit dem Sie die Entscheidungen der Spieler für die nächste Runde akzeptieren können. Bevor Sie das Kästchen sofort anklicken, überlegen Sie, ob Sie zuerst eine Nachbesprechung/Diskussion durchführen möchten oder ob Sie das Spiel zu einem späteren Zeitpunkt fortsetzen möchten, z. B. nach dem Mittagessen, nächste Woche, während der nächsten Unterrichtsstunde usw.",
  "Alle Rollen sind nun eingerichtet. Bitten Sie Ihre Spieler:innen, sich **jetzt** mit der oben angegebenen Spiel-ID anzumelden. \nWeisen Sie sie an, sich die Lage ihrer Region in den letzten 45 Jahren anzusehen und ihre Entscheidungen zur Verbesserung der Lebensbedingungen ihrer Bevölkerung zu diskutieren. \n\nÜberprüfen Sie wiederholt, ob sich alle Ihre Spieler angemeldet haben, indem Sie auf die Schaltfläche **Anmeldung überprüfen** klicken. \n\nSobald alle eingeloggt sind, wird ein Kontrollkästchen angezeigt, mit dem Sie die Entscheidungen der Spieler für die nächste Runde akzeptieren können. Bevor Sie das Kästchen sofort anklicken, überlegen Sie, ob Sie zuerst eine Nachbesprechung/Diskussion durchführen möchten oder ob Sie das Spiel zu einem späteren Zeitpunkt fortsetzen möchten, z. B. nach dem Mittagessen, nächste Woche, während der nächsten Unterrichtsstunde usw.",
  "Tous les rôles ont été configurés. Demandez à vos joueurs de se connecter **maintenant** à l'aide de l'identifiant de jeu indiqué ci-dessus. \nDemandez-leur d'examiner la situation de leur région au cours des 45 dernières années et de discuter de leurs décisions visant à améliorer la vie de leur population. \nVérifiez régulièrement que tous vos joueurs se sont connectés en cliquant sur le bouton **Vérifier la connexion**. \n\nUne fois que tous les joueurs sont connectés, vous verrez apparaître la case à cocher pour accepter les décisions des joueurs pour le prochain tour. Avant de cocher la case immédiatement, demandez-vous si vous souhaitez d'abord faire un débriefing/une discussion, ou si vous préférez poursuivre le jeu plus tard, par exemple après le déjeuner, la semaine prochaine, pendant la prochaine période d'enseignement, etc.",
  "Alle roller er nå opprettet. Be spillerne logge inn **nå** ved å bruke spill-ID-en som er vist ovenfor. \nBe dem se på tilstanden i regionen deres de siste 45 årene og diskutere beslutningene de har tatt for å forbedre livene til innbyggerne. \nSjekk gjentatte ganger om alle spillerne har logget inn ved å klikke på **Sjekk innlogging**-knappen. \n\nNår alle har logget seg på, vil du se avmerkingsboksen for å godta spillernes beslutninger for neste runde. Før du merker av i boksen, bør du vurdere om du først vil ha en debriefing/diskusjon, eller om du vil fortsette spillet senere, f.eks. etter lunsj, neste uke, i neste undervisningstime osv.",
  "_last_"
]
after_rdy_submit_gm_card_wait_str = [
  "All your players logged in.\nTell them to look at the state of their region for last 45 years and discuss their decisions to improve the lives of their people.\n\nAfter their deliberations all regions are now free to submit their decisions. Once more, tell them how much time they have for this step. When ready, click on the **Ready to advance...** button. The app will tell you if any region is not yet ready.",
  "Alle Ihre Spieler:innen sind angemeldet.\nBitten Sie sie, sich die Lage ihrer Region in den letzten 45 Jahren anzusehen und ihre Entscheidungen zur Verbesserung der Lebensbedingungen ihrer Bevölkerung zu diskutieren.\n\nNach ihren Beratungen können nun alle Regionen ihre Entscheidungen einreichen. Teilen Sie ihnen erneut mit, wie viel Zeit ihnen für diesen Schritt zur Verfügung steht. \nWenn alle bereit sind, klicken Sie auf die Schaltfläche **Bereit zum Weitermachen...**. Die App informiert Sie, wenn eine Region noch nicht bereit ist.",
  "Alle Ihre Spieler:innen sind angemeldet.\nBitte sie, sich die Lage ihrer Region in den letzten 45 Jahren anzusehen und ihre Entscheidungen zur Verbesserung der Lebensbedingungen ihrer Bevölkerung zu diskutieren.\n\nNach ihren Beratungen können nun alle Regionen ihre Entscheidungen einreichen. Teilen Sie ihnen erneut mit, wie viel Zeit ihnen für diesen Schritt zur Verfügung steht. \nWenn alle bereit sind, klicken Sie auf die Schaltfläche **Bereit zum Weitermachen...**. Die App informiert Sie, wenn eine Region noch nicht bereit ist.",
  "Tous vos joueurs sont connectés.\nDemandez-leur d'examiner la situation de leur région au cours des 45 dernières années et de discuter de leurs décisions visant à améliorer la vie de leur population.\n\nAprès leurs délibérations, toutes les régions sont désormais libres de soumettre leurs décisions. Une fois de plus, indiquez-leur le temps dont ils disposent pour cette étape. \nLorsque vous êtes prêt, cliquez sur le bouton **Prêt à avancer...**. L'application vous indiquera si une région n'est pas encore prête.",
  "Alle spillerne dine er logget inn. \nBe dem se på tilstanden i regionen deres de siste 45 årene og diskutere beslutningene de har tatt for å forbedre livene til innbyggerne. \n\nEtter at de har diskutert, kan alle regionene nå sende inn beslutningene sine. Fortell dem igjen hvor mye tid de har til dette trinnet. \nNår du er klar, klikker du på knappen **Klar til å gå videre...**. Appen vil fortelle deg om noen regioner ennå ikke er klare.",
  "_last_"
]

gm_card_wait_1_btn_check_tx_str = [
  "Check LogIn ",
  "Anmeldungen prüfen ",
  "Anmeldungen prüfen ",
  "Vérifier la connexion", 
  "Sjekk innlogging", 
  "_last_"
]
gm_card_wait_1_btn_kick_off_round_1_tx_str = [
  "Ready to advance the model for the next round? ",
  "Modell für die nächste Runde laufen lassen ",
  "Modell für die nächste Runde laufen lassen ",
  "Prêt à faire avancer le modèle pour le prochain tour?", 
  "Klar til å fremme modellen for neste runde?", 
  "_last_"
]
checkbox_1_tx = [
  "Accept decisions for next round",
  "Entscheidungen für die nächste Runde akzeptieren",
  "Entscheidungen für die nächste Runde akzeptieren",
  "Accepter les décisions pour le prochain tour",
  "Godta avgjørelser for neste runde",
  "_last_"
]
gm_wait_kickoff_r1_tx_str = [
  "Still waiting for the region(s) below to submit their decisions ... You may want to ask if they need help ... ",
  "Warten immer noch darauf, dass die unten aufgeführten Regionen ihre Entscheidungen übermitteln ... Sie können fragen, ob sie Hilfe benötigen ... ",
  "Warten immer noch darauf, dass die unten aufgeführten Regionen ihre Entscheidungen übermitteln ... Sie können fragen, ob sie Hilfe benötigen ... ",
  "Toujours en attente que la région ci-dessous soumette leurs décisions ... vous voudrez peut-être demander s'ils ont besoin d'aide ...", 
  "Venter fortsatt på regionen (e) nedenfor for å sende inn beslutningene sine ... Det kan være lurt å spørre om de trenger hjelp ...", 
  "_last_"
]
gos = [
  "The game master/mistress has not yet enabled the transmission of your decisions for this round.",
  "Der Spielleiter/die Spielleiterin hat die Übermittlung Ihrer Entscheidungen für diese Runde noch nicht freigegeben.",
  "Der Spielleiter/die Spielleiterin hat die Übermittlung Ihrer Entscheidungen für diese Runde noch nicht freigegeben.",
  "Le maître/la maîtresse du jeu n'a pas encore activé la transmission de vos décisions pour ce tour.",
  "Spillmesteren har ennå ikke aktivert overføringen av dine beslutninger for denne runden.",
  "_last_"
]
gos_title = [
  "Sorry ...",
  "Entschuldigung ...",
  "Entschuldigung ...",
  "Désolé...",
  "Beklager ...",
  "_last_"
]
gm_wait_round_done_tx0_str = [
  "The model has been advanced to 2040. Tell your players to click on the \n*Get the results...*  or \n*Check if all ...* button.\nIf you want to accept your players decisions for the next round, check the relevant checkbox. (You may not want to accept decisions right away, for example, if you want to do a debrief / discussion, or if you want to continue the game at a later time, i.e. after lunch, next week, during the next teaching period, etc.)",
  "Das Modell wurde bis 2040 fortgeschrieben. Bitten Sie Ihre Spieler, auf die Schaltfläche \n*Ergebnisse abrufen...* oder \n*Überprüfen, ob ...* zu klicken.\nWenn Sie die Entscheidungen für die nächste Runde annehmen möchten, aktivieren Sie das entsprechende Kontrollkästchen. (Möglicherweise möchten Sie Entscheidungen nicht sofort annehmen, beispielsweise wenn Sie eine Nachbesprechung/Diskussion durchführen möchten oder wenn Sie das Spiel zu einem späteren Zeitpunkt fortsetzen möchten, z. B. nach dem Mittagessen, nächste Woche, während der nächsten Unterrichtsstunde usw.)",
  "Das Modell wurde bis 2040 fortgeschrieben. Bitten Sie Ihre Spieler, auf die Schaltfläche \n*Ergebnisse abrufen...* oder \n*Überprüfen, ob ...* zu klicken.\nWenn Sie die Entscheidungen für die nächste Runde annehmen möchten, aktivieren Sie das entsprechende Kontrollkästchen. (Möglicherweise möchten Sie Entscheidungen nicht sofort annehmen, beispielsweise wenn Sie eine Nachbesprechung/Diskussion durchführen möchten oder wenn Sie das Spiel zu einem späteren Zeitpunkt fortsetzen möchten, z. B. nach dem Mittagessen, nächste Woche, während der nächsten Unterrichtsstunde usw.)",
  "Le modèle a été actualisé jusqu'en 2040. Dites à vos joueurs de cliquer sur le bouton «Obtenir les résultats...» ou «Vérifier si le meneur de jeu...»\nSi vous souhaitez accepter les décisions pour le prochain tour, cochez la case correspondante. (Vous pouvez choisir de ne pas accepter les décisions immédiatement, par exemple si vous souhaitez organiser une réunion/discussion ou si vous souhaitez reprendre le jeu plus tard, par exemple après le déjeuner, la semaine prochaine, pendant le prochain cours, etc.)",
  "Modellen har blitt oppdatert frem til 2040. Be spillerne dine om å klikke på knappen \n*Få resultatene...* eller \n*Sjekk om ...*\nHvis du ønsker å godta avgjørelsene for neste runde, merker du av i den aktuelle boksen. (Det kan hende du ikke ønsker å godta avgjørelsene med en gang, for eksempel hvis du ønsker å gjennomføre en etterdiskusjon eller hvis du ønsker å fortsette spillet på et senere tidspunkt, f.eks. etter lunsj, neste uke, i neste time osv.)",
  "_last_"
]
gm_wait_round_done_tx2_str = [
  "The model has been advanced to 2060. Tell your players to study and discuss their results, within and between regions. Are things going the right way? \nThen, they should decide on the policies for the next round. When they are ready, the Minister for the Future should submit their regional decisions. Tell them how much time they have. ",
  "Das Modell wurde bis 2060 fortgeschrieben. Bitten Sie Ihre Spieler:innen, die Ergebnisse innerhalb und zwischen den Regionen anzuschauen und zu diskutieren. Läuft alles in die richtige Richtung? Sind sie zufrieden?\nAnschliessend sollten sie über die Massnahmen für die nächste Runde entscheiden. Sobald sie bereit sind, sollte der/die ZukunftsMinister:in die regionalen Entscheidungen übermitteln. Sagen sie deutlich, wie viel Zeit ihnen zur Verfügung steht. ",
  "Das Modell wurde bis 2060 fortgeschrieben. Bitten Sie Ihre Spieler:innen, die Ergebnisse innerhalb und zwischen den Regionen anzuschauen und zu diskutieren. Läuft alles in die richtige Richtung? Sind sie zufrieden?\nAnschliessend sollten sie über die Massnahmen für die nächste Runde entscheiden. Sobald sie bereit sind, sollte der/die ZukunftsMinister:in die regionalen Entscheidungen übermitteln. Sagen sie deutlich, wie viel Zeit ihnen zur Verfügung steht. ",
  "Le modèle a été avancé jusqu'en 2040. Demandez à vos joueurs d'étudier leurs résultats et d'en discuter, au sein des régions et entre elles. Les choses vont-elles dans le bon sens ? \nEnsuite, ils doivent décider des politiques pour le prochain tour. Lorsqu'ils seront prêts, le ministre de l'Avenir leur soumettra leurs décisions régionales. Indiquez-leur le temps dont ils disposent. ",
  "Modellen har blitt kjørt framover frem til 2060. Be spillerne studere og diskutere resultatene, både innenfor og mellom regionene. Går det riktig vei? \nSå skal de bestemme seg for politikken for neste runde. Når de er klare, skal fremtidsministeren sende inn de regionale beslutningene. Fortell dem hvor mye tid de har. ",
  "_last_"
]
gm_wait_round_done_tx3_str = [
  "The model has been advanced to the end, the year 2100. Tell your players to study and discuss their results, within and between regions. Are things going the right way? Are they safisfied? Are their citizens satisfied? Is the earth still habitable? \nFinally, take them out of the game back to the here and now; and start your debriefing.\nThanks for playing - much appreciated!\nFeedback? Send to post at blue minus way dot net\n\nBye-bye",
  "Das Modell wurde bis zum Ende, dem Jahr 2100, fortgeschrieben. Bitten Sie Ihre Spieler:innen, ihre Ergebnisse innerhalb und zwischen den Regionen anzuschauen und zu diskutieren. Läuft alles nach Plan? Sind sie zufrieden? Sind ihre Bürger zufrieden? Ist die Erde noch bewohnbar? \nZum Schluss nehmen Sie sie aus dem Spiel zurück ins Hier und Jetzt und beginnen Sie mit der Nachbesprechung.\nDanke fürs Spielen - wir schätzen ihre Zeit und Einsatz sehr!\nRückmeldung? Bitte an post at blue minus way dot net\n\nAuf Wiedersehen",
  "Das Modell wurde bis zum Ende, dem Jahr 2100, fortgeschrieben. Bitten Sie Ihre Spieler:innen, ihre Ergebnisse innerhalb und zwischen den Regionen anzuschauen und zu diskutieren. Läuft alles nach Plan? Sind sie zufrieden? Sind ihre Bürger zufrieden? Ist die Erde noch bewohnbar? \nZum Schluss nehmen Sie sie aus dem Spiel zurück ins Hier und Jetzt und beginnen Sie mit der Nachbesprechung.\nDanke fürs Spielen - wir schätzen Deine Zeit und Einsatz sehr!\nRückmeldung? Bitte an post at blue minus way dot net\n\nCiao",
  "Le modèle a été mis à jour jusqu'à la fin, en 2100. Demandez à vos joueurs de regarder et de discuter de leurs résultats dans et entre les régions. Tout se déroule-t-il comme prévu ? Sont-ils satisfaits ? Leurs citoyens sont-ils satisfaits ? La Terre est-elle encore habitable ? \nEnfin, ramenez-les hors du jeu, ici et maintenant, et commencez le débriefing.\nMerci de jouer - nous apprécions votre temps et votre engagement!\nRéponse? Envoyez-le à post at blue minus way dot net.\n\nAu revoir",
  "Modellen ble oppdatert frem til slutten av år 2100. Be spillerne dine se på og diskutere resultatene innad i og mellom regionene. Går alt etter planen? Er de fornøyde? Er innbyggerne fornøyde? Er jorden fortsatt beboelig? \nTil slutt tar du dem ut av spillet og tilbake til her og nå, og begynner debriefingen.\nTakk for at du har spillet - vi setter pris på din tid og innsats! \nTilbakemeldinger? Vennligst send til post at blue minus way dot net\n\nHa det bra",
  "_last_"
]
sim_success_tx40_str = [
  "...the model ran successfully to 2040. Now we are waiting for the decisions for 2040-2060.\nHave you set all your policy decisions? ",
  "...das Modell lief erfolgreich bis 2040. Jetzt warten wir noch auf alle Entscheidungen für 2040-2060.\nHaben Sie alle Ihre politischen Entscheidungen getroffen? ",
  "...das Modell lief erfolgreich bis 2040. Jetzt warten wir noch auf alle Entscheidungen für 2040-2060.\nHaben Sie alle Ihre politischen Entscheidungen getroffen? ",
  "...le modèle a fonctionné avec succès jusqu'en 2040. Maintenant, on attend les décisions pour 2040-2060.\nAvez-vous pris toutes vos décisions politiques? ",
  "...modellen kjørte vellykket frem til 2040. Nå venter vi fortsatt på beslutningene for 2040-2060.\nHar dere tatt alle de politiske beslutningene?  ",
  "_last_"
]
sim_success_tx21_str = [
  "...the model ran successfully to the end, 2100 ",
  "...das Modell lief erfolgreich bis zum Schluss, dem Jahr 2100 ",
  "...das Modell lief erfolgreich bis zum Schluss, dem Jahr 2100 ",
  "...le modèle a fonctionné avec succès jusqu'à la fin, l'année 2100",
  "...modellen kjørte med suksess frem til slutten av år 2100",
  "_last_"
]
p_info_40_fut = [
  "\nBelow are the model results until 2040.",
  "\nNachfolgend die Ergebnisse bis 2040.",
  "\nWeiter unten die Ergebnisse bis 2040.",
  "\nVoici les résultats jusqu'en 2040.",
  "\nNedenfor vises resultatene frem til 2040.",
  "_last_"  
]
p_info_60_fut = [
  "\nBelow are the model results until 2060.",
  "\nNachfolgend die Ergebnisse bis 2060.",
  "\nWeiter unten die Ergebnisse bis 2060.",
  "\nVoici les résultats jusqu'en 2060.",
  "\nNedenfor vises resultatene frem til 2060.",
  "_last_"  
]
p_info_21_fut = [
  "\nBelow are the model results until 2100.",
  "\nNachfolgend die Ergebnisse bis 2100.",
  "\nWeiter unten die Ergebnisse bis 2100.",
  "\nVoici les résultats jusqu'en 2100.",
  "\nNedenfor vises resultatene frem til 2100.",
  "_last_"  
]
sim_success_tx60_str = [
  "...the model ran successfully to 2060. Now we are waiting for the decisions for 2060-2100.\nHave you set all your policy decisions? ",
  "...das Modell lief erfolgreich bis 2060. Jetzt warten wir noch auf alle Entscheidungen für 2060-2100.\nHaben Sie alle Ihre politischen Entscheidungen getroffen? ",
  "...das Modell lief erfolgreich bis 2060. Jetzt warten wir noch auf alle Entscheidungen für 2060-2100.\nHaben Sie alle Ihre politischen Entscheidungen getroffen? ",
  "...le modèle a fonctionné avec succès jusqu'en 2060. Maintenant, on attend les décisions pour 2060-2100.\nAvez-vous pris toutes vos décisions politiques ?",
  "...modellen kjørte vellykket frem til 2060. Nå venter vi fremdeles på beslutningene for 2060-2100.\nHar du tatt alle policybeslutningene dine?",
  "_last_"
]
sim_success_title_tx_str = [
  "Success ",
  "Erfolgreich ",
  "Erfolgreich ",
  "Réussite ", 
  "Vellykket ",
  "_last_"
]
sim_success_title_txend_str = [
  "Success ",
  "Erfolgreich ",
  "Erfolgreich ",
  "Réussite ", 
  "Vellykket ",
  "_last_"
]
pcgd_generating_tx1_str = [
  "Generating graphs until 2040 and decision sheet for 2040 ",
  "Diagramme bis 2040 und Entscheidungsblatt für 2040 werden erstellt ",
  "Diagramme bis 2040 und Entscheidungsblatt für 2040 werden erstellt ",
  "Génération de graphiques jusqu'en 2040 et feuille de décision pour 2040", 
  "Generere grafer til 2040 og beslutningsark for 2040", 
  "_last_"
]
pcgd_generating_tx2_str = [
  "Generating graphs until 2060 and decision sheet for 2060 ",
  "Diagramme bis 2060 und Entscheidungsblatt für 2060 werden erstellt ",
  "Diagramme bis 2060 und Entscheidungsblatt für 2060 werden erstellt ",
  "Génération de graphiques jusqu'en 2060 et feuille de décision pour 2060", 
  "Generere grafer til 2060 og beslutningsark for 2060", 
  "_last_"
]
pcgd_generating_tx3_str = [
  "Generating graphs until 2100 ",
    " Diagramme bis 2100 werden erstellt ",
    " Diagramme bis 2100 werden erstellt ",
    "Génération de graphiques jusqu'à 2100", 
    "Generere grafer til 2100", 
    "_last_"
]
gm_wait_round_started_tx_str = [
    "The simulation started. Please wait until it is done... ",
    "Die Simulation hat begonnen. Bitte warten Sie, bis sie abgeschlossen ist... ",
    "Die Simulation hat begonnen. Bitte warten Sie, bis sie abgeschlossen ist... ",
    "La simulation a commencé. Veuillez attendre que ce soit fait ...", 
    "Simuleringen startet. Vent til det er gjort ...", 
    "_last_"
]
gm_start_round_tx_2_str = [
    "Check if all regions are ready to advance to 2060 ... ",
    "Überprüfen Sie, ob alle Regionen ihre Massnahmen bis 2060 übermittelt haben ... ",
    "Überprüfen Sie, ob alle Regionen ihre Massnahmen bis 2060 übermittelt haben ... ",
    "Vérifiez si toutes les régions sont prêtes à passer à 2060 ...", 
    "Sjekk om alle regioner er klare til å gå videre til 2060 ...", 
    "_last_"
]
gm_start_round_tx_3_str = [
    "Check if all regions are ready to advance to 2100 ... ",
    "Überprüfen Sie, ob alle Regionen ihre Massnahmen bis 2100 übermittelt haben ... ",
    "Überprüfen Sie, ob alle Regionen ihre Massnahmen bis 2100 übermittelt haben ... ",
    "Vérifiez si toutes les régions sont prêtes à passer à 2100 ...", 
    "Sjekk om alle regioner er klare til å gå videre til 2100 ...", 
    "_last_"
]
waiting_for_gm_to_start_round_str = [
    "... for simulation to start ... ",
    "... bis die Simulation beginnt ... ",
    "... bis die Simulation beginnt ... ",
    "... pour que la simulation commence ...", 
    "... for simulering å starte ...", 
    "_last_"
]
gm_wait_sub2_tx_str = [
    "... for all submissions for the round 2040 to 2060 ... ",
    "... auf alle Massnahmen für die Runde 2040 bis 2060 ... ",
    "... auf alle Massnahmen für die Runde 2040 bis 2060 ... ",
    "... pour toutes les soumissions du tour 2040 à 2060 ...", 
    "... for alle innleveringer for runden 2040 til 2060 ...", 
    "_last_"
]
gm_wait_sub3_tx_str = [
    "... for all submissions for the round 2060 to 2100 ... ",
    "... auf alle Massnahmen für die Runde 2060 bis 2100 ... ",
    "... auf alle Massnahmen für die Runde 2060 bis 2100 ... ",
    "... pour toutes les soumissions du tour 2060 à 2100 ...", 
    "... for alle innleveringer for runden 2060 til 2100 ...", 
    "_last_"
]
setup_npbp_label_tx_str = [
    "Hold on, all roles are being prepared ... ",
    "Warten Sie bis alle Rollen vorbereitet sind ... ",
    "Warten Sie bis alle Rollen vorbereitet sind ... ",
    "Attendez, tous les rôles sont préparés ...", 
    "Hold på, alle roller blir forberedt ...", 
    "_last_"
]
msg_ro_str = [
    "Role assignments are set up ... Now tell your players to join game  + cid +  and log in to their roles. You need to wait until all players have submitted their decisions for round 1, 2025 to 2040 ",
    "Die Rollenzuweisungen sind eingerichtet ... Sagen Sie Ihren Spielern:innen nun, dass sie dem Spiel  + cid +  beitreten und sich in ihre Rollen einloggen sollen. Sie selbst müssen warten, bis alle Spieler:innen ihre Entscheidungen für Runde 1 (2025 bis 2040) übermittelt haben. ",
    "Die Rollenzuweisungen sind eingerichtet ... Sagen Sie Ihren Spielern:innen nun, dass sie dem Spiel  + cid +  beitreten und sich in ihre Rollen einloggen sollen. Sie selbst müssen warten, bis alle Spieler:innen ihre Entscheidungen für Runde 1 (2025 bis 2040) übermittelt haben. ",
    "Les affectations de rôles sont configurées ... Maintenant, dites à vos joueurs de rejoindre Game + CID + et de vous connecter à leurs rôles. Vous devez attendre que tous les joueurs aient soumis leurs décisions pour le tour 1, 2025 à 2040", 
    "Rolloppgaver er satt opp ... Fortell nå spillerne dine om å bli med på Game + CID + og logge inn på rollene sine. Du må vente til alle spillere har sendt sine beslutninger for runde 1, 2025 til 2040", 
    "_last_"
]
pcr_submit_title_str = [
    "Congratulations! ",
    "Herzlichen Glückwunsch! ",
    "Glückwunsch! ",
    "Félicitations! ",
    "Gratulerer! ",
    "_last_"
]
pcr_submit_msg1_str = [
    "You have been confirmed as ",
    "Sie wurden bestätigt als ",
    "Du wurdest bestätigt als ",
    "Vous avez été confirmé comme ",
    "Du er bekreftet som ",
    "_last_"
]
pcr_submit_msg2_str = [
    " in ",
    " in ",
    " in ",
    " dans ", 
    " i ",
    "_last_"
]
pcr_submit_msg3_str = [
    "Your personal Game ID is ",
    "Ihre persönliche Spiel-ID lautet ",
    "Ihre persönliche Spiel-ID lautet ",
    "Votre identifiant de jeu personnel est ",
    "Din personlige spill-ID er ",
    "_last_"
]
player_board_tx_str = [
    "Player Board - ",
    "Spieler:innen Board ",
    "Spieler:innen Board ",
    "Tableau des joueurs-", 
    "Spillerbrett-", 
    "_last_"
]
pcgd_rd1_info_tx_str = [
    "You are responsible to better the lives of your people. In the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry - social unrest, and worse, is just around the corner!\nStudy all your indicators, see how they develop over the years, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, scroll down to the decisions you need to take as minister that hopefully improve the lives of your citizens in the next round. ",
    "Sie sind dafür verantwortlich, das Leben Ihrer Bevölkerung zu verbessern. In den folgenden Diagrammen ist die Lage gut, wenn die Linie im **grünen** Bereich liegt. Wenn sie im **roten** Bereich liegt, müssen Sie sich Sorgen machen, soziale Unruhen oder Schlimmeres stehen unmittelbar bevor!\nSchauen Sie alle Ihre Indikatoren an, verfolgen Sie deren Entwicklung über die Jahre und tauschen Sie sich aus mit Kollegen:innen, zunächst in Ihrer Region, aber auch in den anderen Regionen.\nWenn Sie bereit sind, scrollen Sie nach unten zu den Entscheidungen, die Sie als Minister:in treffen müssen, um das Leben Ihrer Bürger:innen in der nächsten Runde, hoffentlich, zu verbessern. ",
    "Sie sind dafür verantwortlich, das Leben Ihrer Bevölkerung zu verbessern. In den folgenden Diagrammen ist die Lage gut, wenn die Linie im **grünen** Bereich liegt. Wenn sie im **roten** Bereich liegt, müssen Sie sich Sorgen machen, soziale Unruhen oder Schlimmeres stehen unmittelbar bevor!\nSchau Dir alle Deine Indikatoren an, verfolge deren Entwicklung über die Jahre und tausche Dich mit Kollegen:innen, zunächst in Deiner Region, aber auch in den anderen Regionen, aus.\nWenn Du soweit bist, scrolle nach unten zu den Entscheidungen, die Du als Minister:in treffen musst, um das Leben Deiner Bürger:innen in der nächsten Runde, hoffentlich, zu verbessern. ",
    "Vous avez la responsabilité d'améliorer la vie de votre peuple. Dans les graphiques ci-dessous, la situation est bonne si la ligne est dans la zone **verte**, si elle est dans la zone **rouge**, vous devez vous inquiéter - l'agitation sociale, voire pire, est au coin de la rue!\nÉtudiez tous vos indicateurs, voyez comment ils évoluent au fil des ans, discutez-en avec vos collègues, d'abord dans votre région, mais aussi dans les autres régions.\nQuand vous êtes prêt, faites défiler vers le bas jusqu'aux décisions que vous devez prendre en tant que ministre pour, espérons-le, améliorer la vie de vos citoyens au cours du prochain cycle de négociations. ",
    "Du er ansvarlig for å forbedre livene til ditt folk. I grafene nedenfor går det bra hvis linjen er i den **grønne** sonen, hvis den er i den **røde** sonen, må du bekymre deg - sosial uro, og det som verre er, er rett rundt hjørnet!\nStuder alle indikatorene dine, se hvordan de utvikler seg over årene, diskuter med kolleger, først i din region, men også i de andre regionene.\nNår du er klar, blar du ned til beslutningene du må ta som minister, som forhåpentligvis vil forbedre livene til innbyggerne dine i neste runde. ",
    "_last_"
]
pcgd_rd1_info_short_str = [
    "Together with your ministerial team, you are responsible to better the lives of your people. In the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry - social unrest, and worse, is just around the corner!\nStudy all your indicators, see how they develop over the years, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, scroll down to see the investment plans of your colleagues. Make sure they are within your regional budget. More instructions are below the graphs. ",
    "Gemeinsam mit Ihrem Minister:innen Team tragen Sie die Verantwortung, das Leben Ihrer Bevölkerung zu verbessern. In den folgenden Grafiken ist die Lage gut, wenn die Linie im **grünen** Bereich liegt. Liegt sie im **roten** Bereich, besteht Grund zur Sorge & soziale Unruhen oder Schlimmeres stehen unmittelbar bevor!\nSchauen Sie alle Ihre Indikatoren an, beobachten Sie deren Entwicklung über die Jahre und tauschen Sie sich aus mit Kollegen:innen, zunächst in Ihrer Region, aber auch in den anderen Regionen.\nWenn Sie bereit sind, scrollen Sie nach unten, um die Investitionspläne Ihrer Kollegen:innen zu sehen. Stellen Sie sicher, dass diese im Rahmen Ihres regionalen Budgets liegen. Weitere Anweisungen finden Sie unter den Grafiken. ",
    "Gemeinsam mit Ihrem Minister:innen Team tragen Sie die Verantwortung, das Leben Ihrer Bevölkerung zu verbessern. In den folgenden Grafiken ist die Lage gut, wenn die Linie im **grünen** Bereich liegt. Liegt sie im **roten** Bereich, besteht Grund zur Sorge & soziale Unruhen oder Schlimmeres stehen unmittelbar bevor!\nSchauen Sie alle Ihre Indikatoren an, beobachten Sie deren Entwicklung über die Jahre und tauschen Sie sich aus mit Kollegen:innen, zunächst in Ihrer Region, aber auch in den anderen Regionen.\nWenn Sie bereit sind, scrollen Sie nach unten, um die Investitionspläne Ihrer Kollegen:innen zu sehen. Stellen Sie sicher, dass diese im Rahmen Ihres regionalen Budgets liegen. Weitere Anweisungen finden Sie unter den Grafiken. ",
    "Avec votre équipe ministérielle, vous avez la responsabilité d'améliorer la vie de votre peuple. Dans les graphiques ci-dessous, la situation est bonne si la ligne est dans la zone **verte**, si elle est dans la zone **rouge**, vous devez vous inquiéter - les troubles sociaux, et pire encore, sont à nos portes!\nÉtudiez tous vos indicateurs, voyez comment ils évoluent au fil des ans, discutez-en avec vos collègues, d'abord dans votre région, mais aussi dans les autres régions.\nQuand vous êtes prêt, faites défiler vers le bas pour voir les plans d'investissement de vos collègues. Assurez-vous qu'ils correspondent au budget de votre région. D'autres instructions figurent sous les graphiques. ",
    "Sammen med ministerteamet ditt er du ansvarlig for å forbedre livene til folket ditt. I grafene nedenfor går det bra hvis linjen er i den **grønne** sonen, hvis den er i den **røde** sonen, må du bekymre deg - sosial uro, og det som verre er, er rett rundt hjørnet!\nStuder alle indikatorene dine, se hvordan de utvikler seg over årene, diskuter med kolleger, først i din region, men også i de andre regionene.\nNår du er klar, kan du bla nedover for å se investeringsplanene til kollegene dine. Sørg for at de er innenfor ditt regionale budsjett. Du finner flere instruksjoner under grafene. ",
    "_last_"
]
pcgd_rd1_infoend_str = [
    "**Outfade** ",
    "pcgd_rd1:info_end_tx *outtake* ",
    "**Ausblenden** ",
    "pcgd_rd1:info_end_tx *Ausgang* ",
    "** outfade **" ,
    "_last_"
]
pcgd_rd1_info_fut_tx_str = [
    "As Minister for the Future, you see the big picture. You also see how much your ministerial colleagues in your region plan to invest in total to improve the lives of your people and the health of the planet. \nIt is **your** task to keep the **total regional investment** within the budget. If *total investment* is **below** 100 % of the budget, all is well. Although if you invest too little, things may get worse, much worse possibly!\nIf it is **above** 100 % of your budget, you need to advise your ministerial colleagues to reduce some of their investments. This is a difficult task where your moderating skills are needed. Good luck!\nAs your ministerial colleagues decide on their investment plans, click on the **Refresh Numbers** button to see the most up to date choices of your colleagues.\nWhen you are all ready, **you**, as Minister for the Future, submit the policy choices from all your colleagues - **be sure to get all their OKs** before you hit the *Submit* button! (*Note* if the Submit button does not show, it is because your region is above the the budget.\nMoney amounts are in constant (2025) Giga $ per year. A Giga is 1,000,000,000 ----- US Americans call this a Billion, others call this a Milliarde. ",
    "Als ZukunftsMinister:in sehen Sie das grosse Ganze. Sie sehen auch, wie viel Ihre Minister:innenkollegen in Ihrer Region insgesamt investieren wollen, um das Leben Ihrer Bevölkerung und die Gesundheit des Planeten zu verbessern. \nEs ist **Ihre** Aufgabe, die **regionalen Gesamtinvestitionen** im Rahmen des Budgets zu halten. Liegen die *Gesamtinvestitionen* **unter** 100 % des Budgets, ist alles in Ordnung. Investieren Sie jedoch zu wenig, kann es schlimmer werden, möglicherweise sogar noch viel schlimmer!\nLiegen sie **über** 100 % Ihres Budgets, müssen Sie Ihre Minister:innenkollegen anweisen, ihre Investitionen zu kürzen. Dies ist eine schwierige Aufgabe, bei der Ihre Moderationsfähigkeiten gefragt sind. Viel Erfolg!\nWährend Ihre Minister:innenkollegen ihre Investitionspläne beschliessen, klicken Sie wiederholt auf die Schaltfläche **Zahlen aktualisieren**, um die aktuellsten Entscheidungen Ihrer Kolleg:Innen anzuzeigen.\nWenn Sie fertig sind, **reichen Sie** als ZukunftsMinister:in die politischen Entscheidungen aller Ihrer Kolleg:Innen ein. **Achten Sie darauf, dass alle ihre Zustimmung geben** bevor Sie auf *Zahlen übermitteln* klicken! (*Hinweis* Wenn die Schaltfläche *Zahlen übermitteln* nicht angezeigt wird, liegt das daran, dass Ihre Region das Budget überschreitet.\n\nGeldbeträge werden in konstanten (2025) Giga-Dollar pro Jahr angegeben. Ein *Giga* entspricht 1.000.000.000 --- US-Amerikaner nennen dies eine Billion, andere eine Milliarde.",
    "Als ZukunftsMinister:in sehen Sie das grosse Ganze. Sie sehen auch, wie viel Ihre Minister:innenkollegen in Ihrer Region insgesamt investieren wollen, um das Leben Ihrer Bevölkerung und die Gesundheit des Planeten zu verbessern. \nEs ist **Ihre** Aufgabe, die **regionalen Gesamtinvestitionen** im Rahmen des Budgets zu halten. Liegen die *Gesamtinvestitionen* **unter** 100 % des Budgets, ist alles in Ordnung. Investieren Sie jedoch zu wenig, kann es schlimmer werden, möglicherweise sogar noch viel schlimmer!\nLiegen sie **über** 100 % Ihres Budgets, müssen Sie Ihre Minister:innenkollegen anweisen, ihre Investitionen zu kürzen. Dies ist eine schwierige Aufgabe, bei der Ihre Moderationsfähigkeiten gefragt sind. Viel Erfolg!\nWährend Ihre Minister:innenkollegen ihre Investitionspläne beschliessen, klicken Sie wiederholt auf die Schaltfläche **Zahlen aktualisieren**, um die aktuellsten Entscheidungen Ihrer Kolleg:Innen anzuzeigen.\nWenn Sie fertig sind, **reichen Sie** als ZukunftsMinister:in die politischen Entscheidungen aller Ihrer Kolleg:Innen ein. **Achten Sie darauf, dass alle ihre Zustimmung geben** bevor Sie auf *Zahlen übermitteln* klicken! (*Hinweis* Wenn die Schaltfläche *Zahlen übermitteln* nicht angezeigt wird, liegt das daran, dass Ihre Region das Budget überschreitet.\n\nGeldbeträge werden in konstanten (2025) Giga-Dollar pro Jahr angegeben. Ein *Giga* entspricht 1.000.000.000 --- US-Amerikaner nennen dies eine Billion, andere eine Milliarde.",
    "En tant que ministre de l'avenir, vous avez une vue d'ensemble. Vous voyez aussi combien vos collègues ministres de votre région prévoient d'investir au total pour améliorer la vie de vos concitoyens et la santé de la planète. \nC'est **votre** tâche de maintenir l'**investissement régional total** dans les limites du budget. Si l'investissement total est inférieur à 100 % du budget, tout va bien. Toutefois, si vous investissez trop peu, les choses risquent d'empirer, voire de s'aggraver ! Si le total est **supérieur** à 100 % de votre budget, vous devez conseiller à vos collègues ministres de réduire certains de leurs investissements. Il s'agit d'une tâche difficile où vos talents de modérateur sont nécessaires. Bonne chance!\nAu fur et à mesure que vos collègues ministres décident de leurs plans d'investissement, cliquez sur le bouton **Rafraîchir les chiffres** pour voir les choix les plus récents de vos collègues.\nQuand vous êtes prêt, **vous**, en tant que ministre de l'avenir, soumettez les choix politiques de tous vos collègues - **assurez-vous d'obtenir leur accord** avant d'appuyer sur le bouton *Soumettre* ! (*Note* si le bouton Soumettre ne s'affiche pas, c'est que votre région est au-dessus du budget.\n\nLes montants sont en Giga $ constants (2025) par an. Un Giga est égal à 1 000 000 000 ----- Les Américains appellent cela un Billion, d'autres appellent cela une Milliarde. " ,
    "Som fremtidsminister ser du det store bildet. Du ser også hvor mye dine ministerkolleger i din region planlegger å investere totalt for å forbedre livene til ditt folk og helsen til planeten. \nDet er **din** oppgave å holde den **samlet regionale investeringen** innenfor budsjettet. Hvis den *totale investeringen* er **under** 100 % av budsjettet, er alt i orden. Men hvis du investerer for lite, kan ting bli verre, mye verre, muligens! Hvis det er **over** 100 % av budsjettet, må du råde dine ministerkolleger til å redusere noen av sine investeringer. Dette er en vanskelig oppgave der det er behov for dine modererende evner. Lykke til! \nNår ministerkollegene dine bestemmer seg for investeringsplanene sine, klikker du på knappen **Oppdater tall** for å se de mest oppdaterte valgene til kollegene dine.\nNår du er klar, sender **du**, som fremtidsminister, inn de politiske valgene fra alle kollegene dine - **se til at du får alle deres OK** før du trykker på *Send*-knappen! (*Hvis Send-knappen ikke vises, er det fordi din region ligger over budsjettet*).\n\nPengebeløpene er i konstant (2025) Giga $ per år. En Giga er 1 000 000 000 ----- US-amerikanere kaller dette en Billion, andre kaller det en Milliarde. ",
    "_last_"
]
pcgd_rd1_infoend_tx_str = [
    "The game is done, the song is over, thought I'd something more to say. © Pink Floyd",
    "Das Spiel ist vorbei, der Song ist zu Ende, ich dachte, ich hätte noch etwas zu sagen. © Pink Floyd",
    "Das Spiel ist vorbei, der Song ist zu Ende, ich dachte, ich hätte noch etwas zu sagen. © Pink Floyd",
    "Le jeu est terminé, la chanson est finie, j'ai pensé que j'avais quelque chose de plus à dire.  © Pink Floyd", 
    "Spillet er over, sangen er over, tenkte jeg hadde noe mer å si.  © Pink Floyd", 
    "_last_"
]
pcgd_rd1_info_end_tx_str = [
  "The model has reached the end. The game is over. Shed your role and come back to the here and now. What happened in the game? What surprised you? What irritated  you? What was too complicated? Too easy? What made you think? What did you realize that you had not noticed before? Would you like to be a minister in real life?",
  "Das Modell hat das Ende erreicht. Das Spiel ist vorbei. Legen Sie Ihre Rolle ab und kehren Sie ins Hier und Jetzt zurück. Was ist während des Spiels passiert? Was hat Sie überrascht? Was hat Sie irritiert? Was war zu kompliziert? Zu einfach? Was hat Sie zum Nachdenken gebracht? Was ist Ihnen aufgefallen, was Sie vorher nicht bemerkt haben? Würden Sie im wirklichen Leben gerne Minister:in sein?",
  "Das Modell hat das Ende erreicht. Das Spiel ist vorbei. Lege Deine ab und kehre ins Hier und Jetzt zurück. Was ist während des Spiels passiert? Was hat Dich überrascht? Was hat Dich irritiert? Was hat Dich zum Nachdenken gebracht? Was ist Dir aufgefallen, dass Du vorher nicht bemerkt hattest? Würdest Du im wirklichen Leben gerne Minister:in sein?",
  "Le modèle est arrivé au bout. Le jeu est terminé. Débarrassez-vous de votre rôle et revenez dans l'ici et le maintenant. Que s'est-il passé pendant le jeu ? Qu'est-ce qui vous a surpris ? Qu'est-ce qui vous a irrité ? Qu'est-ce qui était trop compliqué ? Trop facile ? Qu'est-ce qui vous a fait réfléchir ? Qu'avez-vous réalisé que vous n'aviez pas remarqué auparavant ? Aimeriez-vous être ministre dans la vraie vie ?",
  "Modellen har nådd slutten. Spillet er over. Legg av deg rollen og kom tilbake til her og nå. Hva skjedde i spillet? Hva overrasket deg? Hva irriterte deg? Hva var for komplisert? For enkelt? Hva fikk deg til å tenke? Hva gikk opp for deg som du ikke hadde lagt merke til før? Kunne du tenke deg å være medlem av regjeringen i virkeligheten?",
    "_last_"  
]
pcgd_generating_tx4_str = [
    "... generating your graphs and decisionsheet ... ",
    "... Ihre Diagramme und Entscheidungsblätter werden generiert... ",
    "... Ihre Diagramme und Entscheidungsblätter werden generiert... ",
    "... générer vos graphiques et votre feuille de décision ...", 
    "... generere grafene og beslutningsarket ...", 
    "_last_"
]
show_hide_plots_hide_tx_str = [
    "Hide graphs ",
    "Diagramme ausblenden ",
    "Diagramme ausblenden ",
    "Masquer les graphiques", 
    "Skjul grafer", 
    "_last_"
]
show_hide_plots_show_tx_str = [
    "Show graphs ",
    "Diagramme anzeigen ",
    "Diagramme anzeigen ",
    "Afficher les graphiques", 
    "Vis grafer", 
    "_last_"
]
pcgd_advance_tx_str = [
    "Check if the model has been advanced ",
    "Überprüfen, ob das Modell fortgeschrieben wurde ",
    "Überprüfen, ob das Modell fortgeschrieben wurde ",
    "Vérifiez si le modèle a été avancé", 
    "Sjekk om modellen er oppdatert",
    "_last_"
]
pcgd_info_after_rd1_tx_str = [
    "The model has been simulated until 2040. Again, in the graphs below things are good if the line is in the **green** zone, if they are in the **red** zone, you need to worry!\nStudy all your indicators, see how they develop over the years. *Given your policy choices, did you expect something different? Are surprised?* Again, discuss with colleagues, first in your region, but also in the other regions.\nWhen you are ready, and in light of what happenend in the last round, scroll down to the decisions you need to take as minister that hopefully improve the lives of your citizens in the next round. ",
    "Das Modell wurde bis 2040 fortgeschrieben. Auch in den folgenden Grafiken ist alles gut, wenn die Linie im **grünen** Bereich liegt. Wenn sie im **roten** Bereich liegt, besteht Grund zur Sorge!\nSchauen Sie sich Sie alle Ihre Indikatoren und beobachten Sie, wie sie sich im Laufe der Jahre entwickeln. *Haben Sie angesichts Ihrer politischen Entscheidungen etwas anderes erwartet? Sind Sie überrascht?* Besprechen Sie dies erneut mit Kollegen:innen, zuerst in Ihrer Region, aber auch in den anderen Regionen.\nWenn Sie bereit sind und im Lichte der Ergebnisse der letzten Runde, scrollen Sie nach unten zu den Entscheidungen, die Sie als Minister:in treffen müssen, um hoffentlich das Leben Ihrer Bürger in der nächsten Runde zu verbessern. ",
    "Das Modell wurde bis 2040 fortgeschrieben. Auch in den folgenden Grafiken ist alles gut, wenn die Linie im **grünen** Bereich liegt. Wenn sie im **roten** Bereich liegt, besteht Grund zur Sorge!\nSchauen Sie sich Sie alle Ihre Indikatoren und beobachten Sie, wie sie sich im Laufe der Jahre entwickeln. *Haben Sie angesichts Ihrer politischen Entscheidungen etwas anderes erwartet? Sind Sie überrascht?* Besprechen Sie dies erneut mit Kollegen:innen, zuerst in Ihrer Region, aber auch in den anderen Regionen.\nWenn Sie bereit sind und im Lichte der Ergebnisse der letzten Runde, scrollen Sie nach unten zu den Entscheidungen, die Sie als Minister:in treffen müssen, um hoffentlich das Leben Ihrer Bürger in der nächsten Runde zu verbessern. ",
    "Le modèle a été simulé jusqu'en 2040. Encore une fois, dans les graphiques ci-dessous, la situation est bonne si la ligne est dans la zone **verte**, si elle est dans la zone **rouge**, vous devez vous inquiéter!\nÉtudiez tous vos indicateurs, voyez comment ils évoluent au fil des ans. *Etant donné vos choix politiques, vous attendiez-vous à quelque chose de différent ? Une fois encore, discutez-en avec vos collègues, d'abord dans votre région, mais aussi dans les autres régions.\nQuand vous êtes prêt, et à la lumière de ce qui s'est passé lors du dernier tour, faites défiler les décisions que vous devez prendre en tant que ministre et qui, nous l'espérons, amélioreront la vie de vos citoyens lors du prochain tour.  ",
    "Modellen er simulert frem til 2040. Igjen, i grafene nedenfor er det bra hvis linjen er i den **grønne** sonen, hvis den er i den **røde** sonen, bør du bekymre deg! \nStuder alle indikatorene dine, se hvordan de utvikler seg over årene.Hadde du forventet noe annet med tanke på dine politiske valg? Diskuter igjen med kolleger, først i din region, men også i de andre regionene.\nNår du er klar, og i lys av det som skjedde i forrige runde, kan du bla deg ned til de beslutningene du som minister må ta som forhåpentligvis kan forbedre livene til innbyggerne dine i neste runde.  " 
    "_last_"
]
not_to_2060_str = [
    "The model has not yet been advanced to 2060. ",
    "Das Modell wurde noch nicht bis zum Jahr 2060 fortgeschrieben. ",
    "Das Modell wurde noch nicht bis zum Jahr 2060 fortgeschrieben. ",
    "Le modèle n'a pas encore été avancé vers 2060.", 
    "Modellen er ennå ikke oppdatert til 2060.",
    "_last_"
]
dec_info_tx_str = [
    "After looking at the situation for your people, you must enact several policies to improve the lives of your people **and** the health of the planet. You know that people cannot thrive on a sick planet. You set the policy by pulling the sliders. After coordinating with your ministerial colleagues, set the slider for each policy. \n\nEach policy has an **investment cost** attached to it. If you set a slider to its minimum, there is no cost, if you set a slider to its maximum, then the full investment cost is due. If you set the slider somewhere between minimum and maximum, the prorated investment cost is due. Your region also has a budget for **all** investments from **all** ministries. \n\nIf you exceed the budget, your colleague, the Minister for the Future, will tell you so and you must re-negotiate with your colleagues, until the total regional investment is below or equal to the budget.\n\nWhen the cabinet of your region is **a)** within the budget and **b)** you are **all** satisfied with your choices, the Minister for the Future will submit all your decisions to the game organizer so that the model can be advanced for the next round. ",
    "Nachdem Sie die Situation Ihrer Bevölkerung analysiert haben, müssen Sie verschiedene Massnahmen ergreifen, um das Leben Ihrer Bevölkerung **und** die Gesundheit des Planeten zu verbessern. Sie wissen, dass Menschen auf einem kranken Planeten nicht leben können. Sie legen die Massnahmen fest, indem Sie die Schieberegler ziehen. Nach Abstimmung mit Ihren Minister:innenKollegen stellen Sie den Schieberegler für jede Massnahme ein. \n\nJede Massnahme ist mit **Investitionskosten** verbunden. Stellen Sie den Schieberegler auf das Minimum, entstehen keine Kosten. Stellen Sie den Schieberegler auf das Maximum, werden die vollen Investitionskosten fällig. Stellen Sie den Schieberegler irgendwo zwischen Minimum und Maximum ein, werden die anteiligen Investitionskosten fällig. Ihre Region verfügt ausserdem über ein Budget für **alle** Investitionen **aller** Minister:innen. \n\nSollten Sie das Budget überschreiten, wird Ihr Kollege, der/die Minister:in für die Zukunft, Sie darüber informieren, und Sie müssen mit Ihren Kollegen:innen neu verhandeln, bis die gesamten regionalen Investitionen unter oder gleich dem Budget liegen.\n\nWenn das Kabinett Ihrer Region **a)** innerhalb des Budgets liegt und **b)** Sie **alle** mit Ihren Entscheidungen zufrieden sind, wird der/die ZukunftsMinister:in alle Ihre Entscheidungen dem/der Spielleiter:in übermitteln, damit das Modell für die nächste Runde fortgeschrieben wird. ",
    "Nachdem Sie die Situation Ihrer Bevölkerung analysiert haben, müssen Sie verschiedene Massnahmen ergreifen, um das Leben Ihrer Bevölkerung **und** die Gesundheit des Planeten zu verbessern. Sie wissen, dass Menschen auf einem kranken Planeten nicht leben können. Sie legen die Massnahmen fest, indem Sie die Schieberegler ziehen. Nach Abstimmung mit Ihren Minister:innenKollegen stellen Sie den Schieberegler für jede Massnahme ein. \n\nJede Massnahme ist mit **Investitionskosten** verbunden. Stellen Sie den Schieberegler auf das Minimum, entstehen keine Kosten. Stellen Sie den Schieberegler auf das Maximum, werden die vollen Investitionskosten fällig. Stellen Sie den Schieberegler irgendwo zwischen Minimum und Maximum ein, werden die anteiligen Investitionskosten fällig. Ihre Region verfügt ausserdem über ein Budget für **alle** Investitionen **aller** Minister:innen. \n\nSollten Sie das Budget überschreiten, wird Ihr Kollege, der/die Minister:in für die Zukunft, Sie darüber informieren, und Sie müssen mit Ihren Kollegen:innen neu verhandeln, bis die gesamten regionalen Investitionen unter oder gleich dem Budget liegen.\n\nWenn das Kabinett Ihrer Region **a)** innerhalb des Budgets liegt und **b)** Sie **alle** mit Ihren Entscheidungen zufrieden sind, wird der/die ZukunftsMinister:in alle Ihre Entscheidungen dem/der Spielleiter:in übermitteln, damit das Modell für die nächste Runde fortgeschrieben wird. ",
    "Après avoir examiné la situation de votre peuple, vous devez mettre en œuvre plusieurs politiques pour améliorer la vie de votre peuple **et** la santé de la planète. Vous savez que les gens ne peuvent pas prospérer sur une planète malade. Vous définissez la politique en tirant sur les curseurs. Après vous être coordonné avec vos collègues ministres, réglez le curseur de chaque politique. \n\nChaque politique a un **coût d'investissement**. Si vous réglez le curseur au minimum, il n'y a pas de coût, si vous réglez le curseur au maximum, le coût total de l'investissement est dû. Si vous placez le curseur entre le minimum et le maximum, le coût d'investissement est calculé au prorata. Votre région dispose également d'un budget pour **tous** les investissements de **tous** les ministères. \n\nSi vous dépassez le budget, votre collègue, le ministre de l'avenir, vous le dira et vous devrez renégocier avec vos collègues, jusqu'à ce que l'investissement régional total soit inférieur ou égal au budget. \n\nLorsque le cabinet de votre région est **a)** dans les limites du budget et **b)** que vous êtes **tous** satisfaits de vos choix, le ministre de l'avenir soumettra toutes vos décisions au meneur de jeu afin que le modèle puisse être avancé pour le prochain tour. ",
    "Etter å ha sett på situasjonen for ditt folk, må du iverksette flere politiske tiltak for å forbedre livene til ditt folk **og** planetens helse. Du vet at mennesker ikke kan trives på en syk planet. Du bestemmer politikken ved å trekke i glidebryterne. Etter å ha koordinert med ministerkollegene dine, stiller du inn glidebryteren for hver politikk. \n\nHver politikk har en **investeringskostnad** knyttet til seg. Hvis du setter en glidebryter på minimum, er det ingen kostnad, og hvis du setter en glidebryter på maksimum, påløper hele investeringskostnaden. Hvis du setter glidebryteren til et sted mellom minimum og maksimum, må du betale den forholdsmessige investeringskostnaden. Regionen din har også et budsjett for **alle** investeringer fra **alle** departementer. \n\nOm du overskrider budsjettet, vil din kollega, fremtidsministeren, fortelle deg det, og du må forhandle på nytt med kollegene dine, helt til den samlet regionale investeringen er under eller lik budsjettet.\n\nNår regjeringen i din region er **a)** innenfor budsjettet og **b)** dere **alle** er fornøyde med valgene deres, vil fremtidsministeren sende alle beslutningene deres til spillederen, slik at modellen kan avansere til neste runde. ",
    "_last_"
]
dec_title_tx_str = [
    "Set your policies ",
    "Entscheiden Sie über ihre Massnahmen ",
    "Entscheiden Sie über ihre Massnahmen ",
    "Décider de ses mesures ",
    "Bestem deg for tiltak ",
    "_last_"
]
fut_info_tx_str = [
    "As Minister for the Future, you see the big picture. You also see how much your ministerial colleagues in your region plan to invest in total to improve the lives of your people and the health of the planet.\n\nIt is **your** task to keep the **total regional investment** within the budget. If *total investment* is **below** 100 % of the budget, all is well. Although if you invest too little, things may get worse, much worse possibly!\n\nIf it is **above** 100 % of your budget, you need to advise your ministerial colleagues to reduce some of their investments. This is a difficult task where your moderating skills are needed. Good luck!\n\nAs your ministerial colleagues decide on their investment plans, click on the **Refresh Numbers** button to see the most up to date choices of your colleagues.\n\nWhen you are all ready, **you**, as Minister for the Future, submit the policy choices from all your colleagues - **be sure to get all their OKs** before you hit the *Submit* button! (*Note* if the Submit button does not show, it is because your region is above the the budget.\n\nMoney amounts are in constant (2025) Giga $ per year. A *Giga* is 1,000,000,000 ----- US Americans call this a Billion, others call this a Milliarde. ",
    "Als ZukunftsMinister:in sehen Sie das grosse Ganze. Sie sehen auch, wie viel Ihre Minister:inkollegen in Ihrer Region insgesamt investieren wollen, um das Leben Eurer Bevölkerung und die Gesundheit des Planeten zu verbessern.\n\nEs ist **Ihre** Aufgabe, die **regionalen Gesamtinvestitionen** im Rahmen des Budgets zu halten. Liegen die *Gesamtinvestitionen* **unter** 100 % des Budgets, ist alles in Ordnung. Investieren Sie jedoch zu wenig, kann es schlimmer werden, möglicherweise sogar noch viel schlimmer!\n\nLiegen sie **über** 100 % Ihres Budgets, müssen Sie Ihre Minister:innenkollegen anweisen, ihre Investitionen zu reduzieren. Dies ist eine schwierige Aufgabe, bei der Ihre Moderationsfähigkeiten gefragt sind. Viel Erfolg!\n\nWährend Ihre Minister:innenkollegen ihre Investitionspläne beschliessen, klicken Sie wiederholt auf die Schaltfläche **Zahlen aktualisieren**, um die aktuellsten Entscheidungen Ihrer Kolleg:Innen anzuzeigen.\n\nWenn Sie fertig sind, **reichen Sie** als ZukunftsMinister:in die politischen Entscheidungen aller Ihrer Kolleg:Innen ein & **holen Sie sich unbedingt deren Zustimmung**, bevor Sie auf die Schaltfläche *Übermitteln* klicken! (*Hinweis* Wenn die Schaltfläche *Zhalen übermitteln* nicht angezeigt wird, liegt das daran, dass Ihre Region das Budget überschreitet.\n\nDie Geldbeträge werden in konstanten (2025) Giga-Dollar pro Jahr angegeben. Ein *Giga* entspricht 1.000.000.000 --- US-Amerikaner nennen dies eine Billion, andere eine Milliarde. ",
    "Als ZukunftsMinister:in siehst Du das grosse Ganze. Du siehst auch, wie viel Deine MinisterKolleg:Innen in Deiner Region insgesamt investieren wollen, um das Leben Eurer Bevölkerung und die Gesundheit des Planeten zu verbessern.\n\nEs ist **Deine** Aufgabe, die **regionalen Gesamtinvestitionen** im Rahmen des Budgets zu halten. Liegen die *Gesamtinvestitionen* **unter** 100 % des Budgets, ist alles in Ordnung. Investiert Ihr jedoch zu wenig, kann es schlimmer werden, möglicherweise sogar noch viel schlimmer!\n\nLiegen sie **über** 100 % Eures Budgets, musst Du Deine Minister:innenkollegen anweisen, ihre Investitionen zu reduzieren. Dies ist eine schwierige Aufgabe, bei der Deine Moderationsfähigkeiten sehr gefragt sind. Viel Erfolg!\n\nWährend Ihre Minister:innenkollegen ihre Investitionspläne beschliessen, klicken Sie wiederholt auf die Schaltfläche **Zahlen aktualisieren**, um die aktuellsten Entscheidungen Ihrer Kolleg:Innen anzuzeigen.\n\nWenn Sie fertig sind, **reichen Sie** als ZukunftsMinister:in die politischen Entscheidungen aller Ihrer Kolleg:Innen ein & **holen Sie sich unbedingt deren Zustimmung**, bevor Sie auf die Schaltfläche *Übermitteln* klicken! (*Hinweis* Wenn die Schaltfläche *Zahlen übermitteln* nicht angezeigt wird, liegt das daran, dass Ihre Region das Budget überschreitet.\n\nDie Geldbeträge werden in konstanten (2025) Giga-Dollar pro Jahr angegeben. Ein *Giga* entspricht 1.000.000.000 --- US-Amerikaner nennen dies eine Billion, andere eine Milliarde. ",
    "En tant que ministre de l'avenir, vous avez une vision d'ensemble. Vous voyez aussi combien vos collègues ministres de votre région prévoient d'investir au total pour améliorer la vie de vos concitoyens et la santé de la planète.\n\nC'est **votre** tâche de maintenir **l'investissement régional total** dans les limites du budget. Si l'investissement total est inférieur à 100 % du budget, tout va bien. Toutefois, si vous investissez trop peu, les choses risquent d'empirer, voire de s'aggraver!\n\nSi le total est **supérieur** à 100 % de votre budget, vous devez conseiller à vos collègues ministres de réduire certains de leurs investissements. Il s'agit d'une tâche difficile où vos talents de modérateur sont nécessaires. Bonne chance!\nPendant que vos collègues ministres décident de leurs plans d'investissement, cliquez sur le bouton **Rafraîchir les chiffres** pour voir les choix les plus récents de vos collègues.\n\nLorsque vous êtes prêt, **vous**, en tant que ministre de l'avenir, soumettez les choix politiques de tous vos collègues - **assurez-vous d'obtenir leur accord** avant d'appuyer sur le bouton *Soumettre* ! (*Remarque:* si le bouton Soumettre ne s'affiche pas, c'est que votre région est au-dessus du budget.\nLes montants sont en Giga $ constants (2025) par an. Un *Giga* est égal à 1 000 000 000 ----- Les Américains appellent cela un Billion, d'autres appellent cela un Milliarde. " ,
    "Som fremtidsminister ser du det store bildet. Du ser også hvor mye dine ministerkolleger i din region planlegger å investere totalt for å forbedre livene til ditt folk og helsen til planeten. Det er **din** oppgave å holde den **samlet regionale investeringen** innenfor budsjettet. Hvis den *samlet investeringen* er **under** 100 % av budsjettet, er alt i orden. Men hvis du investerer for lite, kan ting bli verre, mye verre, muligens! \n\nHvis den er **over** 100 % av budsjettet, må du råde dine ministerkolleger til å redusere noen av sine investeringer. Dette er en vanskelig oppgave der det er behov for dine modererende evner. Lykke til! \n\nNår ministerkollegene dine bestemmer seg for investeringsplanene sine, klikker du på knappen **Oppdater tall** for å se de mest oppdaterte valgene til kollegene dine.\n\nNNår du er klar, sender **du**, som fremtidsminister, inn de politiske valgene fra alle kollegene dine - **se til at du får alle deres OK** før du trykker på *Send*-knappen! Hvis Send-knappen ikke vises, er det fordi din region ligger over budsjettet. \n\nPengebeløpene er i konstant (2025) Giga $ per år. En *Giga* er 1 000 000 000 --- US-amerikanere kaller dette en Billion, andre kaller det en Milliarde. ",
    "_last_"
]
fut_bud_lb1_tx_str = [
    "Your total budget is ",
    "Ihr Gesamtbudget ist ",
    "Ihr Gesamtbudget ist ",
    "Votre budget total est ", 
    "Det totale budsjettet er ", 
    "_last_"
]
fut_bud_lb2_tx_str = [
    "All the investment plans of all your fellow ministers summed up are ",
    "Alle Investitionspläne aller Ihrer Minister:innenkollegen zusammengefasst sind ",
    "Alle Investitionspläne aller Ihrer Minister:innenkollegen zusammengefasst sind ",
    "Tous les plans d'investissement de tous vos collègues ministres résumés sont ", 
    "Alle investeringsplanene til alle dine medministre oppsummert er ", 
    "_last_"
]
fut_bud_lb3_tx_str = [
    "All Investment plans as % of your budget ",
    "Alle Investitionspläne als % Ihres Budgets ",
    "Alle Investitionspläne als % Ihres Budgets ",
    "Tous les plans d'investissement combinés en % de votre budget ", 
    "Alle investeringsplaner samlet som % av budsjettet ditt ", 
    "_last_"
]
cfpov_tx_str = [
    "Poverty ",
    "Armut ",
    "Armut ",
    "Pauvreté ", 
    "Fattigdom", 
    "_last_"
]
cfpov_lb_tx_str = [
    "Regional investment plans against poverty ",
    "Regionale Investitionspläne gegen Armut ",
    "Regionale Investitionspläne gegen Armut ",
    "Investissement régional prévoit contre la pauvreté", 
    "Regionale investeringsplaner mot fattigdom", 
    "_last_"
]
cfineq_tx_str = [
    "Inequality ",
    "Ungleichheit ",
    "Ungleichheit ",
    "Inégalité", 
    "Ulikhet", 
    "_last_"
]
cfineq_lb_tx_str = [
    "Regional investment plans against inequality ",
    "Regionale Investitionspläne gegen Ungleichheit ",
    "Regionale Investitionspläne gegen Ungleichheit ",
    "Investissement régional prévoit contre les inégalités", 
    "Regionale investeringsplaner mot ulikhet", 
    "_last_"
]
cfemp_tx_str = [
    "Empowerment/Equal rights ",
    "Empowerment/Gleichberechtigung ",
    "Empowerment/Gleichberechtigung ",
    "Empowerment/Égalité des droits ",
    "Myndiggjøring/Like rettigheter",
    "_last_"
]
cfemp_lb_tx_str = [
    "Regional investment plans for empowerment ",
    "Regionale Investitionspläne zur Stärkung der Selbstbestimmung ",
    "Regionale Investitionspläne zur Stärkung der Selbstbestimmung ",
    "Plans d'investissement régionaux pour l'autonomisation", 
  "Regionale investeringsplaner for empowerment / myndiggjøring", 
    "_last_"
]
cffood_tx_str = [
    "Food & agriculture ",
    "Ernährung und Landwirtschaft ",
    "Ernährung und Landwirtschaft ",
    "Nourriture et agriculture", 
    "Ernæring og landbruk",
    "_last_"
]
cffood_lb_tx_str = [
    "Regional investment for food and agriculture ",
    "Regionale Investitionen für Ernährung und Landwirtschaft ",
    "Regionale Investitionen für Ernährung und Landwirtschaft ",
    "Investissement régional pour l'alimentation et l'agriculture", 
    "Regional investering for mat og landbruk", 
    "_last_"
]
cfener_tx_str = [
    "Energy ",
    "Energie ",
    "Energie ",
    "Énergie ", 
    "Energi", 
    "_last_"
]
cfener_lb_tx_str = [
    "Regional investment for energy ",
    "Regionale Investitionen für die Energiewende ",
    "Regionale Investitionen für die Energiewende ",
    "Investissement régional pour l'énergie", 
    "Regional investering for energi", 
    "_last_"
]
refresh_numbers_tx_str = [
    "RFRESH numbers ",
    "Zahlen aktualisieren ",
    "Zahlen aktualisieren ",
    "Actualiser les chiffres",
    "Oppdater tall",
    "_last_"
]
submit_numbers_tx_str = [
    "SUBMIT numbers for ",
    "Zahlen übermitteln für ",
    "Zahlen übermitteln für ",
    "Soumettre des numéros pour ", 
    "Send inn tall for ", 
    "_last_"
]
confirm_submit_tx_str = [
    "Yes to submit, No to go back ",
    "Ja zum Absenden, Nein zum Zurückgehen ",
    "Ja zum Absenden, Nein zum Zurückgehen ",
    "Oui à soumettre, Non pour revenir",
    "Ja å sende inn, Nei å gå tilbake",
    "_last_"
]
confirm_title_tx_str = [
    "Really submit the decisions?",
    "Die Entscheidungen wirklich einreichen?",
    "Die Entscheidungen wirklich einreichen?",
    "Soumettre vraiment les décisions ?", 
    "Skal du virkelig sende inn avgjørelsene?", 
    "_last_"
]
after_submit_tx_str = [
    "Your regions decisions have been submitted - thanks!\nOnce all regions have submitted their decisons, the model will be advanced for the next round. This will take a bit of time ... ",
    "Die Entscheidungen Ihrer Region wurden übermittelt - Danke!\nSobald alle Regionen ihre Entscheidungen übermittelt haben, wird das Modell für die nächste Runde fortgeschrieben. Das wird etwas dauern ... ",
    "Die Entscheidungen Deiner Region wurden übermittelt - Danke!\nSobald alle Regionen ihre Entscheidungen übermittelt haben, wird das Modell für die nächste Runde fortgeschrieben. Das wird etwas dauern ... ",
    "Vos décisions de régions ont été soumises - merci! \nDès que toutes les régions auront transmis leurs décisions, le modèle sera avancé pour le prochain tour. Cela prendra un peu de temps ...",
    "Dine regioner avgjørelser er sendt inn - takk! \nSå snart alle regionene har sendt inn sine beslutninger, modellen vil bli oppdatert for neste runde. Dette vil ta litt tid ...",
    "_last_"
]
nothing_submitted_tx_str = [
    "Nothing was submitted ... ",
    "Es wurde nichts übermittelt ",
    "Es wurde nichts übermittelt ",
    "Rien n'a été soumis ...", 
    "Ingenting ble sendt inn ...", 
    "_last_"
]
not_all_looked_at_title = [
  "Your regional colleagues aren't ready",
  "Die Kollegen:innen in Ihrer Region sind noch nicht so weit",
  "Die Kolleg:Innen in Deiner Region sind noch nicht so weit",
  "Les collègues de votre région ne sont pas encore prêts",
  "Vos collèges régionaux ne sont pas prêts",
  "_last_"
]
not_all_looked_at_tx = [
  "Not all your regional ministerial colleagues have looked at their results:",
  "Noch haben sich nicht alle Ihre regionalen Minister:innenkollegen ihre Ergebnisse angeschaut:",
  "Noch haben sich nicht alle Deine regionalen Minister:innenkollegen ihre Ergebnisse angeschaut:",
  "Tous vos collègues ministres régionaux n'ont pas encore consulté leurs résultats:",
  "Alle dine regionale ministerkolleger har ennå ikke sett på resultatene sine:",
  "_last_"
]
p_advance_to_next_round_tx_str = [
    "Get the results until 2040 and the decision sheet for 2040-2060 - your childrens future ",
    "Laden Sie sich die Ergebnisse bis 2040 und den Entscheidungsbogen für 2040-2060 herunter - die Zukunft Ihrer Kinder ",
    "Lade Dir die Ergebnisse bis 2040 und den Entscheidungsbogen für 2040-2060 herunter - die Zukunft Deiner Kinder ",
    "Obtenez les résultats jusqu'en 2040 et la feuille de décision pour 2040-2060 - votre avenir pour enfants", 
    "Få resultatene til 2040 og beslutningsarket for 2040-2060 - fremtiden til barna dine", 
    "_last_"
]
p_advance_to_1_tx_str = [
    "Get the results until 2060 and the decision sheet for 2060-2100 - your grandchildrens future ",
    "Laden Sie sich die Ergebnisse bis 2060 und den Entscheidungsbogen für 2060-2100 herunter - die Zukunft Ihrer Enkelkinder ",
    "Lade Dir die Ergebnisse bis 2060 und den Entscheidungsbogen für 2060-2100 herunter - die Zukunft Deiner Enkelkinder ",
    "Obtenez les résultats jusqu'en 2060 et la feuille de décision pour 2060-2100 - l'avenir de vos petits-enfants. ",
    "Få resultatene frem til 2060 og beslutningsarket for 2060-2100 - dine barnebarns fremtid ",
    "_last_"
]
p_advance_to_2_tx_str = [
    "Get the results until the end of the century ",
    "Ergebnisse bis zum Ende des Jahrhunderts laden ",
    "Ergebnisse bis zum Ende des Jahrhunderts laden ",
    "Obtenez les résultats jusqu'à la fin du siècle", 
    "Få resultatene til slutten av århundret", 
    "_last_"
]
p_advance_to_next_round_wait_str = [
  "Waiting for model to be advanced ...",
  "Warten auf die Fortschreibung des Modells ...",
  "Warten auf die Fortschreibung des Modells ...",
  "En attente de la mise à jour du modèle ...",
  "Venter på at modellen skal oppdateres ...",
  "_last_"
]
p_waiting_model_run_tx_str = [
    "... still waiting for the game organizer to advance the model ... ",
    "wir warten darauf, dass der/die Spielleiter:in das Modell fortschreibt ",
    "wir warten darauf, dass der/die Spielleiter:in das Modell fortschreibt ",
    "... toujours en attente que l'organisateur de jeu avance le modèle ...", 
    "... venter fortsatt på at spillarrangøren skal fremme modellen ...", 
    "_last_"
]
waiting_tx_str = [
    "Waiting ... ",
    "Warten ... ",
    "Warten ... ",
    "En attendant ... ", 
    "Venter ...", 
    "_last_"
]
nicht_all_sub_p_tx_str = [
    "Not all regions have submitted their decisions, your game organizer knows who we are waiting for ... ",
    "Noch haben nicht alle Regionen ihre Entscheidungen übermittelt, ihr:e Spielleiter:in weiss, auf wen wir warten ... ",
    "Noch haben nicht alle Regionen ihre Entscheidungen übermittelt, ihr:e Spielleiter:in weiss, auf wen wir warten ... ",
    "Toutes les régions n'ont pas soumis leurs décisions, votre chef de jeu sait qui nous attendons ...", 
    "Ikke alle regioner har sendt sine beslutninger, spilllederen din vet hvem vi venter på ...", 
    "_last_"
]
nicht_all_sub_gm_tx_str = [
    "Not all regions have submitted their decisions ... ",
    "Noch haben nicht alle Regionen ihre Entscheidungen übermittelt ... ",
    "Noch haben nicht alle Regionen ihre Entscheidungen übermittelt ... ",
    "Toutes les régions n'ont pas soumis leurs décisions ...", 
    "Ikke alle regioner har sendt sine avgjørelser ...", 
    "_last_"
]
all_submitted_p_tx_str = [
    "Now, aLL regions have submitted their decisions, your game organizer will advance the model shortly and let you know when your results are ready ",
    "Alle Regionen haben jetzt ihre Entscheidungen übermittelt. Ihr:e Spielleiter:in wird das Modell in Kürze fortschreiben und Sie informieren, wenn die Ergebnisse vorliegen. ",
    "Alle Regionen haben jetzt ihre Entscheidungen übermittelt. Dein:e Spielleiter:in wird das Modell in Kürze fortschreiben und Dich informieren, wenn die Ergebnisse vorliegen. ",
    "Toutes les régions ont soumis leurs décisions, votre chef de jeu fera progresser le modèle sous peu et vous fera savoir quand vos résultats seront prêts", 
    "Alle regioner har sendt sine beslutninger, spilllederen din vil modellen viderføre om kort tid og gi deg beskjed når resultatene er klare", 
    "_last_"
]
running_model_tx_str = [
    "... advancing the model ... ",
    "... das Modell wird fortgeschrieben ... ",
    "... das Modell wird fortgeschrieben ... ",
    "... avancer le modèle ...", 
    "... modellen blir videreført ...", 
    "_last_"
]
credits_btn_tx_str = [
    "Credits ",
    "Credits ",
    "Credits ",
    "Les crédits ",
    "Credits" ,
    "_last_"
]
credits_tx_str = [
    "We use the open-source regional earth4all model developed by U Goluke and PE Stoknes. It, in turn, is based on the earth4all global model which J Randers developed. The game has been developed with anvil.works by U Goluke and countless alpha and beta testers. The rights to the game belong to ... ",
    "Wir verwenden das open-source earth4all 10-Regionen Modell und wurde von U Goluke und PE Stoknes entwickelt. Es basiert auf dem globalen earth4all-Modell, das J Randers entwickelt hat. Das Spiel wurde mit anvil.works von U Goluke und zahllosen Alpha- und Beta-Testern entwickelt. Die Rechte an dem Spiel liegen bei ... ",
    "Wir nutzen das open-source earth4all 10-Regionen Modell. Es wurde von U Goluke und PE Stoknes entwickelt. Es basiert auf dem globalen earth4all-Modell, das J Randers entwickelt hat. Das Spiel wurde mit anvil.works programmiert von U Goluke. Zahllose Alpha- und Beta-Testern haben es getestet, aber an allen Fehlern sind wir schuld. Die Rechte an dem Spiel liegen bei ... ",
    "Nous utilisons le modèle régional open source earth4all développé par U Goluke et PE Stoknes.. Il est basé sur le modèle global earth4all développé par J Randers. Le jeu a été développé avec anvil.works par U Goluke et dinnombrables testeurs alpha et bêta. Les droits du jeu sont détenus par ... ",
    "Vi bruker den åpne kildekode-modellen earth4all, utviklet av U Goluke og PE Stoknes. Den er på sin side basert på den Earth4all Global Model som J Randers utviklet. Spillet er utviklet med Anvil.Works av U Goluke og utallige alfa- og beta-testere. Rettighetene til spillet tilhører ..." ,
    "_last_"
]
credits_title_str = [
    "Standing on someone's shoulders ... ",
    "Wir stehen auf den Schultern von Anderen ... ",
    "Wir stehen auf den Schultern von Anderen ... ",
    "Nous sommes soutenus par les autres ... ",
    "Stående på skuldre av andre ..." ,
    "_last_"
]
lang_dd_menu_tx_str = [
    "Change the language ",
    "Ändern Sie die Sprache ",
    "Ändere die Sprache ",
    "Changer de langue ",
    "Endre språket" ,
    "_last_"
]
lang_info_str = [
  "**First, the language.** \nIf English is fine, just click on the *Lets Go* button, otherwise, select from the drop-down menu on the right the correct language. We are adding more and more languages, if you want to help with the translation, let us know. \nlang at blue minus way dot net",
  "**Zuerst die Sprache.** \nWenn formelles Deutsch ausreicht, klicken Sie einfach auf die Schaltfläche *Los gehts*, andernfalls wählen Sie aus dem Dropdown-Menü auf der rechten Seite die gewünschte Sprache. Mit der Zeit fügen wir mehr und mehr Sprachen hinzu, wenn Sie bei der Übersetzung helfen wollen, lassen Sie es uns wissen. \nlang at blue minus way dot net",
  "**Zuerst die Sprache.** \nWenn informelles Deutsch ausreicht, klicke einfach auf die Schaltfläche *Los gehts*, andernfalls wähle aus dem Dropdown-Menü auf der rechten Seite die gewünschte Sprache. Mit der Zeit fügen wir mehr und mehr Sprachen hinzu, wenn Du bei der Übersetzung / Anpassung helfen willst, lass es uns wissen. \nlang at blue minus way dot net",
  "**Tout dabord, choisissez la langue.** \nSi le français suffit, il vous suffit de cliquer sur le bouton *Allons-y*, sinon, sélectionnez la langue de votre choix dans le menu déroulant à droite. Au fil du temps, nous ajoutons de plus en plus de langues, si vous voulez aider à la traduction, faites-le nous savoir. \nlang at blue minus way dot net",
  "**For det første er språket.** \nOm bokmål er bra, bare klikk på *La oss gå* -knappen, ellers, velg fra rullegardinmenyen til høyre riktig språk. Vi legger til flere og flere språk, hvis du vil hjelpe med oversettelsen, gi oss beskjed. \nlang at blue minus way dot net" ,
  "_last_"
]
lang_lets_go_tx = [
  "Let's go",
  "Los geht's",
  "Los geht's",
  "Allons-y",
  "La oss gå",
  "_last_"
]
lang_avail_items = [
  "English",
  "Deutsch-Sie",
  "Deutsch-Du",
  "Français",
  "Norsk-Bokmål",
  "_last_"  
]
enter_code_tx = [
  "Start-code, please",
  "Start-Code, bitte",
  "Start-Code, bitte",
  "Code de démarrage, s'il vous plaît",
  "Start-Code, vær så snilll",
  "_last_"
]  
enter_code_title_tx = [
  "Enter code",
  "Code eingeben",
  "Code eingeben",
  "Entrer le code",
  "Skriv inn kode",
  "_last_"
]  
wrong_code_tx = [
  "Wrong code, check with whoever knows the code",
  "Falscher Code, fragen Sie jemanden, der den Code kennt",
  "Falscher Code, frage jemanden, der den Code kennt",
  "Code erroné, vérifier auprès de la personne qui connaît le code",
  "Feil kode, sjekk med den som kan koden",
  "_last_"
]
